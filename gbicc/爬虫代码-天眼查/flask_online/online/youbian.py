#!/usr/bin/env python  
# -*- encoding: utf-8 -*-
import os

import requests
from bs4 import BeautifulSoup
""" 
@author: niuweidong 
@software: PyCharm 
@file: youbian.py 
@time: 2018/10/31 15:03 
"""

headers={

"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
"Accept-Encoding": "gzip, deflate",
"Accept-Language": "zh-CN,zh;q=0.9",
"Cache-Control": "max-age=0",
"Connection": "keep-alive",
"Cookie": "bdshare_firstime=1540969261444",
"Host": "www.ip138.com",
"If-None-Match": "24bfd7318954d41:15b6",
"Referer": "http://www.ip138.com/30/",
"Upgrade-Insecure-Requests": "1",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3486.0 Safari/537.36"

}

def func():
    url = 'http://www.ip138.com/post/'
    resp=requests.get(url,headers=headers)
    resp.encoding="gb2312"
    text=resp.text
    # print(text)
    soup=BeautifulSoup(text, 'lxml')
    hrefs=soup.find("div",id="newAlexa").find_all('a')
    href_list={}
    for href in hrefs:
        # href_list.append()
        href_list[href.string]=href.get('href')
        # print(href.get('href'))
    youbian_url="http://www.ip138.com"
    print(href_list)

    llll=[]
    # with open('youbian.txt', mode='w') as f:
    dicts = {}
    for i in href_list.keys():
        url_2=youbian_url+href_list[i]
        re=requests.get(url_2,headers=headers)
        re.encoding='gb2312'
        text2=re.text
        # text2.replace('')
        soup2=BeautifulSoup(text2, 'lxml')

        trs=soup2.find('table',attrs={'class':'t12'}).find_all('tr')
        # print(soup2.find('table',attrs={'class':'t12'}).prettify())

        lists=[]
        shi_list=[]

        names=[]
        values=[]
        ll={}
        quxian_dics = {}
        t=0
        for tr in trs:
           
            # type=0
            tds=tr.find_all('td')
            # print(len(tds))
            # print(td.text)
            if len(tds)==4:
                t= 1
                # quxian_dics[tds[0].text] = tds[1].text
                # name=tds[0].text
                names.append(tds[0].text)
                values.append(tds[1].text)
                # print(name)
                shi_dict={}
                k=len(names)-1
                v=len(values)-1
                if k>0:
                    quxian_dics[names[k-1]]=values[v-1]
                    ll[names[k-1]]=quxian_dics.copy()
                    
                    quxian_dics = {}
                
                
            elif len(tds)==6:
                
                quxian_dics[tds[0].text]=tds[1].text
                quxian_dics[tds[3].text] = tds[4].text
                
        if t==0:
            print('{}{}'.format(i,quxian_dics))

            ll[i] = quxian_dics.copy()

            
            # print(ll)
        # name=quxian_dics.keys()
        # print(type(name))
        # print(name)
        # exit()
        
        # ll[name]=quxian_dics.copy()
        dicts[i]=ll.copy()

    print(dicts)
        # llll.append(dicts2)
        # print(dicts)

            # f.writelines(dicts)


def func2():
    dits={}
    list0 = []
    list1 = []
    list2 = []
    for i in dits.keys():

        # 市区列表
        for k,v in enumerate(dits[i]):
            if k<6:
                continue
            # print(k,v)
            if k%3==0:
                list0.append(v)
            elif k%3==1:
                list1.append(v)
            else:
                list2.append(v)
    dicts={}
    list_temp=[]
    print(list0)
    print(list1)

    print(list2)
    print(len(list0))
    print(len(list1))
    print(len(list2))
    # exit()
    lisss = {}
    for i,v in enumerate(list2):
        if i==0:
            list_temp.append(v)
        # if i <6:
        #     continue
        name=''

        # print(list2[i],list_temp)
        if v in list_temp:
            lisss[list0[i]]=list1[i]
        else:
            print(lisss)
            dicts[name]=lisss.copy()
            lisss={}
            list_temp.append(v)
            name = list0[i]
        # print(lisss)
        #
    print(dicts)
class Main():
    def __init__(self):
        pass


if __name__ == "__main__":
    func()

    # print(0%3)
    # print(1 % 3)
    # print(2 % 3)
    # print(3 % 3)
    # print(4 % 3)
