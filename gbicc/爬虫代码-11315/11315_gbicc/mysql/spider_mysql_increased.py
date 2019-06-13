# -*- coding:utf-8 -*-
import datetime
import logging.config
import re
import time
import random
import requests
import urllib3
from bs4 import BeautifulSoup
from cpca import *
from db import single_oracle, USER_AGENTS, single_mongodb
from mysql.db import single_mysql
from redis_cache import single_reids
import sys
from setting import proxyUser,proxyPass

urllib3.disable_warnings()  # 证书验证，如果不加这句话，还会有警告

# logging.config.fileConfig("../log_file/11315_increased.conf")
logging.config.fileConfig("../log_file/11315_increased.conf")
logger = logging.getLogger("loggerTxt")
proxyHost = "http-dyn.abuyun.com"
proxyPort = "9020"

# proxyUser = "H305R0IC625W29HD"
# proxyPass = "07014EDF361ACDB3"
# =======H4LG0005632SP1YD:CA6EAB506F5B965F
# proxyUser = "H4LG0005632SP1YD"
# proxyPass = "CA6EAB506F5B965F"

# proxyUser = "H09EIQ188A9U99AD"
# proxyPass = "6546F4FA2BC7D868"


proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
    "host": proxyHost,
    "port": proxyPort,
    "user": proxyUser,
    "pass": proxyPass,
}
proxies = {
    "http": proxyMeta
}
#proxies={}

# proxies = {'http': 'http://H017W84J271F18FD:451D275088D7ABD3@proxy.abuyun.com:9020', 'https': 'http://H017W84J271F18FD:451D275088D7ABD3@proxy.abuyun.com:9020'}
# proxies = {}

class RequestClass(object):
    
    def __init__(self, proxies):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1: WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
            
        }
        self.proxies = proxies
        self.session = requests.session()
    
    # 必须有url 别的参数看情况传入  **kwargs为一个字典类型
    def request_url(self, url, **kwargs):
        if "headers" not in kwargs:
            kwargs['headers'] = self.headers
        
        if "proxies" not in kwargs:
            kwargs['proxies'] = self.proxies
        # 当为https的时候将验证关闭
        
        try:
            logger.debug(url)
            logger.debug("get: " + url + " proxies: " + str(kwargs["proxies"]))
            response = self.session.get(url=url, **kwargs)
        except Exception as e:
            logger.debug(e)
            response = self.session.get(url=url, **kwargs)
        # logger.debug('request_file.......cookie=%s' % str(self.session.cookies))
        return response
    
    def get_cookies(self):
        # 将cookie转为字典
        cookie_dict = requests.utils.dict_from_cookiejar(self.session.cookies)
        return cookie_dict
    
    def set_cookies(self, **kwargs):
        cookie_dict = self.get_cookies()
        for key, value in kwargs.items():
            cookie_dict[key] = value
        cookies = requests.utils.cookiejar_from_dict(cookie_dict, cookiejar=None, overwrite=True)
        self.session.cookies = cookies

def web_spider(url):
    
    headers = {
        "User-Agent": random.choice(USER_AGENTS)
    }
    requestsClass = RequestClass(proxies=proxies)
    con = requestsClass.request_url(url=url, headers=headers, proxies=proxies, timeout=10)
    logger.debug(con)
    if u"正在 请求 请 稍候" in con.text:
        time.sleep(2)
        url = re.search('.*href="(.*?)"', con.text).group(1)
        Referer = con.url
        headers["Referer"] = Referer
        con = requestsClass.request_url(url=url, headers=headers, timeout=6)
    
    return con


def try_and_text(func, *variable):
    s = '解析有误'
    if not func:
        return 'NA'
    try:
        s = eval(func)
    except Exception as e:
        logger.error(e)
    finally:
        return s

def re_get_text(text,html_,flag=True):
    res='解析有误'
    try:
        zhu_suo = re.search(r'{}</th><td>(.*?)</td>'.format(text), html_).group(1)
        if flag:
            return zhu_suo

        res = re.split(r'<.*?>', zhu_suo)
        res = ''.join([i for i in res if i != ''][::2])
    except Exception as e :
        logger.debug(html_)
        logger.exception(e)
    else:
        return res

