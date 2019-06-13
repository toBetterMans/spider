#!/usr/bin/env python  
# -*- encoding: utf-8 -*-  

""" 
@author: niuweidong 
@software: PyCharm 
@file: js_2_python.py 
@time: 2019/05/23 11:22 
"""
r = "abcdefghijklmnopqrstuvwxyz1234567890-~!"

def func():
    e = {}
    global r
    # r=list(r)
    # print(r)
    for k,v in enumerate(r):
        e[v]=k
    print(e)

class Main():
    
    def __init__(self):
        pass

if __name__ == "__main__":
    func()
