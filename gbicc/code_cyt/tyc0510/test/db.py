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
    def get_onn(self):
        self._conn = cx_Oracle.connect(ORALCE_USER, ORALCE_PASSWORD, ORALCE_HOST + "/" + SERVICE, encoding='utf8')
        self._cursor = self._conn.cursor()
    
    def execute(self, sql):
        """执行指定sql语句"""
        self.get_onn()
        self._cursor.execute(sql)  # 执行语句
        self._conn.commit()  # 然后提交
    
    def execute_param(self, sql, param):
        """执行指定sql语句"""
        self.get_onn()
        self._cursor.execute(sql, param)  # 执行语句
        self._conn.commit()  # 然后提交
    
    def oracle_insert_sql_param(self, sql, param):
        try:
            logger.debug('sql={},param='.format(sql))
            self.execute_param(sql, param)
            # return self._cursor.fetchone()
            # self.pool.commit()
        except:
            logger.exception("Execute {} error: {}".format(sql, traceback.format_exc()))
        finally:
            self.__del__()
    
    def oracle_insert_param_only(self, sql):
        """
               单条数据插入mysql
               :param table: 表名
               :param column_name: 需要插入的列,字符串“（，，，，）”
               :param insert_value: 插入列的值,字符串“（，，，，）”
               :return: 没有返回值
               """
        # sql = "insert into " + table + column_name + " values" + insert_value
        try:
            logger.debug(sql)
            self.execute(sql)
            # return self._cursor.fetchone()
            # self.pool.commit()
        except:
            logger.exception("Execute {} error: {}".format(sql, traceback.format_exc()))
        finally:
            self.__del__()
    
    @insert_count_deractor
    def oracle_insert_param(self, sql):
        """
        单条数据插入mysql
        :param table: 表名
        :param column_name: 需要插入的列,字符串“（，，，，）”
        :param insert_value: 插入列的值,字符串“（，，，，）”
        :return: 没有返回值
        """
        # sql = "insert into " + table + column_name + " values" + insert_value
        try:
            logger.debug(sql)
            self.execute(sql)
            # return self._cursor.fetchone()
            # self.pool.commit()
        except:
            logger.exception("Execute {} error: {}".format(sql, traceback.format_exc()))
        finally:
            self.__del__()
    
    def oracle_insert(self, table, column_name, insert_value):
        """
        单条数据插入mysql
        :param table: 表名
        :param column_name: 需要插入的列,字符串“（，，，，）”
        :param insert_value: 插入列的值,字符串“（，，，，）”
        :return: 没有返回值
        """
        sql = "insert into " + table + column_name + " values" + insert_value
        try:
            logger.debug(sql)
            self.execute(sql)
            # return self._cursor.fetchone()
            # self.pool.commit()
        except:
            logger.exception("Execute {} error: {}".format(sql, traceback.format_exc()))
            # OracleClient.__pool.rollback()
        finally:
            self.__del__()
    
    def oracle_find_by_param_all(self, param):
        # type: (object) -> object
        try:
            logger.debug(param)
            self.execute(param)
            return self._cursor.fetchall()
        except:
            logger.exception("Execute {} error: {}".format(param, traceback.format_exc()))
        finally:
            self.__del__()
    
    def oracle_update(self, sql):
        try:
            logger.debug(sql)
            self.execute(sql)
            # return self._cursor.fetchone()
        except:
            logger.exception("Execute {} error: {}".format(sql, traceback.format_exc()))
        finally:
            self.__del__()
    
    def __del__(self):
        """释放连接池资源"""
        self._cursor.close()
        self._conn.close()

class MongodbClient(object):
    
    def __init__(self, host=MONGODB_HOST, port=MONGODB_PORT):
        self.db = MongoClient(host=host, port=port)[MONGODB_DATABASE]
        # self.db.authenticate(MONGODB_USER, MONGODB_PASSWORD)

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

