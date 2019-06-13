#!/usr/bin/env python

import datetime
import logging.config
import random
import time
from urllib import parse

from bs4 import BeautifulSoup
# from fake_useragent import UserAgent
from lxml import etree

from db import single_mongodb, single_oracle
from request_file import *
from setting import proxy_pass, proxy_user, USER_AGENTS

urllib3.disable_warnings()
# ua=UserAgent()
logging.config.fileConfig("../log_file/search.conf")
logger = logging.getLogger("loggerTxt")
proxyHost = "http-dyn.abuyun.com"
proxyPort = "9020"

proxyUser = proxy_user
proxyPass = proxy_pass

proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
    "host": proxyHost,
    "port": proxyPort,
    "user": proxyUser,
    "pass": proxyPass,
}
proxies = {
    "http": proxyMeta,
    "https": proxyMeta,
}


# proxies = {}

def replace_special_string(strings=''):
    if not strings:
        return 'NA'
    return strings.replace(
        u'<em>',
        u'').replace(
        u'</em>',
        u'').replace(
        u'\ue004',
        u'').replace(
        u'\ufffd',
        u'').replace(
        u'\u2022',
        u'').replace(
        u'\xb3',
        u'').replace(
        u'\ue005',
        u'').replace(
        u'\xa9',
        '').replace(
        u'\u003C',
        u'').replace(
        u'\u003E',
        u'').replace(
        u'\ufffd',
        u'').replace(
        u'\ufffd',
        u'').replace(
        u'\xa9',
        u'').replace(
        u'\u002F',
        u'').replace(
        u'\u003E',
        u'').replace(
        u"'",
        u'"').replace(
        u'\u003c\u0065\u006d\u003e',
        u'').replace(
        u'\u003c\u002f\u0065\u006d\u003e',
        '').replace(
        u'\xa5',
        u'').replace(
        u'\xa0',
        u'').replace(r'\uff08', '(').replace(u'\u0029', ')').replace('（', '(').replace('）', ')')