def detail_spider_parse(detail_url, html, i, url,lisss):
    try:
        company_11315 = {}
        # main_url: 主页的url地址
        company_11315['main_url'] = url
        # detail_html: 主页的html页面
        company_11315['main_html'] = html
        # number: 公司的id号
        company_11315['number'] = i
        # add_time: 插入时间
        company_11315['add_time'] = datetime.datetime.now() + datetime.timedelta(hours=8)
        # detial_url: 详情页url
        company_11315['detail_url'] = detail_url

        detail_resp = web_spider(detail_url)
        detail_html = detail_resp.text
        # detail_html:详情页html
        company_11315['detail_html'] = detail_html
        # 存入mongodb
        # result = single_mongodb.mongodb_insert("company_11315", company_11315)

        if detail_resp and detail_resp.status_code == 200:
            if "系统检测到您的请求存在异常" not in detail_html and "你可能访问的太快了" not in detail_html and "正在 请求 请 稍候" not in detail_html:
                lisss['establish_date'] = '登陆可见'
                lisss['register_office'] = '登陆可见'
                lisss['check_date'] = '登陆可见'
                ssss_text = ''.join(detail_html.split())
                lisss['register_num'] = re_get_text('注册号', ssss_text, False)
                lisss['company_type'] = re_get_text('类型', ssss_text, False)
                # lisss['legal_representative'] = try_and_text(re_get_text('法定代表人',ssss_text,True))
                try:
                    legal_representative = re.search('法定代表人</th><td>(.*?)</td>', ssss_text)
                    if not legal_representative:
                        legal_representative = re.search('经营者</th><td>(.*?)</td>', ssss_text)
                    if not legal_representative:
                        legal_representative = re.search('负责人</th><td>(.*?)</td>', ssss_text)
                    if not legal_representative:
                        legal_representative = re.search('投资人</th><td>(.*?)</td>', ssss_text)
                    if not legal_representative:
                        legal_representative = re.search('执行事务合伙人</th><td>(.*?)</td>', ssss_text)
                    if not legal_representative:
                        legal_representative = re.search('股东</th><td>(.*?)</td>', ssss_text)
                    if not legal_representative:
                        legal_representative = re.search('首席代表</th><td>(.*?)</td>', ssss_text)

                    lisss['legal_representative'] = legal_representative.group(1).replace("'",'')
                except Exception as e:
                    logger.exception(e)

                    lisss['legal_representative'] = 'NA'
                lisss['register_fund'] = re_get_text('注册资本.*?',ssss_text, False)
                try:
                    residence = re.search(r'住所</th><td>(.*?)</td>', ssss_text)
                    if not residence:
                        residence = re.search(r'经营场所</th><td>(.*?)</td>', ssss_text)
                    if not residence:
                        residence = re.search(r'营业场所</th><td>(.*?)</td>', ssss_text)
                    if not residence:
                        residence = re.search(r'地址</th><td>(.*?)</td>', ssss_text)
                    lisss['residence'] = residence.group(1).replace("'", '')
                except Exception as e:
                    logger.exception(e)
                    lisss['residence'] = 'NA'
                lisss['business_term_begin'] = re_get_text('期限自', ssss_text, True)
                lisss['business_term_end'] = re_get_text('期限至', ssss_text, True)
                lisss['business_scope'] = re_get_text('范围', ssss_text, True).replace("'",'')
                lisss['credit_num'] = re_get_text('统一信用代码', ssss_text, True)
                lisss['register_status'] = re_get_text('登记状态', ssss_text, True)
            else:
                logger.info("IP 被封或者访问过快")
                detail_spider_parse(detail_url, html, i, url,lisss)

    except Exception as e:
        logger.exception(e)
    else:
        return lisss


def increased_or_reset(flag):
    '''
    redis计数器的简单实现
    :param flag:
    :return:
    '''
    if flag==1:
        single_reids.server.incr('11315_NA_count')
    else:
        single_reids.server.set('11315_NA_count', 0)


