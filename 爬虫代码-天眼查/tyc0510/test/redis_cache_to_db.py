# !/usr/bin/env python
# -*- coding:utf-8 -*-
import logging.config

import redis

from setting import REDIS_HOST, REDIS_DB, REDIS_PORT

# 打开数据库连接

logging.config.fileConfig('../log_file/redis_cache.conf')

logger = logging.getLogger('loggerTxt')

class SimpleHash(object):
    
    def __init__(self, cap, seed):
        self.cap = cap
        self.seed = seed
    
    def hash(self, value):
        ret = 0
        for i in range(len(value)):
            ret += self.seed * ret + ord(value[i])
        return (self.cap - 1) & ret

class RedisUtilBD(object):
    
    def __init__(self):
        '''
        :param host: the host of Redis
        :param port: the port of Redis
        :param db: witch db in Redis
        :param blockNum: one blockNum for about 90,000,000; if you have more strings for filtering, increase it.
        :param key: the key's name in Redis
        '''
        self.server = redis.Redis(
            host=REDIS_HOST,
            port=REDIS_PORT,
            db=REDIS_DB)

single_redis_to_db = RedisUtilBD()
if __name__ == '__main__':
    pass
