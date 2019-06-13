# -*- coding:utf-8 -*-
'''
    oracle数据库
    45张表
'''

from sqlalchemy.dialects.oracle import NUMBER, VARCHAR2, DATE, CLOB
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column

Base = declarative_base()

class Batch_list(Base):
    '''
        批次表 batch_list
    '''
    __tablename__ = 'batch_list'
    
    company_number = Column(NUMBER(24), primary_key=True)
    mark = Column(NUMBER(3))
    company_name = Column(VARCHAR2(300))
    company_address = Column(VARCHAR2(300))
    searched = Column(NUMBER(3))
    error = Column(NUMBER(3))
    add_time = Column(VARCHAR2(300))
    agency_num = Column(VARCHAR2(300))
    agency_name = Column(VARCHAR2(300))
    batch = Column(VARCHAR2(150))
    end_time = Column(VARCHAR2(150))
    batch_type = Column(VARCHAR2(3))
    
    def __repr__(self):
        return "('company_number:%d', 'mark:%d', 'company_name:%s', 'company_address:%s',\
                 'searched:%d', 'error:%d', 'add_time:%s', 'agency_num:%s', 'agency_name:%s',\
                 'batch:%s', 'end_time:%s', 'batch_type:%s')" % \
               (self.company_number, self.mark, self.company_name, self.company_address,
                self.searched, self.error, self.add_time, self.agency_num, self.agency_name, \
                self.batch, self.end_time, self.batch_type)

class Batch_detail(Base):
    '''
        新企业名单 batch_detail
    '''
    __tablename__ = 'batch_detail'
    
    company_number = Column(NUMBER(24), primary_key=True)
    mark = Column(NUMBER(3))
    add_time = Column(VARCHAR2(300))
    company_name = Column(VARCHAR2(300))
    company_address = Column(VARCHAR2(300))
    searched = Column(NUMBER(3))
    error = Column(NUMBER(3))
    agency_num = Column(VARCHAR2(300))
    agency_name = Column(VARCHAR2(300))
    batch = Column(VARCHAR2(150))
    txt_id = Column(VARCHAR2(150))
    batch_type = Column(VARCHAR2(3))
    
    def __repr__(self):
        return "('company_number:%d', 'mark:%d', 'add_time:%s', 'company_name:%s', 'company_address:%s', \
                'searched:%d', 'error:%d', 'agency_num:%s', 'agency_name:%s', 'batch_name:%s', 'txt_id:%s', \
                'batch_type:%s,')" % \
               (self.company_number, self.mark, self.add_time, self.company_name, self.company_address,
                self.searched, self.error, self.agency_num, self.agency_name, self.batch, self.txt_id,
                self.batch_type)

class Branch(Base):
    __tablename__ = 'branch'
    id = Column(NUMBER(30), primary_key=True)
    branch_level2 = Column(VARCHAR2(18))
    branch_level2_short_name = Column(VARCHAR2(18))
    
    def __repr__(self):
        return "('id:%d', 'branch_level2:%s', 'branch_level2_short_name:%s')" % (
        self.id, self.branch_level2, self.branch_level2_short_name)

class Company_11315(Base):
    __tablename__ = 'company_11315'
    
    company_number = Column(NUMBER(24), primary_key=True)
    url = Column(VARCHAR2(300))
    company_name = Column(VARCHAR2(300))
    company_industry = Column(VARCHAR2(600))
    address_1 = Column(VARCHAR2(300))
    address_2 = Column(VARCHAR2(300))
    address_3 = Column(VARCHAR2(300))
    company_area = Column(VARCHAR2(900))
    company_address = Column(VARCHAR2(900))
    add_time = Column(DATE)
    searched = Column(NUMBER(3))
    error = Column(NUMBER(3))
    parse = Column(NUMBER(3))
    mark = Column(NUMBER(3))
    branch = Column(VARCHAR2(18))
    
    def __repr__(self):
        return "('company_number:%d', 'url:%s', 'company_name:%s', 'company_industry:%s', 'address_1:%s', 'address_2:%s', 'address_3:%s', 'company_area:%s', 'company_address:%s', 'add_time:%s', 'searched:%d', 'error:%d', 'parse:%d', 'mark:%d', 'branch:%s')" % \
               (self.company_number, self.url, self.company_name, self.company_industry, self.address_1, self.address_2,
                self.address_3, self.company_area, self.company_address, self.add_time, self.searched, self.error,
                self.parse, self.mark, self.branch)

class Company_11315_ZYFD(Base):
    __tablename__ = 'company_11315_zyfd'
    
    company_number = Column(NUMBER(24), primary_key=True)
    url = Column(VARCHAR2(300))
    company_name = Column(VARCHAR2(300))
    company_industry = Column(VARCHAR2(600))
    address_1 = Column(VARCHAR2(300))
    address_2 = Column(VARCHAR2(300))
    address_3 = Column(VARCHAR2(300))
    company_area = Column(VARCHAR2(900))
    company_address = Column(VARCHAR2(900))
    add_time = Column(DATE)
    searched = Column(NUMBER(3))
    error = Column(NUMBER(3))
    parse = Column(NUMBER(3))
    mark = Column(NUMBER(3))
    branch = Column(VARCHAR2(18))
    
    def __repr__(self):
        return "('company_number:%d', 'url:%s', 'company_name:%s', 'company_industry:%s', 'address_1:%s', 'address_2:%s', 'address_3:%s', 'company_area:%s', 'company_address:%s', 'add_time:%s', 'searched:%d', 'error:%d', 'parse:%d', 'mark:%d', 'branch:%s')" % \
               (self.company_number, self.url, self.company_name, self.company_industry, self.address_1, self.address_2,
                self.address_3, self.company_area, self.company_address, self.add_time, self.searched, self.error,
                self.parse, self.mark, self.branch)

class CompanyBasicInfo(Base):
    '''
         公司列表搜索信息 company_basic_info
    '''
    __tablename__ = 'company_basic_info'
    
    id = Column(NUMBER(24), primary_key=True)
    search_name = Column(VARCHAR2(90))
    ent_name = Column(VARCHAR2(90))
    legal_representative = Column(VARCHAR2(150))
    registered_capital = Column(VARCHAR2(150))
    registration_date = Column(VARCHAR2(30))
    location = Column(VARCHAR2(15))
    score = Column(VARCHAR2(15))
    status_type = Column(VARCHAR2(30))
    url = Column(VARCHAR2(150))
    txt_id = Column(VARCHAR2(150))
    page_spider = Column(NUMBER(3))
    parsed = Column(NUMBER(3))
    mark = Column(NUMBER(3), default=0)
    add_time = Column(DATE)
    agency_num = Column(VARCHAR2(300))
    agency_name = Column(VARCHAR2(300))
    batch = Column(VARCHAR2(150))
    branch = Column(VARCHAR2(18))
    
    def __repr__(self):
        return "('id:%d', 'txt_id:%s', 'ent_name:%s', 'legal_representative:%s', 'registered_capital:%s', \
                'registration_date:%s', 'location:%s', 'score:%s', 'status_type:%s', 'url:%s', 'txt_id:%s',\
                'page_spider:%s', 'parsed:%s', 'mark:%d', 'add_time:%s', 'agency_num:%s','agency_name:%s', \
                'batch:%s', 'branch%s')" % \
               (self.id, self.txt_id, self.ent_name, self.legal_representative, self.registered_capital,
                self.registration_date, self.location, self.score, self.status_type, self.url, self.txt_id,
                self.page_spider, self.parsed, self.mark, self.add_time, self.agency_num, self.agency_name,
                self.batch, self.branch)

Base = Base = declarative_base()

class Fm_pub_cust_corp_test(Base):
    __tablename__ = 'fm_pub_cust_corp_test'
    
    key_id = Column(NUMBER(30), primary_key=True)
    jigouhao = Column(VARCHAR2(45))
    kehumingcheng = Column(VARCHAR2(300))
    yingyezhizhao = Column(VARCHAR2(300))
    zuzhijigoudaima = Column(VARCHAR2(300))
    zhucedengjiriqi = Column(VARCHAR2(25))
    guoshuizhenghao = Column(VARCHAR2(150))
    dishuizhenghao = Column(VARCHAR2(150))
    qiyexingzhi = Column(VARCHAR2(150))
    qiyezhucedizhi = Column(VARCHAR2(3000))
    yuangongrenshu = Column(NUMBER(30))
    jingyingfanwei = Column(VARCHAR2(600))
    chengliriqi = Column(VARCHAR2(25))
    jingyingnianxian = Column(NUMBER(30))
    yijihangyemingcheng = Column(VARCHAR2(750))
    erjihangyemingcheng = Column(VARCHAR2(150))
    sanjihangyemingcheng = Column(VARCHAR2(300))
    zhuceziben = Column(NUMBER)
    shishouziben = Column(NUMBER)
    zhengjianleixing = Column(VARCHAR2(90))
    zhengjianhaoma = Column(VARCHAR2(150))
    qiyegudingdianhua = Column(VARCHAR2(120))
    zhuyaolianxifangshi = Column(VARCHAR2(120))
    qiyeqitadianhua = Column(VARCHAR2(120))
    
    def __repr__(self):
        return "('key_id:%d', 'jigouhao:%s', 'kehumingcheng:%s', 'yingyezhizhao:%s', 'zuzhijigoudaima:%s', 'zhucedengjiriqi:%s', 'guoshuizhenghao:%s', 'dishuizhenghao:%s', 'qiyexingzhi:%s', 'qiyezhucedizhi:%s', 'yuangongrenshu:%d', 'jingyingfanwei:%s',  'chengliriqi:%s', 'jingyingnianxian:%d',  'yijihangyemingcheng:%s', 'erjihangyemingcheng:%s', 'sanjihangyemingcheng:%s', 'zhuceziben:%f', 'shishouziben:%f', 'zhengjianleixing:%s', 'zhengjianhaoma:%s', 'qiyegudingdianhua:%s', 'zhuyaolianxifangshi:%s', 'qiyeqitadianhua:%s')" % \
               (self.key_id, self.jigouhao, self.kehumingcheng, self.yingyezhizhao, self.zuzhijigoudaima,
                self.zhucedengjiriqi, self.guoshuizhenghao, self.dishuizhenghao, self.qiyexingzhi, self.qiyezhucedizhi,
                self.yuangongrenshu, self.jingyingfanwei, self.chengliriqi, self.jingyingnianxian,
                self.yijihangyemingcheng, self.erjihangyemingcheng, self.sanjihangyemingcheng, self.zhuceziben,
                self.shishouziben, self.zhengjianleixing, self.zhengjianhaoma, self.qiyegudingdianhua,
                self.zhuyaolianxifangshi, self.qiyeqitadianhua)

