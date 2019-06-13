#!/usr/bin/env python
# -*- coding:utf-8 -*-
import logging.config
import random
import time
from urllib import parse

from db import USER_AGENTS
from request_file import *
from setting import proxy_pass, proxy_user

urllib3.disable_warnings()

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

# proxies={}


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

    def login(self):
        self.username, self.cookie = self.tyc.login()

    def get_company_list(self, cache=''):
        self.login()
        key = cache
        # 网页抓取
        logger.info("Search Company %s" % key)
        url = "https://www.tianyancha.com/search?key=%s&checkFrom=searchBox" % parse.quote(key)
        try:
            
            con = self.tyc.request_url(url=url, headers=self.headers)
            logger.debug(con.text)
            if con.status_code != 403:
                
                if 'login' in con.url:
                    logger.debug('cookie {}  未登录！'.format(self.cookie))
                    self.get_company_list(cache)
                if u"请输入您的手机号码" in con.text or u"我们只是确认一下你不是机器人" in con.text or con is None or con.status_code != 200:
                    logger.info("userName: %s  forbid " % self.username)
                    print("userName: %s  forbid " % self.username)
                    single_redis.server.hdel('cookies', self.tyc.username)
                    single_redis.put_cookies(phone=self.tyc.username, cookie=self.cookie, name='forbids')
                    self.login()
                    return None
                    # 解析公司列表页面，搜索信息存入mysql，并返回公司详情url
                logger.debug(con.url)

                # self.parse_company_list(cache, con.text)
                # self.update_error(cache, 1)
                # logger.exception("Exception Logged={}".format(e))
            else:
                logger.info("IP is forbid!")
                self.get_company_list(cache)
        except requests.exceptions.ProxyError as error:
            # print error

            logger.info("Proxy Error!{}".format(error))
        except Exception as e:
            logger.exception(e)
            self.get_company_list(cache)
        # 判断账号是否被封

def main(args):
    # import sys

    # reload(sys)
    # sys.setdefaultencoding('utf-8')
    # print 'starting tyc_company_search_A.py ......'
    # C:\Users\niu\AppData\Local\Temp\OraInstall2019-03-11_11-51-53AM
    count = 0
    while True:
        try:
    
            # cache['company_name'] = cache['company_name']
            company_name = '吉贝克'
            ds = DetailSpider()
            ds.get_company_list(company_name)
            single_redis.put_cookies(name='cookies', phone=str(ds.username), cookie=str(dict(ds.tyc.session.cookies)))
            ds.count += 1
            if ds.count == 44:
                ds.login()
            del ds
            time.sleep(20)
        except Exception as e:
            logger.exception("Exception Logged {}".format(e))
if __name__ == "__main__":
    main(1)
