#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import base64

import urllib
import urllib2
from io import BytesIO
import os
import requests
import time
import json
# from ruokuai import RClient

from request_file import RequestClass
from redis_cache import single_reids
import sys
from PIL import Image
import numpy as np
reload(sys)
sys.setdefaultencoding('utf-8')

""" 
@author: niuweidong 
@software: PyCharm 
@file: get_company.py 
@time: 2018/09/12 16:02 
"""
# https://antirobot.tianyancha.com/captcha/verify?return_url=https%3A%2F%2Fwww.tianyancha.com%2Fsearch%3Fkey%3D%25E6%258B%25BC%25E5%25A4%259A%25E5%25A4%259A&rnd=
# 机器人解封页面

'''
验证码坐标范围：[{"x":0,"y":97},{"x":0,"y":3},{"x":313,"y":4},{"x":316,"y":94}]

'''

def jianjiao(image_source):
    host = 'http://apigateway.jianjiaoshuju.com'
    path = '/api/v_1/yzmCrd.html'
    method = 'POST'
    appcode = '68C9A16A71DDE2C4EE623ACF5AE648C5'
    appKey = 'AKID191d0b7a10e195468d353987c67e2685'
    appSecret = 'c02b2a2ea0b028654d6c0b07038501ff'
    querys = ''
    bodys = {}
    url = host + path
    with open(image_source, "rb") as f:
        # print(f)
        bodys['v_pic'] = base64.b64encode(f.read())
        print(bodys['v_pic'])
        bodys['v_type'] = 'crd'
        post_data = urllib.urlencode(bodys)
        request = urllib2.Request(url, post_data)
        request.add_header('appcode', appcode)
        request.add_header('appKey', appKey)
        request.add_header('appSecret', appSecret)
        # // 根据API的要求，定义相对应的Content - Type
        request.add_header('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8')
        response = urllib2.urlopen(request)
        
        content = response.read()
        print(type(content))
        content=json.loads(content)
        if (content):
            return content



# logging.config.fileConfig("../log_file/companySearchLogA.conf")
# logger = logging.getLogger("loggerTxt")
dicts = {}
proxyHost = "http-dyn.abuyun.com"
proxyPort = "9020"

proxyUser = "H4LG0005632SP1YD"
proxyPass = "CA6EAB506F5B965F"

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
proxies = {}

verify_url = 'https://antirobot.tianyancha.com/captcha/verify?return_url=https%3A%2F%2Fwww.tianyancha.com%2Fsearch%3Fkey%3D%25E6%258B%25BC%25E5%25A4%259A%25E5%25A4%259A&rnd='
data_id_url = 'https://antirobot.tianyancha.com/captcha/getCaptcha.json?t=1539311796128&_=1539311796111'
data_id_heders = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Host': 'antirobot.tianyancha.com',
    # 'Referer': ' https://antirobot.tianyancha.com/captcha/verify?return_url=https%3A%2F%2Fwww.tianyancha.com%2Fsearch%3Fkey%3D%25E6%258B%25BC%25E5%25A4%259A%25E5%25A4%259A&rnd=',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3486.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}
antirobot_headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    'Cache - Control': 'max - age = 0',
    "Connection": "keep-alive",
    'Host': 'antirobot.tianyancha.com',
    'Upgrade - Insecure - Requests': '1',
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3486.0 Safari/537.36"
}
# https://antirobot.tianyancha.com/captcha/checkCaptcha.json?captchaId=598a97f3-bba2-49fa-8cbf-4f4630b8b803&clickLocs=[{%22x%22:243,%22y%22:43},{%22x%22:222,%22y%22:54}]&t=1539312834761&_=1539311796112

# https://antirobot.tianyancha.com/captcha/checkCaptcha.json?captchaId=191b1e38-1011-4935-b983-f8ac9e16b76e&clickLocs=[{'y': 42.79, 'x': 271.0}, {'y': 46.79, 'x': 40.0}, {'y': 14.79, 'x': 237.0}]&t=1539324729789&_=1539324739052 proxies: {}
submit_headers = {

    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Host': 'antirobot.tianyancha.com',
    'Referer': 'https://antirobot.tianyancha.com/captcha/verify?return_url=https%3A%2F%2Fwww.tianyancha.com%2Fsearch%3Fkey%3D%25E6%258B%25BC%25E5%25A4%259A%25E5%25A4%259A&rnd=',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3486.0 Safari/537.36',
    'X-CSRFToken': 'null',
    'X-Requested-With': 'XMLHttpRequest'

}


