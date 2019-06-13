#!/usr/bin/env python  
# -*- encoding: utf-8 -*-  

""" 
@author: niuweidong 
@software: PyCharm 
@file: replace_special_util.py 
@time: 2019/06/12 16:05 
"""

def replace_special_chars(text:str):
    '''
    去除字符串中的特殊字符
    :param text: 字符串
    :return: 字符串
    '''
    try:
        text= text.replace(
            u'<em>',
            u'').replace(
            u'</em>',
            u'').replace(
            u'\ue004',
            u'').replace(
            u'\ufffd',
            u'').replace(
            u'\u2022',
            u'').replace(
            u'\xb3',
            u'').replace(
            u'\ue005',
            u'').replace(
            u'\xa9',
            '').replace(
            u'\u003C',
            u'').replace(
            u'\u003E',
            u'').replace(
            u'\ufffd',
            u'').replace(
            u'\ufffd',
            u'').replace(
            u'\xa9',
            u'').replace(
            u'\u002F',
            u'').replace(
            u'\u003E',
            u'').replace(
            u"'",
            u'"').replace(
            u'\u003c\u0065\u006d\u003e',
            u'').replace(
            u'\u003c\u002f\u0065\u006d\u003e',
            '').replace(
            u'\xa5',
            u'').replace(
            u'\xa0',
            u'').replace(r'\uff08', '(').replace(u'\u0029', ')').replace('（', '(').replace('）', ')')
    except Exception as e:
        print(e)
    return text
    

if __name__ == "__main__":
    pass  
