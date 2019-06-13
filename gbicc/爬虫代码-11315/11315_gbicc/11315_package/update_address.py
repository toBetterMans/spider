#!/usr/bin/env python  
# -*- encoding: utf-8 -*-  

""" 
@author: niuweidong 
@software: PyCharm 
@file: update_address.py 
@time: 2019/04/02 13:32 
"""

from cpca import *
def func():
    pass


if __name__ == "__main__":
    while 1:
        id_companyName=single_reids.server.rpop('11315_updates')
        if not id_companyName:
            single_reids.put_11315_update()
            id_companyName = single_reids.server.rpop('11315_updates')
        id_companyName=id_companyName.decode()
        
        print(id_companyName)
        # print(id_companyName.decode())
        id=id_companyName.split(';')[0]
        adress = id_companyName.split(';')[1]
        # cpca  的核心方法 传入 地址的列表，如['xx省xx市xx县'] ，cut=False :不使用结巴分词，根据默认字典进行全局匹配 cut=True：单纯结巴分词
        df = transform([adress], cut=False)
        addr_1=addr_2=addr_3=None
        print(df)
        for addr in df.index:
            print(addr)
            addr_1 = df.loc[addr].values[0]
            addr_2 = df.loc[addr].values[1]
            addr_3 = df.loc[addr].values[2]
        if addr_3:
            single_oracle.oracle_update("update company_11315 set address_1='{}',address_2='{}',address_3='{}',parse=6 where company_number={}".format(addr_1,addr_2,addr_3,id))
