# -*- coding:utf-8 -*-
import json
import logging.config
import random
import re
import time
from io import BytesIO
from urllib import parse

from bs4 import BeautifulSoup
from bson.objectid import ObjectId
# from fake_useragent import UserAgent
from fontTools import ttLib

from db import single_oracle, single_mongodb
from request_file import *
from setting import tyc_page, detail_href, detail_onclick, proxy_user, proxy_pass, USER_AGENTS

# 爬取企业详情与分页
urllib3.disable_warnings()  # 如果不加这句话，还会有警告

logging.config.fileConfig("../log_file/pageA.conf")

logger = logging.getLogger("loggerTxt")
# ua = UserAgent()
proxyHost = "http-dyn.abuyun.com"
proxyPort = "9020"

# proxyUser = "H09EIQ188A9U99AD"
# proxyPass = "6546F4FA2BC7D868"
proxyUser = proxy_user
proxyPass = proxy_pass
proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
    "host": proxyHost,
    "port": proxyPort,
    "user": proxyUser,
    "pass": proxyPass,
}
# proxie = 'http://httpapi.datatocrm.com/index.php?token=niuweidong'
proxies = {
    "http": proxyMeta,
    "https": proxyMeta,
}
# proxies = '127.0.0.1:8888'
ne = ['2633141825201321121345332721524273528936811101916293117022304236',
      '1831735156281312241132340102520529171363214283321272634162219930',
      '2332353860219720155312141629130102234183691124281413251227261733',
      '2592811262018293062732141927100364232411333831161535317211222534',
      '9715232833130331019112512913172124126035262343627321642220185148',
      '3316362031032192529235212215274341412306269813312817111724201835',
      '3293412148301016132183119242311021281920736172527353261533526224',
      '3236623313013201625221912357142415851018341117262721294332103928',
      '2619332514511302724163415617234183291312001227928218353622321031',
      '3111952725113022716818421512203433241091723133635282932601432216']
_0x4fec = [
    'f9D1x1Z2o1U2f5A1a1P1i7R1u2S1m1F1',
    'o2A1x2F1u5~j1Y2z3!p2~r3G2m8S1c1',
    'i3E5o1~d2!y2H1e2F1b6`g4v7',
    'p1`t7D3x5#w2~l2Z1v4Y1k4M1n1',
    'C2e3P1r7!s6U2n2~p5X1e3#',
    'g4`b6W1x4R1r4#!u5!#D1f2',
    '!z4U1f4`f2R2o3!l4I1v6F1h2F1x2!',
    'b2~u9h2K1l3X2y9#B4t1',
    't5H1s7D1o2#p2#z1Q3v2`j6',
    'r1#u5#f1Z2w7!r7#j3S1']
base64chars = "abcdefghijklmnopqrstuvwxyz1234567890-~!"

page_headers = {
    "Accept": "text/hcourtl,application/xhcourtl+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    
    "Host": "www.tianyancha.com",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": random.choice(USER_AGENTS),
}

nn = []

def tt(e, t, n):
    global nn
    # #print(e, t, n, nn)
    if n == []:
        nn.append([])
    else:
        nn[int(e)].append(str(t))

def get_chars_by_companyId(company_id):
    t_default = ",,06btf2,,0zl5whqisecpmu98y,,1,,118oszunvmb9fd7hcpy203j-ilktq46raw5exg,,,0kjrxn-034d1ao7vg,2s6h0pg3nmyldxeakzuf4rb-7oci8v219q,2wtj5,3x70digacthupf6veq4b5kw9s-jly3onzm21r8,4zj3l1us45gch7ot2ka-exybn8i6qp0drvmwf9,,68q-udk7tz4xfvwp2e9om5g1jin63rlbhycas0,5jhpx3d658ktlzb4nrvymga01c9-27qewusfoi,,,7d49moi5kqncs6bjyxlav3tuh-rz207gp8f1we,87-gx65nuqzwtm0hoypifks9lr12v4e8cbadj3,91t8zofl52yq9pgrxesd4nbuamchj3vi0-w7k6"
    t_defaults = t_default.split(",")
    
    for k in t_defaults:
        t = list(k)
        if len(t) > 0:
            for i in range(1, len(t)):
                tt(t[0], t[i], None)
        else:
            tt(None, None, [])
    r = str(ord(str(company_id)[0]))
    # print(r)
    rs = r[1] if len(r) > 1 else r
    rs = int(rs)
    # print(rs)
    return nn[rs]

def gen_ucourt(key, fnStr):
    """生成Cookie中的_ucourt"""
    key = str(key)
    rsid = gen_rsid(key)
    i = 0
    chars = ''
    while i < len(rsid):
        chars += base64chars[int(rsid[i])]
        i += 1
    # print(chars)
    # print(fnStr)
    m = re.search("wtf=function\(\)\{return'(.*?)'\}\}\(window\)", fnStr, re.S)
    if not m:
        raise RuntimeError("未匹配上_ucourt")
    fxck = m.group(1).split(",")
    
    fxckStr = ''
    i = 0
    gen_chars = get_chars_by_companyId(key)
    while i < len(fxck):
        fxckStr += gen_chars[int(fxck[i])]
        i += 1
    # print(fxckStr)
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

