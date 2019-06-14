#!/usr/bin/env python  
# -*- encoding: utf-8 -*-  

""" 
@author: niuweidong 
@software: PyCharm 
@file: try_and_except_util.py 
@time: 2019/06/14 14:43 
"""

def try_and_text(func, variable):
    s = '解析有误'
    if not func:
        return 'NA'
    try:
        s = eval(func)
    except Exception as e:
        print(e)
    finally:
        return s

if __name__ == "__main__":
    pass  
