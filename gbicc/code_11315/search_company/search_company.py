#!/usr/bin/env python  
# -*- encoding: utf-8 -*-  

""" 
@author: niuweidong 
@software: PyCharm 
@file: search_company.py 
@time: 2019/03/06 9:24 
"""
import urllib
from lxml import etree

import requests

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
sessin = requests.session()
sessin.proxies = proxies

def get_company_list():
    company_list = []
    with open('company_11315.txt') as f:
        company_list = f.readlines()
    return company_list

def search_company(companys):
    
    result_dict = {}
    not_list=[]
    for company in companys:
        try:
            company = company.strip().replace(r'\n', '')
            resp = sessin.get('http://www.11315.com/newsearch?name={}'.format(urllib.quote(company)))
            print(resp.status_code)
            if resp.status_code == 200:
                text = etree.HTML(resp.text)
                result_count = text.xpath('//p[@class="title_top title_name"]/a/text()')
                result_dict[company] = result_count[0]
                print('企业：{}， 结果：{}'.format(company, result_count))
            else:
                not_list.append(company)
        except Exception as e:
            not_list.append(company)
            print(e)
    print(result_dict)
    with open('result.txt', 'w+') as f:
        f.write(result_dict)
    if not_list:
        search_company(not_list)
    else:
        print('已搜索完！！')
class Main():
    
    def __init__(self):
        pass

if __name__ == "__main__":
    companys = get_company_list()
    search_company(companys)