class Tmp_bd_four_indu_classif1(Base):
    __tablename__ = 'tmp_bd_four_indu_classif1'
    companyname = Column(VARCHAR2(900))
    regnum = Column(VARCHAR2(300), primary_key=True)
    productrange = Column(CLOB)
    four_indu_classif = Column(VARCHAR2(600))
    branch_name = Column(VARCHAR2(300))
    y_n_pass = Column(VARCHAR2(6))
    txt_id = Column(VARCHAR2(300))
    
    def __repr__(self):
        return "('companyname:%s', 'regnum:%s', 'productrange:%s','four_indu_classif:%s', 'branch_name:%s', 'y_n_pass:%s', 'txt_id;%s')" % (
        self.companyname, self.regnum, self.productrange, self.four_indu_classif, self.branch_name, self.y_n_pass,
        self.txt_id)

class Tmp_bd_four_indu_classif2(Base):
    __tablename__ = 'tmp_bd_four_indu_classif2'
    
    companyname = Column(VARCHAR2(900))
    regnum = Column(VARCHAR2(300), primary_key=True)
    productrange = Column(CLOB)
    term = Column(VARCHAR2(600))
    scope = Column(VARCHAR2(600))
    four_indu_classif = Column(VARCHAR2(600))
    scope_index = Column(NUMBER)
    term_index = Column(NUMBER)
    
    def __repr__(self):
        return "('companyname:%s', 'regnum:%s',  'productrange:%s','term:%s', 'scope:%s', 'four_indu_classif:%s', 'scope_index;%f', 'term_index;%f')" % (
        self.companyname, self.regnum, self.productrange, self.term, self.scope, self.four_indu_classif,
        self.scope_index, self.term_index)

class Tyc_jyfx_dcdy(Base):
    '''
        动产抵押表 tyc_jyfx_dcdy
    '''
    __tablename__ = 'tyc_jyfx_dcdy'
    
    id = Column(NUMBER(24), primary_key=True)
    txt_id = Column(VARCHAR2(150))
    ent_name = Column(VARCHAR2(150))
    registration_date = Column(VARCHAR2(90))
    registration_number = Column(VARCHAR2(150))
    guarantee_type = Column(VARCHAR2(150))
    guarantee_amount = Column(VARCHAR2(150))
    registration_department = Column(VARCHAR2(300))
    status = Column(VARCHAR2(30))
    detail_info = Column(CLOB)
    mark = Column(NUMBER(3), default=0)
    add_time = Column(DATE)
    aquity_amount = Column(NUMBER(30, 2))
    agency_num = Column(VARCHAR2(300))
    agency_name = Column(VARCHAR2(300))
    batch = Column(VARCHAR2(150))
    
    def __repr__(self):
        return "('id:%d', 'txt_id:%s', 'ent_name:%s', 'registration_date:%s', 'registration_number:%s',\
                'guarantee_type:%s', 'guarantee_amount:%s', 'registration_department:%s', 'status:%s', \
                'detail_info:%s', 'mark:%d', 'add_time:%s', 'aquity_amount:%d', 'agency_num:%s', \
                'agency_name:%s', 'batch:%s')" % \
               (self.id, self.txt_id, self.ent_name, self.registration_date, self.registration_number,
                self.guarantee_type, self.guarantee_amount, self.registration_department, self.status,
                self.detail_info, self.mark, self.add_time, self.aquity_amount, self.agency_num,
                self.agency_name, self.batch)

class Tyc_jyfx_gqcz(Base):
    '''
        股权出质表 tyc_jyfx_gqcz
    '''
    __tablename__ = 'tyc_jyfx_gqcz'
    
    id = Column(NUMBER(24), primary_key=True)
    # mongodb文本ID
    txt_id = Column(VARCHAR2(150))
    # 所属公司名称
    ent_name = Column(VARCHAR2(150))
    # 公告时间
    announcement_date = Column(VARCHAR2(90))
    # 登记编号
    registration_number = Column(VARCHAR2(90))
    # 出质人
    pledgor = Column(VARCHAR2(150))
    # 质权人
    pledgee = Column(VARCHAR2(150))
    # 状态
    status = Column(VARCHAR2(15))
    # 详情
    detail_info = Column(CLOB)
    # 标记号
    mark = Column(NUMBER(3), default=0)
    # 添加时间
    add_time = Column(DATE)
    
    aquity_amount = Column(NUMBER(30, 2))
    # 机构号
    agency_num = Column(VARCHAR2(300))
    # 机构名称
    agency_name = Column(VARCHAR2(300))
    # 批次
    batch = Column(VARCHAR2(150))
    
    def __repr__(self):
        return "('id:%d', 'txt_id:%s', 'ent_name:%s', 'announcement_date:%s', 'registration_number:%s', \
                'pledgor:%s', 'pledgee:%s', 'status:%s', 'detail_info:%s',\
                'mark:%d', 'add_time:%s', 'aquity_amount:%d', 'agency_num:%s', 'agency_name:%s', 'batch:%s')" % \
               (self.id, self.txt_id, self.ent_name, self.announcement_date, self.registration_number, self.pledgor,
                self.pledgee, self.status, self.detail_info, self.mark, self.add_time, self.aquity_amount,
                self.agency_num, self.agency_name, self.batch)

class Tyc_jyfx_jyyc(Base):
    '''
        经营异常表 tyc_jyfx_jyyc
    '''
    __tablename__ = 'tyc_jyfx_jyyc'
    
    id = Column(NUMBER(24), primary_key=True)
    txt_id = Column(VARCHAR2(150))
    ent_name = Column(VARCHAR2(150))
    insert_date = Column(VARCHAR2(90))
    insert_cause = Column(VARCHAR2(300))
    insert_department = Column(VARCHAR2(150))
    mark = Column(NUMBER(3), default=0)
    add_time = Column(DATE)
    agency_num = Column(VARCHAR2(300))
    agency_name = Column(VARCHAR2(300))
    batch = Column(VARCHAR2(150))
    
    def __repr__(self):
        return "('id:%d', 'txt_id:%s', 'ent_name:%s', 'insert_date:%s', 'insert_cause:%s', 'insert_department:%s', \
                'mark:%d', 'add_time:%s', 'agency_num:%s', 'agency_name:%s', 'batch:%s')" % \
               (self.id, self.txt_id, self.ent_name, self.insert_date, self.insert_cause, self.insert_department,
                self.mark, self.add_time, self.agency_num, self.agency_name, self.batch)

class Tyc_jyfx_qsgg(Base):
    '''
        欠税公告表 tyc_jyfx_qsgg
    '''
    __tablename__ = 'tyc_jyfx_qsgg'
    
    id = Column(NUMBER(24), primary_key=True)
    txt_id = Column(VARCHAR2(300))
    ent_name = Column(VARCHAR2(300))
    taxes_date = Column(VARCHAR2(150))
    taxes_num = Column(VARCHAR2(300))
    taxes_type = Column(VARCHAR2(300))
    taxes_money = Column(VARCHAR2(300))
    taxes_balance = Column(VARCHAR2(300))
    taxes_office = Column(VARCHAR2(1200))
    mark = Column(NUMBER(4), default=0)
    addtime = Column(DATE)
    agency_num = Column(VARCHAR2(300))
    agency_name = Column(VARCHAR2(300))
    batch = Column(VARCHAR2(150))
    
    def __repr__(self):
        return "('id:%d', 'txt_id:%s', 'ent_name:%s', 'taxes_date:%s', 'taxes_num:%s', 'taxes_type:%s', \
                'taxes_money:%s', 'taxes_balance:%s', 'taxes_office:%s', mark:%d', 'addtime:%s', \
                'agency_num:%s', 'agency_name:%s', 'batch:%s')" % \
               (self.id, self.txt_id, self.ent_name, self.taxes_date, self.taxes_num, self.taxes_type,
                self.taxes_money, self.taxes_balance, self.taxes_office, self.mark, self.addtime, self.agency_num,
                self.agency_name, self.batch)

class Tyc_jyfx_xzcf(Base):
    '''
        行政处罚表 tyc_jyfx_xzcf
    '''
    __tablename__ = 'tyc_jyfx_xzcf'
    
    id = Column(NUMBER(24), primary_key=True)
    txt_id = Column(VARCHAR2(150))
    ent_name = Column(VARCHAR2(150))
    decision_date = Column(VARCHAR2(90))
    decision_number = Column(VARCHAR2(150))
    type = Column(VARCHAR2(1500))
    decision_department = Column(VARCHAR2(90))
    detail_info = Column(CLOB)
    punishment_name = Column(VARCHAR2(900))
    punishment_area = Column(VARCHAR2(300))
    mark = Column(NUMBER(3), default=0)
    add_time = Column(DATE)
    agency_num = Column(VARCHAR2(300))
    agency_name = Column(VARCHAR2(300))
    batch = Column(VARCHAR2(150))
    
    def __repr__(self):
        return "('id:%d', 'txt_id:%s', 'ent_name:%s', 'decision_date:%s', 'decision_number:%s', 'type:%s', \
                'decision_department:%s', 'detail_info:%s', 'punishment_name:%s', 'punishment_area:%s', \
                 'mark:%d', 'add_time:%s', 'agency_num:%s', 'agency_name:%s', 'batch:%s')" % \
               (self.id, self.txt_id, self.ent_name, self.decision_date, self.decision_number, self.type,
                self.decision_department, self.detail_info, self.punishment_name, self.punishment_area,
                self.mark, self.add_time, self.agency_num, self.agency_name, self.batch)

