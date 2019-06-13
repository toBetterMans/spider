#!/usr/bin/env python
# -*- coding:utf-8 -*-
import logging.config
import time
# 打开数据库连接
from hashlib import md5

import redis

from db import single_oracle

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

class Redis_Util(object):
    
    def __init__(self, blockNum=1, key='bloomfilter',host='',port='',db=''):
        '''
        :param host: the host of Redis
        :param port: the port of Redis
        :param db: witch db in Redis
        :param blockNum: one blockNum for about 90,000,000; if you have more strings for filtering, increase it.
        :param key: the key's name in Redis
        '''
        self.server = redis.Redis(host=host, port=int(port), db=db)
        self.bit_size = 1 << 31  # Redis的String类型最大容量为512M，现使用256M
        self.seeds = [543, 460, 171, 876, 796, 607, 650, 81, 837, 545, 591, 946, 846, 521, 913, 636, 878, 735, 414, 372,
                      344, 324, 223, 180, 327, 891, 798, 933, 493, 293, 836, 10, 6, 544, 924, 849, 438, 41, 862, 648,
                      338,
                      465, 562, 693, 979, 52, 763, 103, 387, 374, 349, 94, 384, 680, 574, 480, 307, 580, 71, 535, 300,
                      53,
                      481, 519, 644, 219, 686, 236, 424, 326, 244, 212, 909, 202, 951, 56, 812, 901, 926, 250, 507, 739,
                      371,
                      63, 584, 154, 7, 284, 617, 332, 472, 140, 605, 262, 355, 526, 647, 923, 199, 518]
        self.key = key
        self.blockNum = blockNum
        self.hashfunc = []
        for seed in self.seeds:
            self.hashfunc.append(SimpleHash(self.bit_size, seed))
    
    # 获取锁
    def get_lock(self, uid):
        # 当前时间戳，用于删除锁时check
        sec = str(time.time())
        
        # 处理超时时间
        timeout = 3000
        
        # 试图锁住uid
        
        res = self.server.set(uid, sec, ex=timeout, nx=True)
        if res == True:
            logger.debug('get lock succeed, return')
            return True, sec
        else:
            logger.debug('get lock failed, lock exist, wait')
            logger.debug('sleeping 10 minetes......')
            time.sleep(60 * 10)
            
            return False, sec
        # return False, None
    
    # 释放锁
    def del_lock(self, uid, sec):
        # 校验
        redis_sec = self.server.get(uid)
        if sec != redis_sec:
            logger.debug('check permission failed :%s' % uid)
            return False
            logger.debug('check permission succeed :%s' % uid)
        
        # 删除
        res = self.server.delete(uid)
        if res:
            logger.debug('del key succeed :%s' % uid)
            return False
        else:
            logger.debug('del key failed :%s' % uid)
            return True
    
    def isContains(self, str_input):
        if not str_input:
            return False
        m5 = md5()
        m5.update(str_input)
        str_input = m5.hexdigest()
        ret = True
        name = self.key + str(int(str_input[0:2], 16) % self.blockNum)
        for f in self.hashfunc:
            loc = f.hash(str_input)
            ret = ret & self.server.getbit(name, loc)
        return ret
    
    def insert(self, str_input):
        m5 = md5()
        m5.update(str_input)
        str_input = m5.hexdigest()
        name = self.key + str(int(str_input[0:2], 16) % self.blockNum)
        for f in self.hashfunc:
            loc = f.hash(str_input)
            self.server.setbit(name, loc, 1)
    
    def put_user(self):
        lock_uid = 'user'
        status, sec = self.get_lock(lock_uid)
        if status:
            users_length = self.server.llen('users')
            
            # if users_length > 100:
            #     self.del_lock(lock_uid, sec)
            #     logger.debug('users length={}'.format(users_length))
            #     return
            
            # SQL 查询语句
            sql = 'SELECT username FROM tyc_user '
            try:
                # 执行SQL语句
                # cursor.execute(sql)
                # 获取所有记录列表
                # results = cursor.fetchall()
                
                results = single_oracle.oracle_find_by_param_all(sql)
                if results:
                    for row in results:
                        self.server.lpush('users', row[0])
                self.del_lock(lock_uid, sec)
                return
            except Exception as e:
                logger.exception(e)
                self.del_lock(lock_uid, sec)
        
        time.sleep(0.001)
    
    def put_page(self):
        lock_uid = 'page'
        status, sec = self.get_lock(lock_uid)
        if status:
            pages_length = self.server.llen('pages')
            
            if pages_length > 500:
                print('users length={}'.format(pages_length))
                self.del_lock(lock_uid, sec)
                return
            sql =  "SELECT txt_id  FROM COMPANY_BASIC_INFO_XIONG_AN  where REGISTERED_CAPITAL!='-' and txt_id not in(select txt_id from tyc_qybj_jbxx)"
            try:
                resuls = single_oracle.oracle_find_by_param_all(sql)
                if resuls:
                    print (len(resuls))
                    for page in resuls:
                        txt_id = page[0]
                        # url = page[0]
                        self.server.lpush('pages', txt_id)
                else:
                    time.sleep(10 % 30)
                    self.del_lock(lock_uid, sec)
                    self.put_page()
                self.del_lock(lock_uid, sec)
            except Exception as e:
                self.del_lock(lock_uid, sec)
                print(e)
    
    def put_company(self):
        lock_uid = 'ent'
        status, sec = self.get_lock(lock_uid)
        if status:
            users_length = self.server.llen('ents')
            
            # if users_length > 2000:
            #     print('users length={}'.format(users_length))
            #     self.del_lock(lock_uid, sec)
            #     return
            
            ents = {}
            # sql = 'select B.* from batch_detail  B where (select count(1) as num from company_basic_info A where A.search_name = B.COMPANY_NAME) = 0'
            # sql='select distinct t1.company_number,t1.company_name  from BATCH_DETAIL_1 t1 where t1.company_name not in (select t.search_name from company_basic_info t)'
            # companys = single_oracle.oracle_find_by_param_all(sql)
            resuls = []
            # 分支机构名单
            sql_fzjg = 'select distinct ent_name from tyc_qybj_fzjg'
            # 对外投资名单
            sql_dwtz = 'select distinct invest_company from tyc_qybj_dwtz'
            resuls.extend(single_oracle.oracle_find_by_param_all(sql_fzjg))
            resuls.extend(single_oracle.oracle_find_by_param_all(sql_dwtz))
            print(len(resuls))
            # logger.debug(companys)
            ents['table'] = 'batch_detail'
            ents['type'] = 'batch_details'
            if resuls:
                for company in resuls:
                    ents['company_name'] = company[0]
                    # if self.isContains(ents['company_name']):  # 判断字符串是否存在
                    #     print('exists!')
                    #     continue
                    # else:
                    #     print ('not exists!')
                    # self.insert(ents['company_name'])
                    ents['agency_num'] = 'NA'
                    ents['agency_name'] =  'NA'
                    ents['batch'] = 'NA'
                    # ents['company_name'] = company[2]
                    ents['address'] =  'NA'
                    ents['number'] = 'NA'
                    self.server.lpush('ents_fzjg_dwtz', str(ents))
                # self.del_lock(lock_uid, sec)
           
        self.del_lock(lock_uid, sec)
    
    def put_phone(self):
        lock_uid = 'phone'
        status, sec = self.get_lock(lock_uid)
        if status:
            users_length = self.server.llen('phones')
            
            if users_length > 200:
                logger.debug('phones length={}'.format(users_length))
                self.del_lock(lock_uid, sec)
                return
            
            companys = single_oracle.oracle_find_by_param_all('user')
            
            print(companys)
            for company in companys:
                self.server.lpush('phones', company[0])
                # print(company[0])
            self.del_lock(lock_uid, sec)
    
    def put_parse(self):
        lock_uid = 'parse'
        status, sec = self.get_lock(lock_uid)
        if status:
            parses_length = self.server.llen('parses')
            print(parses_length)
       
            try:
                # txt_ids = single_oracle.oracle_find_by_param_all(
                #     "select B.txt_id from  company_basic_info B where (select count(1) as num from tyc_qybj_jbxx A where A.ent_name = B.ent_name) = 0")
                # sql = 'select B.* from company_basic_info  B where (select count(1) as num from tyc_qybj_jbxx A where A.txt_id = B.txt_id) = 0'
                # sql='select a.txt_id,b.company_name from company_basic_info a, batch_detail_1 b where a.search_name=b.company_name'
                # sql='select distinct txt_id,company_name  from tyc_sffx_flss'
                # sql = 'select B.txt_id,B.search_name from company_basic_info  B ,batch_detail_1 C where B.search_name=C.company_name '
                # 分支机构，对外投资
                sql="SELECT txt_id,search_name  FROM company_basic_info "
                resuls=single_oracle.oracle_find_by_param_all(sql)
                print(len(resuls))
                # if resuls.count() == 0:
                #     param = {'parse': {'$exists': False}}
                #     resuls = mongo.mongodb_find_limit('company_detail_info', param,projection, 100000)
                # results = single_oracle.oracle_find_by_param_all(sql)
                
                for page in resuls:
                    txt_id = page[0]
                    company_name=page[1]
                    # print ('已解析')
                    # print(page[1])
                    # find_sql='select count(*) from tyc_qybj_jbxx where txt_id='{}''.format(txt_id)
                    # print (mysql.mysql_find_by_param(find_sql))
                    
                    # mysql.mysql_update_param(
                    #     'update company_basic_info set  parsed=1 where txt_id='{}''.format(txt_id))
                    # print(txt_id)
                    # continue
                    # self.server.lpush('sxr_parses',str(company_name))
                    self.server.lpush('parses', str(txt_id)+','+str(company_name))
                self.del_lock(lock_uid, sec)
            except Exception as e:
                self.del_lock(lock_uid, sec)
                logger.exception(e)
    
    def put_bloomfilter(self):
        pass


if __name__ == '__main__':
    single_redis_local = Redis_Util(host='127.0.0.1', port=6379, db='')
    # single_redis_remote = Redis_Util(host='10.0.32.85', port=6379, db='')
    # cookies=single_redis_local.server.hgetall('cookies')
    # for k,v in cookies.items():
    #     single_redis_remote.server.hset('cookies',k,v)
    single_redis_local.put_parse()
    # bf.put_page()
    # bf.put_parse()
    # import xlrd
    # book=xlrd.open_workbook('not_xiong_an.xls')
    # s=book.sheet_by_index(0)
    # length=s.nrows
    # #
    # for i in range(1,length):
    #     name=s.cell(i,1).value
    #     single_redis_local.server.hset('not_xiong_an',name,1)
    # s2=book.sheet_by_index(1)
    # length=s2.nrows
    # for i in range(1,length):
    #     name=s2.cell(i,1).value
    #
    #     single_redis_local.server.hset('not_xiong_an',name,1)