class ReqCompany(object):
    def __init__(self):
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

        # self.redisClient = RedisUtil()
        self.tyc = RequestClass(proxies=proxies)
        self.username = ''
        self.mark_count = self.login()

        self.output_img = ''

    def login(self):
        self.username,self.cookie = self.tyc.login()
        return  0

    def check(self):
        url = "https://www.tianyancha.com/search?key=%s&checkFrom=searchBox" % urllib.quote('北京小度信息科技有限公司')
        try:
            con = self.tyc.session.get(url=url, headers=self.headers,proxies=proxies)
            # 判断账号是否被封
            if con.status_code != 403:
                if u"请输入您的手机号码" in con.text or u"我们只是确认一下你不是机器人" in con.text or con is None or con.status_code != 200:
                    print ("userName: {}  forbid " .format(self.username))
                    return True
        except requests.exceptions.ProxyError as error:
            print (error)
            # logger.info("Proxy Error!", error)
        except Exception as e:
            print (e)
            self.check()
        time.sleep(1)
        return False


    def varify_code(self):
        # rc = RClient('feiniubuke', 'feiniubuke123', '1', 'b40ffbee5c1cf4e38028c197eb2fc751')
        # im = open(self.output_img, 'rb').read()
        # resut_tuple = rc.rk_create(im, 6900)
        resut_tuple=jianjiao(self.output_img)
        return resut_tuple

    def get_company_list(self, company_name):
        key = company_name
        satrTime = int(time.time() * 1000)
        # 网页抓取
        try:
            if self.check():
            # print("Search Company %s")

                url = verify_url
                data_con = self.tyc.session.get(url=data_id_url, headers=data_id_heders,proxies=proxies)
                data_id = data_con.json()['data']['id']
                targetImage_base64 = data_con.json()['data']['targetImage']
                bgImage = data_con.json()['data']['bgImage']
                targetImage = base64.b64decode(targetImage_base64)
                bgImage = base64.b64decode(bgImage)

                baseimg = Image.open(BytesIO(bgImage))

                sz = baseimg.size
                basemat = np.atleast_2d(baseimg)

                im = Image.open(BytesIO(targetImage))
                # resize to same width
                sz2 = im.size
                if sz2 != sz:
                    im = im.resize((sz[0], round(sz2[0] / sz[0] * sz2[1])), Image.ANTIALIAS)
                mat = np.atleast_2d(im)
                basemat = np.append(basemat, mat, axis=0)

                self.output_img = 'merge{}.png'.format(str(os.getpid())+'-')
                report_img = Image.fromarray(basemat).convert('L').save(self.output_img)

                # report_img.save( self.output_img)
                # from PIL import Image
                # img = Image.open( self.output_img).convert('L')
                # img.save(self.output_img)
                # picture = cv2.imread('merge.png', cv2.IMREAD_COLOR)
                # picture = cv2.cvtColor(picture, cv2.COLOR_BGR2GRAY)
                # picture = picture[int(top):int(bottom), int(left):int(right)]
                # cv2.imwrite('merge.png', picture)
                print('已获取验证码图片。。。')
                results = self.varify_code()
                print('已获取验证码坐标。。。')
                # results=u'24,49.258,83'
                print(results)
                results_json = str(results['v_code'])
                results=results_json.split('|')
                list_str = '['
                for i in results:
                    list_str += '{%22x%22' + ':' + str(i.split(',')[0])
                    list_str += ',%22y%22' + ':' + str(i.split(',')[1]) + "},"

                list_str = list_str[:-1] + ']'
                # print(list_str)
                endTime = int(time.time() * 1000)
                submit_url = 'https://antirobot.tianyancha.com/captcha/checkCaptcha.json?captchaId={dataId}&clickLocs={lists}&t={starTime}&_={endTime}'
                submit_url = submit_url.format(dataId=data_id, lists=list_str, starTime=endTime, endTime=satrTime)
                con = self.tyc.session.get(url=submit_url, headers=submit_headers,proxies=proxies)

                print(con.text)
                Success = con.json().get('state')  # state=ok 成功；state=fail 失败
                # print(con.headers)成功{'Success': '1', 'Content-Encoding': 'gzip', 'Transfer-Encoding': 'chunked', 'Vary': 'Accept-Encoding', 'Connection': 'keep-alive', 'Date': 'Fri, 12 Oct 2018 09:14:19 GMT', 'Content-Type': 'application/json;charset=UTF-8'} 会有Success
                print ("^"*40)
                print(Success)
                # os.remove('./' + self.output_img)
                
                if Success == 'fail':
                    self.get_company_list('北京当当网信息技术有限公司')
                else:
                    # update_sql = "UPDATE tyc_user SET user_forbid=0 WHERE username='{}'".format(self.username)
                    # single_oracle.oracle_update(update_sql)
                    if not self.check():
                        new_name=self.output_img.split('.')[0] + results_json.replace('|','_') + '.png'
                        os.rename(self.output_img,new_name)
                        self.cookie=self.tyc.get_cookies()
                        single_reids.server.hdel('cookies', str(self.username))
                        single_reids.put_cookies(self.username,str(self.cookie))
                        single_reids.server.hdel('forbids',str(self.username))
                        self.login()
                        self.get_company_list('北京当当网信息技术有限公司')
            else:
                print('没有被封')
                # update_sql = "UPDATE tyc_user SET user_forbid=0 WHERE username='{}'".format(self.username)
                # single_oracle.oracle_update(update_sql)
                self.cookie = self.tyc.get_cookies()
                single_reids.server.hdel('cookies',str(self.username))
                single_reids.put_cookies(self.username, self.cookie)
                single_reids.server.hdel('forbids', str(self.username))
                self.login()
                self.get_company_list('北京当当网信息技术有限公司')
        except Exception as e:
            print (e)

#
def main(args):
    i = 0
    # print(sTime)
    while True:
        try:
            print('开始解码。。。。。。。。' + str(i))
            sTime = time.time()
            r = ReqCompany()
            mm = r.get_company_list('北京当当网信息技术有限公司')
            eTime = time.time()
            print('解码完成。。。。。。。。')
            # print(eTime)
            # print(type(eTime))
            print((int(eTime) - int(sTime)))
            i = i + 1
        except Exception as e:
            print(e)

if __name__ == "__main__":
    main(1)
