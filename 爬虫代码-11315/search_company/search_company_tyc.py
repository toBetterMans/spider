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
from fake_useragent import UserAgent
import requests
ua=UserAgent()
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
sessin.headers={
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Content-Type": "application/json; charset=UTF-8",
            "X-Requested-With": "XMLHttpRequest",
            'User-Agent': ua.random,
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Cookie": "aliyungf_tc=AQAAAOGB0Xkx7w0A4ycTJOKU2YOWPubu; csrfToken=NvwnUMPXoZZRgNg1_dXcOhJq; TYCID=408557303fe211e9ac26db09b0d3d13e; undefined=408557303fe211e9ac26db09b0d3d13e; ssuid=7092339507; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1551400942,1551411517,1551774145,1551857428; _ga=GA1.2.2064289855.1551857660; _gid=GA1.2.1599629821.1551857660; __insp_wid=677961980; __insp_nv=true; __insp_targlpu=aHR0cHM6Ly93d3cudGlhbnlhbmNoYS5jb20vc2VhcmNoP2tleT0lRTQlQjklOTAlRTglQTclODY%3D; __insp_targlpt=5LmQ6KeGX_ebuOWFs_aQnOe0oue7k_aenC3lpKnnnLzmn6U%3D; __insp_norec_sess=true; bannerFlag=true; token=d1841f2bfffc49678c3395a5735ff8e4; _utm=843745cc824b410c8200750220aca4f4; tyc-user-info=%257B%2522claimEditPoint%2522%253A%25220%2522%252C%2522myAnswerCount%2522%253A%25220%2522%252C%2522myQuestionCount%2522%253A%25220%2522%252C%2522explainPoint%2522%253A%25220%2522%252C%2522privateMessagePointWeb%2522%253A%25220%2522%252C%2522nickname%2522%253A%2522%25E6%2596%2587%25E6%25A0%25B9%25E8%258B%25B1%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522privateMessagePoint%2522%253A%25220%2522%252C%2522state%2522%253A%25220%2522%252C%2522announcementPoint%2522%253A%25220%2522%252C%2522isClaim%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522discussCommendCount%2522%253A%25221%2522%252C%2522monitorUnreadCount%2522%253A%2522185%2522%252C%2522onum%2522%253A%25220%2522%252C%2522claimPoint%2522%253A%25220%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMzQwODYxMTg3MyIsImlhdCI6MTU1MTg1NzY3MywiZXhwIjoxNTY3NDA5NjczfQ.7E1LpfhRC9dn5FSUYe-cu-UBu-FaQz48eNlRdSGjC-DV4E6iC0DyiJ7eZowipgBAa_pHdGxJKaLdfS2hqqHE4w%2522%252C%2522pleaseAnswerCount%2522%253A%25221%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522bizCardUnread%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252213408611873%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMzQwODYxMTg3MyIsImlhdCI6MTU1MTg1NzY3MywiZXhwIjoxNTY3NDA5NjczfQ.7E1LpfhRC9dn5FSUYe-cu-UBu-FaQz48eNlRdSGjC-DV4E6iC0DyiJ7eZowipgBAa_pHdGxJKaLdfS2hqqHE4w; refresh_page=null; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1551857677; __insp_slim=1551857676991",
            "Host ": "www.tianyancha.com"
        }
def get_company_list():
    company_list = []
    with open('company_11315.txt') as f:
        company_list = f.readlines()
    return company_list

'''

'''
def search_company(companys):
    url = "https://www.tianyancha.com/search?key={}&checkFrom=searchBox"
    result_dict = {}
    not_list=[]
    with open('result.txt', 'w+') as f:
        for company in companys:
            try:
                company = company.strip().replace(r'\n', '')
                resp = sessin.get(url.format(urllib.quote(company)),headers={})
                print(resp.status_code)
                if resp.status_code == 200:
                    text = etree.HTML(resp.text)
                    result_count = text.xpath('//div[@id="search"]/span[@class="tips-num"]/text()')
                    result_dict[company] = result_count[0]
                    print('企业：{}， 结果：{}'.format(company, result_count[0]))
                else:
                    not_list.append(company)
            except Exception as e:
                not_list.append(company)
                print(e)
        print(result_dict)
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
