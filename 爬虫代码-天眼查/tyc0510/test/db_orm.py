# -*- coding:utf-8 -*-
import datetime
import functools
import logging.config
import time
import traceback

# import MySQLdb as mysql
# import logging
import cx_Oracle
from bson import ObjectId
from pymongo import MongoClient

from redis_cache_to_db import single_redis_to_db
from setting import *
from models import *
# reload(sys)
# sys.setdefaultencoding('utf-8')
# from setting import MONGODB_USER

# from MySQLdb.cursors import *
# import cx_oracle as oracle


logging.config.fileConfig("../log_file/db.conf")
logger = logging.getLogger("loggerTxt")

def get_current_timestamp():
    return str(time.mktime(datetime.datetime.now().date().timetuple()))

# 没有解决并发问题
def insert_count_deractor(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        table_param = 'company_11315_count,qyxq_info_count,company_11315_add_count,qyxq_info_add_count,data_date'
        tamp = get_current_timestamp()
        table_sql = args[1]
        if 'company_basic_info' not in table_sql:
            return func(*args, **kwargs)
        try:
            check_current = single_redis_to_db.server.hexists('py_st_com_info_count_flag', tamp)
            if check_current == 0:
                total_count_11315 = single_oracle.oracle_find_by_param_all('select count(1) from company_11315 ')[0][0]
                total_count_tyc = single_oracle.oracle_find_by_param_all('select count(1) from company_basic_info ')[0][
                    0]
                single_oracle.oracle_insert_param_only(
                    'insert into py_st_com_info_count({}) values ({},{},{},{},{})'.format(table_param,
                                                                                          total_count_11315,
                                                                                          total_count_tyc, 0, 0,
                                                                                          tamp))
                single_redis_to_db.server.hset('py_st_com_info_count_flag', tamp, 1)
            else:
                single_oracle.oracle_update(
                    'update py_st_com_info_count set qyxq_info_count=qyxq_info_count+1 , qyxq_info_add_count=qyxq_info_add_count+1 where data_date={current_day}'.format(
                        current_day=get_current_timestamp()))
        
        except Exception as e:
            logger.exception(e)
        finally:
            return func(*args, **kwargs)
    
    return wrapper

class OracleClient(object):
    """数据连接对象，产生数据库连接池.
    此类中的连接采用连接池实现获取连接对象：conn = oracle.getConn()
    释放连接对象;conn.close()或del conn
    """
    
    # 连接池对象
    # __pool = None
    
    # def __init__(self):
    #     # 数据库构造函数，从连接池中取出连接，并生成操作游标
    
    # @staticmethod
    # def get_onn(self):
    #     self._conn = cx_Oracle.connect(ORALCE_USER, ORALCE_PASSWORD, ORALCE_HOST + "/" + SERVICE, encoding='utf8')
    #     self._cursor = self._conn.cursor()
    
    # def execute(self, sql):
    #     """执行指定sql语句"""
    #     self.get_onn()
    #     self._cursor.execute(sql)  # 执行语句
    #     # self._conn.commit()  # 然后提交
    
    # def execute_param(self, sql, param):
    #     """执行指定sql语句"""
    #     self.get_onn()
    #     self._cursor.execute(sql, param)  # 执行语句
    #     self._conn.commit()  # 然后提交
    
    def oracle_insert_sql_param(self, cls):
        try:
            single_oracle_orm.add(cls)
            single_oracle_orm.commit()
            # logger.debug('sql={},param='.format(sql))
            # self.execute_param(sql, param)
            # return self._cursor.fetchone()
            # self.pool.commit()
        except:
            logger.exception("Execute {} error: {}".format(cls.__tablename__, traceback.format_exc()))
        finally:
            single_oracle_orm.rollback()
    
    def oracle_insert_param_only(self, cls):
        """
               单条数据插入mysql
               :param table: 表名
               :param column_name: 需要插入的列,字符串“（，，，，）”
               :param insert_value: 插入列的值,字符串“（，，，，）”
               :return: 没有返回值
               """
        # sql = "insert into " + table + column_name + " values" + insert_value
        try:
            single_oracle_orm.add(cls)
            single_oracle_orm.commit()
            # logger.debug(sql)
            # self.execute(sql)
            # return self._cursor.fetchone()
            # self.pool.commit()
        except:
            logger.exception("Execute {} error: {}".format(cls.__tablename__, traceback.format_exc()))
        finally:
            self.__del__()
    
    @insert_count_deractor
    def oracle_insert_param(self, cls):
        """
        单条数据插入mysql
        :param table: 表名
        :param column_name: 需要插入的列,字符串“（，，，，）”
        :param insert_value: 插入列的值,字符串“（，，，，）”
        :return: 没有返回值
        """
        # sql = "insert into " + table + column_name + " values" + insert_value
        try:
            single_oracle_orm.add(cls)
            single_oracle_orm.commit()
            # logger.debug(sql)
            # self.execute(sql)
            # return self._cursor.fetchone()
            # self.pool.commit()
        except:
            logger.exception("Execute {} error: {}".format(cls.__tablename__, traceback.format_exc()))
        finally:
            self.__del__()
    
    def oracle_insert(self, cls):
        """
        单条数据插入mysql
        :param table: 表名
        :param column_name: 需要插入的列,字符串“（，，，，）”
        :param insert_value: 插入列的值,字符串“（，，，，）”
        :return: 没有返回值
        """
        # sql = "insert into " + table + column_name + " values" + insert_value
        try:
            single_oracle_orm.add(cls)
            single_oracle_orm.commit()
            # logger.debug(sql)
            # self.execute(sql)
            # return self._cursor.fetchone()
            # self.pool.commit()
        except:
            logger.exception("Execute {} error: {}".format(cls.__tablename__, traceback.format_exc()))
            # OracleClient.__pool.rollback()
        finally:
            self.__del__()
    
    def oracle_find_by_param_all(self, cls,filter):
        # type: (object) -> object
        try:
            return single_oracle_orm.query(cls).filter_by(filter)
            # single_oracle_orm.commit()
            # logger.debug(param)
            # self.execute(param)
            # return self._cursor.fetchall()
        except:
            logger.exception("Execute {} error: {}".format(cls, traceback.format_exc()))
        finally:
            self.__del__()
    
    def oracle_update(self, cls):
        try:
            pass
            # logger.debug(sql)
            # self.execute(sql)
            # return self._cursor.fetchone()
        except:
            logger.exception("Execute {} error: {}".format(cls.__tablename__, traceback.format_exc()))
        finally:
            self.__del__()
    
    def __del__(self):
        """释放连接池资源"""
        self._cursor.close()
        self._conn.close()

class MongodbClient(object):
    
    def __init__(self, host=MONGODB_HOST, port=MONGODB_PORT):
        self.db = MongoClient(host=host, port=port)[MONGODB_DATABASE]
        self.db.authenticate(MONGODB_USER, MONGODB_PASSWORD)

    # db = client.admin
    # # 认证用户密码
    # db.authenticate('root', '123456')
    def mongodb_insert(self, table, parameter):
        """
        :param table: 表名
        :param parameter: 插入mongodb的数据，字典类型
        :return: 返回该条插入的数据，方便获取ID ["_id"]
        """
        x = self.db[table].insert(parameter)
        return str(x)
    
    def mongodb_find_one(self, table, parameter={}):
        """
            传入字典类型数据，查找符合条件的，单条数据，并返回字典型数据集合,table为表名
        """
        return self.db[table].find_one(parameter)
    
    def mongodb_find(self, table, parameter, projection={}):
        """
            传入字典类型数据，查找符合条件的所有数据，并返回字典型数据集合,table为表名
        """
        return self.db[table].find(parameter, projection)
    
    def mongodb_remove(self, table, parameter):
        """
            传入字典型数据，删除符合条件的数据集,table为表名
        """
        self.db[table].remove(parameter)
    
    def mongodb_find_limit(self, table='', param={}, projection={}, limit=0):
        return self.db[table].find(param, projection).limit(limit)
    
    def mongodb_count(self, table='', param={}):
        return self.db[table].find(param).count()
    
    def mongodb_update(self, table, condition_parameter, result_parameter):
        """
            传入条件参数、需要修改的参数，都为字典型，自动添加更新日期,table为表名
        """
        self.db[table].update_many(
            condition_parameter,
            {
                "$set": result_parameter,
                "$currentDate": {"updateTime": True}
            }
        )

def create_insert_sql(table_name, table_column, column_count):
    insert_sql = 'insert into ' + table_name + ' ' + table_column + ' values('
    for i in range(1, column_count + 1):
        insert_sql += ':' + str(i) + ','
    insert_sql = insert_sql[:-1]
    insert_sql += ')'
    return insert_sql

single_mongodb = MongodbClient()
single_oracle = OracleClient()
if __name__ == "__main__":
    # import sys
    #
    # reload(sys)
    # sys.setdefaultencoding('utf-8')
    mongo_where_parameter = {}
    mongo_where_parameter['_id'] = ObjectId('5cf50d0ef96e1407b72910c3')
    mongodb = MongodbClient()
    s = mongodb.mongodb_find_one('company_detail_info', mongo_where_parameter)
    
    print(s)
