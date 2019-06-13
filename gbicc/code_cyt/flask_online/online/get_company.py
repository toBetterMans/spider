#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import logging
import random
import re
import sys
import urllib
from imp import reload
from io import BytesIO

import requests
from bs4 import BeautifulSoup
from fontTools import ttLib
from lxml import etree

from redis_cache import single_reids
from request_file import RequestClass
from setting import USER_AGENTS

# import reTest
reload(sys)
sys.setdefaultencoding('utf-8')
# from db import *

""" 
@author: niuweidong 
@software: PyCharm 
@file: get_company.py 
@time: 2018/09/12 16:02 
"""
logging.config.fileConfig('../log_file/get_company.conf')

logger = logging.getLogger('loggerTxt')


# logging.config.fileConfig("../log_file/companySearchLogA.conf")
# logger = logging.getLogger("loggerTxt")

def decode_dict_date(word, dicts):
    logger.error('decode_dict_date  yuan=== {}'.format(word))
    try:
        new_word = ''
        for i in word:
            if i in dicts.keys():
                new_word += dicts[i]
            else:
                new_word += i
        logger.error('decode_dict_date  xin====={}'.format(new_word))
        return new_word
    except Exception as e:
        logger.error(e)
        new_word = word
    return new_word


def decode_dict_money(word, dicts):
    logger.error('yuan==={}'.format(word))

    if '人' in word or '币' in word:
        word = word[0:-4] + '万人民币'
    else:
        word = word[0:-3] + '万美元'

    new_word = ''
    try:
        for i in word:
            if i in dicts.keys():
                new_word += dicts[i]
            else:
                new_word += i
        logger.error('xin====={}'.format(new_word))
        return new_word
    except Exception as e:
        logger.error(e)
        new_word = word
    return new_word


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
    "http": proxyMeta,
    "https": proxyMeta,
}


# proxies = {}