def web_parse(html, i, url):

    if "您想浏览的网页找不到" in html or "入档信息更新" in html:

        insert_value = ""
        value_list = [str(i), url, str("NA"), "SYSDATE"
            , str(0)]
        value_list = ['"' + value + '"' for value in value_list]
        insert_value += '(' + ','.join(value_list) + '),'
        # single_mysql.mysql_insert_param(
        #     "insert into company_11315 (company_number, url, company_name, add_time, mark) values ({},'{}','{}',{},{})".format(
        #         int(i), url, "NA", "SYSDATE", 0))
        single_mysql.mysql_insert_param(
            "insert into company_11315  (url, company_name, add_time, error, company_number) values ('{}','{}',SYSDATE,1,{})".format(url, "NA", int(i)))
        logger.info("此url不对应任何公司" + str(i))
        increased_or_reset(1)

    else:
        increased_or_reset(0)
        soup = BeautifulSoup(html, 'lxml')
        try:
            trs = soup.find('table', class_="v1Table01").find_all("tr")
            company_industry = "null"
            company_area = "null"
            
            # company_address = trs[4].find("td").text.replace("查看地图", "").strip()
            company_address = soup.find('table', class_="v1Table01").find_all('th', string=re.compile("详细地址"))[0].find_next_sibling('td').text.replace("查看地图", "").replace("'", '').strip()
            main_produce = soup.find('table', class_="v1Table01").find_all('th', string=re.compile("主营产品"))[
                0].find_next_sibling('td').text.strip()
            company_name = trs[0].find_all("th")[1].get('title')
            # 法人是图片 ，不从这里取
            # fa_ren=trs[1].find('td').text.strip()
            insert_value = ""
            address_1 = address_2 = address_3 = branch = 'NA'

            detail_href = soup.find('a', href=re.compile("http://www.11315.com/cil/index/")).get('href')
            # ss=detail_spider_parse(detail_href)
            # logger.debug(ss)
            lisss={}
            lisss = detail_spider_parse(detail_href,html, i, url, lisss)
            logger.debug(lisss)
        #print(residence, register_status, credit_num)

            if company_name != "NA" and company_name != "None":
                df = transform([company_address or lisss['register_office']], cut=False)
                for addr in df.index:
                    print(addr)
                    address_1 = (df.loc[addr].values[0])
                    address_2 = (df.loc[addr].values[1])
                    address_3 = (df.loc[addr].values[2])
                # print(address_3,address_2,address_1)

                branch = 'NA'
            column = "(company_number,url, company_name, company_industry, company_area, company_address, add_time, mark, address_1, address_2, address_3,parse,branch,register_num, company_type, legal_representative, register_fund, residence,business_term_begin, business_term_end, business_scope, register_status,credit_num, detail_url)"

            # if branch and branch!='NA':
                #sql="insert into company_11315_zyfd "+column+" values ({},'{}','{}','{}','{}','{}',{},{},'{}','{}','{}',{},'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(i, url, company_name, company_industry, company_area, company_address, "SYSDATE", 0, address_1, address_2, address_3, 1, branch,register_num, company_type, legal_representative, register_fund, residence, business_term_begin, business_term_end, business_scope, register_status,credit_num)
            #     sql = "update company_11315_zyfd set url='{}',company_name='{}', company_industry='{}',company_area='{}',company_address='{}',add_time={}, mark={},address_1='{}',address_2='{}',address_3='{}',parse={},branch='{}',register_num='{}',company_type='{}',legal_representative='{}',register_fund='{}',residence='{}',business_term_begin='{}',business_term_end='{}',business_scope='{}',register_status='{}',credit_num='{}' where company_number = {}".format(
            #         url, company_name, company_industry, company_area, company_address, "SYSDATE", 11, address_1,
            #         address_2,
            #         address_3, 11, branch, register_num, company_type, legal_representative, register_fund, residence,
            #         business_term_begin, business_term_end, business_scope, register_status, credit_num, i)
            # else:

            sql="insert into company_11315 "+column+" values ({},'{}','{}','{}','{}','{}',{},{},'{}','{}','{}',{},'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(i, url, company_name, company_industry, company_area, company_address, "SYSDATE", 0, address_1, address_2, address_3, 1, branch,lisss['register_num'], lisss['company_type'], lisss['legal_representative'], lisss['register_fund'], lisss['residence'], lisss['business_term_begin'], lisss['business_term_end'],lisss['business_scope'], lisss['register_status'], lisss['credit_num'], detail_href)

            # del_sql = 'delete from company_11315 where company_number={}'.format(i)
            # single_oracle.execute(del_sql)
            # sql = "insert into company_11315 " + column + " values ({},'{}','{}','{}','{}','{}',{},{},'{}','{}','{}',{},'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(
            #     i, url, company_name, company_industry, company_area, company_address,
            #     "SYSDATE", 0, address_1, address_2, address_3, 1, branch,
            #     register_num, company_type, legal_representative, register_fund, residence,
            #     business_term_begin, business_term_end, business_scope,register_status, credit_num)

            # 更新慈溪
            # sql = "update company_11315 set url='{}',company_name='{}', company_industry='{}',company_area='{}',company_address='{}',add_time={}, mark={},address_1='{}',address_2='{}',address_3='{}',parse={},branch='{}',register_num='{}',company_type='{}',legal_representative='{}',register_fund='{}',residence='{}',business_term_begin='{}',business_term_end='{}',business_scope='{}',register_status='{}',credit_num='{}' where company_number = {}".format(url, company_name, company_industry, company_area,company_address, "SYSDATE", 11, address_1, address_2, address_3, 1,branch, lisss['register_num'], lisss['company_type'], lisss['legal_representative'], lisss['register_fund'],lisss['residence'], lisss['business_term_begin'], lisss['business_term_end'], lisss['business_scope'],lisss['register_status'], lisss['credit_num'], i)

            # print(sql)
            #logger.info(sql)
            # single_oracle.mysql_insert_param(sql)
            single_mysql.mysql_insert_param(sql)

        except Exception as e:
            logger.error(e)
            # single_mysql.mysql_insert_param(
            #     "insert into company_11315 (company_number, url, company_name, add_time, mark,error) values ({},'{}','{}',{},{},{},{})".format(i, url, "NA", "SYSDATE", 1,2))
            single_mysql.mysql_insert_param(
                " insert into company_11315  (url, company_name, add_time, error, company_number) values ('{}','{}',SYSDATE,2,{})".format(url, "NA", int(i)))
            raise e


