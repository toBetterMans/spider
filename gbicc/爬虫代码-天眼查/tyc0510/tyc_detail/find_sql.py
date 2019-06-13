#!/usr/bin/env python  
# -*- encoding: utf-8 -*-  

""" 
@author: niuweidong 
@software: PyCharm 
@file: find_sql.py 
@time: 2019/02/11 10:00 
"""
import timeit

from db import single_oracle

area_list = ['繁昌',
             '万州',
             '桃江',
             '丰宁',
             '新野',
             '肇东',
             '海门',
             '泰兴',
             '高淳',
             '武进',
             '锡山',
             '慈溪',
             '宁海',
             '浦东',
             '常熟',
             '滕州',
             '诸城',
             '邹城',
             '文登',
             '招远',
             '安塞',
             '苍南',
             '武义',
             '青田',
             '江山',
             '淳安',
             '丽水',
             ]
comany_table = 'company_basic_info'
company_11315 = 'company_11315'
company_11315_zyfd = company_11315 + '_zyfd'
sql_template = "select count(*) from {table} where {where}"
sql_11315_type = sql_template.format(table=company_11315, where='type is not null')
sql_11315_zyfd_type = sql_template.format(table=company_11315_zyfd, where='type is not null')
sql_11315_27 = sql_template.format(table=company_11315, where="address_2=''")
sql_company_not_page = sql_template.format(table=comany_table, where='page_spider=0')
sql_company_all_count = sql_template.format(table=comany_table, where='1=1')

sql_company = ""

def func():
    sql = "select count(company_number) from {table} where instr({address},'{area}') > 0 "
    
    for i in area_list:
        for table in [company_11315, company_11315_zyfd]:
            for address in ['address_2', 'address_3']:
                sql_ = sql.format(table=table, address=address, area=i)
                print(single_oracle.oracle_find_by_param_all(sql_))

class Main():
    
    def __init__(self):
        pass

if __name__ == "__main__":
    timeit.timeit()
    func()
