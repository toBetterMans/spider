#!/usr/bin/python3
# -*- coding:utf-8 -*-
import MySQLdb
import redis
# 打开数据库连接
from setting import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE, REDIS_HOST, REDIS_DB, REDIS_PORT


def put_user():
    db = MySQLdb.connect(MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE)
    redis_client = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)
    users_length=redis_client.llen('users')

    if users_length>0:
        print('users length={}'.format(users_length))
        return
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 查询语句
    sql = 'SELECT username FROM tyc_user WHERE user_forbid=0 and username is not null ORDER BY username ASC ;'
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        if results:
            for row in results:
                # print (row[0])
                redis_client.lpush('users',row[0])
        return
    except:
        print("Error: unable to fetch data")
    finally:
        # 关闭数据库连接
        db.close()

if __name__ == '__main__':
    put_user()