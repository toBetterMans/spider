# -*- coding:utf-8 -*-
import hashlib
import time
import urllib
from bs4 import BeautifulSoup
import datetime
from db import *
from math import *
import re
import json
import logging
import logging.config
from request_file import *
from bson.objectid import ObjectId
import urllib3
urllib3.disable_warnings()  # 如果不加这句话，还会有警告

logging.config.fileConfig("../log_file/pageSpiderLog.conf")
logger = logging.getLogger("loggerTxt")

proxy = {}

ne = ['2633141825201321121345332721524273528936811101916293117022304236', '1831735156281312241132340102520529171363214283321272634162219930', '2332353860219720155312141629130102234183691124281413251227261733', '2592811262018293062732141927100364232411333831161535317211222534', '9715232833130331019112512913172124126035262343627321642220185148', '3316362031032192529235212215274341412306269813312817111724201835', '3293412148301016132183119242311021281920736172527353261533526224', '3236623313013201625221912357142415851018341117262721294332103928', '2619332514511302724163415617234183291312001227928218353622321031', '3111952725113022716818421512203433241091723133635282932601432216']
_0x4fec = ['f9D1x1Z2o1U2f5A1a1P1i7R1u2S1m1F1', 'o2A1x2F1u5~j1Y2z3!p2~r3G2m8S1c1', 'i3E5o1~d2!y2H1e2F1b6`g4v7', 'p1`t7D3x5#w2~l2Z1v4Y1k4M1n1', 'C2e3P1r7!s6U2n2~p5X1e3#', 'g4`b6W1x4R1r4#!u5!#D1f2', '!z4U1f4`f2R2o3!l4I1v6F1h2F1x2!', 'b2~u9h2K1l3X2y9#B4t1', 't5H1s7D1o2#p2#z1Q3v2`j6', 'r1#u5#f1Z2w7!r7#j3S1']
base64chars = "abcdefghijklmnopqrstuvwxyz1234567890-~!"

headers = {
    "Accept": "*/*",
    "Content-Type": "application/json; charset=UTF-8",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
    "Accept-Encoding": "gzip, deflate, sdch, br",
    "Accept-Language": "zh-CN,zh;q=0.8"
}


def gen_utm(key, fnStr):
    """生成Cookie中的_utm"""
    key = str(key).decode("utf-8")
    rsid = gen_rsid(key)

    i = 0
    chars = ''
    while i < len(rsid):
        chars += base64chars[int(rsid[i])]
        i += 1

    m = re.search("wtf=function\(\)\{return'(.*?)'\}\}\(window\)", fnStr, re.S)
    if not m:
        raise RuntimeError("未匹配上_utm")
    fxck = m.group(1).split(",")

    fxckStr = ''
    i = 0
    while i < len(fxck):
        fxckStr += chars[int(fxck[i])]
        i += 1
    return fxckStr


def gen_rsid(tid):
    r = str(ord(tid[0:1]))
    r = r[1] if len(r) > 1 else r

    u = 0
    o = _0x4fec[int(r)]
    i = ne[int(r)]
    a = []
    s = 0
    while u < len(o):
        if not ("`" != o[u] and "!" != o[u] and "~" != o[u]):
            a.append(i[s:(s + 1)])
            s += 1

        if "#" == o[u]:
            a.append(i[s:(s + 1)])
            a.append(i[(s + 1):(s + 3)])
            a.append(i[(s + 3):(s + 4)])
            s += 4

        if 96 < ord(o[u]) < 123:
            l = int(o[u + 1])
            c = 0
            while c < l:
                a.append(i[s:(s + 2)])
                s += 2
                c += 1

        if 64 < ord(o[u]) < 91:
            l = int(o[u + 1])
            c = 0
            while c < l:
                a.append(i[s:(s + 1)])
                s += 1
                c += 1
        u += 1
    return a

