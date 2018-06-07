# -*- coding:utf-8 -*-
# !/usr/bin/env python
# from request_file import *
# import requests
from lxml import etree
import urllib2
# proxy = {'http': 'http://H017W84J271F18FD:451D275088D7ABD3@proxy.abuyun.com:9020'}
proxy={}
headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "max-age=0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.18 Safari/537.36"
}
url1 = "http://www.baidu.com/"
url2 = "https://www.tianyancha.com/"
req=urllib2.Request(url1,None,headers,proxy)
resp=urllib2.urlopen(req)
test=resp.read()

# /detect/what-is-my-ip-address
html=etree.HTML(test)
text=html.parse("//a[@href='/detect/what-is-my-ip-address']/text()")
print(text)
# requests.Request.headers = headers
# s = requests.Session()
# s.headers.update(headers)
# s.proxies.update(proxy)
# con1 = requests.get(url1,headers=headers)
# print con1.status_code
print("------------------------------------")
# con2 = s.get(url1)
print type(text)
# print( test.decode("gbk"))
# print test.decode("utf-8")
