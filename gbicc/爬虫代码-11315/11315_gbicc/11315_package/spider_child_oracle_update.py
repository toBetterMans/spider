# -*- coding:utf-8 -*-
import logging.config
import random
import re
import time

import requests
from bs4 import BeautifulSoup
from requests.packages import urllib3

from db import single_oracle, USER_AGENTS
from redis_cache_type import single_reids

# from request_file import RequestClass

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
oracleClient = single_oracle

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
    con = requestsClass.request_url(url=url, headers=headers, proxies=proxies, timeout=6)
    logger.debug(con)
    if u"正在 请求 请 稍候" in con.text:
        time.sleep(2)
        url = re.search('.*href="(.*?)"', con.text).group(1)
        Referer = con.url
        headers["Referer"] = Referer
        con = requestsClass.request_url(url=url, headers=headers, timeout=6)
    
    return con

# def get_branch_by_address(address):
#     for strs in branch_list.keys():
#         if strs in address:
#             return branch_list[strs]

# def detail_parse(html):
#     soup = BeautifulSoup(html, 'lxml')
#     detail_tbody = soup.find('div', id='main').find('tbody')
#     trs = detail_tbody.find_all('tr')
#
#     register_num = ''.join(trs[0].find('td').get_text(',').split(',')[::2])
#     ent_name = ''.join(trs[1].find('td').get_text(',').split(',')[::2])
#     company_type = ''.join(trs[2].find('td').get_text(',').split(',')[::2])
#     legal_representative = trs[3].find('td').get_text()
#     register_fund = ''.join(trs[4].find('td').get_text(',').split(',')[::2])
#     establish_date = '登陆可见'
#     residence = trs[6].find('td').get_text()
#     business_term_begin = trs[7].find('td').get_text()
#     business_term_end = trs[8].find('td').get_text()
#     business_scope = trs[9].find('td').get_text()
#     register_office = '登陆可见'
#     check_date = '登陆可见'
#     register_status = trs[12].find('td').get_text()
#     credit_num = trs[13].find('td').get_text()

def web_parse(index_soup, i, url):
    try:
        company_number = i
        logger.debug(type(index_soup))
        # trs = index_soup.find('table', class_="v1Table01").find_all("tr")
        detail_div = index_soup.find('div', class_='v1-business')
        if detail_div:
            
            
            
            
            
            detail_href = detail_div.find('a', href=re.compile("http://www.11315.com/cil/index/")).get('href')
            print(detail_href)
        else:
            oracleClient.oracle_update(
                "update {table} set error=4,searched=2 where company_number={company_number}".format(
                    company_number=company_number, table='company_11315'))
            oracleClient.oracle_update(
                "update {table} set error=4 ,searched=2 where company_number={company_number}".format(
                    company_number=company_number, table='company_11315_zyfd'))
            return
        # '''<a href="http://www.11315.com/cil/index/1429507736101" target="_blank">查看</a>'''
        
        detail_resp = web_spider(detail_href)
        if detail_resp.status_code == 200:
            # detail_parse(detail_resp.text)
            soup = BeautifulSoup(detail_resp.text, 'lxml')
            detail_tbody = soup.find('div', id='main').find('tbody')
            trs = detail_tbody.find_all('tr')
            num = len(trs)
            register_num = 'NA'
            ent_name = 'NA'
            company_type = 'NA'
            legal_representative = 'NA'
            register_fund = 'NA'
            residence = 'NA'
            business_term_begin = 'NA'
            business_term_end = 'NA'
            business_scope = 'NA'
            register_status = 'NA'
            credit_num = 'NA'
            detail_xpath = etree.HTML(detail_resp.text)
            # soup = BeautifulSoup(detail_resp.text, 'lxml')
            trs = detail_xpath.xpath('//div[@id="main"]//table/tbody/tr')
            # trs = detail_tbody.find_all('tr')
            num = len(trs)
            register_num = 'NA'
            # ent_name = 'NA'
            company_type = 'NA'
            legal_representative = 'NA'
            register_fund = 'NA'
            residence = 'NA'
            business_term_begin = 'NA'
            business_term_end = 'NA'
            business_scope = 'NA'
            register_status = 'NA'
            credit_num = 'NA'
            register_num = ''.join(trs[0].xpath('./td//text()')[::2])
            # ent_name = ''.join(trs[1].find('td').get_text(',').split(',')[::2])
            company_type = ''.join(trs[2].xpath('./td//text()')[::2])
            legal_representative = trs[3].xpath('./td')[0].xpath('string()')
            register_fund = ''.join(trs[4].xpath('./td//text()')[::2])
            if len(trs) > 6:
                residence = trs[6].xpath('./td/text()')
                business_term_begin = trs[7].xpath('./td/text()')
                business_term_end = trs[8].xpath('./td/text()')
                business_scope = trs[9].xpath('./td/text()')
                register_status = trs[12].xpath('./td/text()')
                credit_num = trs[13].xpath('./td/text()')
            sql = "update {table} set register_num = '{register_num}',company_type = '{company_type}',legal_representative = '{legal_representative}',register_fund = '{register_fund}',residence = '{residence}',business_term_begin = '{business_term_begin}',business_term_end = '{business_term_end}',business_scope = '{business_scope}',searched=2 ,register_status = '{register_status}',credit_num = '{credit_num}' where company_number={company_number}"
            
            oracleClient.oracle_update(
                sql.format(
                    company_type=company_type, register_num=register_num, legal_representative=legal_representative,
                    register_fund=register_fund, residence=residence, business_term_begin=business_term_begin,
                    business_term_end=business_term_end, business_scope=business_scope, register_status=register_status,
                    credit_num=credit_num, company_number=company_number, table='company_11315_zyfd'))
            oracleClient.oracle_update(
                sql.format(
                    register_num=register_num, company_type=company_type, legal_representative=legal_representative,
                    register_fund=register_fund, residence=residence, business_term_begin=business_term_begin,
                    business_term_end=business_term_end, business_scope=business_scope, register_status=register_status,
                    credit_num=credit_num, company_number=company_number, table='company_11315'))
    except Exception as e:
        logger.exception(e)
        oracleClient.oracle_update(
            "update {table} set error=4,searched=2 where company_number={company_number}".format(
                company_number=company_number, table='company_11315'))
        oracleClient.oracle_update(
            "update {table} set error=4 ,searched=2 where company_number={company_number}".format(
                company_number=company_number, table='company_11315_zyfd'))
        logger.info("返回页面内容不符合!" + str(company_number))

def main(args):
    print(u'启动', args)
    import sys
    
    reload(sys)
    while True:
        i = single_reids.server.rpop('11315_updates')
        if not i:
            single_reids.put_11315_update()
            continue
        Retry = 1
        url = "http://" + str(i) + ".11315.com/"
        
        # 一个公司连接最多访问10次
        while Retry <= 10:
            logger.info(url + "------%d", Retry)
            
            try:
                con = web_spider(url)
                # 对访问状态及页面内容进行初步判断
                if con and con.status_code == 200:
                    html = con.text.encode("utf-8")
                    index_soup = BeautifulSoup(html, 'lxml')
                    if "系统检测到您的请求存在异常" not in html and "你可能访问的太快了" not in html and "正在 请求 请 稍候" not in html:
                        try:
                            if index_soup == None or not index_soup:
                                continue
                            web_parse(index_soup, i, url)
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
                    # time.sleep(3)
                    continue
            except Exception as e:
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
            
           
    

if __name__ == "__main__":
    main(1)
