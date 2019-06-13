# -*- coding:utf-8 -*-
import hashlib
import datetime
import time
import json
import urllib
import logging
import logging.config

from bs4 import BeautifulSoup
from requests.packages import urllib3

from db import *
from tyc_bean import *
from request_file import *

urllib3.disable_warnings()

logging.config.fileConfig("../log_file/companySearchLog.conf")
logger = logging.getLogger("loggerTxt")

# proxy = {'http': 'http://H017W84J271F18FD:451D275088D7ABD3@proxy.abuyun.com:9020'}
# proxy = {}
# 代理服务器
proxyHost = "proxy.abuyun.com"
proxyPort = "9020"

# 代理隧道验证信息
proxyUser = "H017W84J271F18FD"
proxyPass = "451D275088D7ABD3"

proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
    "host" : proxyHost,
    "port" : proxyPort,
    "user" : proxyUser,
    "pass" : proxyPass,
}

proxies = {
    "http"  : proxyMeta,
    "https" : proxyMeta,
}


class DetailSpider(object):
    def __init__(self):
        self.headers = {
            "Origin": "https://www.tianyancha.com",
            "Accept": "*/*",
            "Content-Type": "application/json; charset=UTF-8",
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
            "Accept-Encoding": "gzip, deflate, sdch, br",
            "Accept-Language": "zh-CN,zh;q=0.8"}
        self.count = 0
        self.username = ""
        self.password = ""
        self.mongodbClient = MongodbClient()
        self.mysqlClient = MysqlClient()
        self.tyc = RequestClass(proxies=proxies)
        self.mark = self.login()

    def login(self):
        """
        :rtype : object
        """
        table = "tyc_user"
        parameters = {
            "user_used": 0,
            "user_forbid": 0,
            "update_time": str(
                datetime.datetime.now() -
                datetime.timedelta(
                    hours=25))}

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
        self.mysqlClient.mysql_update(
            "tyc_user", update_parameters_2, where_parameters)

        # 把下一个将要使用的登录名的user_used=1
        update_parameters = {
            "user_used": 1
        }
        where_parameters = {
            "id": tyc_user[0]
        }
        self.mysqlClient.mysql_update(
            table, update_parameters, where_parameters)

        self.username = tyc_user[1]
        self.password = tyc_user[2]

        data = '{"mobile": "' + self.username + '", "cdpassword": "' + hashlib.md5(
            self.password).hexdigest() + '", "loginway": "PL", "autoLogin": true}'
        url_login = "https://www.tianyancha.com/cd/login.json"

        mark = 3
        while mark:
            try:
                con_login = self.tyc.request_url(
                    url=url_login, headers=self.headers, data=data)
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

    def get_company_list(self, key, number, table):
        key = key.encode("utf-8")

        # 网页抓取
        logger.info("Search Company %s", key)
        url = "https://www.tianyancha.com/search?key=%s&checkFrom=searchBox" % urllib.quote(
            key)
        con = self.tyc.request_url(url=url, headers=self.headers)

        print con.status_code
        # logger.info("test: %s" % con.text)

        # 判断账号是否被封
        if con.status_code != 403:
            if u"请输入您的手机号码" in con.text or u"我们只是确认一下你不是机器人" in con.text or con is None or con.status_code != 200:
                logger.info("userName: %s  forbid " % self.username)

                update_parameters_1 = {
                    "spaider_type": "search",
                    "user_forbid": 1
                }
                where_parameters = {
                    "username": self.username
                }
                self.mysqlClient.mysql_update(
                    "tyc_user", update_parameters_1, where_parameters)
                self.login()
                return None

            try:
                # 解析公司列表页面，搜索信息存入mysql，并返回公司详情url
                self.parse_company_list(key, number, con.text, table)
            except Exception as e:
                self.mysqlClient.mysql_update(
                    table, {
                        'searched': 1, 'error': 1}, {
                        'number': number})
                logger.exception("Exception Logged")
        else:
            logger.info("IP is forbid!")
            time.sleep(2)
            self.get_company_list(key, number, table)

    def parse_company_list(self, key, number, text, table):
        """
        如果第一行公司名称与输入key一致，则取第一行，否则遍历第一页，如果第一页都没有与输入key一致的，则还取第一行
        解析公司列表页面，存储基本信息到mysql，并返回公司名称和公司详情连接
        :param key: 关键字
        :param text: 网页内容
        :return: ent_name, url
        """
        key = key.decode("utf-8")
        logger.info("Parse list page %s", key)
        soup = BeautifulSoup(text, 'lxml')
        div_first = soup.find('div', class_="search_result_single")
        if div_first:
            ent_name = div_first.find('a', class_="query_name").text.strip()
            if key == ent_name:
                pass
            else:
                div_all = soup.find_all('div', class_="search_result_single")
                for div in div_all:
                    if key == div.find('a', class_="query_name").text.strip():
                        div_first = div
                        break
            try:
                ent_name = div_first.find(
                    'a', class_="query_name").text.strip()
                url = div_first.find('a', class_="query_name")["href"].strip()
                try:
                    legal_representative = div_first.find(
                        'div', class_="search_row_new").find_all(
                        'div', class_="title overflow-width")[0].find('a').text.strip()
                except AttributeError:
                    legal_representative = div_first.find(
                        'div', class_="search_row_new").find_all(
                        'div', class_="title overflow-width")[0].find('span').text.strip()
                registered_capital = div_first.find(
                    'div', class_="search_row_new").find_all(
                    'div', class_="title overflow-width")[1].find('span').text.strip()
                registration_date = div_first.find(
                    'div', class_="search_row_new").find_all(
                    'div', class_="title overflow-width")[2].find('span').text.strip()
                location = div_first.find('div', class_="search_row_new").find(
                    'div', class_="float-right").find_all('span')[0].text.strip()
                try:
                    score = div_first.find('div', class_="search_row_new").find(
                        'div', class_="float-right").find_all('span')[1].text.strip()
                except IndexError:
                    score = ""
                status_type = div_first.find(
                    'div', class_="search_right_item").find(
                    'div', class_="statusTypeNor").text.strip()

                # 抓取公司详细信息
                mongo_result = self.get_detail(ent_name, url)
                if mongo_result is None:
                    return None

                txt_id = mongo_result['_id']

                value_list = [key,
                              ent_name,
                              legal_representative,
                              registered_capital,
                              registration_date,
                              location,
                              score,
                              status_type,
                              url,
                              str(txt_id),
                              str(datetime.datetime.now()),
                              str(0)]
                value_list = ['"' + value + '"' for value in value_list]
                insert_value = '(' + ','.join(value_list) + ')'

                # 存储公司基本信息入mysql
                logger.info("Save basic info to mysql %s", key)
                self.mysqlClient.mysql_insert(
                    CompanyBasicInfo.table_name,
                    CompanyBasicInfo.column_name,
                    insert_value)
                self.mysqlClient.mysql_update(
                    table, {
                        'searched': 1, 'error': 0}, {
                        'number': number})
            except Exception as e:
                self.mysqlClient.mysql_update(
                    table, {
                        'searched': 1, 'error': 1}, {
                        'number': number})
                logger.exception("Exception Logged: %s" % ent_name)

        else:
            logger.info("Don't find this company--%s", key)
            self.mysqlClient.mysql_update(
                table, {
                    'searched': 1, 'error': 2}, {
                    'number': number})

    def get_detail(self, ent_name, url):
        """
        爬取公司详情页面，存入mongodb，解析详情并存入mysql
        :param ent_name: 公司名称
        :param url: 公司详情url
        :return:
        """
        res = {"ent_name": ent_name, "url": url}

        logger.info("Spider detail info %s", ent_name)
        con = self.tyc.request_url(url=url, headers=self.headers)
        if con.status_code != 403:

            if u"请输入您的手机号码" in con.text or u"我们只是确认一下你不是机器人" in con.text or con is None or con.status_code != 200:
                logger.info("userName: %s  forbid " % self.username)

                update_parameters_1 = {
                    "spaider_type": "search",
                    "user_forbid": 1
                }
                where_parameters = {
                    "username": self.username
                }
                self.mysqlClient.mysql_update(
                    "tyc_user", update_parameters_1, where_parameters)
                self.login()
                return None

            res["text"] = con.text
            res["parse"] = 0
            res["error_list"] = ""
            res["addTime"] = datetime.datetime.now() + \
                datetime.timedelta(hours=8)

            # 公司详细信息页面存入mongodb
            logger.info("Save detail html to mongodb %s", ent_name)
            mongo_result = self.mongodbClient.mongodb_insert(
                "company_detail_info", res)

            return mongo_result
        else:
            logger.info("IP is forbid!")
            time.sleep(60 * 60)
            self.get_detail(ent_name, url)


