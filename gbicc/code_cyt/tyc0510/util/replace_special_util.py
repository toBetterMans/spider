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
<<<<<<< HEAD
        text = text.replace(
            r'<em>',
            '').replace(
            r'</em>',
            '').replace(
            r'\ue004',
            '').replace(
            r'\ufffd',
            '').replace(
            r'\u2022',
            '').replace(
            r'\xb3',
            '').replace(
            r'\ue005',
            '').replace(
            r'\xa9',
            '').replace(
            r'\u003C',
            '').replace(
            r'\u003E',
            '').replace(
            r'\ufffd',
            '').replace(
            r'\ufffd',
            '').replace(
            r'\xa9',
            '').replace(
            r'\u002F',
            '').replace(
            r'\u003E',
            '').replace(
            r"'",
            r'"').replace(
            r'\u003c\u0065\u006d\u003e',
            '').replace(
            r'\u003c\u002f\u0065\u006d\u003e',
            '').replace(
            r'\xa5',
            '').replace(
            r'\xa0',
            '').replace(r'\uff08', '(').replace(r'\u0029', ')').replace('（', '(').replace('）', ')')
=======
        text= text.replace(
            r'<em>',
            r'').replace(
            r'</em>',
            r'').replace(
            r'\ue004',
            r'').replace(
            r'\ufffd',
            r'').replace(
            r'\u2022',
            r'').replace(
            r'\xb3',
            r'').replace(
            r'\ue005',
            r'').replace(
            r'\xa9',
            '').replace(
            r'\u003C',
            r'').replace(
            r'\u003E',
            r'').replace(
            r'\ufffd',
            r'').replace(
            r'\ufffd',
            r'').replace(
            r'\xa9',
            r'').replace(
            r'\u002F',
            r'').replace(
            r'\u003E',
            r'').replace(
            u"'",
            r'"').replace(
            r'\u003c\u0065\u006d\u003e',
            r'').replace(
            r'\u003c\u002f\u0065\u006d\u003e',
            '').replace(
            r'\xa5',
            r'').replace(
            r'\xa0',
            r'').replace(r'\uff08', '(').replace(r'\u0029', ')').replace('（', '(').replace('）', ')')
>>>>>>> e61a9a1a6497e8258888f5bcf7b7c942587a251f
    except Exception as e:
        print(e)
    return text


if __name__ == "__main__":
    #
    a = r'{"bondNum":"7090","remark":"","interestDiff":175,"bondName":"01中国移动债","bondStopTime":1308067200000,"issuedPrice":100,"tip":"对于含权债，票面利率\u002F利差指行权前的票面利率\u002F利差。","id":34569,"refInterestRate":2.5,"escrowAgent":"中央国债登记结算公司","bondTimeLimit":"10年","debtRating":"AAA","publishTime":992793600000,"realIssuedQuantity":50,"isDelete":null,"faceInterestRate":4,"updateTime":1554887651000,"exeRightType":"","planIssuedQuantity":0,"calInterestType":"浮动利率","publishExpireTime":1308326400000,"createTime":1464250069000,"publisherName":"中国移动通信集团广东有限公司","faceValue":100,"flowRange":"公开发行","bondType":"企业债","bondTradeTime":1143475200000,"exeRightTime":null,"creditRatingGov":"中诚信国际信用评级有限公司","payInterestHZ":"年","startCalInterestTime":992793600000}'
    b = replace_special_chars(a)
    print(b)
