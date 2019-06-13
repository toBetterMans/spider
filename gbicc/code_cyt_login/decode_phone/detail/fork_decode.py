#!/usr/bin/env python  
# -*- encoding: utf-8 -*-  

""" 
@author: niuweidong 
@software: PyCharm 
@file: fork_main.py 
@time: 2018/10/30 9:58 
"""
import multiprocessing
import sys
from multiprocessing import process
from decode_phone_ruokuai import main
import time
def func(args):
    print(args)
    # time.sleep(int(args)*7)
    main(args)



if __name__ == "__main__":
    mains=sys.argv
    print(mains)
    if len(mains)==1:
        max_pool_amount=10
    # print(mains.count())
    # for i in mains[1:]:
    #
    #     print(i)
    else:
        max_pool_amount = mains[1:]
        max_pool_amount=max_pool_amount[0]
        max_pool_amount=int(max_pool_amount)
        print(max_pool_amount)
    # max_pool_amount=int(mains[1:][0])
    pool = multiprocessing.Pool(processes=max_pool_amount)
    for i in range(max_pool_amount):
        msg = "hello %d" % (i)
        pool.apply_async(func, (i,))  # 维持执行的进程总数为processes，当一个进程执行完毕后会添加新的进程进去
        time.sleep(30)

    print "Mark~ Mark~ Mark~~~~~~~~~~~~~~~~~~~~~~"
    pool.close()
    pool.join()  # 调用join之前，先调用close函数，否则会出错。执行完close后不会有新的进程加入到pool,join函数等待所有子进程结束
    print "Sub-process(es) done."

