#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@author: niuweidong
@software: PyCharm
@file: test_remove_tags.py
@time: 2019/06/12 15:13
"""
import html as ht
from lxml import html
from lxml import etree


def __remove_tag(lxml_html, tag):
    head_ele = lxml_html.xpath('//{tag}'.format(tag=tag))
    for e in head_ele:
        e.getparent().remove(e)

def remove_unused_tags(text: str):
    '''
    去除 path标签和head标签内容，缩减HTML内容，可缩减20000行左右，接近1/3-1/2
    :param text: 需要去除标签的HTML文本
    :return: text:抛异常返回传入文本，否则返回缩减后的文本
    '''
    try:
        lxml_html = etree.HTML(text)
        __remove_tag(lxml_html, 'head')
        __remove_tag(lxml_html, 'path')
        __remove_tag(lxml_html, 'svg')
        text = html.tostring(lxml_html).decode()
        text = ht.unescape(text)
    except Exception as e:
        print(e)
    return text


if __name__ == "__main__":
    with open('../test/华为.html', 'r+', encoding='utf-8') as f:
        text = f.read()
        print(len(text))
        text = remove_unused_tags(text)
        print(len(text))
        print(text)  # unescape()将字符串中的uncode变化转成中文
        # lxml_html.