class Tyc_jyfx_yzwf(Base):
    '''
        严重违法表 tyc_jyfx_yzwf
    '''
    __tablename__ = 'tyc_jyfx_yzwf'
    
    id = Column(NUMBER(20), primary_key=True)
    txt_id = Column(VARCHAR2(100))
    ent_name = Column(VARCHAR2(100))
    illegal_date = Column(DATE(30))
    illegal_reason = Column(VARCHAR2(1000))
    office = Column(VARCHAR2(200))
    mark = Column(NUMBER(4), default=0)
    addtime = Column(DATE(0))
    agency_num = Column(VARCHAR2(100))
    agency_name = Column(VARCHAR2(100))
    batch = Column(VARCHAR2(10))
    
    def __repr__(self):
        return "('id:%d', 'txt_id:%s', 'ent_name:%s', 'illegal_dat:%s', 'illegal_reason:%s', 'office:%s', \
                'mark:%d', 'addtime:%s', 'agency_num:%s', 'agency_name:%s', 'batch:%s')" % \
               (self.id, self.txt_id, self.ent_name, self.illegal_date, self.illegal_reason, self.office,
                self.mark, self.addtime, self.agency_num, self.agency_name, self.batch)

class Tyc_jyzk_ccjc(Base):
    '''
        抽查检查表 tyc_jyzk_ccjc
    '''
    __tablename__ = 'tyc_jyzk_ccjc'
    
    id = Column(NUMBER(24), primary_key=True)
    # mongodb文本ID
    txt_id = Column(VARCHAR2(150))
    # 所属公司名称
    ent_name = Column(VARCHAR2(150))
    # 日期
    register_date = Column(VARCHAR2(90))
    # 类型
    company_type = Column(VARCHAR2(60))
    # 结果
    result = Column(VARCHAR2(300))
    # 检查实施机关
    check_department = Column(VARCHAR2(90))
    # 标记号
    mark = Column(NUMBER(3), default=0)
    # 添加时间
    add_time = Column(DATE)
    # 机构号
    agency_num = Column(VARCHAR2(300))
    # 机构名称
    agency_name = Column(VARCHAR2(300))
    # 批次
    batch = Column(VARCHAR2(150))
    
    def __repr__(self):
        return "(id:%d', 'txt_id:%s', 'ent_name:%s', 'register_date:%s', 'company_type:%s', 'result:%s',\
                'check_department:%s', mark:%d', 'add_ime:%s', 'agency_num:%s',\
                'agency_name:%s', 'batch:%s')" % \
               (self.id, self.txt_id, self.ent_name, self.register_date, self.company_type, self.result,
                self.check_department, self.mark, self.add_time, self.agency_num, self.agency_name, self.batch)

class Tyc_jyzk_cpxx(Base):
    '''
        产品信息表 tyc_jyzk_cpxx
    '''
    __tablename__ = 'tyc_jyzk_cpxx'
    
    id = Column(NUMBER(24), primary_key=True)
    # mongodb文本ID
    txt_id = Column(VARCHAR2(150))
    # 所属公司名称
    ent_name = Column(VARCHAR2(150))
    # 产品名称
    product_name = Column(VARCHAR2(150))
    # 产品简称
    product_referred = Column(VARCHAR2(150))
    # 产品分类
    product_classification = Column(VARCHAR2(60))
    # 领域
    field = Column(VARCHAR2(60))
    # 详情
    detail_info = Column(CLOB)
    # 标记号
    mark = Column(NUMBER(3), default=0)
    # 添加时间
    add_time = Column(DATE)
    # 机构号
    agency_num = Column(VARCHAR2(300))
    # 机构名称
    agency_name = Column(VARCHAR2(300))
    # 批次
    batch = Column(VARCHAR2(150))
    
    def __repr__(self):
        return "(id:%d', 'txt_id:%s', 'ent_name:%s', 'product_name:%s', 'product_referred:%s', \
                'product_classification:%s', 'field:%s', 'detail_info:%s', mark:%d', 'add_time:%s',\
                'agency_num:%s', 'agency_name:%s', 'batch:%s')" % \
               (self.id, self.txt_id, self.ent_name, self.product_name, self.product_referred,
                self.product_classification, self.field, self.detail_info, self.mark, self.add_time,
                self.agency_num, self.agency_name, self.batch)

class Tyc_jyzk_gdxx(Base):
    '''
        购地信息表
        tyc_jyzk_gdxx
    '''
    __tablename__ = 'tyc_jyzk_gdxx'
    
    id = Column(NUMBER(24), primary_key=True)
    txt_id = Column(VARCHAR2(300))
    ent_name = Column(VARCHAR2(300))
    gd_sign_date = Column(VARCHAR2(90))
    gd_num = Column(VARCHAR2(300))
    gd_act_date = Column(VARCHAR2(90))
    gd_area = Column(VARCHAR2(300))
    gd_region = Column(VARCHAR2(300))
    gd_operate = Column(VARCHAR2(300))
    mark = Column(NUMBER(4), default=0)
    addtime = Column(DATE)
    agency_num = Column(VARCHAR2(300))
    agency_name = Column(VARCHAR2(300))
    batch = Column(VARCHAR2(150))
    
    def __repr__(self):
        return "('id:%d', 'txt_id:%s', 'ent_name:%s', 'gd_sign_date:%s', ' gd_num:%s', 'gd_act_date:%s', \
                'gd_area:%s', gd_region:%s', ' gd_operate:%s', mark:%d', 'addtime:%s', \
                'agency_num:%s', 'agency_name:%s', 'batch:%s')" % \
               (self.id, self.txt_id, self.ent_name, self.gd_sign_date, self.gd_num, self.gd_act_date,
                self.gd_area, self.gd_region, self.gd_operate, self.mark, self.addtime, self.agency_num,
                self.agency_name, self.batch)

class Tyc_jyzk_jckxy(Base):
    '''
        进出口信用表 tyc_jyzk_jckxy
    '''
    __tablename__ = 'tyc_jyzk_jckxy'
    
    id = Column(NUMBER(24), primary_key=True)
    txt_id = Column(VARCHAR2(150))
    ent_name = Column(VARCHAR2(150))
    register_customs = Column(VARCHAR2(90))
    customs_number = Column(VARCHAR2(150))
    manger_type = Column(VARCHAR2(150))
    detail_info = Column(CLOB)
    mark = Column(NUMBER(3), default=0)
    addtime = Column(DATE)
    agency_num = Column(VARCHAR2(300))
    agency_name = Column(VARCHAR2(300))
    batch = Column(VARCHAR2(150))
    
    def __repr__(self):
        return "('id:%d', 'txt_id:%s', 'ent_name:%s', 'register_customs:%s', 'customs_number:%s', 'manger_type:%s',\
                ' detail_info:%s', 'mark:%d', 'addtime:%s', 'agency_num:%s','agency_name:%s', 'batch:%s')" % \
               (self.id, self.txt_id, self.ent_name, self.register_customs, self.customs_number, self.manger_type,
                self.detail_info, self.mark, self.addtime, self.agency_num, self.agency_name, self.batch)

class Tyc_jyzk_swpj(Base):
    '''
        税务评级表 tyc_jyzk_swpj
    '''
    __tablename__ = 'tyc_jyzk_swpj'
    
    id = Column(NUMBER(24), primary_key=True)
    # mongodb文本ID
    txt_id = Column(VARCHAR2(150))
    # 所属公司名称
    ent_name = Column(VARCHAR2(150))
    # 年份
    year = Column(VARCHAR2(30))
    # 纳税评级
    tax_rating = Column(VARCHAR2(30))
    # 类型
    tax_type = Column(VARCHAR2(30))
    # 纳税人识别号
    tax_identification_number = Column(VARCHAR2(300))
    # 评价单位
    evaluate_department = Column(VARCHAR2(150))
    # 标记号
    mark = Column(NUMBER(3), default=0)
    # 添加时间
    add_time = Column(DATE)
    # 机构号
    agency_num = Column(VARCHAR2(300))
    # 机构名称
    agency_name = Column(VARCHAR2(300))
    # 批次
    batch = Column(VARCHAR2(150))
    
    def __repr__(self):
        return "('id:%d', 'txt_id:%s', 'ent_name:%s', 'year:%s', 'tax_rating:%s', 'tax_type:%s', \
                'tax_identification_number:%s', 'evaluate_department:%s', mark:%d', 'add_time:%s',\
                'agency_num:%s', 'agency_name:%s', 'batch:%s')" % \
               (self.id, self.txt_id, self.ent_name, self.year, self.tax_rating, self.tax_type,
                self.tax_identification_number, self.evaluate_department, self.mark, self.add_time,
                self.agency_num, self.agency_name, self.batch)

class Tyc_jyzk_wxgzh(Base):
    '''
     微信公众号表 tyc_jyzk_wxgzh
    '''
    __tablename__ = 'tyc_jyzk_wxgzh'
    
    id = Column(NUMBER(24), primary_key=True)
    txt_id = Column(VARCHAR2(150))
    ent_name = Column(VARCHAR2(150))
    mp_name = Column(VARCHAR2(90))
    mp_number = Column(VARCHAR2(150))
    mp_info = Column(CLOB)
    mark = Column(NUMBER(3), default=0)
    addtime = Column(DATE)
    agency_num = Column(VARCHAR2(300))
    agency_name = Column(VARCHAR2(300))
    batch = Column(VARCHAR2(150))
    
    def __repr__(self):
        return "('id:%d', 'txt_id:%s', 'ent_name:%s', 'mp_name:%s', 'mp_number:%s', 'mp_info:%s',\
                'mark:%d', 'addtime:%s', 'agency_num:%s','agency_name:%s', 'batch:%s')" % \
               (self.id, self.txt_id, self.ent_name, self.mp_name, self.mp_number, self.mp_info,
                self.mark, self.addtime, self.agency_num, self.agency_name, self.batch)

