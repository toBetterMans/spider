#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@author: niuweidong
@software: PyCharm
@file: replace_special_util.py
@time: 2019/06/12 16:05
"""

def replace_special_chars(text: str):
    '''
    去除字符串中的特殊字符
    :param text: 字符串
    :return: 字符串
    '''
    try:
        text = text.replace(r'<em>', r'') \
            .replace(r'</em>', r'') \
            .replace(r'\ue004', r'') \
            .replace(r'\ufffd', r'') \
            .replace(r'\u2022', r'') \
            .replace(r'\xb3', r'') \
            .replace(r'\ue005', r'') \
            .replace(r'\xa9', '') \
            .replace(r'\u003C', r'') \
            .replace(r'\u003E', r'') \
            .replace(r'\ufffd', r'') \
            .replace(r'\ufffd', r'') \
            .replace(r'\xa9', r'') \
            .replace(r'\u002F', r'/') \
            .replace(r'\u003E', r'') \
            .replace(u"'", r'"') \
            .replace(r'\u003c\u0065\u006d\u003e', r'<em>') \
            .replace(r'\u003c\u002f\u0065\u006d\u003e', '</em>') \
            .replace(r'\xa5', r'') \
            .replace(r'\xa0', r'') \
            .replace(r'\uff08', '(').replace(r'\u0029', ')') \
            .replace(r'（', '(').replace(r'）', ')').replace(r'\u3000', '')
    except Exception as e:
        print(e)
    return text

if __name__ == "__main__":
    pass