class ReqCompany(object):
    def __init__(self, type):
        self.headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Content-Type": "application/json; charset=UTF-8",
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent": random.choice(USER_AGENTS),
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Host ": "www.tianyancha.com"
        }
        self.redisClient = single_reids
        self.tyc = RequestClass(proxies=proxies)
        self.mark_count = self.login()
        self.result_dicts = {}
        self.type = type

    def get_dict(self, font_url):
        logger.error('字典url={}'.format(font_url))
        dicts = {}
        mm = self.tyc.session.get('https://static.tianyancha.com/fonts-styles/fonts/{}/tyc-num.woff'.format(font_url),
                                  headers={
                                      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3486.0 Safari/537.36'},
                                  proxies=proxies)
        # with open('./fonts.woff', "wb") as f:
        #     f.write(mm.content)

        tt = ttLib.TTFont(BytesIO(mm.content))
        names = tt.getGlyphNames()[:10]
        orders = tt.getGlyphOrder()[2:12]

        for i in range(len(names)):
            dicts[orders[i]] = names[i]
        return dicts

    def login(self):
        self.cookie = self.tyc.login()

    def get_dict(self, font_url):
        logger.error('字典url={}'.format(font_url))
        dicts = {}
        # font_url = '88/88b54b20'
        mm = self.tyc.session.get('https://static.tianyancha.com/fonts-styles/fonts/{}/tyc-num.woff'.format(font_url),
                                  headers={
                                      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3486.0 Safari/537.36'})
        with open('./fonts.woff', "wb") as f:
            f.writelines(mm.content)
        from fontTools import ttLib

        # tt = ttLib.TTFont("fonts.woff")
        tt = ttLib.TTFont(BytesIO(mm.content))
        names = tt.getGlyphNames()[:10]
        orders = tt.getGlyphOrder()[2:12]
        logger.error(names)
        logger.error(tt.getGlyphNames())
        logger.error(tt.getGlyphOrder())
        logger.error(orders)
        for i in range(len(names)):
            dicts[orders[i]] = names[i]
        return dicts

    def get_company_list(self, company_name):
        key = company_name
        # 网页抓取
        logger.error("Search Company %s")
        url = "https://www.tianyancha.com/search?key=%s&checkFrom=searchBox" % urllib.quote(key)
        try:
            con = self.tyc.request_url(url=url, headers=self.headers)
            # 判断账号是否被封
            if con.status_code != 403:
                if u"请输入您的手机号码" in con.text or u"我们只是确认一下你不是机器人" in con.text or con is None or con.status_code != 200:
                    logger.error("userName: {}  forbid ".format(self.username))
                    # logger.error ("userName: %s  forbid " % con.text)
                    single_reids.server.lpush('forbids', self.cookie)
                    self.login()
                    raise requests.exceptions.ProxyError
                try:
                    # 解析公司列表页面，搜索信息存入mysql，并返回公司详情url
                    self.parse_company_list(company_name, con.text)
                    logger.error(self.result_dicts)
                    return self.result_dicts
                except Exception as e:
                    logger.error(e)
                    # self.mysqlClient.mysql_update(cache['table'], {'searched': 1, 'error': 1},
                    #                               {'company_number': cache['number']})
                    logger.error("Exception Logged{}".format(e))
            else:
                logger.error("IP is forbid!")
                # time.sleep(60 * 60)
                raise requests.exceptions.ProxyError
        except requests.exceptions.ProxyError as error:
    
            logger.error(error)
            logger.error("Proxy Error! {}".format(error))
            self.get_company_list(company_name)
        except Exception as e:
            logger.error(e)
            self.get_company_list(company_name)

    def parse_company_list(self, company_name, text=''):
        """
        如果第一行公司名称与输入key一致，则取第一行，否则遍历第一页，如果第一页都没有与输入key一致的，则还取第一行
        解析公司列表页面，存储基本信息到mysql，并返回公司名称和公司详情连接
        :param key: 关键字
        :param text: 网页内容
        :return: ent_name, url
        """
        # logger.error('parse_company_list()')
        logger.error("parse_company_list() {}".format(company_name))
        key = company_name

        soup = BeautifulSoup(text, 'lxml')
        etree_xpath = etree.HTML(text)
        result_count = etree_xpath.xpath('//span[@class="tips-num"]/text()')
        # div_first = soup.find('div', class_="search_result_single") result_count
        div_first = soup.find('div', class_="search-item sv-search-company")
        div_none = soup.find('div', class_="result-list no-result")
        # print div_first.text.encode('utf8')
        # sdfsdfsfdsf
        if div_first:
            # print '有div_first'
            # ent_name = div_first.find('div', class_='header').find('a', class_="name").text.strip()
            company_divs = soup.find_all('div', class_="search-result-single")

            # ent_name = company_divs[0].xpath('.//img/@alt')[0]
            ent_name = company_divs[0].img['alt']
            ent_name = ent_name.replace('<em>', '').replace('</em>', '').strip()

            if ent_name:
                ent_name = ent_name.encode('utf-8')
            if self.type == 0:
                if key == ent_name:
                    pass
                else:
                    # div_first = soup.find_all('div', class_="search-result-single")
                    for company_div in company_divs:
                        ent_name = company_div.img['alt']
                        ent_name = ent_name.replace('<em>', '').replace('</em>', '').strip()
                        if key == ent_name:
                            div_first = company_div
                            break
            try:
                header_div = div_first.find('div', class_='header')
                # ent_name = header_div.find('a', class_="name").text.strip()
                if ent_name:
                    ent_name = ent_name.encode('utf-8')
                url = header_div.find('a', class_="name")["href"].strip()
                self.get_detail(url, ent_name)


            except Exception as e:
                logger.error(e)
                # self.mysqlClient.mysql_update(cache['table'], {'searched': 1, 'error': 1},
                #                               {'company_number': cache['number']})
                logger.error("Exception Logged: {}".format(e))

        else:
            logger.error(soup.prettify())
            logger.error("can't find this company--{}".format(key))
            # logger.error('无公司', key)
            return 'None'
            # self.mysqlClient.mysql_update(cache['table'], {'searched': 1, 'error': 2},
            #                               {'company_number': cache['number']})

    def get_detail(self, url, key):
        """
        爬取公司详情页面，存入mongodb，解析详情并存入mysql
        :param ent_name: 公司名称
        :param url: 公司详情url
        :return:
        """
        logger.error('get_detail() {}'.format(key))

        try:
            con = self.tyc.request_url(url=url, headers=self.headers)
            if con.status_code != 403:
                if u"请输入您的手机号码" in con.text or u"我们只是确认一下你不是机器人" in con.text or con is None or con.status_code != 200:
                    self.login()
                    raise requests.exceptions.ProxyError
                    single_reids.server.lpush('forbids', self.cookie)
                self.parse_detail(con.text, key)
            else:
                logger.error("IP is forbid!")
                raise requests.exceptions.ProxyError
        except requests.exceptions.ProxyError as error:
            logger.error(error)
            self.get_detail(key, url)
            logger.error("Proxy Error!", error)
        except Exception as e:
            logger.error(e)
            logger.error("Login false!")
            logger.error("Exception Logged {}".format(e))

            self.get_detail(key, url)

    def parse_detail(self, text='', key=''):
        re_fonts = re.compile(
            r'<link rel="stylesheet" href="https://static.tianyancha.com/fonts-styles/css/(.*?)/font.css">')
        font_uri = re_fonts.search(text).group(1)
        dicts = self.get_dict(font_uri)
        logger.error("Parse detail info 基本信息 ")
        selectors = etree.HTML(text)
        top = (selectors.xpath('//div[@id="company_web_top"]'))
        baseinfo = {}
        table_lists = (selectors.xpath('//div[contains(@id,"_container_baseInfo")]//table'))
        if top:
            top = top[0]
            email = top.xpath('.//span[@class="email"]/text()')
            email = email[0] if email else '-'
            detail_basic = top.xpath(
                './/div[@class="box -company-box "]//div[@class="content"]//div[contains(@class,"detail")]')
            if detail_basic:
                detail_basic = detail_basic[0]
                telephone = detail_basic.xpath('./div[position()=1]/div[position()=1]/span[2]/text()')[0]
                telephone = telephone
                urls = detail_basic.xpath('./div[position()=2]//a[@class="company-link"][position()=1]/text()')
                url = '' or urls[0] if urls else 'NA'

            if table_lists:
                trs0 = table_lists[0].xpath('./tbody//tr')
                trs1 = table_lists[1].xpath('./tbody//tr')
                if trs0:
                    # dict_list
                    registerFund = trs1[0].xpath('./td[2]//@title')[0] or 'NA'
                    companyStatus = trs1[1].xpath('./td[2]//text()')[0]
                    registerNum = trs1[1].xpath('./td[4]//text()')[0]
                    tissueNum = trs1[2].xpath('./td[position()=4]/text()')[0]
                    creditNum = trs1[2].xpath('./td[position()=2]/text()')[0]
                    companyType = trs1[3].xpath('./td[position()=4]/text()')[0]
                    taxpayerNum = trs1[3].xpath('./td[position()=2]/text()')[0]
                    industry = trs1[4].xpath('./td[position()=4]/text()')[0]
                    businessTerm = trs1[4].xpath('./td[position()=2]/span/text()')[0]
                    registerDate = trs1[0].xpath('./td[position()=4]//text()')[0] or ''

                    checkDate = trs1[5].xpath('./td[position()=4]//text()')[0]
                    regDate = ''.join(registerDate.strip('-'))
                    checDate = ''.join(checkDate.strip('-'))
                    if dicts:
                        if regDate > '2019' or regDate < '1950':
                            registerDate = decode_dict_date(registerDate, dicts)
                        if checDate > '2019' or checDate < '1950':
                            checkDate = decode_dict_date(checkDate, dicts)

                    businessTerm = businessTerm
                    registerDate = registerDate
                    checkDate = checkDate
                    registerOffice = trs1[7].xpath('./td[position()=4]//text()')[0]
                    englishName = trs1[8].xpath('./td[position()=4]//text()')[0].replace("'", '"')
                    registerSite = trs1[8].xpath('./td[position()=2]//text()')[0]
                    businessScope = trs1[9].xpath(
                        './td[position()=2]/span//text()')
                    businessScope = businessScope[0].replace("'", '') if businessScope else '-'

                    # 新增 纳税人资质
                    taxQualificate = trs1[5].xpath('./td[position()=2]//text()')
                    taxQualificate = taxQualificate[0] if taxQualificate else '-'
                    # 人员规模
                    persionSize = trs1[6].xpath('./td[position()=4]//text()')[0]
                    # 实缴资本：
                    paidCapital = trs1[6].xpath('./td[position()=2]//text()')[0]
                    # 参保人数：
                    insuredPersion = trs1[7].xpath('./td[position()=2]//text()')[0]

                    entName = key
                    # baseinfo['COMPANYSTATUS'] = trs0[2].xpath('./td/div[position()=2]/text()')[0]

                    baseinfo['REGISTERFUND'] = registerFund.split(u'万')[0] + '0000'
                    if u'人民币' in registerFund:

                        baseinfo['CURRENCY'] = 'CNY'
                    elif u'美元' in registerFund:
                        baseinfo['CURRENCY'] = 'USD'
                    # baseinfo['TISSUENUM'] = trs1[0].xpath('./td[position()=4]/text()')[0]
                    baseinfo['CREDITNUM'] = creditNum
                    baseinfo['COMPANYTYPE'] = companyType
                    baseinfo['LOCALTAXPAYERNUM'] = taxQualificate
                    baseinfo['COUNTRYTAXPAYERNUM'] = taxQualificate

                    baseinfo['INDUSTRY'] = industry
                    BUSINESSTERM = businessTerm
                    baseinfo['STARTDATE'] = BUSINESSTERM[:10]
                    baseinfo['VALIDATEDATE'] = BUSINESSTERM[-10:]

                    registerDate = registerDate
                    baseinfo['REGISTERDATE'] = decode_dict_date(registerDate, dicts)
                    # baseinfo['checkDate'] = decode_dict_date(checkDate, dicts)

                    # baseinfo['ENGLISHNAME'] = trs1[6].xpath('./td[position()=4]/text()')[0]
                    baseinfo['REGISTERSITE'] = registerSite
                    baseinfo['ADDRESS'] = baseinfo['REGISTERSITE']
                    baseinfo['BUSINESSSCOPE'] = businessScope
                    baseinfo['ENTNAME'] = entName
                    # logger.error(baseinfo)
                    self.result_dicts = baseinfo


if __name__ == "__main__":
    r = ReqCompany('0')
    mm = r.get_company_list('北京当当网信息技术有限公司')
    logger.error(mm)