class Tyc_jyzk_zp(Base):
    '''
     招聘表 tyc_jyzk_zp
    '''
    __tablename__ = 'tyc_jyzk_zp'
    
    id = Column(NUMBER(24), primary_key=True)
    # mongodb文本ID
    txt_id = Column(VARCHAR2(150))
    # 所属公司名称
    ent_name = Column(VARCHAR2(150))
    # 发布时间
    publish_date = Column(VARCHAR2(90))
    # 招聘职位
    recruitment_job = Column(VARCHAR2(300))
    # 薪资
    salary = Column(VARCHAR2(300))
    # 工作经验
    work_year = Column(VARCHAR2(150))
    # 招聘人数
    recruitment_numbers = Column(VARCHAR2(30))
    # 所在城市
    work_city = Column(VARCHAR2(30))
    # 详情
    detail_info = Column(CLOB)
    # 标记号
    mark = Column(NUMBER(3), default=0)
    # 添加时间
    add_time = Column(DATE)
    # 机构号
    agency_num = Column(VARCHAR2(300))
    # 机构名称
    agency_name = Column(VARCHAR2(300))
    # 批次
    batch = Column(VARCHAR2(150))
    
    def __repr__(self):
        return "('id:%d', 'txt_id:%s', 'ent_name:%s', 'publish_date:%s', 'recruitment_job:%s' , 'salary:%s',\
                'work_year:%s', 'recruitment_numbers:%s', 'work_city:%s', 'detail_info:%s', mark:%d', 'add_time:%s', \
                'agency_num:%s', 'agency_name:%s', 'batch:%s')" % \
               (self.id, self.txt_id, self.ent_name, self.publish_date, self.recruitment_job, self.salary,
                self.work_year, self.recruitment_numbers, self.work_city, self.detail_info, self.mark,
                self.add_time, self.agency_num, self.agency_name, self.batch)

class Tyc_jyzk_zqxx(Base):
    '''
        债券信息表
        tyc_jyzk_zqxx
    '''
    __tablename__ = 'tyc_jyzk_zqxx'
    
    id = Column(NUMBER(24), primary_key=True)
    txt_id = Column(VARCHAR2(150))
    ent_name = Column(VARCHAR2(300))
    publish_date = Column(VARCHAR2(90))
    bond_name = Column(VARCHAR2(150))
    bond_code = Column(VARCHAR2(150))
    bond_type = Column(VARCHAR2(90))
    latest_rating = Column(VARCHAR2(90))
    detail_info = Column(CLOB)
    mark = Column(NUMBER(3), default=0)
    add_time = Column(DATE)
    agency_num = Column(VARCHAR2(300))
    agency_name = Column(VARCHAR2(300))
    batch = Column(VARCHAR2(150))
    
    def __repr__(self):
        return "('id:%d', 'txt_id:%s', 'ent_name:%s', 'publish_date:%s', 'bond_name:%s', 'bond_code:%s', \
                'bond_type:%s', 'latest_rating:%s', 'detail_info:%s', mark:%d', 'add_time:%s', \
                'agency_num:%s', 'agency_name:%s', 'batch:%s')" % \
               (self.id, self.txt_id, self.ent_name, self.publish_date, self.bond_name, self.bond_code,
                self.bond_type, self.latest_rating, self.detail_info, self.mark, self.add_time,
                self.agency_num, self.agency_name, self.batch)

class Tyc_jyzk_ztb(Base):
    '''
        招投标表
        tyc_jyzk_ztb
    '''
    __tablename__ = 'tyc_jyzk_ztb'
    
    id = Column(NUMBER(24), primary_key=True)
    # mongodb文本ID
    txt_id = Column(VARCHAR2(150))
    # 所属公司名称
    ent_name = Column(VARCHAR2(150))
    # 发布时间
    publish_date = Column(VARCHAR2(90))
    # 标题
    title = Column(VARCHAR2(1500))
    # 标题url
    title_url = Column(VARCHAR2(150))
    # 采购人
    procurement = Column(VARCHAR2(1500))
    # 标记号
    mark = Column(NUMBER(3), default=0)
    # 添加时间
    add_time = Column(DATE)
    # 机构号
    agency_num = Column(VARCHAR2(300))
    # 机构名称
    agency_name = Column(VARCHAR2(300))
    # 批次
    batch = Column(VARCHAR2(150))
    
    def __repr__(self):
        return "('id:%d', 'txt_id:%s', 'ent_name:%s', 'publish_date:%s', 'title:%s', 'title_url:%s', \
                'procurement:%s', mark:%d', 'add_time:%s', 'agency_num:%s', 'agency_name:%s', 'batch:%s')" % \
               (self.id, self.txt_id, self.ent_name, self.publish_date, self.title, self.title_url,
                self.procurement, self.mark, self.add_time, self.agency_num, self.agency_name, self.batch)

class Tyc_jyzk_zzzs(Base):
    '''
        资质证书表 tyc_jyzk_zzzs
    '''
    __tablename__ = 'tyc_jyzk_zzzs'
    
    id = Column(NUMBER(24), primary_key=True)
    txt_id = Column(VARCHAR2(300))
    ent_name = Column(VARCHAR2(300))
    certificate_num = Column(VARCHAR2(300))
    certificate_type = Column(VARCHAR2(300))
    send_date = Column(VARCHAR2(90))
    off_date = Column(VARCHAR2(90))
    mark = Column(NUMBER(4), default=0)
    addtime = Column(DATE)
    agency_num = Column(VARCHAR2(300))
    agency_name = Column(VARCHAR2(300))
    batch = Column(VARCHAR2(150))
    
    def __repr__(self):
        return "(id:%d', 'txt_id:%s', 'ent_name:%s', 'certificate_num:%s', 'certificate_type:%s', \
                 'send_date:%s', 'off_date:%s', mark:%d', 'addtime:%s', 'agency_num:%s', \
                'agency_name:%s', 'batch:%s')" % \
               (self.id, self.txt_id, self.ent_name, self.certificate_num, self.certificate_type,
                self.send_date, self.off_date, self.mark, self.addtime, self.agency_num,
                self.agency_name, self.batch)

class Tyc_qybj_bgjl(Base):
    '''
        企业背景-->变更记录 tyc_qybj_bgjl
    '''
    __tablename__ = 'tyc_qybj_bgjl'
    
    # 主键(自增)
    id = Column(NUMBER(30), primary_key=True)
    # mongodb文本ID
    txt_id = Column(VARCHAR2(300))
    # 所属公司名称
    ent_name = Column(VARCHAR2(300))
    # 变更时间
    alter_date = Column(VARCHAR2(150))
    # 变更项目
    alter_project = Column(VARCHAR2(300))
    # 变更前
    alter_befor = Column(CLOB)
    # 变更后
    alter_after = Column(CLOB)
    # 标记号
    mark = Column(NUMBER(4), default=0)
    # 添加时间
    addtime = Column(DATE)
    # 机构号
    agency_num = Column(VARCHAR2(300))
    # 机构名称
    agency_name = Column(VARCHAR2(300))
    # 批次
    batch = Column(VARCHAR2(150))
    
    def __repr__(self):
        return "('id:%d', 'txt_id:%s', 'ent_name:%s', 'alter_data:%s', 'alter_project:%s', \
                'alter_befor:%s', 'alter_after:%s', 'mark:%d', 'addtime:%s', 'agency_num:%s',\
                'agency_name:%s', 'batch:%s')" % \
               (self.id, self.txt_id, self.ent_name, self.alter_date, self.alter_project, self.alter_befor,
                self.alter_after, self.mark, self.addtime, self.agency_num, self.agency_name, self.batch)

class Tyc_qybj_dwtz(Base):
    '''
        对外投资表 tyc_qybj_dwtz
    '''
    __tablename__ = 'tyc_qybj_dwtz'
    
    # 主键(自增)
    id = Column(NUMBER(24), primary_key=True)
    # mongodb文本ID
    txt_id = Column(VARCHAR2(300))
    # 所属公司名称
    ent_name = Column(VARCHAR2(300))
    # 被投资企业名称
    invest_company = Column(VARCHAR2(300))
    # 被投资法定代表人
    invest_person = Column(VARCHAR2(300))
    # 注册资本
    invest_fund = Column(VARCHAR2(300))
    # 投资数额
    invest_amount = Column(VARCHAR2(300))
    # 投资占比
    invest_ratio = Column(VARCHAR2(300))
    # 注册时间
    invest_date = Column(VARCHAR2(300))
    # 状态
    invest_status = Column(VARCHAR2(300))
    # 标记号
    mark = Column(NUMBER(4), default=0)
    # 添加时间
    addtime = Column(DATE)
    # 机构号
    agency_num = Column(VARCHAR2(300))
    # 机构名称
    agency_name = Column(VARCHAR2(300))
    # 批次
    batch = Column(VARCHAR2(150))
    
    def __repr__(self):
        return "('id:%d', 'txt_id:%s', 'ent_name:%s', invest_company:%s', 'invest_person:%s', 'invest_fund:%s'\
                'invest_fund:%s', 'invest_amount:%s', 'invest_ratio:%s', 'invest_date:%s',\
                 'invest_status:%s', 'mark:%d', 'addtime:%s', 'agency_num:%s', 'agency_name:%s',\
                 'batch:%s')" % \
               (self.id, self.txt_id, self.ent_name, self.invest_company, self.invest_person, self.invest_fund,
                self.invest_fund,
                self.invest_amount, self.invest_ratio, self.invest_date, self.invest_status, self.mark,
                self.addtime, self.agency_num, self.agency_name, self.batch)