class PageSpider(object):
    def __init__(self):
        self.headers = {
            "Accept": "*/*",
            "Content-Type": "application/json; charset=UTF-8",
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
            "Accept-Encoding": "gzip, deflate, sdch, br",
            "Accept-Language": "zh-CN,zh;q=0.8"
        }
        self.count = 0
        self.username = ""
        self.password = ""
        self.mongodbClient = MongodbClient()
        self.mysqlClient = MysqlClient()
        self.tyc = RequestClass(proxies=proxy)
        self.mark = self.login()

    def login(self):
        """
        :rtype : object
        """
        table = "tyc_user"
        parameters = {
            "user_used": 0,
            "user_forbid": 0,
            "update_time": str(datetime.datetime.now() - datetime.timedelta(hours=25))
        }

        while True:
            tyc_user = self.mysqlClient.mysql_find_one(table, parameters)
            if tyc_user:
                break
            else:
                logger.info("No available userName!")
                time.sleep(60)
                continue

        # 把当前的登录名的user_used=0
        update_parameters_2 = {
            "user_used": 0
        }
        where_parameters = {
            "username": self.username
        }
        self.mysqlClient.mysql_update("tyc_user", update_parameters_2, where_parameters)

        # 把下一个将要使用的登录名的user_used=1
        update_parameters = {
            "user_used": 1
        }
        where_parameters = {
            "id": tyc_user[0]
        }
        self.mysqlClient.mysql_update(table, update_parameters, where_parameters)

        self.username = tyc_user[1]
        self.password = tyc_user[2]

        data = '{"mobile": "' + self.username + '", "cdpassword": "' + hashlib.md5(self.password).hexdigest() + '", "loginway": "PL", "autoLogin": true}'
        url_login = "https://www.tianyancha.com/cd/login.json"

        mark = 3
        while mark:
            try:
                con_login = self.tyc.request_url(url=url_login, headers=self.headers, data=data)
            except requests.exceptions.ProxyError as error:
                mark -= 1
                logger.info("Proxy Error!")
                continue
            except Exception as e:
                mark -= 1
                logger.info("Login false!")
                logger.exception("Exception Logged")
                continue

            if mark:
                break

        if con_login.status_code != 200:
            logger.info("Login false!")
            return False

        text = con_login.text

        if json.loads(text)["state"] == 'ok':
            auth_token = json.loads(text)["data"]["token"]
            self.tyc.set_cookies(auth_token=auth_token)
            self.count = 0
            logger.info("Login successful!")
            return True

        logger.info("Logon false, The reason is: %s" % text)
        return False

    def count_func(self):
        if self.count == 180:
            update_parameters = {
                "update_time": str(datetime.datetime.now())
            }
            where_parameters = {
                "username": self.username
            }
            self.mysqlClient.mysql_update("tyc_user", update_parameters, where_parameters)
            self.login()

    def forbid_func(self, con):
        # 判断账号是否被封
        if con.status_code != 403:
            if u"请输入您的手机号码" in con.text or u"我们只是确认一下你不是机器人" in con.text or con is None or con.status_code != 200:
                logger.info("userName: %s  forbid " % self.username)

                update_parameters_1 = {
                    "spaider_type": "page",
                    "user_forbid": 1
                }
                where_parameters = {
                    "username": self.username
                }
                self.mysqlClient.mysql_update("tyc_user", update_parameters_1, where_parameters)
                self.login()
                return True
        else:
            logger.info("IP is forbid!")
            time.sleep(60 * 60)
            return True
        return False

    def func(self, id, i, table_key, company_name):
        for j in range(3):
            tycTime = str(int(time.time() * 1000))
            try:
                url_tongji = "https://www.tianyancha.com/tongji/%s.json?_=%s" % (id, tycTime)
                con_tongji = self.tyc.request_url(url=url_tongji, headers=self.headers)

                con_text = con_tongji.text
                json_obj = json.loads(con_text)
                fnStr = ''
                for item in json_obj["data"].split(","):
                    fnStr += chr(int(item))

                token = re.search('token=(.*?);', fnStr, re.S).group(1)
                utm = gen_utm(company_name, fnStr)

                self.tyc.set_cookies(token=token, _utm=utm)
                url_page = tyc_page[table_key][0] + "&pn=%s&%s=%s&_=%s" % (i, tyc_page[table_key][1], id, tycTime)
                con_page = self.tyc.request_url(url=url_page, headers=self.headers)

                tycText = con_page.text

                self.count += 1
                # 判断是否达到180次
                self.count_func()

                return tycText
            except AttributeError as e:
                logger.info("userName: %s  forbid " % self.username)
                update_parameters_1 = {
                    "spaider_type": "page",
                    "user_forbid": 1
                }
                where_parameters = {
                    "username": self.username
                }
                self.mysqlClient.mysql_update("tyc_user", update_parameters_1, where_parameters)
                self.login()
                continue
            except Exception as e:
                logger.exception("Exception Logged")

    def get_page_detail(self, id, company_name, table_key, page_count):
        page_list = []
        if tyc_page[table_key][1] == "id":
            for i in range(2, int(ceil(int(page_count) / int(tyc_page[table_key][2]))) + 2):
                tycText = self.func(str(id), str(i), table_key, id)
                page_list.append(tycText)
        else:
            for i in range(2, int(ceil(int(page_count) / int(tyc_page[table_key][2]))) + 2):
                tycText = self.func(urllib.quote(company_name.encode("utf-8")), str(i), table_key, company_name)
                page_list.append(tycText)

                if table_key == "nav-main-lawsuitCount":
                    soup = BeautifulSoup(tycText, 'lxml')
                    self.company_law_spider(company_name, soup)

        return page_list

    def company_page_spider(self, ent_name, soup, url):
        logger.info("%s--分页抓取开始" % ent_name)
        spans = soup.find_all('span', class_="intro-count")
        page_dict = {}
        self.headers["Referer"] = url

        for span in spans:
            div = span.find_parent()
            table_key = div['id']
            page_count = span.text
            company_name = ent_name
            company_id = url.replace("https://www.tianyancha.com/company/", "")
            page_count = int(page_count.encode("utf-8"))

            if table_key in tyc_page and page_count > tyc_page[table_key][2]:
                logger.info("%s--%s表" % (company_name, table_key))
                page_list = self.get_page_detail(company_id, company_name, table_key, page_count)
                page_dict[table_key] = page_list

        logger.info("%s--分页抓取结束" % ent_name)

        return page_dict

    def company_year_spider(self, ent_name, soup):
        logger.info("%s--年报抓取开始" % ent_name)
        year_dict = {}

        years = soup.find_all('a', href=re.compile("/reportContent/*"))
        for year in years:
            url = "https://www.tianyancha.com" + year['href']
            con = self.tyc.request_url(url=url, headers=self.headers)

            self.count += 1
            # 判断是否达到180次
            self.count_func()

            # 判断账号是否被封
            if self.forbid_func(con):
                con = self.tyc.request_url(url=url, headers=self.headers)

            year_dict[year['href'][-4:]] = con.text

        logger.info("%s--年报抓取结束" % ent_name)

        return year_dict

    def company_law_spider(self, ent_name, soup):
        logger.info("%s--判决文书抓取开始" % ent_name)
        try:
            laws = soup.find_all('a', href=re.compile("https://www.tianyancha.com/lawsuit/*"))
            for law in laws:
                url = law['href']
                law_number = soup.find("a", href=url).find_parent().find_next_siblings('td')[-1].text
                con = self.tyc.request_url(url=url, headers=self.headers)

                self.count += 1
                # 判断是否达到180
                self.count_func()
                # 判断账号是否被封
                if self.forbid_func(con):
                    con = self.tyc.request_url(url=url, headers=self.headers)

                law_dict[str(law.text + law_number).replace('.', "-")] = con.text
        except Exception as e:
                logger.exception("Exception Logged")

        logger.info("%s--判决文书抓取结束" % ent_name)


