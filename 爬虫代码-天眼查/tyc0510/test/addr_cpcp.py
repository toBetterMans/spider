# -*- coding:utf-8 -*-
# !/usr/bin/env python

'''
    auth：dyl
    software:Python
    env:Python3.5
    time:2019/3/24
'''
import os

import cx_Oracle
from cpca import *

from db import single_oracle

def db_conn():
    db = cx_Oracle.connect('c##shitou/123456@127.0.0.1/ORCL', encoding='utf-8')
    cursor = db.cursor()
    
    return cursor

# 执行oracle sql
def execute(sql):
    '''
    :param sql: oracle sql
    :return:    查询结果列表
    '''
    # cursor = db_conn()
    # sql = 'select company_address from company_11315_xa'
    # res = cursor.execute(sql)
    res = single_oracle.oracle_find_by_param_all(sql)
    return res

# 地址切分
def cpca_addr(res):
    '''
    :param res: 列表
    :return:
    '''
    if os.path.exists('./addr_2.txt'):
        os.remove('./addr_2.txt')
    with open('./addr_2.txt', 'a', encoding='utf-8')as f:
        
        for re in res:
            print(re[0])
            l = [re[0].replace(' ', '')]
            if re[0]:
                df = transform(l, myumap, cut=False)
                for addr in df.index:
                    addr_3 = df.loc[addr].values[0]
                    addr_2 = df.loc[addr].values[1]
                    addr_1 = df.loc[addr].values[2]
                    if addr_1:
                        if (addr_3 == '雄县' or addr_3 == '容城县' or addr_3 == '安新县',
                            addr_3 == '容城' or addr_3 == '安新') and addr_1 == '河北省':
                            # 测试 70
                            update_sql = "update tyc_qybj_jbxx set province ='{sheng}',city='{shi}',county='{xian}' where company_name='{comp_name}'".format(
                                sheng=addr_1, shi=addr_2, xian=addr_3, comp_name=re[1])
                            # 本地
                            # update_sql = "update company_11315 set address_1 ='{sheng}',address_2='{shi}',address_3='{xian}' where company_name='{comp_name}'".format(sheng=addr_1, shi=addr_2, xian=addr_3, comp_name=re[1])
                            single_oracle.execute(update_sql)
                            # print(update_sql)
                            f.write(re[0] + '   省:' + addr_1 + ',市:' + addr_2 + ',县:' + addr_3 + '\n')

# 切分营业期限
def business_term(res):
    for re in res:
        # print(re[0])
        
        if re[0] and re[0] != '-':
            term_l = re[0].split('至')
            # 营业期限自
            begin = term_l[0]
            # 营业期限至
            end = term_l[1]
            if end == '无固定期限':
                end = '2999-12-31'
            # print(begin, end)
        elif re[0] == '-':
            begin = '-'
            end = '-'
            # print(begin,end)
        
        sql = "update tyc_qybj_jbxx set business_term_begin ='{begin}', business_term_end = '{end}' where company_name='{name}'".format(
            begin=begin, end=end, name=re[1])
        print(sql)
        single_oracle.execute(sql)

if __name__ == '__main__':
    # sql = 'select company_address, company_name from company_11315'
    # 查询地址，切分省市县
    addr_sql = 'select register_site, company_name from tyc_qybj_jbxx'
    res = execute(addr_sql)
    cpca_addr(res)
    
    # 营业期限
    # term_sql ='select business_term from tyc_qybj_jbxx'
    # res = execute(addr_sql)
    # cpca_addr(res)
    
    # # 营业期限
    # term_sql ='select business_term,company_name from tyc_qybj_jbxx'
    # result = execute(term_sql)
    # business_term(result)
