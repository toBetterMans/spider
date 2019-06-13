# -*- coding:utf-8 -*-
#!/usr/bin/env python
import datetime
import requests
from requests.packages import urllib3
from selenium.webdriver.remote import webdriver

urllib3.disable_warnings()
driver = webdriver.Remote("http://localhost:4444/wd/hub", webdriver.DesiredCapabilities.HTMLUNIT)
proxy = {'http': 'http://H017W84J271F18FD:451D275088D7ABD3@proxy.abuyun.com:9020'}
# proxy = {}
class RequestClass(object):
    def __init__(self, proxies):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
        }
        self.proxies = proxies
        self.session = requests.session()

    def request_url(self, url, **kwargs):
        if "headers" not in kwargs:
            kwargs['headers'] = self.headers

        if "proxies" not in kwargs:
            kwargs['proxies'] = self.proxies

        if url.startswith("https"):
            kwargs['verify'] = False

        if "data" in kwargs:
            print "post: " + url + " proxies: " + str(kwargs["proxies"])
            response = self.session.post(url=url, **kwargs)
        else:
            print "get: " + url + " proxies: " + str(kwargs["proxies"])
            response = self.session.get(url=url, **kwargs)
        return response

class DetailSpider(object):
    def __init__(self):
        self.headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Host": "www.qichacha.com/",
            "Referer": "https://www.qichacha.com/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)         Chrome/67.0.3396.10 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest"
        }
        self.count = 0
        self.username = ""
        self.password = ""
        self.tyc = RequestClass(proxies=proxy)
        print(proxy)

    def login(self):
        """
        :rtype : object
        """
        parameters = {
            "user_used": 0,
            "user_forbid": 0,
            "update_time": str(
                datetime.datetime.now() -
                datetime.timedelta(
                    hours=25))}

        # url_login = "https://www.tianyancha.com/cd/login.json"
        url_login = "http://www.qichacha.com/"
        try:
            con_login = self.tyc.request_url(
                url=url_login, headers=self.headers)
            print(con_login)
            print(con_login.text)
        except requests.exceptions.ProxyError as error:
            pass
        except Exception as e:
            pass
        if con_login.status_code != 200:
            return False
        text = con_login.text
        print(text)

if __name__ == "__main__":
    import sys
    reload(sys)
    sys.setdefaultencoding('utf-8')
    ds = DetailSpider()
    ds.login()