class Tyc_qybj_fzjg(Base):
    '''
        企业背景-->分支机构 tyc_qybj_fzjg
    '''
    __tablename__ = 'tyc_qybj_fzjg'
    
    # 主键(自增)
    id = Column(NUMBER(24), primary_key=True)
    # mongodb文本ID
    txt_id = Column(VARCHAR2(300))
    # 所属公司名称
    ent_name = Column(VARCHAR2(300))
    # 企业名称
    company_name = Column(VARCHAR2(600))
    # 法定代表人
    legal_representative = Column(VARCHAR2(300))
    # 状态
    status = Column(VARCHAR2(300))
    # 注册时间
    registered_date = Column(VARCHAR2(300))
    # 标记号
    mark = Column(NUMBER(4), default=0)
    # 添加时间
    add_time = Column(DATE)
    # 机构号
    agency_num = Column(VARCHAR2(300))
    # 机构名称
    agency_name = Column(VARCHAR2(300))
    # 批次
    batch = Column(VARCHAR2(150))
    
    def __repr__(self):
        return "('id:%d', 'txt_id:%s', 'ent_name:%s', 'company_name:%s', 'legal_representative:%s', \
                'status:%s', 'registered_date:%s', 'mark:%d', 'add_time:%d', 'agency_num:%s', \
                'agency_name:%s', 'batch:%s')" % \
               (self.id, self.txt_id, self.ent_name, self.company_name, self.legal_representative,
                self.status, self.registered_date, self.mark, self.add_time, self.agency_num,
                self.agency_name, self.batch)

class Tyc_qybj_gdxx(Base):
    '''
        企业背景-->股东信息  tyc_qybj_gdxx
    '''
    __tablename__ = 'tyc_qybj_gdxx'
    
    # 主键(自增)
    id = Column(NUMBER(24), primary_key=True)
    # mongodb文本ID
    txt_id = Column(VARCHAR2(300))
    # 所属公司名称
    ent_name = Column(VARCHAR2(300))
    # 股东
    shareholder = Column(VARCHAR2(300))
    # 出资比例
    fund_ratio = Column(VARCHAR2(300))
    # 认缴出资
    fund_subcribe = Column(VARCHAR2(300))
    # 标记号
    mark = Column(NUMBER(4), default=0)
    # 添加时间
    addtime = Column(VARCHAR2(300))
    # 机构号
    agency_num = Column(VARCHAR2(300))
    # 机构名称
    agency_name = Column(VARCHAR2(300))
    # 批次
    batch = Column(VARCHAR2(150))
    
    def __repr__(self):
        return "('id:%d', 'txt_id:%s', 'ent_name:%s', 'shareholder:%s', 'fund_ration:%s', 'fund_subcribe:%s', \
                'mark:%d', 'addtime:%s', 'agency_num:%s', 'agency_name:%s', 'batch:%s')" % \
               (self.id, self.txt_id, self.ent_name, self.shareholder, self.fund_ratio, self.fund_subcribe,
                self.mark, self.addtime, self.agency_num, self.agency_name, self.batch)

class TycQybjJbxx(Base):
    '''
       企业背景-->基本信息 tyc_qybj_jbxx
    '''
    __tablename__ = 'tyc_qybj_jbxx'
    
    # 主键(自增)
    id = Column(NUMBER(24), primary_key=True)
    # mongodb文本ID
    txt_id = Column(VARCHAR2(300))
    # 所属公司名称
    ent_name = Column(VARCHAR2(300))
    # 工商注册号
    register_num = Column(VARCHAR2(300))
    # 组织机构代码
    tissue_num = Column(VARCHAR2(300))
    # 统一信用代码
    credit_num = Column(VARCHAR2(300))
    # 企业类型
    company_type = Column(VARCHAR2(300))
    # 纳税人识别号
    taxpayer_num = Column(VARCHAR2(300))
    # 行业
    industry = Column(VARCHAR2(300))
    # 营业期限
    business_term = Column(VARCHAR2(300))
    # 核准日期
    check_date = Column(VARCHAR2(300))
    # 登记机关
    register_office = Column(VARCHAR2(300))
    # 注册地址
    register_site = Column(VARCHAR2(300))
    # 注册资本
    register_fund = Column(VARCHAR2(300))
    # 注册时间
    register_date = Column(VARCHAR2(300))
    # 企业状态
    company_status = Column(VARCHAR2(300))
    # 经营范围
    business_scope = Column(CLOB)
    # 电话
    telephone = Column(VARCHAR2(150))
    # 邮箱
    email = Column(VARCHAR2(300))
    # 网址
    url = Column(VARCHAR2(1500))
    # 英文名称
    english_name = Column(VARCHAR2(300))
    # 标记号
    mark = Column(NUMBER(4), default=0)
    # 添加时间
    addtime = Column(DATE)
    # 机构号
    agency_num = Column(VARCHAR2(300))
    # 机构名称
    agency_name = Column(VARCHAR2(300))
    # 批次
    batch = Column(VARCHAR2(150))
    # 四级行业
    industry_4 = Column(VARCHAR2(150))
    # 银行分支机构号
    branch = Column(VARCHAR2(20))
    
    def __repr__(self):
        return "('id:%d', 'txt_id:%s', 'ent_name:%s', 'register_num:%s', 'tissue_num:%s', 'credit_num:%s', 'company_type:%s',  \
               'taxpayer_num:%s', 'industry:%s', 'business_term:%s', 'check_date:%s', 'register_office:%s', 'register_site:%s', \
               'register_fund:%s', 'register_date:%s', 'company_status:%s', 'business_scope:%s', 'telephone:%s', 'email:%s', \
               'url:%s', 'english_name:%s', 'mark:%d', 'addtime:%s', 'agency_num:%s', 'agency_name:%s', 'batch:%s', 'industry_4:%s', \
               'branch:%s')" % \
               (self.id, self.txt_id, self.ent_name, self.register_num, self.tissue_num, self.credit_num,
                self.company_type, self.taxpayer_num,
                self.industry, self.business_term, self.check_date, self.register_office, self.register_site,
                self.register_fund, self.register_date,
                self.company_status, self.business_scope, self.telephone, self.email, self.url, self.english_name,
                self.mark, self.addtime, self.agency_num,
                self.agency_name, self.batch, self.industry_4, self.branch)

class Tyc_qybj_qynb(Base):
    '''
        企业年报 tyc_qybj_qynb
    '''
    __tablename__ = 'tyc_qybj_qynb'
    
    id = Column(NUMBER(24), primary_key=True)
    txt_id = Column(VARCHAR2(300))
    ent_name = Column(VARCHAR2(300))
    detail_url = Column(VARCHAR2(300))
    year = Column(VARCHAR2(60))
    mark = Column(NUMBER(3), default=0)
    add_time = Column(DATE)
    agency_num = Column(VARCHAR2(300))
    agency_name = Column(VARCHAR2(300))
    batch = Column(VARCHAR2(150))
    
    def __repr__(self):
        return "('id:%d', 'txt_id:%s', 'ent_name:%s', 'detail_url:%s', \
                'year:%s', 'mark:%d', ''add_time:%s', 'agency_num:%s', \
                'agency_name:%s', 'batch:%s')" % \
               (self.id, self.txt_id, self.ent_name, self.detail_url,
                self.year, self.mark, self.add_time, self.agency_num,
                self.agency_name, self.batch)

class Tyc_qybj_zyry(Base):
    '''
        企业背景-->主要人员 tyc_qybj_zyry
    '''
    __tablename__ = 'tyc_qybj_zyry'
    
    # 主键（自增）
    id = Column(NUMBER(24), primary_key=True)
    # mongodb文本ID
    txt_id = Column(VARCHAR2(300))
    # 所属公司名称
    ent_name = Column(VARCHAR2(300))
    # 职位
    position = Column(VARCHAR2(300))
    # 姓名
    name = Column(VARCHAR2(300))
    # 标记号
    mark = Column(NUMBER(4), default=0)
    # 添加时间
    addtime = Column(DATE)
    # 机构号
    agency_num = Column(VARCHAR2(300))
    # 机构名称
    agency_name = Column(VARCHAR2(300))
    # 批次
    batch = Column(VARCHAR2(150))
    
    def __repr__(self):
        return "('id:%d', 'txt_id:%s', 'ent_name:%s', 'position:%s', 'name:%s', 'mark:%d', \
               'addtime:%s', 'agency_num:%s', 'agency_name:%s', 'batch:%s',)" % \
               (self.id, self.txt_id, self.ent_name, self.position, self.name, self.mark,
                self.addtime, self.agency_num, self.agency_name, self.batch)

class Tyc_qyfz_hxtd(Base):
    '''
        tyc_qyfz_hxtd tyc_qyfz_hxtd
    '''
    __tablename__ = 'tyc_qyfz_hxtd'
    
    # 主键(自增)
    id = Column(NUMBER(24), primary_key=True)
    # mongodb文本ID
    txt_id = Column(VARCHAR2(300))
    # 所属公司名称
    ent_name = Column(VARCHAR2(300))
    # 人物名称
    person_name = Column(VARCHAR2(150))
    # 人物介绍
    person_info = Column(CLOB)
    # 标记号
    mark = Column(NUMBER(4), default=0)
    # 添加时间
    addtime = Column(DATE)
    # 机构号
    agency_num = Column(VARCHAR2(300))
    # 机构名称
    agency_name = Column(VARCHAR2(300))
    # 批次
    batch = Column(VARCHAR2(150))
    
    def __repr__(self):
        return "('id:%d', 'txt_id:%s', 'ent_name:%s' , 'person_name:%s', \
                'person_info:%s', 'mark:%d', 'addtime:%s', 'agency_num:%s', \
                'agency_name:%s', 'batch:%s')" % \
               (self.id, self.txt_id, self.ent_name, self.person_name,
                self.person_info, self.mark, self.addtime, self.agency_num,
                self.agency_name, self.batch)

