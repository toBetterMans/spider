#!/usr/bin/env python
# -*- coding:utf-8 -*-
import logging.config
import time
from hashlib import md5

import redis

from db import single_oracle
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

class RedisUtil(object):
    
    def __init__(self, blockNum=1, key='bloomfilter'):
        '''
        :param host: the host of Redis
        :param port: the port of Redis
        :param db: witch db in Redis
        :param blockNum: one blockNum for about 90,000,000; if you have more strings for filtering, increase it.
        :param key: the key's name in Redis
        '''
        self.server = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)
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
    
    def get_configs_by_tablename(self, function):
        sql_conf = "select  c.condition, c.over, c.id from (select min(a.priority) min_p from config a where a.function = '{}') b, config c where c.priority = b.min_p and c.over != 1 and c.function = '{}'".format(
            function, function)
        # sql = "SELECT company_number, company_name, branch, address_3 from company_11315 where address_3 like '%通州%' and address_2 = '北京市' and searched=0"
        configs = single_oracle.oracle_find_by_param_all(sql_conf)
        print(configs)
        if not configs or not configs[0]:
            return
        condition = configs[0][0]
        over = configs[0][1]
        id = configs[0][2]
        return [condition, over, id]
    
    # 获取锁
    def get_lock(self, uid):
        # 当前时间戳，用于删除锁时check
        sec = str(time.time())
        
        # 处理超时时间
        timeout = 3000
        
        # 试图锁住uid
        
        res = self.server.set(uid, sec, ex=timeout, nx=True)
        if res == True:
            logger.debug('get lock {} succeed, return'.format(uid))
            return True, sec
        else:
            logger.debug('get lock failed, lock {} exist, wait'.format(uid))
            logger.debug('sleeping 10 minetes......')
            time.sleep(60 * 10)
            
            return False, sec
        # return False, None
    
    # 释放锁
    def del_lock(self, uid, sec):
        # 校验
        
        redis_sec = self.server.get(uid).decode()
        # print(sec.decode(),redis_sec.decode())
        print(type(sec), type(redis_sec))
        # redis_sec=redis_sec.decode()
        # sec = sec.decode()
        
        if sec != redis_sec:
            logger.debug('check permission {} failed '.format(uid))
            return False
        
        # 删除
        res = self.server.delete(uid)
        if res:
            logger.debug('del key {} succeed '.format(uid))
            return False
        else:
            logger.debug('del key {} failed '.format(uid))
            return True
    
    def isContains(self, str_input):
        # logger.debug('md5 str type:{}'.format(type(str_input)))
        if not str_input:
            return False
        if not isinstance(str_input, bytes):
            str_input = str_input.encode()
            # logger.debug('md5 str after encode type:{}'.format(type(str_input)))
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
        if not str_input:
            return False
        if not isinstance(str_input, bytes):
            str_input = str_input.encode()
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
        # single_oracle.execute('update company_basic_info set PAGE_SPIDER=0')
        # self.server.delete(lock_uid)
        status, sec = self.get_lock(lock_uid)
        if status:
            pages_length = self.server.llen('pages')
            
            if pages_length > 1000:
                print('users length={}'.format(pages_length))
                self.del_lock(lock_uid, sec)
                return
            sql = "SELECT search_name,txt_id FROM company_basic_info where parsed=0 and page_spider=0 and {} and rownum <= 10000"
            
            try:
                tablename_condition = self.get_configs_by_tablename('put_page')
                results = single_oracle.oracle_find_by_param_all(
                    sql.format(tablename_condition[0]))
                
                # results = single_oracle.oracle_find_by_param_all(sql)
                if results:
                    print(len(results))
                    if tablename_condition[1] == 0:
                        update_sql = "update config set over = 2 where id = {}".format(tablename_condition[2])
                        single_oracle.oracle_update(update_sql)
                    if len(results) > 10:
                        results = results[10:]
                    for page in results:
                        txt_id = page[1]
                        # url = page[0]
                        # if self.isContains(txt_id):
                        #     single_oracle.oracle_update(
                        #         "update company_basic_info set PAGE_SPIDER=1 where txt_id={}".format(txt_id))
                        #     continue
                        # self.insert(txt_id)
                        self.server.lpush('pages', txt_id)
                else:
                    # single_oracle.oracle_update(
                    #     "update config set over = 1 where id = {}".format(tablename_condition[2]))
                    # return
                    sql = "SELECT search_name,txt_id  FROM company_basic_info where parsed=0 and page_spider=0 "
                    results = single_oracle.oracle_find_by_param_all(sql)
                    for page in results:
                        txt_id = page[1]
                        if self.isContains(txt_id):
                            single_oracle.oracle_update(
                                "update company_basic_info set PAGE_SPIDER=1 where txt_id={}".format(txt_id))
                            continue
                        self.insert(txt_id)
                        self.server.lpush('pages', txt_id)
                self.del_lock(lock_uid, sec)
            except Exception as e:
                self.del_lock(lock_uid, sec)
                print(e)
    
    def put_company_(self):
        lock_uid = 'ent'
        status, sec = self.get_lock(lock_uid)
        if status:
            users_length = self.server.llen('ents')
            if users_length > 1000:
                print('users length={}'.format(users_length))
                self.del_lock(lock_uid, sec)
                return
            ents = {}
            # 慈溪
            sql = 'SELECT company_number,company_name,address_3 FROM company_11315 where mark = 11 and searched != 1'
            try:
                companys = single_oracle.oracle_find_by_param_all(sql)
                print(len(companys))
                ents['table'] = 'company_11315'
                ents['type'] = 'company_11315s'
                if companys:
                    for company in companys:
                        if company[1] == 'None' or company[1] == 'NA' or company[1] == None:
                            print('发现空的公司名称={}'.format(company))
                            single_oracle.oracle_update(
                                "update {table} set searched=1 where company_number={number}".format(
                                    table=ents['table'], number=company[0]))
                            continue
                        ents['company_name'] = company[1].encode('utf-8')
                        print('not exists!')
                        ents['address'] = company[2] or ''
                        ents['number'] = company[0]
                        self.server.lpush('ents', str(ents))
                self.del_lock(lock_uid, sec)
            except Exception as e:
                self.del_lock(lock_uid, sec)
                logger.debug(e)
    
    def put_company(self):
        lock_uid = 'ent'
        status, sec = self.get_lock(lock_uid)
        if status:
            users_length = self.server.llen('ents')
            
            if users_length > 1000:
                print('users length={}'.format(users_length))
                self.del_lock(lock_uid, sec)
                return
            
            ents = {}
            sql = "SELECT company_number, company_name, branch, address_3 from company_11315 where {} and rownum <= 10000"
            # sql = 'SELECT * FROM batch_detail WHERE searched=0'
            # sql = 'SELECT company_number,company_name,company_address FROM company_11315'
            #
            # sql = "SELECT company_number, company_name, branch, address_3 from company_11315 where address_3 like '%颍上%' and searched = 0"
            try:
                # companys = single_oracle.oracle_find_by_param_all(sql)
                # print(len(companys))
                # if not companys or len(companys) == 0:
                tablename_condition = self.get_configs_by_tablename('put_company')
                print(tablename_condition)
                tablename_condition = tablename_condition if tablename_condition else ['searched=0']
                sql = sql.format(tablename_condition[0])
                # print(sql)
                companys = single_oracle.oracle_find_by_param_all(sql)
                # print(companys)
                # logger.debug(companys)
                ents['table'] = 'company_11315'
                ents['type'] = 'company_11315s'
                
                if companys[0][0]:
                    if tablename_condition[1] == 0:
                        update_sql = "update config set over = 2 where id = {}".format(tablename_condition[2])
                        single_oracle.oracle_update(update_sql)
                    if len(companys) > 10:
                        companys=companys[10:]
                    for company in companys:
                        if company[1] == 'None' or company[1] is None or company[1] == None:
                            print('发现空的公司名称={}'.format(company))
                            single_oracle.oracle_update(
                                "update {table} set searched=1 where company_number={number}".format(
                                    table=ents['table'], number=company[0]))
                            continue
                        ents['company_name'] = company[1]
                        # if self.isContains(ents['company_name']):  # 判断字符串是否存在
                        #     print('exists!')
                        #     single_oracle.oracle_update(
                        #         "update {table} set searched=1 where company_number={number}".format(
                        #             table=ents['table'], number=company[0]))
                        #     continue
                        # print('not exists!')
                        # self.insert(ents['company_name'])
                        ents['agency_num'] = 'NA'
                        ents['agency_name'] = 'NA'
                        ents['batch'] = 'NA'
                        # ents['company_name'] = company[2]
                        ents['address'] = company[3] or 'NA'
                        ents['number'] = company[0] or 'NA'
                        ents['branch'] = company[2] or 'NA'
                        
                        self.server.lpush('ents', str(ents))
                    # self.del_lock(lock_uid, sec)
                # else:
                #     # and branch in ('蕲春县',
                #     #                   '京山县',
                #     #                   '谷城县',
                #     #                   '枣阳市',
                #     #                   '老河口市',
                #     #                   '潜江经济开发区',
                #     #                   '潜江区',
                #     #                   '潜江市经济开发区',
                #     #                   '湖北省潜江市浩口镇',
                #     #                   '潜江市总口管理区',
                #     #                   '潜江县',
                #     #                   '监利县',
                #     #                   '松滋市',
                #     #                   '公安县',
                #     #                   '沙洋县',
                #     #                   '南漳县',
                #     #                   '黄梅县',
                #     #                   '武穴市',
                #     #                   '大冶市',
                #     #                   '宜城市',
                #     #                   '宜城县',
                #     #                   '曹县 ',
                #     #                   '沂水县',
                #     #                   '青州市',
                #     #                   '临邑县',
                #     #                   '单县 ',
                #     #                   '曲阜市',
                #     #                   '五莲县',
                #     #                   '栖霞市',
                #     #                   '栖霞区',
                #     #                   '巨野县',
                #     #                   '东明县',
                #     #                   '汶上县',
                #     #                   '龙口市',
                #     #                   '宁海县',
                #     #                   '镇海区',
                #     #                   '象山区',
                #     #                   '象山县',
                #     #                   '北仑区',
                #     #                   '全椒县',
                #     #                   '来安县',
                #     #                   '界首市',
                #     #                   '颍上县',
                #     #                   '阜南县',
                #     #                   '太和县',
                #     #                   '临泉县',
                #     #                   '临颍县',
                #     #                   '滑县 ',
                #     #                   '项城市',
                #     #                   '杞县 ',
                #     #                   '淮阳县',
                #     #                   '沈丘县',
                #     #                   '石柱县',
                #     #                   '重庆石柱',
                #     #                   '石柱土家族自治县',
                #     #                   '长寿区',
                #     #                   '合川区',
                #     #                   '重庆合川区',
                #     #                   '市辖区合川区',
                #     #                   '奉节县',
                #     #                   '重庆奉节县',
                #     #                   '巫山县',
                #     #                   '重庆巫山县',
                #     #                   '万州区',
                #     #                   '市辖区万州区',
                #     #                   '重庆城口县',
                #     #                   '城口县',
                #     #                   '涪陵区',
                #     #                   '市辖区涪陵区',
                #     #                   '垫江县',
                #     #                   '重庆垫江县',
                #     #                   '巫溪县',
                #     #                   '重庆巫溪县',
                #     #                   '南岸区',
                #     #                   '安福县',
                #     #                   '响水县',
                #     #                   '岳池县',
                #     #                   '四川岳池县',
                #     #                   '广安岳池县',
                #     #                   '蓬溪县',
                #     #                   '武胜县',
                #     #                   '广安武胜县',
                #     #                   '邻水县',
                #     #                   '广安邻水县',
                #     #                   '达川区',
                #     #                   '四川巴中经济开发区',
                #     #                   '巴中经济开发区',
                #     #                   '巴中区',
                #     #                   '四川巴中通江县',
                #     #                   '巴中军分区',
                #     #                   '郫都区',
                #     #                   '平川区',
                #     #                   '泾川县',
                #     #                   '平凉泾川县',
                #     #                   '习水县',
                #     #                   '贵州习水县',
                #     #                   '赤水市',
                #     #                   '桐梓县',
                #     #                   '湄潭县',
                #     #                   '务川 ',
                #     #                   '务川县',
                #     #                   '正安县',
                #     #                   '道真县',
                #     #                   '道真 ',
                #     #                   '道真自治县',
                #     #                   '凤冈县',
                #     #                   '余庆县',
                #     #
                #     #                   '汨罗市',
                #     #                   '通州区',
                #     #                   '大通 ',
                #     #                   '大通县',
                #     #                   '大通区',
                #     #                   '西青区',
                #     #                   '市辖区西青区',
                #     #                   '龙岗区',
                #     #                   '龙岗镇平湖区',
                #     #                   '深圳市龙岗区',
                #     #                   '龙岗开发区',
                #     #                   '宜丰县',
                #     #                   '上饶县',
                #     #                   '泰和县',
                #     #                   '新干县',
                #     #                   '乾县 ',
                #     #                   '蒲城县',
                #     #                   '凤翔县',
                #     #                   '兴平市',
                #     #                   '兴平县',
                #     #                   '汉滨区',
                #     #                   '城固县',
                #     #                   '汉中城固县',
                #     #                   '蓝田县',
                #     #                   '睢宁县',
                #     #                   '吴江区',
                #     #                   '繁昌县',
                #     #                   '万州县',
                #     #                   '桃江县',
                #     #                   '丰宁县',
                #     #                   '新野县',
                #     #                   '江肇东县',
                #     #                   '泰兴县',
                #     #                   '高淳县',
                #     #                   '武进县',
                #     #                   '锡山县',
                #     #                   '慈溪县',
                #     #                   '宁海县',
                #     #                   '浦东县',
                #     #                   '常熟县',
                #     #                   '滕州县',
                #     #                   '诸城县',
                #     #                   '邹城县',
                #     #                   '文登县',
                #     #                   '招远县',
                #     #                   '安塞县',
                #     #                   '苍南县',
                #     #                   '武义县',
                #     #                   '青田县',
                #     #                   '江山县',
                #     #                   '淳安县',
                #     #                   '丽水县',
                #     #                   '繁昌区',
                #     #                   '万州区',
                #     #                   '桃江区',
                #     #                   '丰宁区',
                #     #                   '新野区',
                #     #                   '江肇东区',
                #     #                   '泰兴区',
                #     #                   '高淳区',
                #     #                   '武进区',
                #     #                   '锡山区',
                #     #                   '慈溪区',
                #     #                   '宁海区',
                #     #                   '浦东区',
                #     #                   '常熟区',
                #     #                   '滕州区',
                #     #                   '诸城区',
                #     #                   '邹城区',
                #     #                   '文登区',
                #     #                   '招远区',
                #     #                   '安塞区',
                #     #                   '苍南区',
                #     #                   '武义区',
                #     #                   '青田区',
                #     #                   '江山区',
                #     #                   '淳安区',
                #     #                   '丽水区')
                #     ents['type'] = '11315'
                #     ents['table'] = 'company_11315'
                #
                #
                # # logger.debug(
                # #     'find from table={} and type={} and lenth={}'.format(ents['table'], type(companys), len(companys)))
                # # if not companys or len(companys) == 0:
                # #     ents['table'] = 'company_11315_zyfd'
                # #     companys = single_oracle.oracle_find_by_param_all(sql.format(table=ents['table']))
                # #     logger.debug('find from table={} and type={} and lenth={}'.format(ents['table'], type(companys),
                # #                                                                       len(companys)))
                #
                #     for company in companys:
                #         if company[1] == 'None' or company[1] is None or company[1] == None:
                #             print('发现空的公司名称={}'.format(company))
                #             single_oracle.oracle_update(
                #                 "update {table} set searched=1 where company_number={number}".format(table=ents['table'], number=company[0]))
                #             continue
                #         ents['company_name'] = company[1]
                #         if self.isContains(ents['company_name']):  # 判断字符串是否存在
                #             print('exists!')
                #
                #             company_sql = "select count(*) from company_basic_info where search_name='{}'"
                #             update_11315 = 'update {} set searched=1 where company_number={}'
                #             check = single_oracle.oracle_find_by_param_all(company_sql.format(ents['company_name']))
                #             print(check)
                #             logger.debug('check type[0] {}'.format(check))
                #             if check[0][0] != 0:
                #                 single_oracle.oracle_update(update_11315.format(ents['table'], company[0]))
                #
                #             else:
                #                 print('放入过滤队列')
                #                 self.insert(ents['company_name'])
                #             continue
                #         else:
                #             print(company)
                #             print('not exists!')
                #         self.insert(ents['company_name'])
                #         ents['branch'] = company[2] or ''
                #         ents['address'] = company[3] or ''
                #         # print cache['company_name']
                #         ents['number'] = company[0]
                #         self.server.lpush('ents', ''.join(ents))

                else:
                    single_oracle.oracle_update("update config set over = 1 where id = {}".format(tablename_condition[2]))
                self.del_lock(lock_uid, sec)
            except Exception as e:
                self.del_lock(lock_uid, sec)
                logger.debug(e)
    
    def put_phone(self):
        lock_uid = 'phone'
        status, sec = self.get_lock(lock_uid)
        if status:
            users_length = self.server.llen('phones')
            
            if users_length > 0:
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
        lock_uid = 'parse_lock'
        # self.server.delete(lock_uid)
        status, sec = self.get_lock(lock_uid)
        print(status, sec)
        if status:
            # parses_length = self.server.llen('parses')
            #
            # if parses_length > 500:
            #     logger.debug('parses length={}'.format(parses_length))
            #     self.del_lock(lock_uid, sec)
            #     return
            
            # mongo = single_mongodb
            param = {'parse': 0}
            projection = {'_id': 1}
            
            try:
                # sql = "SELECT txt_id,search_name  FROM company_basic_info WHERE {} and rownum <= 10000 and txt_id is not null"
                sql = "SELECT txt_id,search_name  FROM company_basic_info WHERE  parsed=0 and page_spider=1 and rownum <= 10000"
                # sql='select B.txt_id,B.search_name from company_basic_info  B where (select count(1) as num from tyc_qybj_jbxx A where A.txt_id = B.txt_id) = 0'
                # results = single_mongodb.mongodb_find_limit('company_detail_info', param,projection, 1000)
                # if results.count() == 0:
                #     param = {'parse': {'$exists': False}}
                #     results = single_mongodb.mongodb_find_limit('company_detail_info', param,projection, 100000)
                ###!!!!!
                tablename_condition = self.get_configs_by_tablename('put_parse')
                results = single_oracle.oracle_find_by_param_all(sql.format(tablename_condition[0]))
                print(len(results))
                if not results:

                    time.sleep(60 * 30)
                else:
                    # if tablename_condition[1] == 0:
                    #     update_sql = "update config set over = 2 where id = {}".format(tablename_condition[2])
                    #     single_oracle.oracle_update(update_sql)

                    if len(results) > 10:
                        results = results[10:]
                    for page in results:
                        txt_id = page[0]
                        search_name = page[1]
                        if isinstance(txt_id, bytes):
                            search_name = search_name.decode()
                        if isinstance(txt_id, bytes):
                            txt_id = txt_id.decode()
                        value = txt_id + ',' + search_name
                        # if self.isContains(value):
                        #     single_oracle.oracle_update(
                        #         "update company_basic_info set parsed=1 where txt_id={}".format(txt_id))
                        #     continue
                        # self.insert(value)
                        self.server.lpush('parses', value)
                logger.debug('塞完待解析数据')
                self.del_lock('parse_lock', sec)
                logger.debug('yi shan chu lock_uid:parse_lock')
            except Exception as e:
                self.del_lock('parse_lock', sec)
                logger.exception(e)
    
    def put_cookies(self, phone, cookie, name='cookies'):
        
        try:
            self.server.hset(name, str(phone), cookie)
        except Exception as e:
            logger.exception(e)
    
    def get_user(self):
        try:
            user = self.server.rpop('users')
            self.server.lpush('users', str(user))
            return user
        except Exception as e:
            logger.exception(e)
    
    def get_cookie(self, phone, name='cookies'):
        count = self.server.hlen(name)
        if count > 20:
            cookie = self.server.hget(name, str(phone))
            return cookie
        return None
    
    def put_bloomfilter(self):
        
        pass

single_redis = RedisUtil()
if __name__ == '__main__':
    bf = RedisUtil()
    bf.put_company()
    # bf.put_user()
    # print(bf.get_configs_by_tablename('put_11315'))
    # print(bf.get_configs_by_tablename('put_page'))
    # print(bf.get_configs_by_tablename('put_company'))
    # print(bf.get_configs_by_tablename('put_parse'))
