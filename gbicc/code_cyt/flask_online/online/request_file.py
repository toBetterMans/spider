#!/usr/bin/env python
# -*- coding:utf-8 -*-
import random

import requests
from requests.packages import urllib3
from redis_cache import single_reids
urllib3.disable_warnings()  # 证书验证，如果不加这句话，还会有警告


class RequestClass(object):
    def __init__(self, proxies):
        self.headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Content-Type": "application/json; charset=UTF-8",
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3486.0 Safari/537.36",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Host ": "www.tianyancha.com"
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
        if url.startswith("https"):
            kwargs['verify'] = False
            retry_count = 0
            if "data" in kwargs:
                try:
                    print ("post: " + url + " proxies: " + str(kwargs["proxies"]))
                    response = self.session.post(url=url, **kwargs)
                except Exception as e:
                    print( e)
                    retry_count += 1
                    if (retry_count < 4):
                        response = self.session.post(url=url, **kwargs)
            else:
                try:
                    print ("get: " + url + " proxies: " + str(kwargs["proxies"]))
                    response = self.session.get(url=url, **kwargs)
                except Exception as e:
                    print( e)
                    retry_count += 1
                    if (retry_count < 4):
                        response = self.session.get(url=url, **kwargs)
            # print('request_file.......cookie=%s' % str(self.session.cookies))
            return response

    def get_cookies(self):
        # 将cookie转为字典
        cookie_dict = requests.utils.dict_from_cookiejar(self.session.cookies)
        return cookie_dict

    def set_cookies(self, cookie_dict):
        
        cookies = requests.utils.cookiejar_from_dict(cookie_dict, cookiejar=None, overwrite=True)
        self.session.cookies = cookies
        
    def set_cookies_kwargs(self, **kwargs):
        cookie_dict = self.get_cookies()
        for key, value in kwargs.items():
            cookie_dict[key] = value
        cookies = requests.utils.cookiejar_from_dict(cookie_dict, cookiejar=None, overwrite=True)
        self.session.cookies = cookies
    def login(self,):
        """
        :rtype : object
        """
        # self.username=single_reids.get_user()
    
        # self.cookie=single_reids.get_cookie(self.username)
        self.cookie = random.choice(single_reids.server.hgetall('cookies').values())
        
        if self.cookie:
            # cookie_dict = single_reids.server.rpop('cookies')
            print(self.cookie)
            self.set_cookies(cookie_dict=eval(self.cookie))
        else:
            self.login()
        return self.cookie
            
if __name__ == "__main__":
    tyc = RequestClass()