class DetailSpider(object):
    def __init__(self):
        self.headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Content-Type": "application/json; charset=UTF-8",
            "X-Requested-With": "XMLHttpRequest",
            'User-Agent': random.choice(USER_AGENTS),
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Host ": "www.tianyancha.com"
        }
        self.count = 0
        self.username = ""
        self.password = ""
        self.tyc = RequestClass(proxies=proxies)

    def update_error(self, cache, error):
        if cache['table'] == '11315_company':
            cache['table'] = 'company_11315'
        update_sql = "update {} set searched=1,error={} where company_number='{}'".format(
            cache['table'], error, cache['number'])
        single_oracle.oracle_update(update_sql)

    def login(self):
        self.username, self.cookie = self.tyc.login()

    def check_login(self, con):
        if con and con.status_code == 200 and 'antirobot' not in con.url:
            return True

        elif not con or u"请输入您的手机号码" in con.text or u"我们只是确认一下你不是机器人" in con.text:
            logger.info("userName: {}  forbid  status_code={}".format(self.username, con.status_code))
            # single_oracle.oracle_update(
            #     "update tyc_user set user_forbid=1 ,user_used=0 where username='{}'".format(self.username))
            single_redis.server.hdel('cookies', self.tyc.username)
            if con.status_code == 401 or '密码登录' in con.text:
                logger.info('cookie失效！！！')
                single_redis.server.lpush('users', self.tyc.username)
            else:
                single_redis.put_cookies(phone=self.tyc.username, cookie=self.cookie, name='forbids')
            return False

    def get_company_list(self, cache={}):
        # self.login()
        key = cache['company_name']
        # 网页抓取
        logger.info("Search Company %s" % key)
        url = "https://www.tianyancha.com/search?key=%s&checkFrom=searchBox" % parse.quote(key)
        try:
            self.login()
            con = self.tyc.request_url(url=url, headers=self.headers)
            if self.check_login(con):
                logger.debug(con.url)
                self.parse_company_list(cache, con.text)
            else:
                logger.info("IP is forbid!")
                self.get_company_list(cache)
        except requests.exceptions.ProxyError as error:
            # print error

            logger.info("Proxy Error!{}".format(error))
        except Exception as e:
            self.update_error(cache, 1)
            logger.exception(e)
            self.get_company_list(cache)
            # 判断账号是否被封

    def parse_company_list(self, cache={}, text=''):
        """
        如果第一行公司名称与输入key一致，则取第一行，否则遍历第一页，如果第一页都没有与输入key一致的，则还取第一行
        解析公司列表页面，存储基本信息到mysql，并返回公司名称和公司详情连接
        :param key: 关键字
        :param text: 网页内容
        :return: ent_name, url
        """
        print('parse_company_list()')
        logger.info("Parse list page %s", cache['company_name'])
        key = cache['company_name']

        soup = BeautifulSoup(text, 'lxml')
        etree_xpath = etree.HTML(text)
        result_count = etree_xpath.xpath('//span[@class="tips-num"]/text()')
        # div_first = soup.find('div', class_="search_result_single") result_count
        div_first = soup.find('div', class_="search-item sv-search-company")
        div_none = soup.find('div', class_="result-list no-result")
        # print div_first.text.encode('utf8')
        if div_first:
            print('有div_first')

            # company_divs = etree_xpath.xpath('//div[@class="search-result-single   "]')
            company_divs = soup.find_all('div', class_="search-result-single")

            # ent_name = company_divs[0].xpath('.//img/@alt')[0]
            ent_name = company_divs[0].img['alt']
            ent_name = ent_name.replace('<em>', '').replace('</em>', '').strip()
            # ent_name = div_first.find('div').find('img').get('alt').replace('<em>', '').replace('</em>', '')

            # if key == ent_name:
            #     pass
            # else:
            #     # div_all = soup.find_all('div', class_="search-result-single ")
            #     # for div in div_all:
            #     #     if key == div.find('a', class_="name").get_text().strip():
            #     #         div_first = div
            #     #         break
            #     for company_div in company_divs:
            #         ent_name = company_div.img['alt']
            #         ent_name = ent_name.replace('<em>', '').replace('</em>', '').strip()
            #         if key == ent_name:
            #             div_first = company_div
            #             break
            try:
                header_div = div_first.find('div', class_='header')

                if not ent_name :
                    logger.info("Don't find this company--%s", key)
                    self.update_error(cache, 2)
                    return
                url = header_div.find('a', class_="name")["href"].strip() or 'None'
                status_type = header_div.find('div')
                if status_type:
                    status_type = status_type.text.strip() or 'None'
                div_info = div_first.find('div', class_="content").find('div', class_='info')
                legal_representative = div_info.find_all('div')[0].find('a')
                if legal_representative:
                    legal_representative = legal_representative.text.strip() or 'None'
                registered_capital = div_info.find_all('div')[1].find('span').text.strip() or 'None'
                registration_date = div_info.find_all('div')[2].find('span').text.strip() or 'None'
                try:
                    location = div_first.find('span', class_="site").text.strip() or 'None'
                except:
                    location = 'NA'
                try:
                    score = div_first.find('div', class_="score").find('span',
                                                                       class_='score-num').text.strip() + div_first.find(
                        'div', class_="score").find('span', class_='score-fen').text.strip() or 'None'
                except:
                    score = 'NA'
                match_text_ellipsis = div_first.find('div', class_='match.text-ellipsis')
                used_name = 'NA'
                if match_text_ellipsis:
                    if u'历史名称' in match_text_ellipsis:
                        used_name = match_text_ellipsis.get_text()
                mongo_result = self.get_detail(key, url, cache)
                while not mongo_result:
                    mongo_result = self.get_detail(key, url, cache)
                txt_id = mongo_result
                column = '(search_name,company_name,legal_representative,registered_capital,registration_date,location,score,used_name,status_type,url,txt_id)'

                insert_values = [key, ent_name, replace_special_string(legal_representative),
                                 replace_special_string(registered_capital), registration_date,
                                 location, score, replace_special_string(used_name), status_type, url, txt_id]
                logger.debug(insert_values)
                # single_oracle.oracle_insert_sql_param(create_insert_sql('company_basic_info',column,len(column.split(','))),insert_values)
                single_oracle.oracle_insert_param(
                    "insert into company_basic_info (search_name,company_name,legal_representative,registered_capital,registration_date,location,score,used_name,status_type,url,txt_id,add_time) values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}',sysdate)".format(
                        key, ent_name, replace_special_string(legal_representative),
                        replace_special_string(registered_capital), registration_date, location, score,
                        replace_special_string(used_name), status_type, url, txt_id))
                if cache['table'] == 'batch_detail':
                    update_sql = "update {} set searched=1,error=0,txt_id='{}' where company_number='{}'".format(
                        cache['table'], txt_id, cache['number'])
                    single_oracle.oracle_update(update_sql)

                else:
                    if cache['table'] == '11315_company':
                        cache['table'] = 'company_11315'
                    self.update_error(cache, 0)
            except Exception as e:
                self.update_error(cache, 1)
                logger.exception(e)

        else:
            logger.info("Don't find this company--%s", key)
            self.update_error(cache, 2)

    def get_detail(self, ent_name, url, cache={}):
        """
        爬取公司详情页面，存入mongodb，解析详情并存入mysql
        :param ent_name: 公司名称
        :param url: 公司详情url
        :return:
        """
        # print 'get_detail()', ent_name
        if cache['type'] == '11315':
            res = {"ent_name": ent_name, "url": url, "branch": cache['branch']}
            res['type'] = '11315'
        else:
            res = {"ent_name": ent_name, "url": url, 'agency_num': cache['agency_num'],
                   'agency_name': cache['agency_name'], 'batch': cache['batch']}
            res['type'] = 'batch_detail'
        logger.info("Spider detail info %s", ent_name)
        mark = 3
        while mark > 0:
            try:
                self.login()
                con = self.tyc.request_url(url=url, headers=self.headers)
                if self.check_login(con):
                    res["page_spide"] = 0
                    res["text"] = con.text
                    res["error_list"] = ""
                    res["addTime"] = datetime.datetime.now()
                    res["address"] = cache['address']
                    logger.info("Save detail html to mongodb %s", ent_name)
                    mongo_result = single_mongodb.mongodb_insert("company_detail_info", res)
                    return mongo_result
                else:
                    logger.info("IP is forbid!")
                    # time.sleep(60 * 60)
                    self.get_detail(ent_name, url, cache)
                mark = -1
            except requests.exceptions.ProxyError as error:
                print(error)
                mark -= 1
                logger.info("Proxy Error!%s" % error)
                continue
            except Exception as e:
                print(e)
                mark -= 1
                logger.info("Login false!")
                logger.exception("Exception Logged %s" % e)
                continue


def main(args):
    # reload(sys)
    # sys.setdefaultencoding('utf-8')
    print('starting tyc_company_search_A.py ......')
    # C:\Users\niu\AppData\Local\Temp\OraInstall2019-03-11_11-51-53AM
    count = 0
    while True:
        try:
            cache = single_redis.server.rpop('ents')
            if not cache:
                single_redis.put_company()
                cache = single_redis.server.rpop('ents')
            if cache == '()' or cache == 'None' or not cache:
                time.sleep(60 * 5)
                continue
            # if not isinstance(cache, str):
            #     logger.debug('cache 格式{} 不对！'.format(type(cache)))
            #     continue
            print(type(cache))
            cache = eval(cache)
            # cache={}
            # cache['company_name'] = '华为技术有限公司'
            ds = DetailSpider()
            ds.get_company_list(cache)
            single_redis.put_cookies(name='cookies', phone=str(ds.username), cookie=str(dict(ds.tyc.session.cookies)))
            ds.count += 1
            if ds.count == 44:
                ds.login()
            del ds
        except Exception as e:
            logger.exception("Exception Logged {}".format(e))


if __name__ == "__main__":
    main(1)
