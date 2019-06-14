# !/usr/bin/env python
# -*- coding:utf-8 -*-
import logging.config
import time
# 打开数据库连接
from hashlib import md5

import redis

from db import single_oracle
from setting import REDIS_HOST, REDIS_DB, REDIS_PORT

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
        self.server = redis.Redis(
            host=REDIS_HOST,
            port=REDIS_PORT,
            db=REDIS_DB)
        self.bit_size = 1 << 31  # Redis的String类型最大容量为512M，现使用256M
        self.seeds = [
            543,
            460,
            171,
            876,
            796,
            607,
            650,
            81,
            837,
            545,
            591,
            946,
            846,
            521,
            913,
            636,
            878,
            735,
            414,
            372,
            344,
            324,
            223,
            180,
            327,
            891,
            798,
            933,
            493,
            293,
            836,
            10,
            6,
            544,
            924,
            849,
            438,
            41,
            862,
            648,
            338,
            465,
            562,
            693,
            979,
            52,
            763,
            103,
            387,
            374,
            349,
            94,
            384,
            680,
            574,
            480,
            307,
            580,
            71,
            535,
            300,
            53,
            481,
            519,
            644,
            219,
            686,
            236,
            424,
            326,
            244,
            212,
            909,
            202,
            951,
            56,
            812,
            901,
            926,
            250,
            507,
            739,
            371,
            63,
            584,
            154,
            7,
            284,
            617,
            332,
            472,
            140,
            605,
            262,
            355,
            526,
            647,
            923,
            199,
            518]
        self.key = key
        self.blockNum = blockNum
        self.hashfunc = []
        for seed in self.seeds:
            self.hashfunc.append(SimpleHash(self.bit_size, seed))

    # 从配置表config中取出查询条件
    def get_configs_by_tablename(self, function):
        sql_conf = "select  c.condition,c.over,c.id from (select min(a.priority) min_p from config a where a.function = '{}' and a.over != 1) b, config c where c.priority = b.min_p and c.over != 1 and c.function = '{}'".format(
            function, function)
        # sql = "SELECT company_number, company_name, branch, address_3 from company_11315 where address_3 like '%通州%' and address_2 = '北京市' and searched=0"
        configs = single_oracle.oracle_find_by_param_all(sql_conf)
        print(configs)
        if not configs or not configs[0] or not configs[1] or not configs[2]:
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
        if res:
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

            if users_length > 100:
                self.del_lock(lock_uid, sec)
                logger.debug('users length={}'.format(users_length))
                return

            # SQL 查询语句
            sql = 'SELECT username FROM tyc_user WHERE user_forbid=0'
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
            sql = 'SELECT url,txt_id  FROM company_basic_info WHERE page_spider=0 AND parsed=0  and ROWNUM <=10000 order by txt_id'
            try:
                resuls = single_oracle.oracle_find_by_param_all(sql)
                if resuls:
                    print(len(resuls))
                    for page in resuls:
                        txt_id = page[1]
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

            if users_length > 0:
                print('users length={}'.format(users_length))
                self.del_lock(lock_uid, sec)
                return

            ents = {}
            sql = 'SELECT *   FROM batch_detail WHERE searched=0 and rownum<=10000'
            companys = single_oracle.oracle_find_by_param_all(sql)
            # logger.debug(companys)
            ents['table'] = 'batch_detail'
            ents['type'] = 'batch_details'
            if companys:
                for company in companys:
                    ents['company_name'] = company[2].encode('utf-8')
                    if self.isContains(ents['company_name']):  # 判断字符串是否存在
                        print('exists!')
                        continue
                    else:
                        print('not exists!')
                    self.insert(ents['company_name'])
                    ents['agency_num'] = company[7] or ''
                    ents['agency_name'] = company[8] or ''
                    ents['batch'] = company[9] or ''
                    ents['company_name'] = company[2]
                    ents['address'] = company[3] or ''
                    ents['number'] = company[0] or ''
                    self.server.lpush('ents', ents)
                # self.del_lock(lock_uid, sec)
            else:
                ents['type'] = '11315'
                ents['table'] = 'company_11315'
                # sql = 'SELECT company_number,company_name,branch,address_3
                # FROM 11315_company WHERE searched=0 and address_3 in
                # ('蕲春县','京山县','谷城县','枣阳市','老河口市','潜江经济开发区','潜江区','潜江市经济开发区','湖北省潜江市浩口镇','潜江市总口管理区','潜江县','监利县','松滋市','公安县','沙洋县','南漳县','黄梅县','武穴市','大冶市','宜城市','宜城县','曹县
                # ','沂水县','青州市','临邑县','单县
                # ','曲阜市','五莲县','栖霞市','栖霞区','巨野县','东明县','汶上县','龙口市','宁海县','镇海区','象山区','象山县','北仑区','全椒县','来安县','界首市','颍上县','阜南县','太和县','临泉县','临颍县','滑县
                # ','项城市','杞县
                # ','淮阳县','沈丘县','石柱县','重庆石柱','石柱土家族自治县','长寿区','合川区','重庆合川区','市辖区合川区','奉节县','重庆奉节县','巫山县','重庆巫山县','万州区','市辖区万州区','重庆城口县','城口县','涪陵区','市辖区涪陵区','垫江县','重庆垫江县','巫溪县','重庆巫溪县','南岸区','安福县','响水县','岳池县','四川岳池县','广安岳池县','蓬溪县','武胜县','广安武胜县','邻水县','广安邻水县','达川区','四川巴中经济开发区','巴中经济开发区','巴中区','四川巴中通江县','巴中军分区','郫都区','平川区','泾川县','平凉泾川县','习水县','贵州习水县','赤水市','桐梓县','湄潭县','务川
                # ','务川县','正安县','道真县','道真
                # ','道真自治县','凤冈县','余庆县','镇赉县','汨罗市','通州区','大通
                # ','大通县','大通区','西青区','市辖区西青区','龙岗区','龙岗镇平湖区','深圳市龙岗区','龙岗开发区','宜丰县','上饶县','泰和县','新干县','乾县
                # ','蒲城县','凤翔县','兴平市','兴平县','汉滨区','城固县','汉中城固县','蓝田县','睢宁县','吴江区')
                # limit 100000'
                sql = "select company_number,company_name,branch,address_3 FROM company_11315 WHERE searched=0 and address_3 in ('宁海','宁海县','宁海区') "
                companys = single_oracle.oracle_find_by_param_all(sql)
                if not companys or len(companys) == 0:
                    ents['table'] = 'company_11315_zyfd'
                    sql = "select company_number,company_name,branch,address_3  FROM  company_11315_zyfd WHERE searched=0 and address_3 in ('宁海','宁海县','宁海区') "
                    companys = single_oracle.oracle_find_by_param_all(sql)
                    if not companys or len(companys) == 0:
                        ents['table'] = 'company_11315'
                        sql = """SELECT company_number, company_name, branch, address_3
  FROM company_11315
 WHERE searched = 0
   and address_3 in ('蕲春县',
                     '京山县',
                     '谷城县',
                     '枣阳市',
                     '老河口市',
                     '潜江经济开发区',
                     '潜江区',
                     '潜江市经济开发区',
                     '湖北省潜江市浩口镇',
                     '潜江市总口管理区',
                     '潜江县',
                     '监利县',
                     '松滋市',
                     '公安县',
                     '沙洋县',
                     '南漳县',
                     '黄梅县',
                     '武穴市',
                     '大冶市',
                     '宜城市',
                     '宜城县',
                     '曹县 ',
                     '沂水县',
                     '青州市',
                     '临邑县',
                     '单县 ',
                     '曲阜市',
                     '五莲县',
                     '栖霞市',
                     '栖霞区',
                     '巨野县',
                     '东明县',
                     '汶上县',
                     '龙口市',
                     '宁海县',
                     '镇海区',
                     '象山区',
                     '象山县',
                     '北仑区',
                     '全椒县',
                     '来安县',
                     '界首市',
                     '颍上县',
                     '阜南县',
                     '太和县',
                     '临泉县',
                     '临颍县',
                     '滑县 ',
                     '项城市',
                     '杞县 ',
                     '淮阳县',
                     '沈丘县',
                     '石柱县',
                     '重庆石柱',
                     '石柱土家族自治县',
                     '长寿区',
                     '合川区',
                     '重庆合川区',
                     '市辖区合川区',
                     '奉节县',
                     '重庆奉节县',
                     '巫山县',
                     '重庆巫山县',
                     '万州区',
                     '市辖区万州区',
                     '重庆城口县',
                     '城口县',
                     '涪陵区',
                     '市辖区涪陵区',
                     '垫江县',
                     '重庆垫江县',
                     '巫溪县',
                     '重庆巫溪县',
                     '南岸区',
                     '安福县',
                     '响水县',
                     '岳池县',
                     '四川岳池县',
                     '广安岳池县',
                     '蓬溪县',
                     '武胜县',
                     '广安武胜县',
                     '邻水县',
                     '广安邻水县',
                     '达川区',
                     '四川巴中经济开发区',
                     '巴中经济开发区',
                     '巴中区',
                     '四川巴中通江县',
                     '巴中军分区',
                     '郫都区',
                     '平川区',
                     '泾川县',
                     '平凉泾川县',
                     '习水县',
                     '贵州习水县',
                     '赤水市',
                     '桐梓县',
                     '湄潭县',
                     '务川 ',
                     '务川县',
                     '正安县',
                     '道真县',
                     '道真 ',
                     '道真自治县',
                     '凤冈县',
                     '余庆县',
                     '镇赉县',
                     '汨罗市',
                     '通州区',
                     '大通 ',
                     '大通县',
                     '大通区',
                     '西青区',
                     '市辖区西青区',
                     '龙岗区',
                     '龙岗镇平湖区',
                     '深圳市龙岗区',
                     '龙岗开发区',
                     '宜丰县',
                     '上饶县',
                     '泰和县',
                     '新干县',
                     '乾县 ',
                     '蒲城县',
                     '凤翔县',
                     '兴平市',
                     '兴平县',
                     '汉滨区',
                     '城固县',
                     '汉中城固县',
                     '蓝田县',
                     '睢宁县',
                     '吴江区',
                     '繁昌县',
                     '万州县',
                     '桃江县',
                     '丰宁县',
                     '新野县',
                     '江肇东县',
                     '泰兴县',
                     '高淳县',
                     '武进县',
                     '锡山县',
                     '慈溪县',
                     '宁海县',
                     '浦东县',
                     '常熟县',
                     '滕州县',
                     '诸城县',
                     '邹城县',
                     '文登县',
                     '招远县',
                     '安塞县',
                     '苍南县',
                     '武义县',
                     '青田县',
                     '江山县',
                     '淳安县',
                     '丽水县',
                     '繁昌区',
                     '万州区',
                     '桃江区',
                     '丰宁区',
                     '新野区',
                     '江肇东区',
                     '泰兴区',
                     '高淳区',
                     '武进区',
                     '锡山区',
                     '慈溪区',
                     '宁海区',
                     '浦东区',
                     '常熟区',
                     '滕州区',
                     '诸城区',
                     '邹城区',
                     '文登区',
                     '招远区',
                     '安塞区',
                     '苍南区',
                     '武义区',
                     '青田区',
                     '江山区',
                     '淳安区',
                     '丽水区')
   and rownum <= 10000
 order by company_number
"""

                companys = single_oracle.oracle_find_by_param_all(sql)
                for company in companys:
                    if company[1] == 'None' or company[1] is None or company[1] is None:
                        print('发现空的公司名称={}'.format(company))
                        single_oracle.oracle_update(
                            "update company_11315 set searched=1 where company_number={}".format(
                                company[0]))

                        continue
                    ents['company_name'] = company[1]
                    if self.isContains(ents['company_name']):  # 判断字符串是否存在
                        print('exists!')
                        # continue
                        company_sql = "select count(*) from company_basic_info where search_name='{}'"
                        update_11315 = 'update {} set searched=1 where company_number={}'
                        check = single_oracle.oracle_find_by_param_all(
                            company_sql.format(ents['company_name']))
                        print(check)
                        logger.debug('check type[0] {}'.format(check))
                        if check[0][0] != 0:
                            single_oracle.oracle_update(
                                update_11315.format(ents['table'], company[0]))
                            continue
                        else:
                            print('放入过滤队列')
                            # self.insert(ents['company_name'])
                    else:
                        print(company)
                        print('not exists!')
                    self.insert(ents['company_name'])
                    ents['branch'] = company[2] or ''
                    ents['address'] = company[3] or ''
                    # print cache['company_name']
                    ents['number'] = company[0]
                    self.server.lpush('ents', ents)
            self.del_lock(lock_uid, sec)

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
        lock_uid = 'parse'
        status, sec = self.get_lock(lock_uid)
        if status:
            parses_length = self.server.llen('parses')

            if parses_length > 500:
                logger.debug('parses length={}'.format(parses_length))
                self.del_lock(lock_uid, sec)
                return

            # mongo = single_mongodb
            # param = {'parse': 0}
            # projection = {'_id': 1}

            try:
                sql = 'SELECT txt_id,add_time  FROM company_basic_info WHERE page_spider=1 AND parsed=0  and ROWNUM <=10000 order by txt_id'
                # resuls = mongo.mongodb_find_limit('company_detail_info', param,projection, 1000)
                # if resuls.count() == 0:
                #     param = {'parse': {'$exists': False}}
                #     resuls = mongo.mongodb_find_limit('company_detail_info', param,projection, 100000)
                results = single_oracle.oracle_find_by_param_all(sql)
                print(len(results))
                if not results:
                    time.sleep(60 % 30)
                    # self.del_lock(lock_uid, sec)
                    # self.put_parse()
                else:
                    for page in results:
                        txt_id = page[0]

                        # print ('已解析')
                        print(page[1])
                        # find_sql='select count(*) from tyc_qybj_jbxx where txt_id='{}''.format(txt_id)
                        # print (mysql.mysql_find_by_param(find_sql))

                        # mysql.mysql_update_param(
                        #     'update company_basic_info set  parsed=1 where txt_id='{}''.format(txt_id))
                        # print(txt_id)
                        # continue

                        self.server.lpush('parses', txt_id)
                self.del_lock(lock_uid, sec)
            except Exception as e:
                self.del_lock(lock_uid, sec)
                logger.exception(e)

    def put_bloomfilter(self):
        pass

    def put_11315_omit(self):
        '''
        11315遗漏的企业名单
        :return:
        '''
        lock_uid = '11315_omit_s'
        status, sec = self.get_lock(lock_uid)
        if status:
            omit_length = self.server.llen('11315_omit')
            if omit_length > 50000:
                logger.debug('parses length={}'.format(parses_length))
                self.del_lock(lock_uid, sec)
                return
            try:
                omit_sql = 'select company_number from company_11315 where {}'
                # select company_number from company_11315 where company_numnber > 3138637 and company_number < 4000000 order by company_number asc
                tablename_condition = self.get_configs_by_tablename(
                    'put_11315_omit')
                results = single_oracle.oracle_find_by_param_all(
                    omit_sql.format(tablename_condition[0]))

                if results[0][0] :
                    if tablename_condition[1] == 0:
                        # TODO
                        sql = 'update config set over = 2 where id = {}'.format(
                            tablename_condition[2])
                        single_oracle.oracle_update(sql)

                    #
                    num_1 = [x[0] for x in results]
                    num_2 = [x for x in range(min(num_l), max(num_l))]
                    omit_list = set(num_2) - set(num_1)
                    for company_number in omit_list:
                        # company_number = result[0]
                        self.server.lpush('11315_omit', company_number)

                    if len(omit_list) == 0:
                    # TODO
                        sql = 'update config set over = 1,over_time = SYSDATE where id = {}'.format(
                            tablename_condition[2])
                        single_oracle.oracle_update(sql)

                self.del_lock(lock_uid, sec)
            except Exception as e:
                self.del_lock(lock_uid, sec)
                logger.exception(e)


    def put_11315_increased(self):
        '''
        11315新增企业名单
        :return:
        '''
        lock_uid = '11315_increased_s'
        status, sec = self.get_lock(lock_uid)
        if status:
            incre_length = self.server.llen('11315_increased')
            if incre_length > 50000:
                logger.debug('parses length={}'.format(parses_length))
                self.del_lock(lock_uid, sec)
                return
            try:
                incre_sql = 'SELECT max(company_number) FROM company_11315 where {}'
                # select company_number from company_11315 where 1=1

                tablename_condition = self.get_configs_by_tablename(
                    'put_11315_increased')
                results = single_oracle.oracle_find_by_param_all(
                    omit_sql.format(tablename_condition[0]))
                if results[0][0]:
                    if tablename_condition[1] == 0:
                        sql = 'update config set over = 2 where id = {}'.format(
                            tablename_condition[2])
                        single_oracle.oracle_update(sql)
                    # XXX: 需要判段什么时候抓取完毕
                    for i in ranage(results[0][0]+1,  i+100000):
                        company_number = i
                        self.server.lpush('11315_omit', company_number)
                else:
                    single_oracle.oracle_update(
                        'update config set over = 1, over_time = SYSDATE where id = {}'.format(
                            tablename_condition[2]))

                self.del_lock(lock_uid, sec)
            except Exception as e:
                self.del_lock(lock_uid, sec)
                logger.exception(e)

    def put_11315(self):
        lock_uid = '11315'
        status, sec = self.get_lock(lock_uid)
        if status:
            parses_length = self.server.llen('11315s')

            if parses_length > 50000:
                logger.debug('parses length={}'.format(parses_length))
                self.del_lock(lock_uid, sec)
                return

            # mongo = single_mongodb
            # param = {'parse': 0}
            # projection = {'_id': 1}

            try:
                #max_sql = 'SELECT Max(company_number) FROM {} '
                max_sql = 'SELECT min(company_number) FROM {} where company_number > 1 and company_number < 30007800 '
                # 查询慈溪市
                # max_sql = "select company_number from {} where (address_2 ='慈溪' or address_2 ='慈溪市' or address_3 ='慈溪' or address_3 ='慈溪市') and mark != 11 and company_name != 'NoCompany'"

                x = 3138637
                y = 4000000
                #max1 = single_oracle.mysql_find_by_param_all(max_sql.format('company_11315_zyfd'))

                #print(max1, max2)
                # print('company_number',max2)
                # max=0
                # if max[0]>110000000:
                #     max = single_mysql.mysql_find_by_param(max_sql.format(sql_2))
                #maxs = max(max1[0][0], max2[0][0])
                # i = max2 + 1
                # i = max2
                for company_number in range(x, y):
                    i = company_number
                # for i in xrange(i, i + 100000):
                #     print(i)
                    self.server.lpush('11315s', i)

                for company_number in range(4000000, 5456193):
                    i = company_number
                    self.server.lpush('11315s', i)

                self.del_lock(lock_uid, sec)
            except Exception as e:
                self.del_lock(lock_uid, sec)
                logger.exception(e)

    def put_11315_update(self):
        lock_uid = '11315_update'
        status, sec = self.get_lock(lock_uid)
        if status:
            parses_length = self.server.llen('11315_updates')

            if parses_length > 50000:
                logger.debug('parses length={}'.format(parses_length))
                self.del_lock(lock_uid, sec)
                return

            # mongo = single_mongodb
            # param = {'parse': 0}
            # projection = {'_id': 1}
            sql = "SELECT company_number FROM {} where company_type is null and error=0 and branch is not null and searched=1 and rownum<=100000"
            try:

                # max1 = single_oracle.oracle_find_by_param_all(sql.format('company_11315_zyfd')
                #     )
                max2 = single_oracle.oracle_find_by_param_all(
                    sql.format('company_11315'))
                # for i in max1:
                #     self.server.lpush('11315_types', i[0])
                for i in max2:
                    self.server.lpush('11315_updates', i[0])
                self.del_lock(lock_uid, sec)
            except Exception as e:
                self.del_lock(lock_uid, sec)
                logger.exception(e)


single_reids = RedisUtil()
if __name__ == '__main__':

    bf = RedisUtil()
    # if bf.isContains('http://www.baidu.com'):  # 判断字符串是否存在
    #     print('exists!')
    # else:
    #     print ('not exists!')
    #     bf.insert('http://www.baidu.com')
    # bf.put_user()
    # bf.put_page()
    bf.put_11315()
