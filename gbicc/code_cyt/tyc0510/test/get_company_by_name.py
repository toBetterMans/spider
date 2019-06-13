# -*- encoding: utf-8 -*-
import random
import urllib
from urllib import parse

import requests
from bs4 import BeautifulSoup
from lxml import etree

from db import single_oracle
from redis_cache import single_redis
from request_file import RequestClass
from setting import USER_AGENTS

""" 
@author: niuweidong 
@software: PyCharm 
@file: get_company.py 
@time: 2018/09/12 16:02 
"""
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
        self.redisClient = single_redis
        self.tyc = RequestClass(proxies=proxies)
        self.mark_count = self.login()
        self.result_dicts = {}
        self.type = type
        self.phone=''

    def check_login(self, con):
        if con and con.status_code == 200 and 'antirobot' not in con.url:
            return True
        elif con.status_code == 404:
            print("userName: {}  forbid  status_code={}".format(self.username, con.status_code))
            return True
        elif not con or u"请输入您的手机号码" in con.text or con.status_code == 401 or '密码登录' in con.text:
            print("userName: {}  cookie失效！！  status_code={}".format(self.username, con.status_code))
            single_redis.server.hdel('cookies', self.tyc.username)
            single_redis.server.lpush('users', self.tyc.username)
            self.login()
            return False
        elif u"我们只是确认一下你不是机器人" in con.text or 'antirobot' in con.url:
            print("userName: {}  forbid  status_code={}".format(self.username, con.status_code))
            single_redis.put_cookies(phone=self.tyc.username, cookie=self.cookie, name='forbids')
            self.login()
            return False

    def login(self):
        self.username, self.cookie = self.tyc.login()
    
    def get_company_list(self, company_name):
        self.login()
        key = company_name
        # 网页抓取
        # logger.error("Search Company %s")
        url = "https://www.tianyancha.com/search?key=%s&checkFrom=searchBox" % parse.quote(key)
        try:
            con = self.tyc.request_url(url=url, headers=self.headers)
            # 判断账号是否被封
            if self.check_login(con):
                try:
                    # 解析公司列表页面，搜索信息存入mysql，并返回公司详情url
                    self.parse_company_list(company_name, con.text)
                    # logger.error(self.result_dicts)
                    return self.result_dicts
                except Exception as e:
                    self.get_company_list(company_name)
            else:
                self.get_company_list(company_name)
            # logger.error(e)
            # self.mysqlClient.mysql_update(cache['table'], {'searched': 1, 'error': 1},
            #                               {'company_number': cache['number']})
            # logger.error("Exception Logged{}".format(e))
        
        except requests.exceptions.ProxyError as error:
            
            # logger.error(error)
            # logger.error("Proxy Error! {}".format(error))
            self.get_company_list(company_name)
        except Exception as e:
            # logger.error(e)
            self.get_company_list(company_name)
    
    def parse_company_list(self, company_name, text=''):
        """
        如果第一行公司名称与输入key一致，则取第一行，否则遍历第一页，如果第一页都没有与输入key一致的，则还取第一行
        解析公司列表页面，存储基本信息到mysql，并返回公司名称和公司详情连接
        :param key: 关键字
        :param text: 网页内容
        :return: ent_name, url
        """
        # #logger.error('parse_company_list()')
        # logger.error("parse_company_list() {}".format(company_name))
        key = company_name
        
        soup = BeautifulSoup(text, 'lxml')
        etree_xpath = etree.HTML(text)
        div_first = soup.find('div', class_="search-item sv-search-company")
        if div_first:
            company_divs = soup.find_all('div', class_="search-result-single")
            ent_name = company_divs[0].img['alt']
            ent_name = ent_name.replace('<em>', '').replace('</em>', '').strip()
            if ent_name:
                ent_name = ent_name
            if self.type == 0:
                if key == ent_name:
                    pass
                else:
                    for company_div in company_divs:
                        ent_name = company_div.img['alt']
                        ent_name = ent_name.replace('<em>', '').replace('</em>', '').strip()
                        if key == ent_name:
                            div_first = company_div
                            break
            try:
                header_div = div_first.find('div', class_='header')
                if ent_name:
                    ent_name = ent_name
                url = header_div.find('a', class_="name")["href"].strip()
                self.get_detail(url, ent_name)
            except Exception as e:
                print(e)
                # logger.error("Exception Logged: {}".format(e))
        
        else:
            return 'None'
    
    def get_detail(self, url, key):
        """
        爬取公司详情页面，存入mongodb，解析详情并存入mysql
        :param ent_name: 公司名称
        :param url: 公司详情url
        :return:
        """
        # logger.error('get_detail() {}'.format(key))
        
        try:
            con = self.tyc.request_url(url=url, headers=self.headers)
            if self.check_login(con):
                self.parse_detail(con.text, key)
            else:
                self.get_detail(url,key)
        except requests.exceptions.ProxyError as error:
            # logger.error(error)
            self.login()
            self.get_detail(key, url)
            # logger.error("Proxy Error!", error)
        except Exception as e:
            # logger.error(e)
            # logger.error("Login false!")
            # logger.error("Exception Logged {}".format(e))
            print(e)
            self.login()
            self.get_detail(key, url)
    
    def parse_detail(self, text='', key=''):
        selectors = etree.HTML(text)
        top = (selectors.xpath('//div[@id="company_web_top"]'))
        baseinfo = {}
        table_lists = (selectors.xpath('//div[contains(@id,"_container_baseInfo")]//table'))
        if top:
            top = top[0]
            detail_basic = top.xpath(
                './/div[@class="box -company-box "]//div[@class="content"]//div[contains(@class,"detail")]')
            if detail_basic:
                detail_basic = detail_basic[0]
                telephone = detail_basic.xpath('./div/div/span//script/text()')
                if telephone:
                    self.phone=telephone[0]
                else:
                    self.phone=None

if __name__ == "__main__":
    r = ReqCompany('0')
    error_company=[]
    ok_company = []
    with open('./error_phone.txt','r+',encoding='utf-8') as f:
        ll=f.readlines()
        print(ll)
        for i in ll:
            error_company.append(i.split(':')[0])
    print(error_company)
    # res = single_oracle.oracle_find_by_param_all(sql)
    with open('./ok_phone.txt','r+',encoding='utf-8') as f:
        ll=f.readlines()
        print(ll)
        for i in ll:
            ok_company.append(i.split(':')[0])
    print(ok_company)
    with open('./compnay_phone.txt','w+') as f:
        ll=f.readlines()
        ll=[i.split(':')[0] for i in ll if i]
        for company_name in error_company:
            if company_name in ok_company:
                print('已有信息：{}'.format(company_name))
                continue
            ok_company.append(company_name)
            mm = r.get_company_list(company_name)
            print(r.phone)
            while '*' in r.phone:
                mm = r.get_company_list(company_name)
                print(r.phone)
            
            if r.phone :
                f.write(company_name+':'+r.phone.replace(
                    '"', '').replace('[', '').replace(']', '')+'\n')
        
            else:
                f.write(company_name + ':' +'无' + '\n')
        # logger.error(mm)