class Tyc_qyfz_jpxx(Base):
    '''
        企业发展-->竞品信息表 tyc_qyfz_jpxx
    '''
    __tablename__ = 'tyc_qyfz_jpxx'
    
    id = Column(NUMBER(24), primary_key=True)
    # mongodb文本ID
    txt_id = Column(VARCHAR2(300))
    # 所属公司名称
    ent_name = Column(VARCHAR2(300))
    # 产品
    jp_product = Column(VARCHAR2(150))
    # 地区
    jp_area = Column(VARCHAR2(300))
    # 当前轮次
    jp_round = Column(VARCHAR2(150))
    # 行业
    jp_industry = Column(VARCHAR2(150))
    # 业务
    jp_business = Column(VARCHAR2(1500))
    # 成立时间
    jp_date = Column(VARCHAR2(150))
    # 估值
    jp_value = Column(VARCHAR2(150))
    # 标记号
    mark = Column(NUMBER(4), default=0)
    # 添加时间
    addtime = Column(DATE)
    # 机构号
    agency_num = Column(VARCHAR2(300))
    # 机构名称
    agency_name = Column(VARCHAR2(300))
    # 批次
    batch = Column(VARCHAR2(150))
    
    def __repr__(self):
        return "('id:%d', 'txt_id:%s', 'ent_name:%s', 'jp_product:%s', 'jp_area:%s', \
                'jp_round:%s', 'jp_industry:%s', 'jp_business:%s', 'jp_date:%s', 'jp_value:%s', \
                'mark:%s', 'addtime:%s', 'agency_num:%s', 'agency_name:%s', 'batch:%s')" % \
               (self.id, self.txt_id, self.ent_name, self.jp_product, self.jp_area, self.jp_round,
                self.jp_industry, self.jp_business, self.jp_date, self.jp_value, self.mark, self.addtime,
                self.agency_num, self.agency_name, self.batch)

class Tyc_qyfz_qyyw(Base):
    '''
        企业发展-->企业业务 tyc_qyfz_qyyw
    '''
    __tablename__ = 'tyc_qyfz_qyyw'
    
    # 主键(自增)
    id = Column(NUMBER(24), primary_key=True)
    # mongodb文本ID
    txt_id = Column(VARCHAR2(300))
    # 所属公司名称
    ent_name = Column(VARCHAR2(300))
    # 业务名称
    business_name = Column(VARCHAR2(150))
    # 业务性质
    business_quale = Column(VARCHAR2(150))
    # 业务简介
    business_info = Column(VARCHAR2(600))
    # 标记号
    mark = Column(NUMBER(3), default=0)
    # 添加时间
    addtime = Column(DATE)
    # 机构号
    agency_num = Column(VARCHAR2(300))
    # 机构名称
    agency_name = Column(VARCHAR2(300))
    # 批次
    batch = Column(VARCHAR2(150))
    
    def __repr__(self):
        return "('id:%d', 'txt_id:%s', 'ent_name:%s', 'business_name:%s', \
                'business_quale:%s', 'business_info:%s', 'mark:%d', 'addtime:%s',\
                'agency_num:%s', 'agency_name:%s', 'batch:%s')" % \
               (self.id, self.txt_id, self.ent_name, self.business_name, self.business_quale,
                self.business_quale, self.mark, self.addtime, self.agency_num, self.agency_name, self.batch)

class Tyc_qyfz_rzls(Base):
    '''
        企业发展-->融资历史 tyc_qyfz_rzls
    '''
    __tablename__ = 'tyc_qyfz_rzls'
    
    # 主键
    id = Column(NUMBER(24), primary_key=True)
    # # mongodb文本ID
    txt_id = Column(VARCHAR2(300))
    # 所属公司名称
    ent_name = Column(VARCHAR2(300))
    # 时间
    finance_date = Column(VARCHAR2(150))
    # 轮次
    finance_round = Column(VARCHAR2(150))
    # 估值
    finance_value = Column(VARCHAR2(150))
    # 金额
    finance_money = Column(VARCHAR2(150))
    # 比例
    finance_ratio = Column(VARCHAR2(150))
    # 投资方
    finance_investor = Column(VARCHAR2(150))
    # 新闻来源
    finance_source = Column(VARCHAR2(150))
    # 标记号
    mark = Column(NUMBER(4), default=0)
    # 添加时间
    addtime = Column(DATE)
    # 机构号
    agency_num = Column(VARCHAR2(300))
    # 机构名称
    agency_name = Column(VARCHAR2(300))
    # 批次
    batch = Column(VARCHAR2(150))
    
    def __repr__(self):
        return "('id:%d', 'txt_id:%s', 'ent_name:%s', 'finance_date:%s', 'finance_round:%s', \
                'finance_value:%s', 'finance_money:%s', 'finance_ratio:%s', 'finance_investor:%s', \
                'finance_spurce:%s', 'mark:%d', 'addtime:%s', 'agency_num:%s', 'agency_name:%s', 'bathc:%s')" % \
               (self.id, self.txt_id, self.ent_name, self.finance_date, self.finance_round, self.finance_value,
                self.finance_money, self.finance_ratio, self.finance_investor, self.finance_source, self.mark,
                self.addtime, self.agency_num, self.agency_name, self.batch)

class Tyc_qyfz_tzsj(Base):
    '''
        企业发展-->投资事件表 tyc_qyfz_tzsj
    '''
    __tablename__ = 'tyc_qyfz_tzsj'
    
    # 主键(自增)
    id = Column(NUMBER(24), primary_key=True)
    # mongodb文本ID
    txt_id = Column(VARCHAR2(300))
    # 所属公司名称
    ent_name = Column(VARCHAR2(300))
    # 时间
    touzi_date = Column(VARCHAR2(150))
    # 轮次
    touzi_round = Column(VARCHAR2(150))
    # 金额
    touzi_money = Column(VARCHAR2(150))
    # 投资方
    touzi_ent = Column(VARCHAR2(1500))
    # 产品
    touzi_product = Column(VARCHAR2(150))
    # 地区
    touzi_area = Column(VARCHAR2(150))
    # 行业
    touzi_industry = Column(VARCHAR2(150))
    # 业务
    touzi_business = Column(VARCHAR2(1500))
    # 标记号
    mark = Column(NUMBER(4), default=0)
    # 添加时间
    addtime = Column(DATE)
    # 机构号
    agency_num = Column(VARCHAR2(300))
    # 机构名称
    agency_name = Column(VARCHAR2(300))
    # 批次
    batch = Column(VARCHAR2(150))
    
    def __repr__(self):
        return "('id:%d', 'txt_id:%s', 'ent_name:%s', 'touzi_date:%s', 'touzi_round:%s', 'touzi_money:%s', \
                'touzi_ent:%s', 'touzi_product:%s', 'touzi_area:%s', 'touzi_industry:%s', 'touzi_business:%s', \
                'mark:%d', 'addtime:%s', 'agency_num:%s', 'agency_name:%s', 'batch:%s')" % \
               (self.id, self.txt_id, self.ent_name, self.touzi_date, self.touzi_round, self.touzi_money,
                self.touzi_ent, self.touzi_product, self.touzi_area, self.touzi_industry, self.touzi_business,
                self.mark, self.addtime, self.agency_num, self.agency_name, self.batch)

class Tyc_sffx_bzxr(Base):
    '''
        被执行人表 tyc_sffx_bzxr
    '''
    __tablename__ = 'tyc_sffx_bzxr'
    
    id = Column(NUMBER(24), primary_key=True)
    # mongodb文本ID
    txt_id = Column(VARCHAR2(150))
    # 所属公司名称
    ent_name = Column(VARCHAR2(150))
    # 立案日期
    record_date = Column(VARCHAR2(90))
    # 执行标的
    execute_underlying = Column(VARCHAR2(30))
    # 案号
    case_number = Column(VARCHAR2(150))
    # 法院
    court = Column(VARCHAR2(150))
    # 标记号
    mark = Column(NUMBER(3), default=0)
    # 添加时间
    add_time = Column(DATE)
    # 机构号
    agency_num = Column(VARCHAR2(300))
    # 机构名称
    agency_name = Column(VARCHAR2(300))
    # 批次
    batch = Column(VARCHAR2(150))
    
    def __repr__(self):
        return "('id:%d', 'txt_id:%s', 'ent_name:%s', 'record_date:%s', 'execute_underlying:%s', 'case_number:%s',\
                'court:%s', 'mark:%d', 'add_time:%s', 'agency_num:%s', 'agency_name:%s', 'batch:%s')" % \
               (self.id, self.txt_id, self.ent_name, self.record_date, self.execute_underlying, self.case_number,
                self.court, self.mark, self.add_time, self.agency_num, self.agency_name, self.batch)

class Tyc_sffx_flss(Base):
    '''
        法律诉讼表 tyc_sffx_flss
    '''
    __tablename__ = 'tyc_sffx_flss'
    
    # 主键(自增)
    id = Column(NUMBER(24), primary_key=True)
    # mongodb文本ID
    txt_id = Column(VARCHAR2(150))
    # 所属公司名称
    ent_name = Column(VARCHAR2(150))
    # 日期
    judgment_date = Column(VARCHAR2(90))
    # 判决文书
    judgment_document = Column(CLOB)
    # 案件类型
    case_type = Column(VARCHAR2(60))
    # 案件身份
    case_identity = Column(VARCHAR2(300))
    # 案件号
    case_number = Column(VARCHAR2(150))
    # 文书连接
    document_url = Column(VARCHAR2(300))
    # 标记号
    mark = Column(NUMBER(3), default=0)
    # 判决书内容
    text_info = Column(CLOB)
    # 添加时间
    add_time = Column(DATE)
    detail_status = Column(NUMBER(3))
    # 机构号
    agency_num = Column(VARCHAR2(300))
    # 机构名称
    agency_name = Column(VARCHAR2(300))
    # 批次
    batch = Column(VARCHAR2(150))
    
    def __repr__(self):
        return "('id:%d', 'txt_id:%s', 'ent_name:%s', 'judgment_data:%s', 'judegment_documnet:%s',\
                'case_type:%s', 'case_identity:%s', 'case_number:%s', 'documnet_url:%s', 'mark:%d',\
                'text_info:%s', 'add_time:%s', 'detail_status:%s', 'agency_num:%s', 'agency_name:%s',\
                'batch:%s')" % \
               (self.id, self.txt_id, self.ent_name, self.judgment_date, self.judgment_document,
                self.case_type, self.case_identity, self.case_number, self.document_url, self.mark,
                self.text_info, self.add_time, self.detail_status, self.agency_num, self.agency_name,
                self.batch)

