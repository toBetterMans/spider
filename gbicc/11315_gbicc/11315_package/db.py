# -*- coding:utf-8 -*-
from setting import *
import MySQLdb
from MySQLdb.cursors import *
from DBUtils.PooledDB import PooledDB


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
            _pool = PooledDB(creator=MySQLdb, mincached=10, maxcached=30, maxconnections=1000, maxusage=1,
                             host=MYSQL_HOST, user=MYSQL_USER, passwd=MYSQL_PASSWORD, db=MYSQL_DATABASE,
                             charset="utf8", cursorclass=Cursor)
        return _pool.connection()

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
        cursor.execute(sql)
        self._db.commit()
        cursor.close()

    def mysql_find_all(self, table, parameters={}):
        """
        :param table: 表名
        :param parameters: where查询条件, 字典类型
        :return: result 返回单条数据
        """
        cursor = self._db.cursor()
        get_sql = "SELECT * FROM " + table + " where mark=0 and parse=0 limit 10"
        if parameters:
            where_condition = ""
            for key, value in parameters.items():
                where_condition += (' and ' + str(key) + "=" + '"' + str(value) + '"')
            get_sql += where_condition

        cursor.execute(get_sql)
        result = cursor.fetchall()
        cursor.close()
        return result

    def mysql_update(self, table, update_parameters={}, where_parameters={}):
        """
        :param table: 表名
        :param parameters:
        :return:
        """
        cursor = self._db.cursor()
        get_sql = "update " + table + " set "
        if update_parameters:
            value_condition = ""
            for key, value in update_parameters.items():
                value_condition += (str(key) + "=" + '"' + str(value) + '", ')
            get_sql += value_condition[0:-2] + " where mark=0 "

        if where_parameters:
            where_condition = ""
            for key, value in where_parameters.items():
                where_condition += (' and ' + str(key) + "=" + '"' + str(value) + '"')
            get_sql += where_condition
        cursor.execute(get_sql)
        self._db.commit()
        cursor.close()


if __name__ == "__main__":
    mysqlClient = MysqlClient()