if __name__ == "__main__":
    import sys
    reload(sys)
    sys.setdefaultencoding('utf-8')

    ds = DetailSpider()
    table = "11315_company"
    parameters = {
        # "address_3": '("蕲春县","京山县","谷城县","枣阳市","老河口市","潜江经济开发区","潜江区","潜江市经济开发区","湖北省潜江市浩口镇","潜江市总口管理区","潜江县","监利县","松滋市","公安县","沙洋县","南漳县","黄梅县","武穴市","大冶市","宜城市","宜城县","曹县 ","沂水县","青州市","临邑县","单县 ","曲阜市","五莲县","栖霞市","栖霞区","巨野县","东明县","汶上县","龙口市","宁海县","镇海区","象山区","象山县","北仑区","全椒县","来安县","界首市","颍上县","阜南县","太和县","临泉县","临颍县","滑县 ","项城市","杞县 ","淮阳县","沈丘县","石柱县","重庆石柱","石柱土家族自治县","长寿区","合川区","重庆合川区","市辖区合川区","奉节县","重庆奉节县","巫山县","重庆巫山县","万州区","市辖区万州区","重庆城口县","城口县","涪陵区","市辖区涪陵区","垫江县","重庆垫江县","巫溪县","重庆巫溪县","南岸区","安福县","宜丰县","上饶县","泰和县","新干县","乾县 ","蒲城县","凤翔县","兴平市","兴平县","汉滨区","城固县","汉中城固县","蓝田县","睢宁县","吴江区","响水县","岳池县","四川岳池县","广安岳池县","蓬溪县","武胜县","广安武胜县","邻水县","广安邻水县","达川区","四川巴中经济开发区","巴中经济开发区","巴中区","四川巴中通江县","巴中军分区","郫都区","平川区","泾川县","平凉泾川县","习水县","贵州习水县","赤水市","桐梓县","湄潭县","务川 ","务川县","正安县","道真县","道真 ","道真自治县","凤冈县","余庆县","镇赉县","汨罗市","通州区","大通 ","大通县","大通区","西青区","市辖区西青区","龙岗区","龙岗镇平湖区","深圳市龙岗区","龙岗开发区")',
        "searched": 0
    }

    while True:
        try:
            result = ds.mysqlClient.mysql_find_one(
                table, parameters=parameters)
            if result:
                number = result[0]
                key = result[2]
                ds.get_company_list(key, number, table)
            else:
                logger.info("No company to spaider!")
                time.sleep(60)
        except Exception as e:
            logger.exception("Exception Logged")

        ds.count += 1
        if ds.count == 45:
            update_parameters = {
                "update_time": str(datetime.datetime.now())
            }
            where_parameters = {
                "username": ds.username
            }
            ds.mysqlClient.mysql_update(
                "tyc_user", update_parameters, where_parameters)
            ds.login()
