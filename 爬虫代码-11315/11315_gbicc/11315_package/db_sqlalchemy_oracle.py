# -*- coding:utf-8 -*-

# from db_config import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from setting import *
# from tyc_oracle_all import *
from tyc_bean import *
import cx_Oracle
class Oracle_Client():

    def __init__(self):
        self.session,self.engine=Oracle_Client.connect_db()

    @staticmethod
    def connect_db():
        try:
            # engine = create_engine('oracle+cx_oracle://tyc:Tyc%2018@10.0.3.213/CASPRD',encoding='utf-8')
            engine = create_engine('oracle+cx_oracle://tyc:tyc@10.10.82.71/edwuat', encoding='gbk')
            DBSession = sessionmaker(bind=engine)
            session = DBSession()
        except Exception as e:
            print(e)
        else:
            return session,engine

        # 关闭连接

    def close_db(self):
        self.session.close()


    # 执行sql
    def execute(self, sql):
        # self.connect_db()
        return self.engine.execute(sql)

    def oracle_insert(self, obj):
        try:
            self.session.add(obj)
            self.session.commit()
        except Exception as e:
            print(e)


    # def oracle_find_by_param(self, param, ent_name):
    #     '''
    #     查询并返回一条数据
    #     :param param: 表名
    #     :return:
    #     '''
    #     try:
    #         if param == 'CompanyBasicInfo':
    #             results = self.session.query(CompanyBasicInfo.id, CompanyBasicInfo.add_time).filter_by(ent_name = '%s' % ent_name)
    #         elif param == 'batch_detail':
    #             results = self.session.query(Batch_detail.company_number).filter_by(searched = 0).all()
    #     except Exception as e:
    #         print(e)
    #     else:
    #         return results
    #     finally:
    #         self.close_db()
    #
    #
    #
    #
    # def oracle_find_by_param_all(self, param):
    #     '''
    #     查询并返回多条数据
    #     :param param:  表名
    #     :return:
    #     '''
    #     try:
    #         if param == 'tyc_user':
    #             results = self.session.query(TYc_user.username).filter(username.isnot(null), user_forbid = 0).order_by(Tyc_user.username.asc()).all
    #         elif param == 'CompanyBasicInfo':
    #             results = self.session.query(CompanyBasicInfo.url, CompanyBasicInfo.txt_id).filter(page_spider=0, parsed=0, add_time > DATE('2018-11-01')).limit(10000).all()
    #         elif param == 'batch_detail':
    #             results = self.session.query(Batch_detail).filter_by(searched = 0).all()
    #     except Exception as e:
    #         print(e)
    #     else:
    #         return results
    #     finally:
    #         self.close_db()

    def oracle_update_param(self, param):
        '''
        传入sql语句，更新数据
        :param param: sql语句
        :return:
        '''
        try:
            self.execute(param)

        except Exception as e:
            print(e)

        finally:
            self.close_db()

    def oracle_delete_by_param(self, param):
        '''
        删除数据
        :param param:
        :return:
        '''
        try:

            self.execute(param)

        except Exception as e:
            print(e)

        finally:
            self.close_db()

    def insert(self,obj):
        self.session.add(obj)
        self.session.commit()
single_oracle=Oracle_Client()
if __name__ == '__main__':
    oracle_db = single_oracle

    res=oracle_db.execute('select count(*) from branch')
    for i in res:
        print(i)
