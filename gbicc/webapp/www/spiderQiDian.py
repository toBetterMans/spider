#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@author: niuweidong
@software: PyCharm
@file: spiderQiDian.py
@time: 2018/04/11 16:46
"""
import sys

import requests
from bs4 import BeautifulSoup

# 请求头字典
header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Cookie": "__cfduid=dd4f2cb7117a778d4d1ada2e19ffd4b611523435325; UM_distinctid=162b3d246a94e1-0059a99013fc5c-7314364b-144000-162b3d246aaed; CNZZDATA1271465101=335071612-1523430650-https%253A%252F%252Fwww.baidu.com%252F%7C1523430650",
    "Host": "www.biquge.cm",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3381.1 Safari/537.36"
}

base_url="http://www.biquge.cm/"
daming="9/9661/"
#请求书籍主页面
request_daming= requests.get(base_url+daming,params=header)
#soup转换
soup=BeautifulSoup(request_daming.text,"html.parser")
dl=soup.select("#wrapper .box_con #list dl")[0]
dd=dl.select("dd")
ff=open(u"C:\\Users\\niu\\Desktop\\爬爬爬.txt","ab+")
for i in dd:
    ss=i.a
    # mm=i.select("a")[0]
    ff.write(i.string)
    # print("ss.get  %s"%ss.get("href"))
    # print(u"%s"%mm  )
ff.close()
