#!/usr/bin/env python  
# -*- encoding: utf-8 -*-  

""" 
@author: niuweidong 
@software: PyCharm 
@file: tyc_test_script.py 
@time: 2018/11/08 10:18 
"""
import os
from lxml import etree
def func():
    with open('tyc.html') as f:
        html=f.read()
    tyc_html_xpath=etree.HTML(html)
    trs=tyc_html_xpath.xpath('//div[@id="_container_announcementcourt"]/table/tbody/tr')
    for tr in trs:
        tds=tr.xpath('./td')
        # s=tds[5].xpath('./script/text()')[0]
        s=tds[5].xpath('string(.)')
        print(s)
        # print(s.replace('"','\\"'))
    
    pass

def int2char():
    v="33,102,117,110,99,116,105,111,110,40,110,41,123,100,111,99,117,109,101,110,116,46,99,111,111,107,105,101,61,39,114,116,111,107,101,110,61,52,98,57,52,50,54,53,102,102,53,100,54,52,100,99,52,56,51,51,56,101,102,100,100,54,56,53,57,52,56,99,97,59,112,97,116,104,61,47,59,39,59,110,46,119,116,102,61,102,117,110,99,116,105,111,110,40,41,123,114,101,116,117,114,110,39,56,44,55,44,50,49,44,51,52,44,50,51,44,51,52,44,50,44,50,53,44,56,44,53,44,51,49,44,56,44,49,57,44,51,54,44,50,49,44,49,57,44,49,49,44,49,56,44,51,49,44,55,44,49,54,44,48,44,50,49,44,48,44,48,44,50,51,44,55,44,49,49,44,49,49,44,53,44,48,44,51,52,39,125,125,40,119,105,110,100,111,119,41,59"
    vs=v.split(',')
    m=[chr(int(s))  for s in vs ]
    print(''.join(m))
class Main():
    
    def __init__(self):
        pass

if __name__ == "__main__":
    int2char()
