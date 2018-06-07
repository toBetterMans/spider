# -*- coding:utf-8 -*-
import requests
from requests.packages import urllib3
urllib3.disable_warnings()  # 证书验证，如果不加这句话，还会有警告


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
            response = self.session.post(url=url, **kwargs)
        else:
            response = self.session.get(url=url, **kwargs)

        return response

    def get_cookies(self):
        cookie_dict = requests.utils.dict_from_cookiejar(self.session.cookies)
        return cookie_dict

    def set_cookies(self, **kwargs):
        cookie_dict = self.get_cookies()
        for key, value in kwargs.items():
            cookie_dict[key] = value
        cookies = requests.utils.cookiejar_from_dict(cookie_dict, cookiejar=None, overwrite=True)
        self.session.cookies = cookies


if __name__ == "__main__":
    tyc = RequestClass()