class Tyc_sffx_fygg(Base):
    '''
        法院公告表 tyc_sffx_fygg
    '''
    __tablename__ = 'tyc_sffx_fygg'
    
    id = Column(NUMBER(24), primary_key=True)
    # mongodb文本ID
    txt_id = Column(VARCHAR2(150))
    # 所属公司名称
    ent_name = Column(VARCHAR2(150))
    # 公告时间
    announcement_date = Column(VARCHAR2(90))
    # 上诉方
    plaintiff = Column(VARCHAR2(300))
    # 被诉方
    defendant = Column(VARCHAR2(3000))
    # 公告类型
    announcement_type = Column(VARCHAR2(150))
    # 法院
    court = Column(VARCHAR2(300))
    # 详情
    detail_info = Column(CLOB)
    # 标记号
    mark = Column(NUMBER(3), default=0)
    # 添加时间
    add_time = Column(DATE)
    # 机构号
    agency_num = Column(VARCHAR2(300))
    # 机构名称
    agency_name = Column(VARCHAR2(300))
    # 批次
    batch = Column(VARCHAR2(150))
    
    def __repr__(self):
        return "('id:%d', 'txt_id:%s', 'ent_name:%s', 'announcement_date:%s', 'plaintiff:%s', 'defendant:%s',\
                'announcement_type:%s', 'court:%s', 'detail:%s', 'mark:%d', 'add_time:%s', 'agency_num:%s', \
                'agency_name:%s', 'batch:%s')" % \
               (self.id, self.txt_id, self.ent_name, self.announcement_date, self.plaintiff, self.defendant,
                self.announcement_type, self.court, self.detail_info, self.mark, self.add_time, self.agency_num,
                self.agency_name, self.batch)

class Tyc_sffx_sxr(Base):
    '''
        失信人员表tyc_sffx_sxr
    '''
    __tablename__ = 'tyc_sffx_sxr'
    
    id = Column(NUMBER(24), primary_key=True)
    txt_id = Column(VARCHAR2(300))
    ent_name = Column(VARCHAR2(300))
    case_date = Column(VARCHAR2(60))
    case_number = Column(VARCHAR2(1500))
    execution_court = Column(VARCHAR2(300))
    performance_state = Column(VARCHAR2(30))
    execute_number = Column(VARCHAR2(300))
    detail_info = Column(CLOB)
    mark = Column(NUMBER(1), default=0)
    add_time = Column(DATE)
    agency_num = Column(VARCHAR2(300))
    agency_name = Column(VARCHAR2(300))
    batch = Column(VARCHAR2(150))
    
    def __repr__(self):
        return "('id:%d', 'txt_id:%s', 'ent_name:%s', 'case_date:%s', 'case_number:%s',\
                'exception_court:%s', 'performance:%s', 'execute_number:%s', 'detail_info:%s',\
                'mark:%d', 'add_time:%s', 'agency_num:%s', 'agency_name:%s', 'batch:%s')" % \
               (self.id, self.txt_id, self.ent_name, self.case_date, self.case_number, self.execution_court,
                self.performance_state, self.execute_number, self.detail_info, self.mark, self.add_time,
                self.agency_num, self.agency_name, self.batch)

class TYc_user(Base):
    __tablename__ = 'tyc_user'
    
    id = Column(NUMBER(24), primary_key=True)
    username = Column(VARCHAR2(60))
    password = Column(VARCHAR2(150))
    user_used = Column(NUMBER(3))
    user_forbid = Column(NUMBER(3))
    spaider_type = Column(VARCHAR2(30))
    update_time = Column(DATE)
    mark = Column(NUMBER(3))
    
    def __repr__(self):
        return "('id:%d', 'username:%s', 'password:%s', 'user_used:%d', 'user_forbid:%s', 'spaider_type:%s', 'update_time:%s', 'mark:%d')" % (
        self.id, self.username, self.password, self.user_used, self.user_forbid, self.spaider_type, self.update_time,
        self.mark)

class Tyc_year_dwtz(Base):
    '''
        对外投资信息表 tyc_year_dwtz
    '''
    __tablename__ = 'tyc_year_dwtz'
    
    id = Column(NUMBER(24), primary_key=True)
    txt_id = Column(VARCHAR2(300))
    ent_name = Column(VARCHAR2(300))
    year = Column(VARCHAR2(60))
    outbound_company = Column(VARCHAR2(300))
    credit_num = Column(VARCHAR2(300))
    mark = Column(NUMBER(4), default=0)
    add_time = Column(DATE)
    agency_num = Column(VARCHAR2(300))
    agency_name = Column(VARCHAR2(300))
    batch = Column(VARCHAR2(150))
    
    def __repr__(self):
        return "('id:%d', 'txt_id:%s', 'ent_name:%s', 'year:%s', 'outbound_company:%s', 'credit_num:%s',\
                'mark:%d', 'add_time:%s', 'agency_num:%s','agency_name:%s', 'batch:%s')" % \
               (self.id, self.txt_id, self.ent_name, self.year, self.outbound_company, self.credit_num,
                self.mark, self.add_time, self.agency_num, self.agency_name, self.batch)

class Tyc_year_gdczxx(Base):
    '''
        股东及出资信息表 tyc_year_gdczxx
    '''
    __tablename__ = 'tyc_year_gdczxx'
    
    id = Column(NUMBER(24), primary_key=True)
    txt_id = Column(VARCHAR2(300))
    ent_name = Column(VARCHAR2(300))
    year = Column(VARCHAR2(60))
    shareholder = Column(VARCHAR2(300))
    subscirbe_contribution = Column(VARCHAR2(300))
    contribution_time = Column(VARCHAR2(300))
    contribution_style = Column(VARCHAR2(300))
    actual_contribution = Column(VARCHAR2(300))
    actual_time = Column(VARCHAR2(300))
    actual_style = Column(VARCHAR2(300))
    mark = Column(NUMBER(4), default=0)
    add_time = Column(DATE)
    agency_num = Column(VARCHAR2(300))
    agency_name = Column(VARCHAR2(300))
    batch = Column(VARCHAR2(150))
    
    def __repr__(self):
        return "('id:%d', 'txt_id:%s', 'ent_name:%s', 'year:%s', 'shareholder:%s', 'subscirbe_contribution:%s', \
                'contribution_time:%s', 'contribution_style:%s', 'actual_contribution:%s', 'actual_time:%s', \
                'actual_style:%s', 'mark:%d', 'add_time:%s', 'agency_num:%s','agency_name:%s', 'batch:%s')" % \
               (self.id, self.txt_id, self.ent_name, self.year, self.shareholder, self.subscirbe_contribution,
                self.contribution_time, self.contribution_style, self.actual_contribution, self.actual_time,
                self.actual_style, self.mark, self.add_time, self.agency_num, self.agency_name, self.batch)

class Tyc_year_jbxx(Base):
    '''
       企业基本信息表    tyc_year_jbxx
    '''
    __tablename__ = 'tyc_year_jbxx'
    
    id = Column(NUMBER(24), primary_key=True)
    txt_id = Column(VARCHAR2(300))
    year = Column(VARCHAR2(60))
    ent_name = Column(VARCHAR2(300))
    credit_num = Column(VARCHAR2(300))
    company_name = Column(VARCHAR2(300))
    company_tel = Column(VARCHAR2(300))
    postal_code = Column(VARCHAR2(300))
    manger_state = Column(VARCHAR2(60))
    people_count = Column(VARCHAR2(300))
    email = Column(VARCHAR2(300))
    website = Column(VARCHAR2(60))
    company_address = Column(VARCHAR2(300))
    buy_equity = Column(VARCHAR2(300))
    mark = Column(NUMBER(4), default=0)
    add_time = Column(DATE)
    agency_num = Column(VARCHAR2(300))
    agency_name = Column(VARCHAR2(300))
    batch = Column(VARCHAR2(150))
    
    def __repr__(self):
        return "('id:%d', 'txt_id:%s', 'year:%s', 'ent_name:%s', 'credit_num:%s', 'company_name:%s', 'company_tel:%s', 'postal_code:%s',\
                 'manger_state:%s', 'people_count:%s', 'email:%s', 'website:%s', 'company_address:%s', 'buy_equity:%s', \
                 'mark:%d', 'add_time:%s', 'agency_num:%s','agency_name:%s', 'batch:%s')" % \
               (self.id, self.txt_id, self.year, self.ent_name, self.credit_num, self.company_name, self.company_tel,
                self.postal_code, self.manger_state, self.people_count, self.email, self.website, self.company_address,
                self.buy_equity, self.mark, self.add_time, self.agency_num, self.agency_name, self.batch)

class Tyc_year_wzhwdxx(Base):
    '''
        网点或网站信息表 tyc_year_wzhwdxx
    '''
    __tablename__ = 'tyc_year_wzhwdxx'
    
    id = Column(NUMBER(24), primary_key=True)
    txt_id = Column(VARCHAR2(300))
    year = Column(VARCHAR2(60))
    ent_name = Column(VARCHAR2(300))
    website_type = Column(VARCHAR2(300))
    web_name = Column(VARCHAR2(300))
    web_url = Column(VARCHAR2(300))
    mark = Column(NUMBER(4), default=0)
    add_time = Column(DATE)
    agency_num = Column(VARCHAR2(300))
    agency_name = Column(VARCHAR2(300))
    batch = Column(VARCHAR2(150))
    
    def __repr__(self):
        return "(id:%d', 'txt_id:%s', 'year:%s', 'ent_name:%s', 'website_type:%s', 'web_name:%s', \
                 'web_url:%s', 'mark:%d', 'add_time:%s', 'agency_num:%s','agency_name:%s', 'batch:%s')" % \
               (self.id, self.txt_id, self.year, self.ent_name, self.website_type, self.web_name,
                self.web_url, self.mark, self.add_time, self.agency_num, self.agency_name, self.batch)

