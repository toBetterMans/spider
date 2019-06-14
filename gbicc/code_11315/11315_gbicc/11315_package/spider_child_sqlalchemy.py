# -*- coding:utf-8 -*-
import random

import requests
from tyc_bean import *
from bs4 import BeautifulSoup
import re
import time
from requests.packages import urllib3
from datetime import datetime
from redis_cache import single_reids
import logging.config
# from db import single_mysql, single_oracle, USER_AGENTS
from db_sqlalchemy_oracle import single_oracle, USER_AGENTS
# from request_file import RequestClass
import addres_parse
urllib3.disable_warnings()  # 证书验证，如果不加这句话，还会有警告

logging.config.fileConfig("../log_file/11315.conf")
logger = logging.getLogger("loggerTxt")
proxyHost = "http-dyn.abuyun.com"
proxyPort = "9020"

proxyUser = "H09EIQ188A9U99AD"
proxyPass = "6546F4FA2BC7D868"

proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
    "host": proxyHost,
    "port": proxyPort,
    "user": proxyUser,
    "pass": proxyPass,
}
proxies = {
    "http": proxyMeta
}
branch_list = {
    '其他': '0',
    '蕲春': '010101',
    '京山': '010201',
    '谷城': '010301',
    '枣阳': '010401',
    '老河口': '010501',
    '潜江': '010601',
    '监利': '010701',
    '松滋': '010801',
    '公安': '010901',
    '沙洋': '011001',
    '南漳': '011101',
    '黄梅': '011201',
    '武穴': '011301',
    '大冶': '011401',
    '宜城': '011501',
    '曹县': '020101',
    '沂水': '020201',
    '青州': '020301',
    '临邑': '020401',
    '单县': '020501',
    '嘉祥': '020601',
    '曲阜': '020701',
    '五莲': '020801',
    '栖霞': '020901',
    '巨野': '021001',
    '东明': '021101',
    '汶上': '021201',
    '龙口': '021301',
    '宁海': '030101',
    '镇海': '030201',
    '象山': '030301',
    '北仑': '030401',
    '全椒': '040101',
    '来安': '040201',
    '界首': '040301',
    '颍上': '040401',
    '阜南': '040501',
    '太和': '040601',
    '临泉': '040701',
    '临颍': '050101',
    '滑县': '050201',
    '项城': '050301',
    '杞县': '050401',
    '淮阳': '050501',
    '沈丘': '050601',
    '石柱': '060101',
    '长寿': '060201',
    '合川': '060301',
    '奉节': '060401',
    '巫山': '060501',
    '万州': '060601',
    '城口': '060701',
    '涪陵': '060801',
    '垫江': '060901',
    '巫溪': '061001',
    '南岸': '061101',
    '安福': '070101',
    '宜丰': '070201',
    '上饶': '070301',
    '泰和': '070401',
    '新干': '070501',
    '乾县': '080101',
    '蒲城': '080201',
    '凤翔': '080301',
    '兴平': '080401',
    '汉滨': '080501',
    '城固': '080601',
    '蓝田': '080701',
    '睢宁': '090101',
    '吴江': '090201',
    '响水': '090301',
    '岳池': '100101',
    '蓬溪': '100201',
    '武胜': '100301',
    '邻水': '100401',
    '达川': '100501',
    '巴中': '100601',
    '郫都': '100701',
    '平川': '110101',
    '泾川': '110201',
    '习水': '120101',
    '赤水': '120201',
    '桐梓': '120301',
    '湄潭': '120401',
    '务川': '120501',
    '正安': '120601',
    '道真': '120701',
    '凤冈': '120801',
    '余庆': '120901',
    '镇赉': '130101',
    '汨罗': '140101',
    '通州': '150101',
    '大通': '160101',
    '西青': '170101',
    '达拉特': '180101',
    '龙岗': '190101'}

# proxies = {'http': 'http://H017W84J271F18FD:451D275088D7ABD3@proxy.abuyun.com:9020', 'https': 'http://H017W84J271F18FD:451D275088D7ABD3@proxy.abuyun.com:9020'}
# proxies = {}
mysqlClient = single_oracle

