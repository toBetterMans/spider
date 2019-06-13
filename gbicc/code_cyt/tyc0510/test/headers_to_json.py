#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/22 14:01
# @Author  : Jun
# @Site    : 
# @File    : headers_to_json.py
# @Software: PyCharm
def headers_to_json(header:str):
    '''
    将字符串转headers字典
    :param header: 传入的header字符串
    :return: headers 字典
    '''
    header_str = {}
    data=header.split('\n')
    for i in data:
        j, k = i.replace('\n','').split(': ')
        header_str[j] = k
    return str(header_str).replace("',","',\n")

if __name__ == '__main__':
    #注意字符串三引号首尾不换行
    hh = """Host: ccdas.ipmph.com
Connection: keep-alive
Accept: */*
Origin: http://ccdas.ipmph.com
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36
DNT: 1
Content-Type: application/json
Referer: http://ccdas.ipmph.com/rwDisease/rwDiseaseList
Accept-Language: zh-CN,zh;q=0.9
Cookie: jeesite.session.id=8e5cf904d598435696820281e17d1d94; JSESSIONID=FA5967706396AD7BF58BFF249AAA17A2; __utma=182039349.1175319252.1560157997.1560157997.1560157997.1; __utmc=182039349; __utmz=182039349.1560157997.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; __utmb=182039349.1.10.1560157997; wzws_cid=124b05ec2c4e42d5beb176eae45a0b09f6dc1e3b4ed043b9737cf8aaf3cc0c9827283b0b1fc81e9188bbf179d7eb2e6be4333ac51128299c29274b7550f2a780
Accept-Encoding: gzip, deflate
Content-Length: 98"""
    res = headers_to_json(hh)
    print(res)
