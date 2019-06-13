# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re
import time
from datetime import datetime
import logging.config
from db import *
from request_file import RequestClass

logging.config.fileConfig("../log_file/11315SpiderLog.conf")
logger = logging.getLogger("loggerTxt")

# 代理服务器
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


# proxies = {'http': 'http://H017W84J271F18FD:451D275088D7ABD3@proxy.abuyun.com:9020', 'https': 'http://H017W84J271F18FD:451D275088D7ABD3@proxy.abuyun.com:9020'}
# proxies = {}
# #mysqlClient = #mysqlClient()


def web_spider(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
    }
    requestsClass = RequestClass(proxies=proxies)
    con = requestsClass.request_url(url=url, timeout=6)

    if u"正在 请求 请 稍候" in con.text:
        time.sleep(2)
        url = re.search('.*href="(.*?)"', con.text).group(1)
        Referer = con.url
        headers["Referer"] = Referer
        con = requestsClass.request_url(url=url, headers=headers, timeout=6)

    return con


def web_parse(soup, url):
    if "您想浏览的网页找不到" in html or "入档信息更新" in html:
        pass
    else:

        try:

            trs = soup.find('div',_class='files_cen')

            company_industry = ""
            company_area = ""
            company_address = ""
            for tr in trs:
                if u"行　　业" in tr.find("th").text.strip():
                    company_industry = tr.find("td").text.strip()
                elif u"所在区域" in tr.find("th").text.strip():
                    company_area = tr.find("td").text.strip()
                elif u"详细地址" in tr.find("th").text.strip():
                    company_address = tr.find("td").text.replace("查看地图".decode("utf-8"), "").strip()

            company_name = trs[0].find_all("th")[1].text.strip()

            #insert_value = ""
            #value_list = [str(i), url, company_name, company_industry, company_area, company_address,
                          # str(datetime.now()), str(0)]

            #value_list = ['"' + value + '"' for value in #value_list]
            #insert_value += '(' + ','.join(#value_list) + '),'
            #insert_value = #insert_value[0:-1]
            column = "(company_number, url, company_name, company_industry, company_area, company_address, add_time, mark)"

            #mysqlClient.mysql_insert("11315_company", column, #insert_value)
        except Exception:
            #insert_value = ""
            #value_list = [str(i), url, str(None), str(datetime.now()), str(0)]

            #value_list = ['"' + value + '"' for value in #value_list]
            #insert_value += '(' + ','.join(#value_list) + '),'
            #insert_value = #insert_value[0:-1]
            column = "(company_number, url, company_name, add_time, mark)"

            #mysqlClient.mysql_insert("11315_company", column, #insert_value)
            logger.info("返回页面内容不符合!" + str(i))


if __name__ == "__main__":
    import sys

    reload(sys)
    sys.setdefaultencoding('utf-8')
    urls = ['http://0394hyx.11315.com/']
    # argv = sys.argv
    # i = argv[1]
    for url in urls:


        try:
            con = web_spider(url)
            # 对访问状态及页面内容进行初步判断
            if con.status_code == 200:
                html = con.text.encode("utf-8")
                if "系统检测到您的请求存在异常" not in html and "你可能访问的太快了" not in html and "正在 请求 请 稍候" not in html:
                    try:
                        soup = BeautifulSoup(html, 'lxml')
                        web_parse(soup, url)

                    except Exception as e:
                        print(e)
                        # logger.info("此number号已存在: %s", i)
                else:
                    logger.info("IP 被封或者访问过快")
            else:
                logger.info("访问状态码异常%s", str(con.status_code))
                time.sleep(3)
        except Exception as e:
            print(e)