class RequestClass(object):
    def __init__(self, proxies):
        self.headers = {
            "User-Agent": random.choice(USER_AGENTS)

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
            logger.debug ("get: " + url + " proxies: " + str(kwargs["proxies"]))
            response = self.session.get(url=url, **kwargs)
        except Exception as e:
            logger.debug( e)
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
    con = requestsClass.request_url(url=url, headers=headers,proxies=proxies,timeout=6)
    logger.debug(con)
    if u"正在 请求 请 稍候" in con.text:
        time.sleep(2)
        url = re.search('.*href="(.*?)"', con.text).group(1)
        Referer = con.url
        headers["Referer"] = Referer
        con = requestsClass.request_url(url=url, headers=headers, timeout=6)

    return con

def get_branch_by_address(address):
    for strs in branch_list.keys():
        if strs in address:
            return branch_list[strs]

def web_parse(html, i, url):
    companuy11315ZYFD=Company_11315_ZYFD()
    companuy11315ZYFD.company_number = int(i)
    companuy11315ZYFD.url=url
    companuy11315ZYFD.add_time=datetime.now()
    if "您想浏览的网页找不到" in html or "入档信息更新" in html:
        # insert_value = ""
        # value_list = [str(i), url, str("NoCompany"), 'to_date('+str(datetime.now())+',"yyyy-mm-dd hh24:mi:ss")', str(0)]
        
        # companuy11315ZYFD.url=url
        companuy11315ZYFD.company_name="NoCompany"
        # companuy11315ZYFD.add_time=datetime.now()
        companuy11315ZYFD.mark=2
        companuy11315ZYFD.error=1
        # companuy11315ZYFD.company_number
        # value_list = ["'" + value +"'" if value else "'-'" for value in value_list ]
        # insert_value += '(' + ','.join(value_list) + '),'
        # insert_value = insert_value[0:-1]
        # column = "(company_number, url, company_name, add_time, mark)"

        mysqlClient.insert(companuy11315ZYFD)
        logger.info("此url不对应任何公司" + str(i))
    else:
        soup = BeautifulSoup(html, 'lxml')
        try:
            trs = soup.find('table', class_="v1Table01").find_all("tr")

            companuy11315ZYFD.company_industry = ""
            companuy11315ZYFD.company_area = ""
            companuy11315ZYFD. company_address = ""
            for tr in trs:
                if u"行  业" in tr.find("th").text.strip():
                    companuy11315ZYFD.company_industry = tr.find("td").text.strip()
                elif u"所在区域" in tr.find("th").text.strip():
                    companuy11315ZYFD.company_area = tr.find("td").text.strip()
                elif u"详细地址" in tr.find("th").text.strip():
                    companuy11315ZYFD.company_address = tr.find("td").text.replace("查看地图".decode("utf-8"), "").strip()

                    companuy11315ZYFD.company_name = trs[0].find_all("th")[1].get('title')

            insert_value = ""
            address_1 = address_2 = address_3=branch = ''
            if companuy11315ZYFD.company_name != "NoCompany" and companuy11315ZYFD.company_name != "None":
                companuy11315ZYFD.address_1, companuy11315ZYFD.address_2, companuy11315ZYFD.address_3 = addres_parse.company_parse(companuy11315ZYFD.company_area, companuy11315ZYFD.company_address )
                companuy11315ZYFD.branch=get_branch_by_address(address_3) or ''
            companuy11315ZYFD.add_time=datetime.now()
            companuy11315ZYFD.mark=0
            companuy11315ZYFD.error=0
            companuy11315ZYFD.parse=1
            # value_list = [str(i), url, company_name, company_industry, company_area, company_address,
            #               'to_date('+str(datetime.now())+',"yyyy-mm-dd hh24:mi:ss")', str(0), address_1, address_2, address_3,str(1),branch]
            # print(value_list)
            # logger.debug(value_list)
            # value_list = ["'" + value +"'" if value else "'-'" for value in value_list]
            # insert_value += '(' + ','.join(value_list) + '),'
            # insert_value = insert_value[0:-1]
            # column = "(company_number, url, company_name, company_industry, company_area, company_address, add_time, mark, address_1, address_2, address_3,parse,branch)"
            
            
            
            # mysqlClient.mysql_insert("company_11315", column, insert_value)
            mysqlClient.insert(companuy11315ZYFD)
        except Exception as e:
            logger.exception(e)
            insert_value = ""
            # value_list = [str(i), url, str(None), 'to_date('+str(datetime.now())+',"yyyy-mm-dd hh24:mi:ss")', str(0)]
            #
            # value_list = ["'" + value +"'" if value else "'-'" for value in value_list]
            # insert_value += '(' + ','.join(value_list) + '),'
            # insert_value = insert_value[0:-1]
            # column = "(company_number, url, company_name, add_time, mark)"
            companuy11315ZYFD.error=2
            companuy11315ZYFD.mark=2
            # mysqlClient.mysql_insert("company_11315", column, insert_value)
            mysqlClient.insert(companuy11315ZYFD)
            logger.info("返回页面内容不符合!" + str(i))


def main(args):
    print(u'启动',args)
    import sys

    reload(sys)
    # sys.setdefaultencoding('utf-8')
    # max_sql = 'SELECT Max(company_number) FROM company_11315 {}'
    # sql_1 = ' where company_number > 100000000 and company_number < 110000000 '
    # sql_2 = ' where company_number>110000000 '
    # sql_3 = ' where company_number<100000000 '
    # max = single_mysql.mysql_find_by_param(max_sql.format(sql_3))
    # if max[0] > 100000000:
    #     max = single_mysql.mysql_find_by_param(max_sql.format(sql_1))
    # if max[0] > 110000000:
    #     max = single_mysql.mysql_find_by_param(max_sql.format(sql_2))
    # i = max[0]
    # # argv = sys.argv
    # # i = int(argv[1])
    # # i = 80001222
    while True:
        i=single_reids.server.rpop('11315s')
        if not i:
            single_reids.put_11315()
            continue
        Retry = 1
        url = "http://" + str(i) + ".11315.com/"

        # 一个公司连接最多访问10次
        while Retry <= 10:
            logger.info(url + "------%d", Retry)

            try:
                con = web_spider(url)
            except requests.exceptions.ReadTimeout, requests.exceptions.ConnectionError :
                logger.info("访问超时或者连接出错")
                Retry += 1
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

            # 对访问状态及页面内容进行初步判断
            if con.status_code == 200:
                html = con.text.encode("utf-8")
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

    # 访问10次，标记访问失败
    # if Retry == 11:
    #     try:
    #         insert_value = ""
    #         value_list = [str(i), url, str(None), str(datetime.now()), str(0)]
    #
    #         value_list = ['"' + value + '"' for value in value_list]
    #         insert_value += '(' + ','.join(value_list) + '),'
    #         insert_value = insert_value[0:-1]
    #         column = "(company_number, url, company_name, add_time, mark)"
    #
    #         mysqlClient.mysql_insert("company_11315", column, insert_value)
    #     except:
    #         pass

if __name__ == "__main__":
    main(1)