if __name__ == "__main__":
    import sys
    reload(sys)
    sys.setdefaultencoding('utf-8')

    ps = PageSpider()

    table = "company_basic_info"
    parameter = {'page_spider': 0}

    while True:
        result = ps.mysqlClient.mysql_find_one(table, parameters=parameter)
        if result:
            try:
                id = result[0]
                ent_name = result[2]
                url = result[9]
                txt_id = result[10]

                mongo_table = "company_detail_info"
                mongo_where_parameter = {
                    "_id": ObjectId(txt_id)
                }
                mongo_result = ps.mongodbClient.mongodb_find_one(mongo_table, mongo_where_parameter)
                text = mongo_result['text']

                result_res = {}
                law_dict = {}
                soup = BeautifulSoup(text, 'lxml')

                # 抓取分页
                try:
                    page_dict = ps.company_page_spider(ent_name, soup, url)
                    result_res["page"] = page_dict
                except Exception as e:
                    logger.exception("Exception Logged")

                # 抓取年报
                try:
                    year_dict = ps.company_year_spider(ent_name, soup)
                    result_res["year"] = year_dict
                except Exception as e:
                    logger.exception("Exception Logged")

                # 法律文书抓取
                try:
                    ps.company_law_spider(ent_name, soup)
                    result_res["law"] = law_dict
                except Exception as e:
                    logger.exception("Exception Logged")

                # 公司详细信息页面存入mongodb
                logger.info("Save page to mongodb %s", ent_name)
                ps.mongodbClient.mongodb_insert("company_detail_info",  result_res)
                ps.mysqlClient.mysql_update("company_basic_info", {'page_spider': 1}, {'id': id})

            except Exception as e:
                ps.mysqlClient.mysql_update("company_basic_info", {'page_spider': 2}, {'id': id})
                logger.exception("Exception Logged")
        else:
            logger.info("No company page to spider!")
            time.sleep(60 * 1)