class Tyc_year_zczk(Base):
    '''
        企业资产状况信息 tyc_year_zczk
    '''
    __tablename__ = 'tyc_year_zczk'
    
    id = Column(NUMBER(24), primary_key=True)
    txt_id = Column(VARCHAR2(300))
    ent_name = Column(VARCHAR2(300))
    year = Column(VARCHAR2(60))
    total_assets = Column(VARCHAR2(300))
    total_sales = Column(VARCHAR2(300))
    operation_income = Column(VARCHAR2(300))
    total_tax = Column(VARCHAR2(300))
    total_income = Column(VARCHAR2(300))
    total_profit = Column(VARCHAR2(300))
    net_profit = Column(VARCHAR2(300))
    total_debt = Column(VARCHAR2(300))
    mark = Column(NUMBER(4), default=0)
    add_time = Column(DATE)
    agency_num = Column(VARCHAR2(300))
    agency_name = Column(VARCHAR2(300))
    batch = Column(VARCHAR2(150))
    
    def __repr__(self):
        return "('id:%d', 'txt_id:%s', 'ent_name:%s', 'year:%s', 'total_assets:%s', 'total_sales:%s', 'operation_income:%s', \
                 'total_tax:%s', 'total_income:%s', 'total_profit:%s', 'net_profit:%s', 'total_debt:%s',\
                 'mark:%d', 'add_time:%s', 'agency_num:%s','agency_name:%s', 'batch:%s')" % \
               (self.id, self.txt_id, self.ent_name, self.year, self.total_assets, self.total_sales,
                self.operation_income, self.total_tax, self.total_income, self.total_profit, self.net_profit,
                self.total_debt, self.mark, self.add_time, self.agency_num, self.agency_name, self.batch)

class Tyc_zscq_sbxx(Base):
    '''
        商标信息表 tyc_zscq_sbxx
    '''
    __tablename__ = 'tyc_zscq_sbxx'
    
    id = Column(NUMBER(24), primary_key=True)
    # mongodb文本ID
    txt_id = Column(VARCHAR2(150))
    # 所属公司名称
    ent_name = Column(VARCHAR2(150))
    # 申请日期
    apply_date = Column(VARCHAR2(90))
    # 商标
    trademark = Column(VARCHAR2(150))
    # 商标名称
    trademark_name = Column(VARCHAR2(1500))
    # 注册号
    registration_number = Column(VARCHAR2(150))
    # 类别
    company_type = Column(VARCHAR2(60))
    # 状态
    status = Column(VARCHAR2(60))
    # 标记号
    mark = Column(NUMBER(3), default=0)
    # 添加时间
    add_time = Column(DATE)
    # 机构号
    agency_num = Column(VARCHAR2(300))
    # 机构名称
    agency_name = Column(VARCHAR2(300))
    # 批次
    batch = Column(VARCHAR2(150))
    
    def __repr__(self):
        return "(id:%d', 'txt_id:%s', 'ent_name:%s', 'apply_date:%s', 'trademark:%s', 'trademark_name:%s',\
                'registration_number:%s', 'company_type:%s', 'status:%s', mark:%d', 'add_time:%s',                         'agency_num:%s', 'agency_name:%s', 'batch:%s')" % \
               (self.id, self.txt_id, self.ent_name, self.apply_date, self.trademark, self.trademark_name,
                self.registration_number, self.company_type, self.status, self.mark, self.add_time, self.agency_num,
                self.agency_name, self.batch)

class Tyc_zscq_wzba(Base):
    '''
        网站备案表 tyc_zscq_wzba
    '''
    __tablename__ = 'tyc_zscq_wzba'
    
    id = Column(NUMBER(24), primary_key=True)
    # mongodb文本ID
    txt_id = Column(VARCHAR2(150))
    # 所属公司名称
    ent_name = Column(VARCHAR2(150))
    # 审核时间
    audit_date = Column(VARCHAR2(90))
    # 网站名称
    web_name = Column(VARCHAR2(150))
    # 网站首页
    web_homepage = Column(VARCHAR2(1500))
    # 域名
    domain_name = Column(VARCHAR2(90))
    # 备案号
    record_number = Column(VARCHAR2(90))
    # 状态
    status = Column(VARCHAR2(30))
    # 单位性质
    department_type = Column(VARCHAR2(60))
    # 标记号
    mark = Column(NUMBER(3), default=0)
    # 添加时间
    add_time = Column(DATE)
    # 机构号
    agency_num = Column(VARCHAR2(300))
    # 机构名称
    agency_name = Column(VARCHAR2(300))
    # 批次
    batch = Column(VARCHAR2(150))
    
    def __repr__(self):
        return "(id:%d', 'txt_id:%s', 'ent_name:%s', 'audit_date:%s', 'web_name:%s', 'web_homepage:%s', \
                'domain_name:%s', 'record_number:%s', 'status:%s', 'department_type:%s',\
                'mark:%d', 'add_time:%s', 'agency_num:%s','agency_name:%s', 'batch:%s')" % \
               (self.id, self.txt_id, self.ent_name, self.audit_date, self.web_name, self.web_homepage,
                self.domain_name, self.record_number, self.status, self.department_type, self.mark,
                self.add_time, self.agency_num, self.agency_name, self.batch)

class Tyc_zscq_zl(Base):
    '''
        专利表 tyc_zscq_zl
    '''
    __tablename__ = 'tyc_zscq_zl'
    
    id = Column(NUMBER(24), primary_key=True)
    # mongodb文本ID
    txt_id = Column(VARCHAR2(150))
    # 所属公司名称
    ent_name = Column(VARCHAR2(150))
    # 申请公布日
    apply_publish_date = Column(VARCHAR2(90))
    # 专利名称
    patent_name = Column(VARCHAR2(150))
    # 申请号
    apply_number = Column(VARCHAR2(150))
    # 申请公布号
    apply_publish_number = Column(VARCHAR2(150))
    # 详情
    detail_info = Column(CLOB)
    # 标记号
    mark = Column(NUMBER(3), default=0)
    # 添加时间
    add_time = Column(DATE)
    # 机构号
    agency_num = Column(VARCHAR2(300))
    # 机构名称
    agency_name = Column(VARCHAR2(300))
    # 批次
    batch = Column(VARCHAR2(150))
    
    def __repr__(self):
        return "(id:%d', 'txt_id:%s', 'ent_name:%s', 'apply_publish_date:%s', 'patent_name:%s', \
                'apply_number:%s', 'apply_publish_number:%s', 'detail_info:%s', mark:%d', 'add_time:%s', \
                'agency_num:%s','agency_name:%s', 'batch:%s')" % \
               (self.id, self.txt_id, self.ent_name, self.apply_publish_date, self.patent_name,
                self.apply_number, self.apply_publish_number, self.detail_info, self.mark,
                self.add_time, self.agency_num, self.agency_name, self.batch)

class Tyc_zscq_zpzzq(Base):
    '''
        作品著作权表 tyc_zscq_zpzzq
    '''
    __tablename__ = 'tyc_zscq_zpzzq'
    
    id = Column(NUMBER(24), primary_key=True)
    txt_id = Column(VARCHAR2(150))
    ent_name = Column(VARCHAR2(150))
    works_name = Column(VARCHAR2(300))
    register_name = Column(VARCHAR2(300))
    company_type = Column(VARCHAR2(90))
    creat_date = Column(VARCHAR2(30))
    register_date = Column(VARCHAR2(30))
    firstpublish_date = Column(VARCHAR2(30))
    mark = Column(NUMBER(3), default=0)
    add_time = Column(DATE)
    agency_num = Column(VARCHAR2(300))
    agency_name = Column(VARCHAR2(300))
    batch = Column(VARCHAR2(150))
    
    def __repr__(self):
        return "(id:%d', 'txt_id:%s', 'ent_name:%s', 'works_name:%s', 'register_name:%s', 'company_type:%s',\
                'creat_date:%s', 'register_data:%s', 'firstpublish_date:%s', 'mark:%d', 'add_time:%s',\
                 'agency_num:%s','agency_name:%s', 'batch:%s')" % \
               (self.id, self.txt_id, self.ent_name, self.works_name, self.register_name, self.company_type,
                self.creat_date, self.register_date, self.firstpublish_date, self.mark, self.add_time,
                self.agency_num, self.agency_name, self.batch)

class Tyc_zscq_zzq(Base):
    '''
        著作权表 tyc_zscq_zzq
    '''
    __tablename__ = 'tyc_zscq_zzq'
    
    id = Column(NUMBER(24), primary_key=True)
    # mongodb文本ID
    txt_id = Column(VARCHAR2(150))
    # 所属公司名称
    ent_name = Column(VARCHAR2(150))
    # 批准日期
    approval_date = Column(VARCHAR2(90))
    # 软件全称
    software_name = Column(VARCHAR2(150))
    # 软件简称
    software_referred = Column(VARCHAR2(150))
    # 登记号
    registration_number = Column(VARCHAR2(150))
    # 分类号
    type_number = Column(VARCHAR2(150))
    # 版本号
    version_number = Column(VARCHAR2(150))
    # 详情
    detail_info = Column(CLOB)
    # 标记号
    mark = Column(NUMBER(3), default=0)
    # 添加时间
    add_time = Column(DATE)
    # 机构号
    agency_num = Column(VARCHAR2(300))
    # 机构名称
    agency_name = Column(VARCHAR2(300))
    # 批次
    batch = Column(VARCHAR2(150))
    
    def __repr__(self):
        return "(id:%d', 'txt_id:%s', 'ent_name:%s', 'approval_date:%s', 'software_name:%s', \
                'software_referred:%s', 'registration_number:%s', 'type_number:%s', 'version_number:%s',\
                'detail_info:%s', 'mark:%d', 'add_time:%s', 'agency_num:%s','agency_name:%s', 'batch:%s')" \
               % \
               (self.id, self.txt_id, self.ent_name, self.approval_date, self.software_name,
                self.software_referred, self.registration_number, self.type_number, self.version_number,
                self.detail_info, self.mark, self.add_time, self.agency_num, self.agency_name, self.batch)
