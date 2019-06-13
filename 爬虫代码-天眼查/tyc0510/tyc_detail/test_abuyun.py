#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests

from setting import proxy_user, proxy_pass

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
def main(args):
    # import sys
    
    # reload(sys)
    # sys.setdefaultencoding('utf-8')
    # print 'starting tyc_company_search_A.py ......'
    # C:\Users\niu\AppData\Local\Temp\OraInstall2019-03-11_11-51-53AM
    count = 0
    try:
       con= requests.get('http://test.abuyun.com/',proxies=proxies)
       print(con.text)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main(1)
