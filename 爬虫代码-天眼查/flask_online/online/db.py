# -*- coding:utf-8 -*-
from pymongo import MongoClient
import MySQLdb
import logging
import logging.config
from MySQLdb.cursors import *

from DBUtils.PooledDB import PooledDB


from setting import *
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import ConfigParser

config = ConfigParser.ConfigParser()
config.read = ('../log_file/db.conf"')
# logging.config.fileConfig("./online/log_file/db.conf")
logger = logging.getLogger("loggerTxt")


class MongodbClient(object):
    def __init__(
            self,
            host=MONGODB_HOST,
            port=MONGODB_PORT,
            password=MONGODB_PASSWORD):
        if MONGODB_PASSWORD:
            self.db = MongoClient(host=host, port=port, password=password)[
                MONGODB_DATABASE]
        else:
            self.db = MongoClient(host=host, port=port)[MONGODB_DATABASE]

    def mongodb_insert(self, table, parameter):
        """
        :param table: 表名
        :param parameter: 插入mongodb的数据，字典类型
        :return: 返回该条插入的数据，方便获取ID ["_id"]
        """
        self.db[table].insert(parameter)
        return self.db[table].find_one(parameter)

    def mongodb_find_one(self, table, parameter={}):
        """
            传入字典类型数据，查找符合条件的，单条数据，并返回字典型数据集合,table为表名
        """
        return self.db[table].find_one(parameter)

    def mongodb_find(self, table, parameter):
        """
            传入字典类型数据，查找符合条件的所有数据，并返回字典型数据集合,table为表名
        """
        return self.db[table].find(parameter)

    def mongodb_remove(self, table, parameter):
        """
            传入字典型数据，删除符合条件的数据集,table为表名
        """
        self.db[table].remove(parameter)

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


class MysqlClient(object):
    _pool = None

    def __init__(self):
        self.host = MYSQL_HOST
        self.password = MYSQL_PASSWORD
        self.port = MYSQL_PORT
        self.user = MYSQL_USER
        self.database = MYSQL_DATABASE
        self._db = MysqlClient._connect()

    @staticmethod
    def _connect():
        if MysqlClient._pool is None:
            _pool = PooledDB(
                creator=MySQLdb,
                mincached=10,
                maxcached=30,
                maxconnections=1000,
                maxusage=1,
                host=MYSQL_HOST,
                user=MYSQL_USER,
                passwd=MYSQL_PASSWORD,
                db=MYSQL_DATABASE,
                charset="utf8",
                cursorclass=Cursor)
        return _pool.connection()

    def find_batch(self):

        cursor = self._db.cursor()
        get_sql = 'SELECT batch ,min(add_time) add_time FROM batch_detail WHERE company_number= (SELECT MAX(company_number) FROM batch_detail)'
        cursor.execute(get_sql)
        result = cursor.fetchone()
        cursor.close()
        return result

    def mysql_insert(self, table, column_name, insert_value):
        """
        单条数据插入mysql
        :param table: 表名
        :param column_name: 需要插入的列,字符串“（，，，，）”
        :param insert_value: 插入列的值,字符串“（，，，，）”
        :return: 没有返回值
        """
        cursor = self._db.cursor()
        sql = "insert into " + table + column_name + "values" + insert_value
        try:
            print (sql)
        except BaseException:
            pass
        cursor.execute(sql)
        self._db.commit()
        cursor.close()

    def mysql_insert_endtime(self, end_time):
        cursor = self._db.cursor()
        get_sql = "insert into batch_detail(ent_time) values('%s')" % (
            end_time)
        cursor.execute(get_sql)
        self._db.commit()
        cursor.close()

    def mysql_find_by_param(self, param):
        cursor = self._db.cursor()
        get_sql = param
        cursor.execute(get_sql)
        # print get_sql
        result = cursor.fetchone()
        cursor.close()
        return result

    def mysql_find_by_param_all(self, param):
        # type: (object) -> object
        cursor = self._db.cursor()
        get_sql = param
        cursor.execute(get_sql)
        # print get_sql
        result = cursor.fetchall()
        cursor.close()
        return result

    def mysql_find_one(self, table, parameters={}):
        """
        :param table: 表名
        :param parameters: where查询条件, 字典类型
        :return: result 返回单条数据
        """
        cursor = self._db.cursor()
        get_sql = "SELECT * FROM " + table + " where 1=1 "
        if parameters:
            where_condition = ""
            for key, value in parameters.items():
                if key == "update_time":
                    where_condition += (' and ' + str(key) +
                                        "<" + '"' + str(value) + '"')
                elif key == "address_3":
                    where_condition += (' and ' + str(key) +
                                        " in " + str(value))
                else:
                    where_condition += (' and ' + str(key) + "=" + str(value))
            get_sql += where_condition
            get_sql += " limit 1"
        # print 'mysql_find_one  ',get_sql
        cursor.execute(get_sql)
        result = cursor.fetchone()
        cursor.close()
        return result

    def mysql_update(self, table, update_parameters={}, where_parameters={}):
        """
        :param table: 表名
        :param parameters:更新的值 , where_parameters: 条件
        :return:
        """
        cursor = self._db.cursor()
        get_sql = "update " + table + " set "
        if update_parameters:
            value_condition = ""
            for key, value in update_parameters.items():
                value_condition += (str(key) + "='" + str(value) + "', ")
            get_sql += value_condition[0:-2] + " where 1=1 "

        if where_parameters:
            where_condition = ""
            for key, value in where_parameters.items():
                where_condition += (' and ' + str(key) +
                                    "=" + '"' + str(value) + '"')
            get_sql += where_condition
            try:
                logger.info('update===%s' % get_sql)
                print 'update===', get_sql
            except BaseException:
                logger.info('mysql_update print sql error!')
        cursor.execute(get_sql)
        self._db.commit()
        cursor.close()

    def mysql_update_param(self, param):
        cursor = self._db.cursor()
        sql = param
        cursor.execute(sql)
        self._db.commit()
        cursor.close()

    def mysql_delete_by_param(self, param):
        cursor = self._db.cursor()
        cursor.execute(param)
        self._db.commit()
        cursor.close()


if __name__ == "__main__":
    import sys
    reload(sys)
    sys.setdefaultencoding('utf-8')
    mongodb = MongodbClient()
    mysqlClient = MysqlClient()
