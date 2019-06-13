#!/usr/bin/env python  
# -*- encoding: utf-8 -*-  

""" 
@author: niuweidong 
@software: PyCharm 
@file: request_clietn.py 
@time: 2018/10/11 11:21 
"""


def func():
    import requests

    user_info = {'ENTINFO':'北京当当网信息技术有限公司','TYPE':'0'}
    
    r = requests.post("http://10.0.32.85:5000/company", data=user_info)

    print(r.text)


class Main():
    def __init__(self):
        pass


if __name__ == "__main__":
    func()