def get_cookie_by_request(company_id, url, re_key, json_obj_list):
    cookie_header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
    }
    graph_con = requests.get(url, headers=cookie_header, proxies=proxies, verify=False)
    json_obj = json.loads(graph_con.text)
    fnStr = ''
    for item in eval(json_obj_list).split(","):
        fnStr += chr(int(item))
    # print(fnStr)
    token = re.search(r'{}=(.*?);'.format(re_key), fnStr, re.S).groups()[0]
    # ps.tyc.set_cookies({'rtoken':rtoken})
    _u = gen_ucourt(company_id, fnStr)
    
    return [token, _u]

class PageSpider(object):
    max_retry_count = 3
    def __init__(self):
        self.company_id = None
        self.headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Content-Type": "application/json; charset=UTF-8",
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent": random.choice(USER_AGENTS),
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Host ": "www.tianyancha.com"}
        self.font_dicts = {}
        self.detail_dicts = {}
        self.count = 0
        self.username = ""
        self.password = ""
        self.tyc = RequestClass(proxies=proxies)
        # self.mark_count = self.login()
        self.tyc_page = tyc_page
        self.re_fonts = re.compile(
            r'<link rel="stylesheet" href="https://static.tianyancha.com/fonts-styles/css/(.*?)/font.css">')
        self.cookies = None
        self.ucourt = None
        self.token = None
        self.TYCID = None
        self.cloud_token = ''
        self.cloud_utm = ''
        self.login()
    
    def get_dict(self, font_url):

        try:
            dicts = {}
            # print('*' * 30)
            # print('url_font={}'.format(font_url))
            logger.info('font_url={}'.format(font_url))
            mm = self.tyc.request_url(
                'https://static.tianyancha.com/fonts-styles/fonts/{}/tyc-num.woff'.format(font_url),
                headers={'User-Agent': random.choice(USER_AGENTS)})
            tt = ttLib.TTFont(BytesIO(mm.content))
            names = tt.getGlyphNames()[:10]
            orders = tt.getGlyphOrder()[2:12]
            for i in range(len(names)):
                dicts[orders[i]] = names[i]
            # print(dicts)
            self.font_dicts = dicts
        except Exception as e:
            logger.exception(e)
            if PageSpider.max_retry_count>3:
                PageSpider.max_retry_count-=1
                self.get_dict(font_url)
    
    def login(self):
        self.username, self.cookie = self.tyc.login()

    def check_login(self, con):
        if con and con.status_code == 404:
            return True
        if u"我们只是确认一下你不是机器人" in con.text or 'antirobot' in con.url:
            logger.info("userName: {}  forbid  status_code={}".format(self.username, con.status_code))
            single_redis.put_cookies(phone=self.tyc.username, cookie=self.cookie, name='forbids')
            self.login()
            return False
        elif con and con.status_code == 200:
            return True
        elif con.status_code >= 400:
            logger.info("userName: {}  forbid  status_code={}".format(self.username, con.status_code))
            self.login()
            return False
        elif not con or not '退出登录' in con.text:
            logger.exception("userName: {}  cookie失效！！  status_code={}".format(self.username, con.status_code))
            single_redis.server.hdel('cookies', self.tyc.username)
            single_redis.server.lpush('users', self.tyc.username)
            self.login()
            return False
    
        else:
            logger.info("userName: {}  forbid  status_code={}".format(self.username, con.status_code))
            single_redis.server.hdel('cookies', self.tyc.username)
            single_redis.server.lpush('users', self.tyc.username)
            self.login()
            return False

    def func(self, id, i, table_key, company_name):
        tycTime = str(int(time.time() * 1000))
        headers1 = {
            "User-Agent": random.choice(USER_AGENTS),
            "Host": "www.tianyancha.com",
            "Connection": "keep-alive",
            "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
            "Accept-Encoding": "gzip, deflate",
            "Accept": "application/json, text/plain, */*",
            "Cache-Control": "no-cache",
            "Tyc-From": "normal",
            "CheckError": "check",
        }

        try:
            # if not (self.ucourt and self.token):
            # url_tongji = "https://www.tianyancha.com/tongji/%s.json?random=%s" % (
            #     id, tycTime)
            # mark_tongji = 5
            # while mark_tongji > 0:
            #     #print('重新获取token。。。。。。。。。。。。。。')
            #     self.login()
            # cookie1 = self.tyc.session.cookies.get('auth_token')
            # con_tongji = self.tyc.request_url(
            #     url=url_tongji, headers=headers1, proxies=proxies)
            # con_tongji.encoding = 'utf-8'
            # logger.info(con_tongji.text)
            #
            # if not self.check_login(con_tongji):
            #     mark_tongji -= 1
            #     continue
            # con_text = con_tongji.text
            # json_obj = json.loads(con_text)
            # fnStr = ''
            # for item in json_obj["data"].split(","):
            #     fnStr += chr(int(item))
            # token = re.search('token=(.*?);', fnStr, re.S)
            # token_u_list = get_cookie_by_request(self.company_id, url_tongji, 'token', 'json_obj["data"]')
            # if token_u_list:
            #     logger.info('获取token成功：{}'.format(token_u_list))
            #     self.cloud_token = token_u_list[0]
            #     mark_tongji = -1
            # else:
            #     logger.info('获取token失败：{}'.format(fnStr))
            # mark_tongji -= 1
            # self.login()
            # continue
            # self.ucourt = token_u_list[1]
            # self.tyc.set_cookies_kwargs(cloud_token=str(self.token), _ucourt=str(self.ucourt))
            # self.TYCID = self.tyc.session.cookies.get('TYCID')
            # headers1.update({
            #     "Referer": "http://www.tianyancha.com/company/%s" % id,
            # })
            tyc_page = self.tyc_page
            url_page = tyc_page[table_key][0] + "&pn=%s&%s=%s&_=%s" % (
                i, tyc_page[table_key][1], id, tycTime)
            mark_page = 3
            while mark_page > 0:
                try:
                    # self.login()
                    # self.count_func()
                    con_page = self.tyc.request_url(
                        url=url_page, headers=self.headers)
                    # 判断账号是否被封
                    # self.forbid_func(con_page)
                    logger.debug('获取分页状态码：{}'.format(con_page.status_code))
                    if self.check_login(con_page):
                        tycText = con_page.text
                        return tycText
                    else:
                        self.func(id, i, table_key, company_name)
                        mark_page = -1
                except requests.exceptions.ProxyError as error:
                    logger.exception("Exception Logged!{}".format(error))
                    mark_page -= 1
                    continue
                except AttributeError as e:
                    logger.exception("Exception Logged!{}".format(e))
                    single_redis.server.hdel('cookies', self.tyc.username)
                    single_redis.put_cookies(phone=self.tyc.username, cookie=self.cookie, name='forbids')
                    self.login()
                    mark_page -= 1
                    continue
                except Exception as e:
                    logger.exception("Exception Logged!{}".format(e))
                    self.login()
                    mark_page -= 1
                    continue

        except Exception as e:
            logger.exception("Exception Logged!{}".format(e))
        return None
    
    # TODO
    def get_page_detail(self, company_name, table_key, page_count):
        try:
            page_list = []
            if self.tyc_page[table_key][1] == "id":
                tycText = self.func(str(self.company_id), str(page_count), table_key, company_name)
            else:
                tycText = self.func(
                    parse.quote(
                        company_name),
                    str(page_count),
                    table_key,
                    company_name)
            if tycText:
                if table_key in detail_href:
                    self.detail_dicts[table_key] = self.company_detail_href(BeautifulSoup(
                        tycText, 'lxml'), detail_href[table_key])
                elif table_key in detail_onclick:
                    if table_key == '_container_certificate':
                        self.detail_dicts[table_key] = self.company_certificate_spider(
                            company_name, BeautifulSoup(tycText, 'lxml'))
                    elif table_key == '_container_judicialAid' or table_key == 'nav-main-judicialaAidCount':
                        self.detail_dicts['_container_judicialAid'] = self.company_help_spider(
                            company_name, BeautifulSoup(tycText, 'lxml'))
                    elif table_key == '_container_zhixing' or table_key == 'nav-main-zhixing':
                        self.detail_dicts['_container_zhixing'] = self.company_zhixing_spider(
                            company_name, BeautifulSoup(tycText, 'lxml'))

                    elif table_key == '_container_dishonest':
                        self.detail_dicts['_container_dishonest'] = self.company_dishonest_spider(
                            company_name, BeautifulSoup(tycText, 'lxml'))
                
                return tycText
        except Exception as e:
            logger.exception("Exception !{}".format(e))
    
    def company_page_spider(self, ent_name, soup, url):
        """
        :param ent_name:
        :param soup:
        :param url:
        :return:判断是否有分页要抓取
        """
        try:
            logger.info("%s--分页抓取开始" % ent_name)
            spans = soup.find_all('div', attrs={"class": "company_pager"})
            page_dict = {}
            self.headers["Referer"] = url
            for span in spans:
                page_lists = []
                try:
                    div = span.find_parent()
                    table_key = div.get('id')
                    data_count = div.find_parent().find_parent().find(
                        'span', {'class': 'data-count'})
                    if data_count:
                        data_count = data_count.text
                    if not table_key:
                        table_key = span.find_parent().find_parent().find(
                            'div', attrs={'class': 'data-header'}).get('id')
                except Exception as findE:
                    logger.exception(findE)
                    continue
                logger.debug('table_key=={}'.format(table_key))
                page_span = span.find('a', string=re.compile(r'...'))
                if page_span:
                    s = page_span.text
                else:
                    s = span.find_all('a')[-2].text
                    # s=s[len(s)-2].text
                s = s.replace('...', '')
                total_page_count = int(s)
                company_name = ent_name
                page_count = []
                total_page_count = 10 if total_page_count > 1 else total_page_count
                # print('total_page_count===', total_page_count)
                total_page_count = 2 if total_page_count > 10 else total_page_count
                try:
                    for index in range(2, total_page_count + 1):
                        keys = self.get_page_detail(
                            company_name, table_key, index)
                        if keys:
                            page_lists.append(keys)
                except Exception as e:
                    logger.exception("Exception !{}".format(e))
                    continue
                if page_lists:
                    page_dict[table_key] = page_lists
                else:
                    page_dict[table_key] = int(data_count)
            logger.info("%s--分页抓取结束" % ent_name)
            return page_dict
        except Exception as e:
            logger.exception("Exception !{}".format(e))
            # print(e)

    def get_detail_spider(self, url, dicts, key, custom_header={}):
        mark = 3
        # https://job.tianyancha.com/f810c3bc82afcecc2b6f54c400858c9f
        host = url.split(r'//')[1].split(r'/')[0]
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'DNT': '1',
            'Host': host,
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': random.choice(USER_AGENTS)
        }
        if custom_header:
            headers = custom_header
        while mark > 0:
            try:
                # #print(dict(self.tyc.session.cookies))
                con = self.tyc.request_url(
                    url=url, headers=headers, proxies=proxies, verify=False)
                # print(con.status_code, '!!!' * 100)
                if not self.check_login(con):
                    # self.login()
                    self.get_detail_spider(url, dicts, key)
                    mark -= 1
                    continue
                # key = str(law_number).replace(".", "-").replace('（','').replace('）','')
                key = str(key).replace("'", '').replace('.', '_')
                dicts[key] = con.text.replace("'", '')
                mark = -1
            except requests.exceptions.ProxyError as error:
                mark -= 1
                logger.info("Proxy Error! {}".format(error))
                continue
            except Exception as e:
                mark -= 1
                logger.exception("Exception !{}".format(e))
                continue
    
    def help_spider_one(self, help, help_dict):
        # url='https://www.tianyancha.com/company/judicialAidDetail.json?id={id}&_={tim}'
        url = detail_onclick['_container_judicialAid']['url']
        url_a = help["onclick"]
        # print(url_a)
        res = re.search(r'"(.*?)"', url_a).groups(1)
        regNo = res[0]
        tim = int(time.time() * 1000)
        url = url.format(id=regNo, tim=tim)
        self.get_detail_spider(url, help_dict, regNo)
    
    def company_help_spider(self, ent_name, soup):
        logger.info("%s-- 司法协助 详情抓取开始 " % ent_name)
        try:
            help_dict = {}
            # <a class="link-click" onclick="opencourtDetail(&quot;22274969&quot;,&quot;41-教育、娱乐服务&quot;)">详情</a>
            helps = soup.find_all(
                'span', onclick=re.compile(
                    detail_onclick['_container_judicialAid']['onclick']))
            for help in helps:
                self.help_spider_one(help, help_dict)
            return help_dict
        except Exception as e:
            logger.exception("Exception !{}".format(e))
    
    def detail_spider_one(self, detail, detail_dict):
        url = detail['href']
        # print(url)
        key = str(url).split('/')[-1].replace('.', '_')
        # print(key)
        self.get_detail_spider(url, detail_dict, key)
    
    def company_detail_href(self, soup, href=''):
        try:
            dicts = {}
            # if href:
            details = soup.find_all('a', href=re.compile(href))
            # else:
            #     details = soup.find_all('span', onclick=re.compile(onclick))
            for detail in details:
                self.detail_spider_one(detail, dicts)
            return dicts
        except Exception as e:
            logger.exception("Exception !{}".format(e))
    
    def certificate_spider_one(self, certificate, certificate_dict):
        # url = 'https://www.tianyancha.com/company/certificateDetail.json?id={id}&_={tim}'
        url = detail_onclick['_container_certificate']['url']
        url_a = certificate["onclick"]
        # print(url_a)
        res = re.search(r"certificatePopup\('(.*?)'\)", url_a).groups(1)
        key = res[0]
        tim = int(time.time() * 1000)
        url = url.format(id=key, tim=tim)
        # req_clkst(self.company_id, 'CompangyDetail.zhengshu', self.username, self.tyc.session)
        self.get_detail_spider(url, certificate_dict, key)
    
    def company_certificate_spider(self, ent_name, soup):
        # https://www.tianyancha.com/company/certificateDetail.json?id=5bc564a00779a577162a3054&_=1542333967628
        logger.info("%s-- 资质证书 详情抓取开始 " % ent_name)
        try:
            certificate_dict = {}
            # <a class="link-click" onclick="opencourtDetail(&quot;22274969&quot;,&quot;41-教育、娱乐服务&quot;)">详情</a>
            certificates = soup.find_all('span', onclick=re.compile(
                detail_onclick['_container_certificate']['onclick']))
            for certificate in certificates:
                self.certificate_spider_one(certificate, certificate_dict)
            return certificate_dict
        except Exception as e:
            logger.exception("Exception !{}".format(e))

    def zhixing_spider_one(self, zhixing, zhixing_dict):
        # url = 'https://www.tianyancha.com/company/certificateDetail.json?id={id}&_={tim}'
        url = detail_onclick['_container_zhixing']['url']
        url_a = zhixing["onclick"]
        zhixing_header = {'Host': 'capi.tianyancha.com',
                          'Connection': 'keep-alive',
                          'Accept': '*/*',
                          'Origin': 'https://www.tianyancha.com',
                          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
                          'DNT': '1',
                          'version': 'TYC-Web',
                          'Referer': 'https://www.tianyancha.com/company/{}'.format(self.company_id),
                          'Accept-Language': 'zh-CN,zh;q=0.9',
                          'Accept-Encoding': 'gzip, deflate'}
        # print(url_a)
        res = re.search(r'openZhixingDetail\("(\d+)"\)', url_a).groups(1)
        key = res[0]
        tim = int(time.time() * 1000)
        url = url.format(zid=key, tim=tim)
        # req_clkst(self.company_id, 'CompangyDetail.zhengshu', self.username, self.tyc.session)
        self.get_detail_spider(url, zhixing_dict, key, custom_header=zhixing_header)
    
    # 被执行人信息
    def company_zhixing_spider(self, ent_name, soup):
        logger.info("%s-- 被执行人信息 详情抓取开始 " % ent_name)
        try:
            zhixing_dict = {}
            # <a class="link-click" onclick="opencourtDetail(&quot;22274969&quot;,&quot;41-教育、娱乐服务&quot;)">详情</a>
            zhixings = soup.find_all('span', onclick=re.compile(
                detail_onclick['_container_zhixing']['onclick']))
            for zhixing in zhixings:
                self.zhixing_spider_one(zhixing, zhixing_dict)
            return zhixing_dict
        except Exception as e:
            logger.exception("Exception !{}".format(e))

    def dishonest_spider_one(self, dishonest, zhixing_dict):
        # url = 'https://www.tianyancha.com/company/certificateDetail.json?id={id}&_={tim}'
        url = detail_onclick['_container_dishonest']['url']
        url_a = dishonest["onclick"]
        dishonest_header = {'Host': 'capi.tianyancha.com',
                            'Connection': 'keep-alive',
                            'Accept': '*/*',
                            'Origin': 'https://www.tianyancha.com',
                            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
                            'DNT': '1',
                            'version': 'TYC-Web',
                            'Referer': 'https://www.tianyancha.com/company/{}'.format(self.company_id),
                            'Accept-Language': 'zh-CN,zh;q=0.9',
                            'Accept-Encoding': 'gzip, deflate'}
        # print(url_a)
        res = re.search(r'openDishonestinfoDetail\("(\d+)"\)', url_a).groups(1)
        key = res[0]
        tim = int(time.time() * 1000)
        url = url.format(did=key, tim=tim)
        # req_clkst(self.company_id, 'CompangyDetail.zhengshu', self.username, self.tyc.session)
        self.get_detail_spider(url, zhixing_dict, key, custom_header=dishonest_header)

    # 失信人信息
    def company_dishonest_spider(self, ent_name, soup):
        logger.info("%s-- 失信人信息 详情抓取开始 " % ent_name)
        try:
            dishonest_dict = {}
            # <a class="link-click" onclick="opencourtDetail(&quot;22274969&quot;,&quot;41-教育、娱乐服务&quot;)">详情</a>
            dishonests = soup.find_all('span', onclick=re.compile(
                detail_onclick['_container_dishonest']['onclick']))
            for dishonest in dishonests:
                self.dishonest_spider_one(dishonest, dishonest_dict)
            return dishonest_dict
        except Exception as e:
            logger.exception("Exception !{}".format(e))
    
    # 2019/05/22 当前不做，原因；VIP可看
    def company_holder_holding_analysis_spider(self, ent_name, soup):
        logger.info('开始抓取最终受益人，实际控制权信息 ---{}'.format(ent_name, soup))
        try:
            zuizhong_html_dicts = {}
            url = 'https://www.tianyancha.com/company/holder_holding_analysis.xhtml?id={id}&_={tim}'
            tim = int(time.time() * 1000)
            url = url.format(zid=self.company_id, tim=tim)
            # req_clkst(self.company_id, 'CompangyDetail.zhengshu', self.username, self.tyc.session)
            self.get_detail_spider(url, zuizhong_html_dicts, 'nav-main-realHoldingCount')
        except:
            pass

    # 股权穿透图
    def company_equal_spider(self, ent_name):
        #         https://capi.tianyancha.com/cloud-equity-provider/v4/equity/indexnode.json?id=24416401

        equal_cookie_url = 'https://capi.tianyancha.com/cloud-equity-provider/v4/qq/name.json?id={id}?random={tim}'
        equal_url = 'https://capi.tianyancha.com/cloud-equity-provider/v4/equity/indexnode.json?id={id}'
        try:
            logger.info('股权穿透图——操作详情 抓取，公司：{}'.format(ent_name))
            equal_dicts = {}

            token_u_list = get_cookie_by_request(self.company_id, equal_cookie_url, 'cloud_token',
                                                 'json_obj["data"]["v"]')
            # print(token_u_list)
            self.tyc.session.cookies.update({'cloud_token': token_u_list[0]})
            self.tyc.session.cookies.update({'cloud_utm': token_u_list[1]})
            self.tyc.session.cookies.pop('_utm')
            # print('*' * 12, dict(self.tyc.session.cookies))
            equal_header = {
                'Accept': 'application/json, text/plain, */*',
                'DNT': '1',
                # 'Referer': 'https://dis.tianyancha.com/dis/old',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
                'host': 'capi.tianyancha.com',
                'Origin': 'https://dis.tianyancha.com',
                'version': 'TYC-Web',
                'Accept-Language': 'zh-CN,zh;q=0.9'
            }

            self.get_detail_spider(
                equal_url.format(id=self.company_id),
                equal_dicts, '_graphTreeInfo_container',
                custom_header=equal_header)
            return equal_dicts
        except Exception as e:
            logger.exception("Exception !{}".format(e))

    # 企业关系——操作详情
    def company_graph_spider(self, ent_name):
        try:
            logger.info('企业关系——操作详情 抓取，公司：{}'.format(ent_name))
            # self.login()
            # print('企业关系——操作详情 抓取，公司：{}'.format(ent_name))
            graph_dicts = {}
            rtycid_url = 'https://dis.tianyancha.com/dis/timeline?graphId={id}&cnz=true'.format(id=self.company_id)
            graph_header = {
                'Host': 'dis.tianyancha.com',
                'Connection': 'keep-alive',
                'Accept': 'application/json, text/plain, */*',
                'DNT': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
                'Referer': 'https://dis.tianyancha.com/dis/old',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Accept-Encoding': 'gzip, deflate'
    
            }
            con = self.tyc.request_url('https://www.tianyancha.com/company/{}'.format(self.company_id))
            # print(con.status_code)
            rtycid_header = graph_header.copy()
            rtycid_header['Upgrade-Insecure-Requests'] = '1'
            rtycid_header[
                'Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3'

            rtycid_header['Referer'] = 'https://www.tianyancha.com/company/{}'.format(self.company_id)
            self.tyc.request_url(rtycid_url, proxies=proxies, verify=False)
            # print(dict(self.tyc.session.cookies))
            graph_cookie_url = 'https://dis.tianyancha.com/qq/{id}.json?random={tim}'.format(
                id=self.company_id, tim=str(int(time.time() * 1000)))
            graph_url = 'https://dis.tianyancha.com/dis/getInfoById/{id}.json?'.format(id=self.company_id)
            token_u_list = get_cookie_by_request(self.company_id, graph_cookie_url, 'rtoken', 'json_obj["data"]["v"]')
            self.rutm = token_u_list[1]
            self.rtoken = token_u_list[0]
            self.tyc.session.cookies.update({'rtoken': self.rtoken})
            self.tyc.session.cookies.update({'_rutm': self.rutm})
            self.tyc.session.cookies.update({'_utm': None})
            self.tyc.session.cookies.update({'aliyungf_tc': None})
            self.tyc.session.cookies.update({'csrfToken': None})
            self.tyc.session.cookies.update({'token': None})
            # #print(dict(self.tyc.session.cookies))
            self.get_detail_spider(
                graph_url,
                graph_dicts, '_graph_container',
                custom_header=graph_header)
            # print(graph_dicts)
            return graph_dicts
        except Exception as e:
            logger.exception("Exception !{}".format(e))

    def company_graphTimeInfo_spider(self, ent_name):
        # 历史沿革 json 操作详情抓取  'https://dis.tianyancha.com/dis/timeline.json?id=24416401'
        try:
            logger.info('历史沿革——操作详情 抓取，公司：{}'.format(ent_name))
            graphTimeInfo_dicts = {}
            self.get_detail_spider(
                'https://dis.tianyancha.com/dis/timeline.json?id={id}'.format(id=self.company_id),
                graphTimeInfo_dicts,
                'nav-main-graphTimeInfo')
            return graphTimeInfo_dicts
        except Exception as e:
            logger.exception("Exception !{}".format(e))

def main(args):
    # reload(sys)
    # sys.setdefaultencoding('utf-8')
    # print('tyc_page_spider starting .....')
    
    mongo_where_parameter = {
    
    }
    mongo = single_mongodb
    # single_redis = single_redis
    while True:
        txt_id = ''
        ps = PageSpider()
        try:
    
            txt_id = single_redis.server.rpop('pages')
            if not txt_id:
                single_redis.put_page()
                txt_id = single_redis.server.rpop('pages')
            
            if not txt_id:
                time.sleep(60)
                continue
            if isinstance(txt_id, bytes):
                txt_id = txt_id.decode()
            mongo_where_parameter['_id'] = ObjectId(txt_id)
            mongo_table = "company_detail_info"
            mongo_result = mongo.mongodb_find_one(
                mongo_table, mongo_where_parameter)
            # #print (mongo_result)
            # #print mongo_result
            # #print mongo_result
            if mongo_result:
                
                txt_id = mongo_result['_id']
                if isinstance(txt_id, bytes):
                    txt_id = txt_id.decode()
                
                url = mongo_result['url']
                ent_name = mongo_result['ent_name']
                count = 0
                text = mongo_result['text']
            else:
                # print('No company page to spider')
                single_oracle.oracle_update(
                    "update company_basic_info set  page_spider=1 where txt_id='{}'".format(txt_id))
                logger.info("No company page to spider!")
                # time.sleep(60 * 1)
                # #print "id=%s;ent_name=%s;txt_id=%s;url=%s;" % (
                # str(id), str(ent_name).encode("utf8"), str(txt_id), str(url))
                # ps.mysqlClient.mysql_update("11315_company",{"searched":0,"parse":0},{"company_name":ent_name})
                # ps.mysqlClient.mysql_delete_by_param("DELETE FROM `company_basic_info` WHERE `txt_id`='%s'"%txt_id)
                continue
            
            result_res = {}
            law_dict = {}
            soup = BeautifulSoup(text, 'lxml')
            ps.company_id = url.replace(
                "https://www.tianyancha.com/company/", "")
    
            # s = ps.company_equal_spider(ent_name)
            # #print(s)
            # break
            # ss = ps.company_graph_spider(ent_name)
            # #print(ss)
            # break
            # ssss = ps.company_graphTimeInfo_spider(ent_name)
            # #print(ssss)
    
            # 股权穿透 json 操作详情抓取  'https://dis.tianyancha.com/dis/timeline.json?id=24416401'
            # try:
            #     result_res["_graphTreeInfo_container"] = ps.company_equal_spider(ent_name)
            # except Exception as e:
            #     logger.exception("Exception !{}".format(e))
            #
            # # 企业关系 json 操作详情抓取  'https://dis.tianyancha.com/dis/timeline.json?id=24416401'
            # try:
            #     result_res["_graph_container"] = ps.company_graph_spider(ent_name)
            # except Exception as e:
            #     logger.exception("Exception !{}".format(e))
    
            # # 历史沿革 json 操作详情抓取  'https://dis.tianyancha.com/dis/timeline.json?id=24416401'
            try:
                result_res["nav-main-graphTimeInfo"] = ps.company_graphTimeInfo_spider(ent_name)
            except Exception as e:
                logger.exception("Exception !{}".format(e))
            # 抓取分页
            try:
                font_uri = ps.re_fonts.search(text).group(1)
                # self.get_dict(font_uri)
                ps.get_dict(font_uri)

                # #print '抓取分页ent_name,soup,url',ent_name.soup,url
                logger.info('开始抓取分页，公司：{}'.format(ent_name))
                page_dict = ps.company_page_spider(ent_name, soup, url)
                result_res["page"] = page_dict
                # logger.info('result_res={}'.format(page_dict))
            except Exception as e:
                logger.exception("Exception !{}".format(e))
            
            # 抓取年报
            try:
                logger.info('开始抓取年报，公司：{}'.format(ent_name))
                # year_dict = ps.company_year_spider(ent_name, soup)
                year_dict = ps.company_detail_href(
                    soup, href=detail_href['year'])
                result_res["year"] = year_dict
            except Exception as e:
                logger.exception("Exception !{}".format(e))
            
            # 法律诉讼 判决文书抓取
            try:
                logger.info('开始法律诉讼 判决文书抓取，公司：{}'.format(ent_name))
                # law_dict=ps.company_law_spider(ent_name, soup)
                law_dict = ps.company_detail_href(
                    soup, href=detail_href['_container_lawsuit'])
                result_res["_container_lawsuit"] = law_dict
            except Exception as e:
                logger.exception("Exception !{}".format(e))
            
            #     法院公告 操作详情
            try:
                logger.info('开始法院诉讼 操作详情抓取，公司：{}'.format(ent_name))
                # court_dict=ps.company_court_spider(ent_name, soup)
                court_dict = ps.company_detail_href(
                    soup, detail_href['_container_lawsuit'])
                result_res["_container_lawsuit"] = court_dict
            except Exception as e:
                logger.exception("Exception !{}".format(e))
            
            # 司法协助 操作详情 https://www.tianyancha.com/company/judicialAidDetail.json?id=37c01954536&_=1542263180441
            try:
                logger.info('开始司法协助 操作详情抓取，公司：{}'.format(ent_name))
                help_dict = ps.company_help_spider(ent_name, soup)
                result_res["_container_judicialAid"] = help_dict
            except Exception as e:
                logger.exception("Exception !{}".format(e))
            
            # 司法拍卖 拍卖公告抓取
            try:
                logger.info('开始司法拍卖——拍卖公告 抓取，公司：{}'.format(ent_name))
                auction_dict = ps.company_detail_href(
                    soup, detail_href['_container_judicialSale'])
                result_res["_container_judicialSale"] = auction_dict
            except Exception as e:
                logger.exception("Exception !{}".format(e))
            
            # 经营状况
            # 招聘信息
            try:
                # https://job.tianyancha.com/c5975357d236facc78f3ca4d1f177fd5
                logger.info('开始招聘信息——操作详情 抓取，公司：{}'.format(ent_name))
                # href=r'https://job.tianyancha.com/'
                job_dict = ps.company_detail_href(
                    soup, detail_href['_container_baipin'])
                # #print(job_dict)
                result_res["_container_baipin"] = job_dict
            except Exception as e:
                logger.exception("Exception !{}".format(e))
            
            # 资质证书
            # https://www.tianyancha.com/company/certificateDetail.json?id=599acc3f57708c2b3095bf6b&_=1542263180445
            try:
                logger.info('开始招聘信息——操作详情 抓取，公司：{}'.format(ent_name))
                
                certificate_dict = ps.company_certificate_spider(
                    ent_name, soup)
                result_res["_container_certificate"] = certificate_dict
            except Exception as e:
                logger.exception("Exception !{}".format(e))
    
            # 被执行人
            try:
                logger.info('开始被执行人信息——操作详情 抓取，公司：{}'.format(ent_name))

                zhixing_dict = ps.company_zhixing_spider(
                    ent_name, soup)
                result_res["_container_zhixing"] = zhixing_dict
            except Exception as e:
                logger.exception("Exception !{}".format(e))
    
            # 失信人信息
            try:
                logger.info('开始失信人信息——操作详情 抓取，公司：{}'.format(ent_name))
        
                zhixing_dict = ps.company_dishonest_spider(
                    ent_name, soup)
                result_res["_container_dishonest"] = zhixing_dict
            except Exception as e:
                logger.exception("Exception !{}".format(e))
            
            #  产品信息 https://www.tianyancha.com/product/da76706c9a87b3d96443c45852bfda58
            try:
                logger.info('开始产品信息——操作详情 抓取，公司：{}'.format(ent_name))
                href = r'https://www.tianyancha.com/product/'
                product_dict = ps.company_detail_href(
                    soup, detail_href['_container_product'])
                result_res["_container_product"] = product_dict
            except Exception as e:
                logger.exception("Exception !{}".format(e))
            
            # 知识产权
            # 商标信息 操作详情抓取 https://www.tianyancha.com/company/courtDetail.json?regNo={22274593}&courtClass=35-&_={1542248889558}
            try:
                logger.info('开始商标信息信息——操作详情 抓取，公司：{}'.format(ent_name))
                brand_dict = ps.company_detail_href(
                    soup, detail_href['_container_tmInfo'])
                result_res["_container_tmInfo"] = brand_dict
            except Exception as e:
                logger.exception("Exception !{}".format(e))
            
            # 专利信息 操作详情抓取  https://www.tianyancha.com/patent/5e89a48b287d29e0f6bee885c713e17f
            try:
                logger.info('开始专利信息——操作详情 抓取，公司：{}'.format(ent_name))
                patent_dict = ps.company_detail_href(
                    soup, detail_href['_container_patent'])
                result_res["_container_patent"] = patent_dict
            except Exception as e:
                logger.exception("Exception !{}".format(e))
    
            result_res["parse"] = 0
            # 公司详细信息页面存入mongodb
            logger.info("Save page to mongodb %s", ent_name)
            mongo_update_where = {
                '_id': ObjectId(txt_id)
            }
            result_res["page_spide"] = 1
            result_res['dicts'] = ps.font_dicts
            # #print(ps.detail_dicts)
            if ps.detail_dicts:
                for k, v in ps.detail_dicts.items():
                    for s, t in v.items():
                        if k == 'nav-main-tmCount':
                            result_res['_container_tmInfo'][s] = t
                        elif k == '_container_recruit':
                            result_res['_container_baipin'][s] = t
                        else:
                            result_res[k][s] = t
            
            # #print(result_res)
            # #print(mongo_update_where)
            single_mongodb.mongodb_update(
                "company_detail_info", mongo_update_where, result_res)
            single_oracle.oracle_update("update company_basic_info set page_spider=1 where txt_id='{}'".format(txt_id))
            single_redis.server.hdel('cookies', str(ps.username))
            single_redis.put_cookies(name='cookies', phone=str(ps.username), cookie=str(dict(ps.tyc.get_cookies())))
            # exit()
        except Exception as e:
            logger.exception("Exception !{}".format(e))
            single_oracle.oracle_update(
                "update company_basic_info set page_spider=2 where txt_id='{}'".format(txt_id)
            )

if __name__ == "__main__":
    main(1)
