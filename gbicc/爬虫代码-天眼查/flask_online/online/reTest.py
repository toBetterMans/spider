#!/usr/bin/env python  
# -*- encoding: utf-8 -*-  
import os
import re
import requests
""" 
@author: niuweidong 
@software: PyCharm 
@file: re.py 
@time: 2018/09/28 17:32 
"""
re_doctor=re.compile(r'bp_doctor_about.*?</script>')
# re_doctor_results=re.compile(r'<h2>(.*?)<\\/h2>.*\\u804c\\u3000\\u3000\\u79f0\\uff1a<\\/td>.*?top\\">(.*?)<\\/td>.*truncate_DoctorSpecialize.*?\\">(.*?)<\\/div>.*\\"full\\".*?\\">(.*?)<span>')
# 图片
re_image=re.compile(r'src=\\"(.*?)\\".*\\/><\\/td>')
# url
re_Url= re.compile(r'href="//(.*?)/\?oa=Admin_Doctor,Online"')
# 科室
re_Section=re.compile(r'<h2>(.*?)<\\/h2>')
# 职称
re_Title=re.compile(r'\\u804c\\u3000\\u3000\\u79f0\\uff1a<\\/td>.*?top\\">(.*?)<\\/td>')
# 擅长
re_Good=re.compile(r'truncate_DoctorSpecialize.*?\\">(.*?)<\\/div>')
# 执业经历
re_Experience1=re.compile(r'\\u6267\\u4e1a\\u7ecf\\u5386.*?top\\">(.*?)<\\/td>')
re_Experience=re.compile(r'"full\\".*?\\">(.*?)<span>')
re_all=re.compile(r'style=\\"word-wrap:break-word;word-break:break-all;\\">(.*?)<\\/div>')
def func():
    url0='https://www.haodf.com/doctor/DE4r0Fy0C9LuSQuZEy6ClyviZLC3b3s8R.htm'
    url1='https://www.haodf.com/doctor/DE4r0Fy0C9LuhnJqrr3evRiUuDINgIYJg.htm'
    # url2='https://www.haodf.com/doctor/DE4r0BCkuHzduS0gaNHeCoEzBhPT2.htm'
    url2='https://www.haodf.com/doctor/DE4r0eJWGqZNwkSyPDHC0YZs9VRuHhQJ.htm'
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3486.0 Safari/537.36'}
    html_text=requests.get(url0,headers=headers).text
    # with open('re.html','r') as f :
    #     #     html_text=f.read()
    # print(html_text)
    re_result=re_doctor.search(html_text)
    re_script = re_result.group(0).replace('&nbsp;', ' ').replace('\\t', '').replace('\\n', '').replace(' ', '')
    # all=re_all.findall(re_script)
    # print(all)
    # for i in all:
    #     print('\n'+i.encode("utf-8").decode("unicode-escape"))
    # exit()


    url=re_Url.search(html_text)
    if url:
        url='http://'+url.group(1)
    else:
        url='暂无'


    # print(re_script)
    image='http:'+re_image.search(re_script).group(1).replace('\\','')
    title = re_Title.search(re_script)
    if title:
        title = title.group(1).encode("utf-8").decode("unicode-escape") or '暂无'
    good=re_Good.search(re_script)
    if good:
        good=good.group(1).encode("utf-8").decode("unicode-escape") or '暂无'
    section = re_Section.search(re_script)
    if section:
        section=section.group(1).encode("utf-8").decode("unicode-escape") or '暂无'
    experience = re_Experience.search(re_script)
    if experience:
        experience = experience.group(1).encode("utf-8").decode("unicode-escape") or '暂无'
    else:
        experience = re_Experience1.search(re_script)
        if experience:
            experience=experience.group(1).encode("utf-8").decode("unicode-escape") or '暂无'
    print(image)
    print(good)
    print(section)
    print(experience)
    print(url)
    print(title)
class Main():
    def __init__(self):
        pass

def foo():
    print("starting...")
    while True:
        res = yield 4
        print("res:",res)



if __name__ == "__main__":
    g = foo()
    print(next(g))
    print("*" * 20)
    print(next(g))
