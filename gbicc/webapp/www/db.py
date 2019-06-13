#!/usr/bin/env python  
# -*- encoding: utf-8 -*-  

""" 
@author: niuweidong 
@software: PyCharm 
@file: db.py 
@time: 2018/04/11 9:22 
"""
# 数据库引擎对象:
import threading
from _threading_local import local


class _Engine(object):
    def __init__(self,connect):
        self._connect=connect
    def connect(self):
        return self._connect

engine=None

#数据库连接的上下文对象
class _DbCtx(threading.local):
    def __init__(self):
        self.connection=None
        self.transactions=0
    def is_init(self):
        return not self.connection is None
    def init(self):
        self.connection=_LasyConnection()
        self.transactions=0
    def cleanup(self):
        self.connection.cleanup()
        self.connection=None
    def cursor(self):
        return self.connection.cursor()

_db_ctx = _DbCtx()

class _ConnectionCtx(object):
    def __enter__(self):
        global _db_ctx
        self.shoud_cleanup=False
        if not _db_ctx.is_init():
            _db_ctx.init()
            self.shoud_cleanup=True

    def __exit__(self, exc_type, exc_val, exc_tb):
        global _db_ctx
        _db_ctx.cleanup()

def connection():
    return _ConnectionCtx()


class _TransactionCtx(object):
    def __enter__(self):
        global _db_ctx
        self.should_close_conn=False
        if not _db_ctx.is_init :
            _db_ctx.init()
            self.should_close_conn=True
        _db_ctx.transactions +=1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        global _db_ctx
        _db_ctx.transactions -=1
        try:
            if _db_ctx.transactions ==0:
                if exc_type is None:
                    self.commit()
                else:
                    self.rollback()
        finally:
            if self.should_close_conn:
                _db_ctx.cleanup()

    def commit(self):
        global _db_ctx
        try:
            _db_ctx.connection.commit()
        except:
            _db_ctx.connection.rollback()
            raise


    def rollback(self):
        global _db_ctx
        _db_ctx.connection.rollback()

if __name__ == "__main__":
    pass  
