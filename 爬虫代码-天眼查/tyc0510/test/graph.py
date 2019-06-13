#!/usr/bin/env python  
# -*- encoding: utf-8 -*-  

""" 
@author: niuweidong 
@software: PyCharm 
@file: test_gragh.py
@time: 2019/05/27 16:04
"""
import datetime
import json
import random
import re
import time
from urllib import parse

from bson import ObjectId

from db import single_mongodb
from request_file import *
from setting import USER_AGENTS

proxies = {
    "http": '127.0.0.1:8888',
    "https": '127.0.0.1:8888'
}
# proxies={}
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

nn = []

def tt(e, t, n):
    global nn
    # print(e, t, n, nn)
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
    print(r)
    rs = r[1] if len(r) > 1 else r
    rs = int(rs)
    print(rs)
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
    print(chars)
    print(fnStr)
    m = re.search(r"wtf=function\(\)\{return'(.*?)'\}\}\(window\)", fnStr, re.S)
    if not m:
        raise RuntimeError("未匹配上_ucourt")
    fxck = m.group(1).split(",")
    
    fxckStr = ''
    i = 0
    gen_chars = get_chars_by_companyId(key)
    while i < len(fxck):
        fxckStr += gen_chars[int(fxck[i])]
        i += 1
    print(fxckStr)
    return fxckStr

def get_cookie_by_request(company_id, url, re_key, json_obj_list,cookies):
    cookie_header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
    }
    if cookies:
        print('rtycid==============',cookies)
        cookie_header['Cookie']=cookies
    graph_con = requests.get(url, headers=cookie_header, proxies=proxies,verify=False)
    json_obj = json.loads(graph_con.text)
    fnStr = ''
    for item in eval(json_obj_list).split(","):
        fnStr += chr(int(item))
    print(fnStr)
    token = re.search(r'{}=(.*?);'.format(re_key), fnStr, re.S).groups()[0]
    # ps.tyc.set_cookies({'rtoken':rtoken})
    _u = gen_ucourt(company_id, fnStr)
    
    return [token, _u]
def genSsuid():
    return str(int(round(2147483647 * random.random()) *int(str(datetime.datetime.now())[-6:-3]) % 1e10))
    

class Main():
    
    def __init__(self):
        self.company_id = None
        self.tyc = RequestClass(proxies=proxies)
        self.ssuid=genSsuid()
        # 企业关系——操作详情
    
    def login(self):
        self.username, self.cookie = self.tyc.login()
    
    def company_graph_spider(self, ent_name):
        try:
            # self.login()
            print('企业关系——操作详情 抓取，公司：{}'.format(ent_name))
            graph_dicts = {}
            self.tyc.session.cookies.update({'ssuid': self.ssuid})  # str(self.suuid)  6912bee274b44f0781e3ae034c44e173
            rtycid_url='https://dis.tianyancha.com/dis/old'
            self.tyc.request_url(rtycid_url)
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
            
            rtycid_header=graph_header.copy()
            rtycid_header['Upgrade-Insecure-Requests']='1'
            rtycid_header['Accept'] ='text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3'
            
            rtycid_header['Referer'] ='https://www.tianyancha.com/company/{}'.format(self.company_id)
            
            print(dict(self.tyc.session.cookies))
            graph_cookie_url = 'https://dis.tianyancha.com/qq/{id}.json?random={tim}'.format(
                id=self.company_id, tim=str(int(time.time() * 1000)))
            graph_url = 'https://dis.tianyancha.com/dis/getInfoById/{id}.json?'.format(id=self.company_id)
            token_u_list = get_cookie_by_request(self.company_id, graph_cookie_url, 'rtoken', 'json_obj["data"]["v"]',cookies=self.tyc.get_cookies().get('RTYCID'))
            self.rutm = token_u_list[1]
            self.rtoken = token_u_list[0]
            
            self.tyc.session.cookies.update({'rtoken': self.rtoken})
            self.tyc.session.cookies.update({'_rutm': self.rutm})
            # self.tyc.session.cookies.update({'RTYCID':'780d591bf6664dca97d68ea5ccaa377a'})
            # self.tyc.session.cookies.update({'TYCID': '445bf2d080ea11e9b64f9d95cf8181ac'})
            # self.tyc.session.cookies.update({'CT_TYCID': '7dead7ec83a14fb886a4d87d6eb9bfef'})
            # self.tyc.session.cookies.update({'csrfToken': 'FE7iecRoMjHa8FipMvCh7FeI'})
            # self.tyc.session.cookies.update({'cloud_token': '6912bee274b44f0781e3ae034c44e173'})
            # self.tyc.session.cookies.update({'_utm': None})
            # self.tyc.session.cookies.update({'aliyungf_tc': None})
            # self.tyc.session.cookies.update({'csrfToken': None})
            # self.tyc.session.cookies.update({'token': None})
            # print(dict(self.tyc.session.cookies))
            self.get_detail_spider(
                graph_url,
                graph_dicts, '_graph_container',
                custom_header=graph_header)
            print(graph_dicts)
            return graph_dicts
        except Exception as e:
            print("Exception !{}".format(e))
    
    def check_login(self, con):
        if con and con.status_code == 200 and 'antirobot' not in con.url:
            return True
        
        elif not con or u"请输入您的手机号码" in con.text or u"我们只是确认一下你不是机器人" in con.text:
            print("userName: {}  forbid  status_code={}".format(self.username, con.status_code))
            print(self.tyc.get_cookies())
            # single_oracle.oracle_update(
            #     "update tyc_user set user_forbid=1 ,user_used=0 where username='{}'".format(self.username))
            single_redis.server.hdel('cookies', self.tyc.username)
            if con.status_code == 401 or '密码登录' in con.text:
                print('cookie失效！！！')
                single_redis.server.lpush('users', self.tyc.username)
            else:
                single_redis.put_cookies(phone=self.tyc.username, cookie=self.cookie, name='forbids')
            return False
    
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
            'Host': str(host),
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': random.choice(USER_AGENTS)
        }
        if custom_header:
            headers = custom_header
        while mark > 0:
            try:
                # self.login()
                print(dict(self.tyc.session.cookies))
                con = self.tyc.request_url(url=url, headers=headers)
                print(con.status_code, '!!!' * 100)
                if not self.check_login(con):
                    self.get_detail_spider(url, dicts, key)
                    mark = -1
                # key = str(law_number).replace(".", "-").replace('（','').replace('）','')
                key = str(key).replace("'", '').replace('.', '_')
                dicts[key] = con.text.replace("'", '')
                mark = -1
            except requests.exceptions.ProxyError as error:
                mark = -1
                print("Proxy Error! {}".format(error))
                continue
            except Exception as e:
                mark = -1
                print("Exception !{}".format(e))
                continue

if __name__ == "__main__":
    m = Main()
    mongo_where_parameter = {}
    mongo_where_parameter['_id'] = ObjectId('5ce688d3fd79703590a40a7b')
    mongo_table = "company_detail_info"
    mongo_result = single_mongodb.mongodb_find_one(
        mongo_table, mongo_where_parameter)
    # text=mongo_result['text']
    # m.soup = BeautifulSoup(text, 'lxml')
    m.company_id = mongo_result['url'].replace(
        "https://www.tianyancha.com/company/", "")
    m.company_graph_spider('软通动力信息技术（集团）有限公司')
