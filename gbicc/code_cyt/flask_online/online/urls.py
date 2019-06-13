#!/usr/bin/env python  
# -*- encoding: utf-8 -*-
import time

import requests

"""
@author: niuweidong 
@software: PyCharm 
@file: urls.py 
@time: 2018/11/19 16:51 
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
proxie = 'http://httpapi.datatocrm.com/index.php?token=niuweidong'
proxies = {
    "http": proxyMeta
}

def func():
    url = 'http://92h.me/portal.php?x=125565'
    headers = {
        
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3486.0 Safari/537.36'
    }
    
    con=requests.get(url=url,headers=headers,proxies=proxies)
    # print(con.text)
    time.sleep(2)
    son1=requests.get(url='http://p86.me/?fromuid=125565',headers=headers,proxies=proxies)
    
    
    # print(son1.text)

class Main():
    
    def __init__(self):
        pass

if __name__ == "__main__":
    i=0
    while True:
        print(i)
        try:
            
            func()
        except:
            print(Exception)
        time.sleep(5)
        i+=1