def main(args):
    print(u'启动', args)
    # import sys
    #
    # reload(sys)
    # check_first_start=True
    flag = single_reids.server.get('11315_increased_flag')


    if not flag or int(flag.decode()) == 0:
        single_reids.put_flag()

        flag = single_reids.server.get('11315_increased_flag')
    while True:
        NA_count = single_reids.server.get('11315_NA_count')

        if NA_count and int(NA_count.decode()) >= int(flag.decode()):
            time.sleep(60*30)
            continue

        # i = single_reids.server.rpop('11315_omit')
        i = single_reids.server.rpop('11315_increased')

        #i=12872429
        print('-'*20, i)
        if not i:
            # time.sleep(60*10)
            # single_reids.put_11315_omit()

            single_reids.put_11315_increased()
            continue
        Retry = 1
        i = i.decode()

        res = single_oracle.oracle_find_by_param_all('select count(*) from company_11315 where company_number = {}'.format(i))
        if res[0][0] != 0:
            print('该id{}已存在'.format(i))
            single_oracle.execute('delete from company_11315 where company_number = {}'.format(i))

        url = "http://" + str(i) + ".11315.com/"
        print(url)

        # 一个公司连接最多访问10次
        while Retry <= 10:
            logger.info(url + "------%d", Retry)

            try:
                con = web_spider(url)
                # 对访问状态及页面内容进行初步判断
                if con.status_code == 200:
                    html = con.text
                    if "系统检测到您的请求存在异常" not in html and "你可能访问的太快了" not in html and "正在 请求 请 稍候" not in html:

                        try:
                            web_parse(html, i, url)
                        except Exception:
                            logger.info("此number号已存在: %s", i)
                        break
                    else:
                        logger.info("IP 被封或者访问过快")
                        Retry += 1
                        continue
                else:
                    logger.info("访问状态码异常%s", str(con.status_code))
                    Retry += 1
                    time.sleep(3)
                    continue
            except Exception as e:
                logger.info("访问超时或者连接出错")
                Retry += 1
                logger.exception(e)
                continue
            except AttributeError as w:
                logger.exception(w)
                logger.info("无法获取二次连接url")
                Retry += 1
                continue
            except Exception as w:
                logger.exception(w)
                logger.info("未知访问错误")
                logger.exception("Exception Logged")
                Retry += 1
                continue
            

if __name__ == "__main__":
    main(1)