# class MysqlClient(object):
#     _pool = None
#
#     def __init__(self):
#         self.host = MYSQL_HOST
#         self.password = MYSQL_PASSWORD
#         self.port = MYSQL_PORT
#         self.user = MYSQL_USER
#         self.database = MYSQL_DATABASE
#
#         # jdbcUrl: jdbc:oracle:thin:
#         #
#         # import cx_Oracle
#         #
#         # conn =cx_Oracle.connect('tyc/Tyc%2018@10.0.3.213:1521/CASPRD')
#         # curs = conn.cursor()
#         # sql = 'select count(*) from branch'
#         # curs.execute(sql)
#         #
#         # for result in curs:
#         #     print(result)
#         #
#         # curs.close()
#         # conn.close()
#
#         # @
#         #
#         # 10.10.82.70:1521:EDWDEV2
#         # username: LOG_REPORT
#         # password: "LOG_REPORT"
#         # driver -
#         #
#         # class -name: oracle.jdbc.driver.OracleDriver
#         # connect('LOG_REPORT/LOG_REPORT@10.10.82.70/EDWDEV2')
#
#         # self.db = PooledDB(mysql, mincached=2, maxcached=3, host=self.host, db=self.database, user=self.user,
#         #                    passwd=self.password, charset='utf8', setsession=['SET AUTOCOMMIT = 1'])
#
#         self.db = cx_Oracle.connect('tyc/Tyc%2018@10.0.3.213:1521/CASPRD')
#         # cx_Oracle.=
#         # self.pool= mysql.connect(MYSQL_HOST, MYSQL_USER,MYSQL_PASSWORD, MYSQL_DATABASE,port=MYSQL_PORT, charset='utf8' )
#
#     # 连接数据库
#     def connect_db(self):
#
#         self.pool = self.db.connection()
#         self.cur = self.pool.cursor()
#
#     # 关闭连接
#     def close_db(self):
#         self.cur.close()
#         self.pool.close()
#
#     # 执行sql
#     def execute(self, sql):
#         self.connect_db()
#         self.cur.execute(sql)
#
#     # 执行sql
#     def execute_param(self, sql,param):
#         self.connect_db()
#         self.cur.execute(sql,param)
#
#     def find_batch(self):
#         get_sql = 'SELECT batch ,min(add_time) add_time FROM batch_detail WHERE company_number= (SELECT MAX(company_number) FROM batch_detail)'
#         try:
#             self.execute(get_sql)
#             return self.cur.fetchall()
#         except:
#             logger.exception("Execute '%s' error: %s" % (get_sql, traceback.format_exc()))
#         finally:
#             self.close_db()
#
#     def mysql_insert(self, table, column_name, insert_value):
#         """
#         单条数据插入mysql
#         :param table: 表名
#         :param column_name: 需要插入的列,字符串“（，，，，）”
#         :param insert_value: 插入列的值,字符串“（，，，，）”
#         :return: 没有返回值
#         """
#         sql = "insert into " + table + column_name + "values" + insert_value
#         try:
#             logger.debug(sql)
#             self.execute(sql)
#             self.pool.commit()
#         except:
#             logger.exception("Execute '%s' error: %s" % (sql, traceback.format_exc()))
#             self.pool.rollback()
#         finally:
#             self.close_db()
#
#     def mysql_insert_endtime(self, end_time):
#         get_sql = "insert into batch_detail(ent_time) values('%s')" % (end_time)
#         try:
#             logger.debug(get_sql)
#             self.execute(get_sql)
#             self.pool.commit()
#         except:
#             logger.exception("Execute '%s' error: %s" % (get_sql, traceback.format_exc()))
#
#             self.pool.rollback()
#         finally:
#             self.close_db()
#
#     def mysql_find_by_param(self, param):
#         try:
#             logger.debug(param)
#             self.execute(param)
#             return self.cur.fetchone()
#         except:
#             logger.exception("Execute '%s' error: %s" % (param, traceback.format_exc()))
#         finally:
#             self.close_db()
#
#     def mysql_find_by_param_all(self, param):
#         # type: (object) -> object
#
#         try:
#             logger.debug(param)
#             self.execute(param)
#             return self.cur.fetchall()
#         except:
#             logger.exception("Execute '%s' error: %s" % (param, traceback.format_exc()))
#         finally:
#             self.close_db()
#
#     def mysql_find_one(self, table, parameters={}):
#         """
#         :param table: 表名
#         :param parameters: where查询条件, 字典类型
#         :return: result 返回单条数据
#         """
#         get_sql = "SELECT * FROM " + table + " where 1=1 "
#         if parameters:
#             where_condition = ""
#             for key, value in parameters.items():
#                 if key == "update_time":
#                     where_condition += (' and ' + str(key) + "<" + '"' + str(value) + '"')
#                 elif key == "address_3":
#                     where_condition += (' and ' + str(key) + " in " + str(value))
#                 else:
#                     where_condition += (' and ' + str(key) + "=" + str(value))
#             get_sql += where_condition
#             get_sql += " limit 1"
#         try:
#             # print 'mysql_find_one  ',get_sql
#             logger.debug(get_sql)
#             self.execute(get_sql)
#             result = self.cur.fetchone()
#             return result
#         except:
#             logger.exception("Execute '%s' error: %s" % (get_sql, traceback.format_exc()))
#         finally:
#             self.close_db()
#
#     def mysql_update(self, table, update_parameters={}, where_parameters={}):
#         """
#         :param table: 表名
#         :param parameters:更新的值 , where_parameters: 条件
#         :return:
#         """
#         get_sql = "update " + table + " set "
#         if update_parameters:
#             value_condition = ""
#             for key, value in update_parameters.items():
#                 value_condition += (str(key) + "='" + str(value) + "', ")
#             get_sql += value_condition[0:-2] + " where 1=1 "
#
#         if where_parameters:
#             where_condition = ""
#             for key, value in where_parameters.items():
#                 where_condition += (' and ' + str(key) + "=" + '"' + str(value) + '"')
#             get_sql += where_condition
#         try:
#             logger.debug(get_sql)
#             self.execute(get_sql)
#             self.pool.commit()
#         except:
#             logger.exception("Execute '%s' error: %s" % (get_sql, traceback.format_exc()))
#             self.pool.rollback()
#         finally:
#             self.close_db()
#
#     def mysql_update_param(self, param):
#         try:
#             logger.debug(param)
#             self.execute(param)
#             self.pool.commit()
#         except:
#             logger.exception("Execute '%s' error: %s" % (param, traceback.format_exc()))
#             self.pool.rollback()
#         finally:
#             self.close_db()
#
#     def mysql_delete_by_param(self, param):
#         try:
#             logger.debug(param)
#             self.execute(param)
#             self.pool.commit()
#         except:
#             logger.exception("Execute '%s' error: %s" % (param, traceback.format_exc()))
#             self.pool.rollback()
#         finally:
#             self.close_db()
#
#         # 获取所有数据列表
#
#     def get_list(self, table, fields):
#         sql = "select %s from %s" % (",".join(fields), table)
#         try:
#             self.execute(sql)
#             result = self.cur.fetchall()
#             if result:
#                 result = [dict((k, row[i]) for i, k in enumerate(fields)) for row in result]
#             else:
#                 result = {}
#             return result
#         except:
#             logger.exception("Execute '%s' error: %s" % (sql, traceback.format_exc()))
#         finally:
#             self.close_db()
#
#     # 获取某一条数据，返回字典
#     def get_one(self, table, fields, where):
#         if isinstance(where, dict) and where:
#             conditions = []
#             for k, v in where.items():
#                 conditions.append("%s='%s'" % (k, v))
#         sql = "select %s from %s where %s" % (",".join(fields), table, ' AND '.join(conditions))
#         try:
#             self.execute(sql)
#             result = self.cur.fetchone()
#             if result:
#                 result = dict((k, result[i]) for i, k in enumerate(fields))
#             else:
#                 result = {}
#             return result
#         except:
#             logger.exception("Execute '%s' error: %s" % (sql, traceback.format_exc()))
#         finally:
#             self.close_db()
#
#     # 更新数据
#     def update(self, table, fields):
#         data = ",".join(["%s='%s'" % (k, v) for k, v in fields.items()])
#         sql = "update %s set %s where id=%s " % (table, data, fields["id"])
#         try:
#             return self.execute(sql)
#         except:
#             logger.exception("Execute '%s' error: %s" % (sql, traceback.format_exc()))
#         finally:
#             self.close_db()
#
#     # 添加数据
#     def create(self, table, data):
#         fields, values = [], []
#         for k, v in data.items():
#             fields.append(k)
#             values.append("'%s'" % v)
#         sql = "insert into %s (%s) values (%s)" % (table, ",".join(fields), ",".join(values))
#         try:
#             return self.execute(sql)
#         except:
#             logger.exception("Execute '%s' error: %s" % (sql, traceback.format_exc()))
#         finally:
#             self.close_db()
#
#     # 删除数据
#     def delete(self, table, where):
#         if isinstance(where, dict) and where:
#             conditions = []
#             for k, v in where.items():
#                 conditions.append("%s='%s'" % (k, v))
#         sql = "delete from %s where %s" % (table, ' AND '.join(conditions))
#         try:
#             return self.execute(sql)
#         except:
#             logger.exception("Execute '%s' error: %s" % (sql, traceback.format_exc()))
#         finally:
#             self.close_db()

# single_mysql=MysqlClient()
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
