# coding: utf-8
from sqlalchemy import CHAR, Column, DateTime, Float, Table, Text, VARCHAR, text, create_engine
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# engine = create_engine('oracle://tyc:tyc@10.10.82.12:1521/tycprd', echo=True)
engine = create_engine('oracle://c##ljj:123456@127.0.0.1:1521/orcl', echo=True, encoding='utf-8')
Database = sessionmaker(bind=engine)
single_oracle_orm = Database()
Base = declarative_base()
metadata = Base.metadata

class BatchDetail(Base):
    __tablename__ = 'batch_detail'
    
    company_number = Column(NUMBER(24, 0, False), primary_key=True)
    mark = Column(NUMBER(6, 0, False), server_default=text("'0'"))
    company_name = Column(VARCHAR(1000), index=True)
    company_address = Column(VARCHAR(800))
    searched = Column(NUMBER(6, 0, False), server_default=text("'0'"))
    error = Column(NUMBER(6, 0, False), server_default=text("'0'"))
    agency_num = Column(VARCHAR(800))
    agency_name = Column(VARCHAR(800))
    batch = Column(VARCHAR(400))
    txt_id = Column(VARCHAR(500))
    batch_type = Column(VARCHAR(150))
    add_time = Column(DateTime)

class BatchList(Base):
    __tablename__ = 'batch_list'
    
    company_number = Column(NUMBER(24, 0, False), primary_key=True)
    mark = Column(NUMBER(6, 0, False), server_default=text("'0'"))
    company_name = Column(VARCHAR(1000))
    company_address = Column(VARCHAR(800))
    searched = Column(NUMBER(6, 0, False), server_default=text("'0'"))
    error = Column(NUMBER(6, 0, False), server_default=text("'0'"))
    agency_num = Column(VARCHAR(800))
    agency_name = Column(VARCHAR(800))
    batch = Column(VARCHAR(400))
    end_time = Column(VARCHAR(400))
    batch_type = Column(VARCHAR(150))
    add_time = Column(DateTime)

class Branch(Base):
    __tablename__ = 'branch'
    
    id = Column(NUMBER(11, 0, False))
    branch_level2 = Column(VARCHAR(300), primary_key=True)
    branch_level2_short_name = Column(VARCHAR(300), nullable=False)

class CheckImportField(Base):
    __tablename__ = 'check_import_field'
    
    id = Column(NUMBER(asdecimal=False), primary_key=True)
    table_name = Column(VARCHAR(500))
    column_name = Column(VARCHAR(200))
    data_type = Column(VARCHAR(200))
    column_comment = Column(VARCHAR(500))
    column_level = Column(NUMBER(asdecimal=False))

class CheckResult(Base):
    __tablename__ = 'check_result'

    id = Column(NUMBER(asdecimal=False), primary_key=True, server_default=text("0"))
    add_time = Column(DateTime, nullable=False)
    table_name = Column(VARCHAR(200), server_default=text("0"))
    table_field = Column(VARCHAR(200))
    standard_value = Column(VARCHAR(2000))
    current_value = Column(VARCHAR(2000))
    standard_version = Column(VARCHAR(200), nullable=False)
    company_name = Column(VARCHAR(2000), nullable=False)
    different_reason = Column(VARCHAR(2000), nullable=False)
    risk_level = Column(NUMBER(asdecimal=False))
    task_status = Column(NUMBER(asdecimal=False), server_default=text("0"))

t_company_11315 = Table(
    'company_11315', metadata,
    Column('company_number', NUMBER(24, 0, False), unique=True),
    Column('url', VARCHAR(800), index=True),
    Column('company_name', VARCHAR(1000), index=True),
    Column('company_industry', VARCHAR(1600)),
    Column('address_1', VARCHAR(200)),
    Column('address_2', VARCHAR(800)),
    Column('address_3', VARCHAR(800), index=True),
    Column('company_area', VARCHAR(2400)),
    Column('company_address', VARCHAR(2400)),
    Column('add_time', DateTime, server_default=text("sysdate")),
    Column('searched', NUMBER(6, 0, False), server_default=text("'0'")),
    Column('error', NUMBER(6, 0, False), server_default=text("'0'")),
    Column('parse', NUMBER(6, 0, False), index=True, server_default=text("'0'")),
    Column('mark', NUMBER(6, 0, False), server_default=text("'0'")),
    Column('branch', VARCHAR(300)),
    Column('register_num', VARCHAR(200)),
    Column('company_type', VARCHAR(300)),
    Column('legal_representative', VARCHAR(300)),
    Column('register_fund', VARCHAR(300)),
    Column('residence', VARCHAR(500)),
    Column('business_term_begin', VARCHAR(150)),
    Column('business_term_end', VARCHAR(100)),
    Column('business_scope', Text),
    Column('register_status', VARCHAR(150)),
    Column('credit_num', VARCHAR(200)),
    Column('detail_url', VARCHAR(200))
)

t_company_11315_standard = Table(
    'company_11315_standard', metadata,
    Column('company_number', NUMBER(24, 0, False)),
    Column('url', VARCHAR(800)),
    Column('company_name', VARCHAR(1000)),
    Column('company_industry', VARCHAR(1600)),
    Column('address_1', VARCHAR(200)),
    Column('address_2', VARCHAR(800)),
    Column('address_3', VARCHAR(800)),
    Column('company_area', VARCHAR(2400)),
    Column('company_address', VARCHAR(2400)),
    Column('add_time', DateTime),
    Column('searched', NUMBER(6, 0, False)),
    Column('error', NUMBER(6, 0, False)),
    Column('parse', NUMBER(6, 0, False)),
    Column('mark', NUMBER(6, 0, False)),
    Column('branch', VARCHAR(300)),
    Column('register_num', VARCHAR(200)),
    Column('company_type', VARCHAR(300)),
    Column('legal_representative', VARCHAR(300)),
    Column('register_fund', VARCHAR(300)),
    Column('residence', VARCHAR(500)),
    Column('business_term_begin', VARCHAR(150)),
    Column('business_term_end', VARCHAR(100)),
    Column('business_scope', Text),
    Column('register_status', VARCHAR(150)),
    Column('credit_num', VARCHAR(200)),
    Column('detail_url', VARCHAR(200))
)

t_company_11315_zyfd = Table(
    'company_11315_zyfd', metadata,
    Column('company_number', NUMBER(24, 0, False), unique=True),
    Column('url', VARCHAR(800), index=True),
    Column('company_name', VARCHAR(1000), index=True),
    Column('company_industry', VARCHAR(1600)),
    Column('address_1', VARCHAR(800)),
    Column('address_2', VARCHAR(800)),
    Column('address_3', VARCHAR(800), index=True),
    Column('company_area', VARCHAR(2400)),
    Column('company_address', VARCHAR(2400)),
    Column('add_time', DateTime, server_default=text("sysdate")),
    Column('searched', NUMBER(6, 0, False)),
    Column('error', NUMBER(6, 0, False)),
    Column('parse', NUMBER(6, 0, False), index=True),
    Column('mark', NUMBER(6, 0, False)),
    Column('branch', VARCHAR(300)),
    Column('register_num', VARCHAR(200)),
    Column('company_type', VARCHAR(300)),
    Column('legal_representative', VARCHAR(300)),
    Column('register_fund', VARCHAR(300)),
    Column('residence', VARCHAR(500)),
    Column('business_term_begin', VARCHAR(150)),
    Column('business_term_end', VARCHAR(100)),
    Column('business_scope', Text),
    Column('register_status', VARCHAR(150)),
    Column('credit_num', VARCHAR(200))
)

class CompanyBasicInfo(Base):
    __tablename__ = 'company_basic_info'
    
    id = Column(NUMBER(24, 0, False), primary_key=True)
    search_name = Column(VARCHAR(60), index=True)
    company_name = Column(VARCHAR(1000), index=True)
    legal_representative = Column(VARCHAR(500))
    registered_capital = Column(VARCHAR(500))
    registration_date = Column(VARCHAR(20))
    location = Column(VARCHAR(10))
    score = Column(VARCHAR(10))
    status_type = Column(VARCHAR(20))
    url = Column(VARCHAR(100), nullable=False)
    txt_id = Column(VARCHAR(100), index=True)
    page_spider = Column(NUMBER(6, 0, False), server_default=text("'0'"))
    parsed = Column(NUMBER(6, 0, False), server_default=text("'0'"))
    add_time = Column(DateTime, server_default=text("sysdate"))
    mark = Column(NUMBER(6, 0, False), server_default=text("'0'"))
    agency_num = Column(VARCHAR(200))
    agency_name = Column(VARCHAR(200))
    batch = Column(VARCHAR(100))
    branch = Column(VARCHAR(15))
    used_name = Column(VARCHAR(200))

class Config(Base):
    __tablename__ = 'config'
    
    id = Column(NUMBER(5, 0, False), primary_key=True)
    function = Column(VARCHAR(500), nullable=False, server_default=text("0 "))
    priority = Column(NUMBER(2, 0, False), nullable=False, server_default=text("0 "))
    over = Column(NUMBER(1, 0, False), nullable=False, server_default=text("0 "))
    over_time = Column(DateTime)
    condition = Column(VARCHAR(4000), nullable=False, server_default=text("'NA' "))
    operator = Column(VARCHAR(100), server_default=text("'Luo Cheng'"))
    jump_a_queue = Column(NUMBER(1, 0, False), nullable=False, server_default=text("0 "))

t_d_region_code = Table(
    'd_region_code', metadata,
    Column('region_code', VARCHAR(200)),
    Column('region_name', VARCHAR(200)),
    Column('countryside_type_code', VARCHAR(200))
)

t_py_st_com_info_count = Table(
    'py_st_com_info_count', metadata,
    Column('company_11315_count', NUMBER(20, 0, False)),
    Column('qyxq_info_count', NUMBER(20, 0, False)),
    Column('company_11315_add_count', NUMBER(20, 0, False)),
    Column('qyxq_info_add_count', NUMBER(20, 0, False)),
    Column('data_date', VARCHAR(20))
)

class TycJyfxDcdy(Base):
    __tablename__ = 'tyc_jyfx_dcdy'
    
    id = Column(NUMBER(24, 0, False), primary_key=True)
    registration_date = Column(VARCHAR(300))
    registration_number = Column(VARCHAR(400))
    guarantee_type = Column(VARCHAR(400))
    guarantee_amount = Column(VARCHAR(400))
    registration_department = Column(VARCHAR(800))
    status = Column(VARCHAR(300))
    detail_info = Column(Text)
    txt_id = Column(VARCHAR(500), index=True)
    company_name = Column(VARCHAR(1000), index=True)
    add_time = Column(DateTime)
    mark = Column(NUMBER(6, 0, False), server_default=text("'0'"))
    agency_num = Column(VARCHAR(800))
    agency_name = Column(VARCHAR(800))
    batch = Column(VARCHAR(400))

class TycJyfxGqcz(Base):
    __tablename__ = 'tyc_jyfx_gqcz'
    
    id = Column(NUMBER(24, 0, False), primary_key=True)
    announcement_date = Column(VARCHAR(300))
    registration_number = Column(VARCHAR(300))
    pledgor = Column(VARCHAR(400))
    pledgee = Column(VARCHAR(400))
    status = Column(VARCHAR(150))
    detail_info = Column(Text)
    txt_id = Column(VARCHAR(500), index=True)
    company_name = Column(VARCHAR(1000), index=True)
    add_time = Column(DateTime)
    mark = Column(NUMBER(6, 0, False), server_default=text("'0'"))
    agency_num = Column(VARCHAR(800))
    agency_name = Column(VARCHAR(800))
    batch = Column(VARCHAR(400))
    pledged_amount = Column(VARCHAR(100))

class TycJyfxGscg(Base):
    __tablename__ = 'tyc_jyfx_gscg'
    
    id = Column(NUMBER(24, 0, False), primary_key=True)
    txt_id = Column(VARCHAR(300))
    company_name = Column(VARCHAR(500))
    bill_number = Column(VARCHAR(100))
    bill_type = Column(VARCHAR(50))
    denomination = Column(VARCHAR(50))
    publish_authority = Column(VARCHAR(200))
    announcement_date = Column(VARCHAR(100))
    detail = Column(Text)
    mark = Column(NUMBER(6, 0, False))
    agency_num = Column(VARCHAR(300))
    agency_name = Column(VARCHAR(300))
    batch = Column(VARCHAR(150))
    add_time = Column(DateTime)

class TycJyfxHbcf(Base):
    __tablename__ = 'tyc_jyfx_hbcf'
    
    id = Column(NUMBER(24, 0, False), primary_key=True)
    txt_id = Column(VARCHAR(300))
    company_name = Column(VARCHAR(500))
    departure_date = Column(VARCHAR(100))
    decision_num = Column(VARCHAR(100))
    punishment_cause = Column(VARCHAR(500))
    penalty_result = Column(VARCHAR(1000))
    penalty_unites = Column(VARCHAR(300))
    detail = Column(Text)
    mark = Column(NUMBER(6, 0, False), server_default=text("'0'"))
    add_time = Column(DateTime)
    agency_num = Column(VARCHAR(300))
    agency_name = Column(VARCHAR(300))
    batch = Column(VARCHAR(150))

class TycJyfxJyyc(Base):
    __tablename__ = 'tyc_jyfx_jyyc'
    
    id = Column(NUMBER(24, 0, False), primary_key=True)
    insert_date = Column(VARCHAR(300))
    insert_cause = Column(VARCHAR(800))
    insert_department = Column(VARCHAR(400))
    txt_id = Column(VARCHAR(500), index=True)
    company_name = Column(VARCHAR(1000), index=True)
    add_time = Column(DateTime)
    mark = Column(NUMBER(6, 0, False), server_default=text("'0'"))
    agency_num = Column(VARCHAR(800))
    agency_name = Column(VARCHAR(800))
    batch = Column(VARCHAR(400))
    out_date = Column(VARCHAR(100))
    out_cause = Column(VARCHAR(3000))
    out_department = Column(VARCHAR(200))

class TycJyfxQsgg(Base):
    __tablename__ = 'tyc_jyfx_qsgg'
    
    id = Column(NUMBER(24, 0, False), primary_key=True)
    txt_id = Column(VARCHAR(800), index=True)
    company_name = Column(VARCHAR(1000), index=True)
    taxes_date = Column(VARCHAR(400))
    taxes_num = Column(VARCHAR(800))
    taxes_type = Column(VARCHAR(800))
    taxes_money = Column(VARCHAR(800))
    taxes_balance = Column(VARCHAR(800))
    taxes_office = Column(VARCHAR(1600))
    mark = Column(NUMBER(6, 0, False), server_default=text("'0'"))
    add_time = Column(DateTime)
    agency_num = Column(VARCHAR(800))
    agency_name = Column(VARCHAR(800))
    batch = Column(VARCHAR(400))
    detail = Column(Text)

class TycJyfxQsxx(Base):
    __tablename__ = 'tyc_jyfx_qsxx'
    
    id = Column(NUMBER(24, 0, False), primary_key=True)
    txt_id = Column(VARCHAR(300))
    company_name = Column(VARCHAR(500))
    add_time = Column(DateTime)
    mark = Column(NUMBER(6, 0, False), server_default=text("0"))
    agency_num = Column(VARCHAR(300))
    agency_name = Column(VARCHAR(300))
    batch = Column(VARCHAR(150))
    principal = Column(VARCHAR(100))
    member = Column(VARCHAR(100))

class TycJyfxSfpm(Base):
    __tablename__ = 'tyc_jyfx_sfpm'
    
    id = Column(NUMBER(24, 0, False), primary_key=True)
    txt_id = Column(VARCHAR(300))
    company_name = Column(VARCHAR(500))
    auction_notice = Column(VARCHAR(600))
    auction_date = Column(VARCHAR(100))
    execute_court = Column(VARCHAR(100))
    auction_target = Column(VARCHAR(200))
    mark = Column(NUMBER(6, 0, False))
    add_time = Column(DateTime)
    agency_num = Column(VARCHAR(300))
    agency_name = Column(VARCHAR(300))
    batch = Column(VARCHAR(150))
    auction_detail = Column(Text)

class TycJyfxSswf(Base):
    __tablename__ = 'tyc_jyfx_sswf'
    
    id = Column(NUMBER(24, 0, False), primary_key=True)
    txt_id = Column(VARCHAR(300))
    company_name = Column(VARCHAR(500))
    taxpayer = Column(VARCHAR(500))
    tax_authority = Column(VARCHAR(300))
    case_character = Column(VARCHAR(100))
    detail = Column(Text)
    mark = Column(NUMBER(6, 0, False))
    add_time = Column(DateTime)
    agency_num = Column(VARCHAR(300))
    agency_name = Column(VARCHAR(300))
    batch = Column(VARCHAR(150))

class TycJyfxTddy(Base):
    __tablename__ = 'tyc_jyfx_tddy'
    
    id = Column(NUMBER(24, 0, False), primary_key=True)
    txt_id = Column(VARCHAR(300))
    company_name = Column(VARCHAR(500))
    located = Column(VARCHAR(500))
    start_end_time = Column(VARCHAR(200))
    administrative_area = Column(VARCHAR(50))
    mortgage_area = Column(VARCHAR(50))
    mortgage_land_use = Column(VARCHAR(200))
    detail = Column(Text)
    mark = Column(NUMBER(6, 0, False))
    add_time = Column(DateTime)
    agency_num = Column(VARCHAR(300))
    agency_name = Column(VARCHAR(300))
    batch = Column(VARCHAR(150))

class TycJyfxXzcf(Base):
    __tablename__ = 'tyc_jyfx_xzcf'
    
    id = Column(NUMBER(24, 0, False), primary_key=True)
    decision_date = Column(VARCHAR(300))
    decision_number = Column(VARCHAR(400))
    type = Column(VARCHAR(4000))
    decision_department = Column(VARCHAR(300))
    detail_info = Column(Text)
    punishment_name = Column(VARCHAR(2400))
    punishment_area = Column(VARCHAR(800))
    txt_id = Column(VARCHAR(500), index=True)
    company_name = Column(VARCHAR(1000), index=True)
    add_time = Column(DateTime)
    mark = Column(NUMBER(6, 0, False), server_default=text("'0'"))
    agency_num = Column(VARCHAR(800))
    agency_name = Column(VARCHAR(800))
    batch = Column(VARCHAR(400))
    punishment_contents = Column(VARCHAR(2000))

class TycJyfxXzchXyzg(Base):
    __tablename__ = 'tyc_jyfx_xzch_xyzg'
    
    id = Column(NUMBER(24, 0, False), primary_key=True)
    txt_id = Column(VARCHAR(300))
    company_name = Column(VARCHAR(500))
    decision_date = Column(VARCHAR(100))
    decision_num = Column(VARCHAR(200))
    punishment_cause = Column(VARCHAR(1000))
    penalty_result = Column(VARCHAR(1000))
    punishment_organ = Column(VARCHAR(300))
    detail = Column(Text)
    mark = Column(NUMBER(6, 0, False))
    add_time = Column(DateTime)
    agency_num = Column(VARCHAR(300))
    agency_name = Column(VARCHAR(300))
    batch = Column(VARCHAR(150))

class TycJyfxYzwf(Base):
    __tablename__ = 'tyc_jyfx_yzwf'
    
    id = Column(NUMBER(24, 0, False), primary_key=True)
    txt_id = Column(VARCHAR(800), index=True)
    company_name = Column(VARCHAR(1000), index=True)
    illegal_date = Column(VARCHAR(300))
    illegal_reason = Column(VARCHAR(4000))
    office = Column(VARCHAR(1600))
    mark = Column(NUMBER(6, 0, False), server_default=text("'0'"))
    add_time = Column(DateTime)
    agency_num = Column(VARCHAR(800))
    agency_name = Column(VARCHAR(800))
    batch = Column(VARCHAR(400))
    out_date = Column(VARCHAR(100))
    out_reason = Column(VARCHAR(3000))
    out_department = Column(VARCHAR(200))

class TycJyzkCcjc(Base):
    __tablename__ = 'tyc_jyzk_ccjc'
    
    add_time = Column(DateTime)
    id = Column(NUMBER(scale=0, asdecimal=False), primary_key=True)
    type = Column(VARCHAR(150))
    result = Column(VARCHAR(300))
    check_department = Column(VARCHAR(150))
    txt_id = Column(VARCHAR(500))
    company_name = Column(VARCHAR(1000))
    mark = Column(CHAR(1), server_default=text("'0'"))
    agency_num = Column(VARCHAR(300))
    agency_name = Column(VARCHAR(300))
    batch = Column(VARCHAR(150))
    check_date = Column(VARCHAR(50))

class TycJyzkCpxx(Base):
    __tablename__ = 'tyc_jyzk_cpxx'
    
    id = Column(NUMBER(24, 0, False), primary_key=True)
    product_name = Column(VARCHAR(400))
    product_referred = Column(VARCHAR(400))
    product_classification = Column(VARCHAR(200))
    field = Column(VARCHAR(200))
    detail_info = Column(Text)
    txt_id = Column(VARCHAR(500), index=True)
    company_name = Column(VARCHAR(1000), index=True)
    add_time = Column(DateTime)
    mark = Column(NUMBER(6, 0, False), server_default=text("'0'"))
    agency_num = Column(VARCHAR(800))
    agency_name = Column(VARCHAR(800))
    batch = Column(VARCHAR(400))

class TycJyzkDkg(Base):
    __tablename__ = 'tyc_jyzk_dkgs'
    
    id = Column(NUMBER(24, 0, False), primary_key=True)
    txt_id = Column(VARCHAR(300))
    company_name = Column(VARCHAR(500))
    release_date = Column(VARCHAR(100))
    site_location = Column(VARCHAR(1000))
    administrative_area = Column(VARCHAR(200))
    acreage = Column(VARCHAR(50))
    land_use = Column(VARCHAR(100))
    publish_organ = Column(VARCHAR(300))
    detail = Column(Text)
    mark = Column(NUMBER(6, 0, False))
    add_time = Column(DateTime)
    agency_num = Column(VARCHAR(300))
    agency_name = Column(VARCHAR(300))
    batch = Column(VARCHAR(150))

class TycJyzkDxxk(Base):
    __tablename__ = 'tyc_jyzk_dxxk'
    
    id = Column(NUMBER(24, 0, False), primary_key=True)
    txt_id = Column(VARCHAR(300))
    company_name = Column(VARCHAR(500))
    license_key = Column(VARCHAR(100))
    business_sphere = Column(VARCHAR(500))
    available = Column(VARCHAR(20))
    detail_info = Column(Text)
    mark = Column(NUMBER(6, 0, False))
    add_time = Column(DateTime)
    agency_num = Column(VARCHAR(300))
    agency_name = Column(VARCHAR(300))
    batch = Column(VARCHAR(150))

class TycJyzkGdxx(Base):
    __tablename__ = 'tyc_jyzk_gdxx'
    
    id = Column(NUMBER(24, 0, False), primary_key=True)
    txt_id = Column(VARCHAR(800), index=True)
    company_name = Column(VARCHAR(1000), index=True)
    gd_sign_date = Column(VARCHAR(300))
    gd_num = Column(VARCHAR(800))
    gd_act_date = Column(VARCHAR(300))
    gd_area = Column(VARCHAR(800))
    gd_region = Column(VARCHAR(800))
    gd_operate = Column(VARCHAR(800))
    mark = Column(NUMBER(6, 0, False), server_default=text("'0'"))
    add_time = Column(DateTime)
    agency_num = Column(VARCHAR(800))
    agency_name = Column(VARCHAR(800))
    batch = Column(VARCHAR(400))
    located = Column(VARCHAR(2000))
    land_use = Column(VARCHAR(100))
    supply_method = Column(VARCHAR(50))
    gd_info = Column(Text)

class TycJyzkGsj(Base):
    __tablename__ = 'tyc_jyzk_gsj'
    
    id = Column(NUMBER(24, 0, False), primary_key=True)
    txt_id = Column(VARCHAR(300))
    company_name = Column(VARCHAR(500))
    license_documet_num = Column(VARCHAR(200))
    license_document_name = Column(VARCHAR(200))
    validity_begin = Column(VARCHAR(100))
    validity_end = Column(VARCHAR(100))
    license_authority = Column(VARCHAR(200))
    license_content = Column(VARCHAR(2000))
    mark = Column(NUMBER(6, 0, False))
    add_time = Column(DateTime)
    agency_num = Column(VARCHAR(300))
    agency_name = Column(VARCHAR(300))
    batch = Column(VARCHAR(150))

class TycJyzkGy(Base):
    __tablename__ = 'tyc_jyzk_gys'
    
    id = Column(NUMBER(24, 0, False), primary_key=True)
    txt_id = Column(VARCHAR(300))
    company_name = Column(VARCHAR(500))
    provider = Column(VARCHAR(500))
    purchase_proportion = Column(VARCHAR(20))
    purchase_amount = Column(VARCHAR(20))
    report_period = Column(VARCHAR(100))
    data_sources = Column(VARCHAR(100))
    incidence_relation = Column(VARCHAR(100))
    mark = Column(NUMBER(6, 0, False))
    add_time = Column(DateTime)
    agency_num = Column(VARCHAR(300))
    agency_name = Column(VARCHAR(300))
    batch = Column(VARCHAR(150))

class TycJyzkJckxy(Base):
    __tablename__ = 'tyc_jyzk_jckxy'
    
    id = Column(NUMBER(24, 0, False), primary_key=True)
    txt_id = Column(VARCHAR(500))
    company_name = Column(VARCHAR(1000))
    register_customs = Column(VARCHAR(300))
    customs_number = Column(VARCHAR(400))
    manager_type = Column(VARCHAR(400))
    detail_info = Column(Text)
    mark = Column(NUMBER(6, 0, False), server_default=text("'0'"))
    add_time = Column(DateTime)
    agency_num = Column(VARCHAR(800))
    agency_name = Column(VARCHAR(800))
    batch = Column(VARCHAR(400))
    industry_category = Column(VARCHAR(50))
    register_date = Column(VARCHAR(100))

class TycJyzkKh(Base):
    __tablename__ = 'tyc_jyzk_kh'
    
    id = Column(NUMBER(24, 0, False), primary_key=True)
    txt_id = Column(VARCHAR(300))
    company_name = Column(VARCHAR(500))
    client = Column(VARCHAR(500))
    sale_proportion = Column(VARCHAR(20))
    sale_amount = Column(VARCHAR(20))
    report_period = Column(VARCHAR(100))
    data_sources = Column(VARCHAR(100))
    incidence_relation = Column(VARCHAR(100))
    mark = Column(NUMBER(6, 0, False))
    add_time = Column(DateTime)
    agency_num = Column(VARCHAR(300))
    agency_name = Column(VARCHAR(300))
    batch = Column(VARCHAR(150))

class TycJyzkSwpj(Base):
    __tablename__ = 'tyc_jyzk_swpj'
    
    add_time = Column(DateTime)
    year = Column(VARCHAR(150))
    id = Column(NUMBER(scale=0, asdecimal=False), primary_key=True)
    tax_rating = Column(VARCHAR(150))
    tax_type = Column(VARCHAR(150))
    tax_identification_number = Column(VARCHAR(300))
    evaluate_department = Column(VARCHAR(300))
    txt_id = Column(VARCHAR(500))
    company_name = Column(VARCHAR(1000))
    mark = Column(CHAR(1), server_default=text("'0'"))
    agency_num = Column(VARCHAR(300))
    agency_name = Column(VARCHAR(300))
    batch = Column(VARCHAR(150))

class TycJyzkTdzr(Base):
    __tablename__ = 'tyc_jyzk_tdzr'
    
    id = Column(NUMBER(24, 0, False), primary_key=True)
    txt_id = Column(VARCHAR(300))
    company_name = Column(VARCHAR(500))
    trade_date = Column(VARCHAR(100))
    located = Column(VARCHAR(500))
    land_area = Column(VARCHAR(20))
    former_land_user = Column(VARCHAR(500))
    current_land_user = Column(VARCHAR(500))
    transfer_price = Column(VARCHAR(20))
    detail = Column(Text)
    mark = Column(NUMBER(6, 0, False))
    add_time = Column(DateTime)
    agency_num = Column(VARCHAR(300))
    agency_name = Column(VARCHAR(300))
    batch = Column(VARCHAR(150))

class TycJyzkWxgzh(Base):
    __tablename__ = 'tyc_jyzk_wxgzh'
    
    id = Column(NUMBER(24, 0, False), primary_key=True)
    txt_id = Column(VARCHAR(500))
    company_name = Column(VARCHAR(1000))
    mp_name = Column(VARCHAR(300))
    mp_number = Column(VARCHAR(400))
    mp_info = Column(Text)
    mark = Column(NUMBER(6, 0, False))
    add_time = Column(DateTime)
    agency_num = Column(VARCHAR(800))
    agency_name = Column(VARCHAR(800))
    batch = Column(VARCHAR(400))
    detail = Column(Text)

class TycJyzkXyzg(Base):
    __tablename__ = 'tyc_jyzk_xyzg'
    
    id = Column(NUMBER(24, 0, False), primary_key=True)
    txt_id = Column(VARCHAR(300))
    company_name = Column(VARCHAR(500))
    license_documet_num = Column(VARCHAR(200))
    license_authority = Column(VARCHAR(200))
    license_date = Column(VARCHAR(100))
    detail = Column(Text)
    mark = Column(NUMBER(6, 0, False))
    add_time = Column(DateTime)
    agency_num = Column(VARCHAR(300))
    agency_name = Column(VARCHAR(300))
    batch = Column(VARCHAR(150))

class TycJyzkZp(Base):
    __tablename__ = 'tyc_jyzk_zp'
    
    id = Column(NUMBER(24, 0, False), primary_key=True)
    publish_date = Column(VARCHAR(300))
    recruitment_job = Column(VARCHAR(800))
    salary = Column(VARCHAR(800))
    work_year = Column(VARCHAR(400))
    recruitment_numbers = Column(VARCHAR(200))
    work_city = Column(VARCHAR(200))
    detail_info = Column(Text)
    txt_id = Column(VARCHAR(500), index=True)
    company_name = Column(VARCHAR(1000), index=True)
    add_time = Column(DateTime)
    mark = Column(NUMBER(6, 0, False), server_default=text("'0'"))
    agency_num = Column(VARCHAR(800))
    agency_name = Column(VARCHAR(800))
    batch = Column(VARCHAR(400))
    education = Column(VARCHAR(50))

class TycJyzkZqxx(Base):
    __tablename__ = 'tyc_jyzk_zqxx'
    
    id = Column(NUMBER(24, 0, False), primary_key=True)
    publish_date = Column(VARCHAR(300))
    bond_name = Column(VARCHAR(400))
    bond_code = Column(VARCHAR(400))
    bond_type = Column(VARCHAR(300))
    latest_rating = Column(VARCHAR(300))
    detail_info = Column(Text)
    txt_id = Column(VARCHAR(500), index=True)
    company_name = Column(VARCHAR(1000), index=True)
    add_time = Column(DateTime)
    mark = Column(NUMBER(6, 0, False), server_default=text("'0'"))
    agency_num = Column(VARCHAR(800))
    agency_name = Column(VARCHAR(800))
    batch = Column(VARCHAR(400))

class TycJyzkZtb(Base):
    __tablename__ = 'tyc_jyzk_ztb'
    
    id = Column(NUMBER(24, 0, False), primary_key=True)
    publish_date = Column(VARCHAR(300))
    title = Column(VARCHAR(4000))
    title_url = Column(VARCHAR(400))
    procurement = Column(VARCHAR(4000))
    txt_id = Column(VARCHAR(500), index=True)
    company_name = Column(VARCHAR(1000), index=True)
    add_time = Column(DateTime)
    mark = Column(NUMBER(6, 0, False), server_default=text("'0'"))
    agency_num = Column(VARCHAR(800))
    agency_name = Column(VARCHAR(800))
    batch = Column(VARCHAR(400))

class TycJyzkZzz(Base):
    __tablename__ = 'tyc_jyzk_zzzs'
    
    id = Column(NUMBER(24, 0, False), primary_key=True)
    txt_id = Column(VARCHAR(800), index=True)
    company_name = Column(VARCHAR(1000), index=True)
    certificate_num = Column(VARCHAR(800))
    certificate_type = Column(VARCHAR(800))
    send_date = Column(VARCHAR(240))
    off_date = Column(VARCHAR(240))
    mark = Column(NUMBER(6, 0, False), server_default=text("'0'"))
    add_time = Column(DateTime)
    agency_num = Column(VARCHAR(800))
    agency_name = Column(VARCHAR(800))
    batch = Column(VARCHAR(400))
    detail = Column(Text)

class TycQybjBgjl(Base):
    __tablename__ = 'tyc_qybj_bgjl'
    
    id = Column(NUMBER(24, 0, False), primary_key=True)
    txt_id = Column(VARCHAR(800), index=True)
    company_name = Column(VARCHAR(1000), index=True)
    alter_date = Column(VARCHAR(400))
    alter_project = Column(VARCHAR(800))
    alter_befor = Column(Text)
    alter_after = Column(Text)
    mark = Column(NUMBER(6, 0, False), server_default=text("'0'"))
    add_time = Column(DateTime)
    agency_num = Column(VARCHAR(800))
    agency_name = Column(VARCHAR(800))
    batch = Column(VARCHAR(400))

class TycQybjDwtz(Base):
    __tablename__ = 'tyc_qybj_dwtz'
    
    invest_company = Column(VARCHAR(800))
    invest_person = Column(VARCHAR(800))
    invest_fund = Column(VARCHAR(800))
    invest_amount = Column(VARCHAR(800))
    invest_ratio = Column(VARCHAR(800))
    invest_date = Column(VARCHAR(800))
    invest_status = Column(VARCHAR(800))
    mark = Column(NUMBER(6, 0, False), server_default=text("'0'"))
    add_time = Column(DateTime)
    agency_num = Column(VARCHAR(800))
    agency_name = Column(VARCHAR(800))
    batch = Column(VARCHAR(400))
    id = Column(VARCHAR(50), primary_key=True)
    txt_id = Column(VARCHAR(500))
    company_name = Column(VARCHAR(1000))

class TycQybjFzjg(Base):
    __tablename__ = 'tyc_qybj_fzjg'
    
    add_time = Column(DateTime)
    mark = Column(NUMBER(6, 0, False), server_default=text("'0'"))
    id = Column(VARCHAR(60), primary_key=True)
    company_name = Column(VARCHAR(1000))
    legal_representative = Column(VARCHAR(500))
    status = Column(VARCHAR(300))
    register_date = Column(VARCHAR(200))
    txt_id = Column(VARCHAR(500))
    ent_name = Column(VARCHAR(1000))
    agency_num = Column(VARCHAR(300))
    agency_name = Column(VARCHAR(300))
    batch = Column(VARCHAR(300))

class TycQybjGdxx(Base):
    __tablename__ = 'tyc_qybj_gdxx'
    
    shareholder = Column(VARCHAR(800))
    fund_ratio = Column(VARCHAR(800))
    fund_subcribe = Column(VARCHAR(800))
    mark = Column(VARCHAR(32), server_default=text("'0'"))
    agency_num = Column(VARCHAR(800))
    agency_name = Column(VARCHAR(800))
    batch = Column(VARCHAR(800))
    id = Column(VARCHAR(100), primary_key=True)
    txt_id = Column(VARCHAR(500))
    company_name = Column(VARCHAR(1000))
    fund_time = Column(VARCHAR(100))
    add_time = Column(DateTime)

class TycQybjGsg(Base):
    __tablename__ = 'tyc_qybj_gsgs'
    
    id = Column(NUMBER(24, 0, False), primary_key=True)
    txt_id = Column(VARCHAR(300))
    company_name = Column(VARCHAR(500))
    shareholder_sponsor = Column(VARCHAR(500))
    shareholder_proportion = Column(VARCHAR(50))
    subscribe_contribution = Column(VARCHAR(100))
    subscribe_date = Column(VARCHAR(100))
    actual_contribution = Column(VARCHAR(100))
    contribution_date = Column(VARCHAR(100))
    detail = Column(Text)
    mark = Column(NUMBER(6, 0, False))
    add_time = Column(DateTime)
    agency_num = Column(VARCHAR(300))
    agency_name = Column(VARCHAR(300))
    batch = Column(VARCHAR(150))

class TycQybjJbxx(Base):
    __tablename__ = 'tyc_qybj_jbxx'
    
    id = Column(NUMBER(30, 0, False), primary_key=True)
    txt_id = Column(VARCHAR(800), index=True)
    company_name = Column(VARCHAR(1000), index=True)
    register_num = Column(VARCHAR(800))
    tissue_num = Column(VARCHAR(800))
    credit_num = Column(VARCHAR(800))
    company_type = Column(VARCHAR(800))
    taxpayer_num = Column(VARCHAR(800))
    industry = Column(VARCHAR(800))
    business_term = Column(VARCHAR(800))
    check_date = Column(VARCHAR(800))
    register_office = Column(VARCHAR(800))
    register_site = Column(VARCHAR(800))
    register_fund = Column(VARCHAR(800))
    register_date = Column(VARCHAR(800))
    company_status = Column(VARCHAR(800))
    business_scope = Column(Text)
    telephone = Column(VARCHAR(400))
    email = Column(VARCHAR(800))
    url = Column(VARCHAR(4000))
    mark = Column(NUMBER(12, 0, False), server_default=text("'0'"))
    add_time = Column(DateTime)
    english_name = Column(VARCHAR(800))
    agency_num = Column(VARCHAR(800))
    agency_name = Column(VARCHAR(800))
    batch = Column(VARCHAR(400))
    industry_4 = Column(VARCHAR(400))
    branch = Column(VARCHAR(200))
    taxpayer_qualificate = Column(VARCHAR(100))
    person_size = Column(VARCHAR(50))
    paid_capital = Column(VARCHAR(50))
    insured_person = Column(VARCHAR(30))
    address_1 = Column(VARCHAR(50))
    address_2 = Column(VARCHAR(50))
    address_3 = Column(VARCHAR(50))
    business_term_begin = Column(VARCHAR(150))
    business_term_end = Column(VARCHAR(150))
    used_name = Column(VARCHAR(300))

class TycQybjQynb(Base):
    __tablename__ = 'tyc_qybj_qynb'
    
    add_time = Column(DateTime)
    mark = Column(NUMBER(6, 0, False), server_default=text("'0'"))
    year = Column(VARCHAR(100))
    id = Column(VARCHAR(50), primary_key=True)
    txt_id = Column(VARCHAR(500))
    detail_url = Column(VARCHAR(300))
    agency_num = Column(VARCHAR(300))
    agency_name = Column(VARCHAR(300))
    batch = Column(VARCHAR(200))
    company_name = Column(VARCHAR(1000))

class TycQybjSjkzq(Base):
    __tablename__ = 'tyc_qybj_sjkzq'
    
    id = Column(NUMBER(24, 0, False), primary_key=True)
    txt_id = Column(VARCHAR(300))
    company_name = Column(VARCHAR(500))
    add_time = Column(DateTime)
    mark = Column(NUMBER(6, 0, False), server_default=text("0"))
    agency_num = Column(VARCHAR(300))
    agency_name = Column(VARCHAR(300))
    batch = Column(VARCHAR(150))
    holding_name = Column(VARCHAR(300))
    invest_proportion = Column(VARCHAR(30))
    equity_chain = Column(VARCHAR(500))

class TycQybjZg(Base):
    __tablename__ = 'tyc_qybj_zgs'
    
    id = Column(NUMBER(24, 0, False), primary_key=True)
    txt_id = Column(VARCHAR(300))
    company_name = Column(VARCHAR(500))
    head_office_name = Column(VARCHAR(500))
    legal_representative = Column(VARCHAR(300))
    register_fund = Column(VARCHAR(300))
    establish_date = Column(VARCHAR(100))
    status = Column(VARCHAR(60))
    mark = Column(NUMBER(6, 0, False))
    add_time = Column(DateTime)
    agency_num = Column(VARCHAR(300))
    agency_name = Column(VARCHAR(300))
    batch = Column(VARCHAR(150))

class TycQybjZyry(Base):
    __tablename__ = 'tyc_qybj_zyry'
    
    mark = Column(NUMBER(6, 0, False), server_default=text("'0'"))
    add_time = Column(DateTime)
    person_name = Column(VARCHAR(200))
    id = Column(NUMBER(scale=0, asdecimal=False), primary_key=True)
    txt_id = Column(VARCHAR(500))
    company_name = Column(VARCHAR(1000))
    position = Column(VARCHAR(200))
    agency_num = Column(VARCHAR(300))
    agency_name = Column(VARCHAR(300))
    batch = Column(VARCHAR(200))

class TycQybjZzsyr(Base):
    __tablename__ = 'tyc_qybj_zzsyr'
    
    id = Column(NUMBER(24, 0, False), primary_key=True)
    txt_id = Column(VARCHAR(300))
    company_name = Column(VARCHAR(500))
    add_time = Column(DateTime)
    mark = Column(NUMBER(6, 0, False), server_default=text("0"))
    agency_num = Column(VARCHAR(300))
    agency_name = Column(VARCHAR(300))
    batch = Column(VARCHAR(150))
    beneficiary_name = Column(VARCHAR(300))
    shareholder_proportion = Column(VARCHAR(30))
    equity_chain = Column(VARCHAR(500))

class TycQyfzHxtd(Base):
    __tablename__ = 'tyc_qyfz_hxtd'
    
    id = Column(NUMBER(24, 0, False), primary_key=True)
    txt_id = Column(VARCHAR(800), index=True)
    company_name = Column(VARCHAR(1000), index=True)
    person_name = Column(VARCHAR(400))
    person_info = Column(Text)
    mark = Column(NUMBER(6, 0, False), server_default=text("'0'"))
    add_time = Column(DateTime)
    agency_num = Column(VARCHAR(800))
    agency_name = Column(VARCHAR(800))
    batch = Column(VARCHAR(400))
    position = Column(VARCHAR(200))

class TycQyfzJpxx(Base):
    __tablename__ = 'tyc_qyfz_jpxx'
    
    id = Column(NUMBER(24, 0, False), primary_key=True)
    txt_id = Column(VARCHAR(800), index=True)
    company_name = Column(VARCHAR(1000), index=True)
    jp_product = Column(VARCHAR(400))
    jp_area = Column(VARCHAR(800))
    jp_round = Column(VARCHAR(400))
    jp_industry = Column(VARCHAR(400))
    jp_business = Column(VARCHAR(4000))
    jp_date = Column(VARCHAR(400))
    jp_value = Column(VARCHAR(400))
    mark = Column(NUMBER(6, 0, False), server_default=text("'0'"))
    add_time = Column(DateTime)
    agency_num = Column(VARCHAR(800))
    agency_name = Column(VARCHAR(800))
    batch = Column(VARCHAR(400))

class TycQyfzQyyw(Base):
    __tablename__ = 'tyc_qyfz_qyyw'
    
    id = Column(NUMBER(24, 0, False), primary_key=True)
    txt_id = Column(VARCHAR(800), index=True)
    company_name = Column(VARCHAR(1000), index=True)
    business_name = Column(VARCHAR(400))
    business_quale = Column(VARCHAR(400))
    business_info = Column(VARCHAR(1600))
    mark = Column(NUMBER(6, 0, False), server_default=text("'0'"))
    add_time = Column(DateTime)
    agency_num = Column(VARCHAR(800))
    agency_name = Column(VARCHAR(800))
    batch = Column(VARCHAR(400))

class TycQyfzRzl(Base):
    __tablename__ = 'tyc_qyfz_rzls'
    
    id = Column(NUMBER(24, 0, False), primary_key=True)
    txt_id = Column(VARCHAR(800), index=True)
    company_name = Column(VARCHAR(1000), index=True)
    finance_date = Column(VARCHAR(400))
    finance_round = Column(VARCHAR(400))
    finance_value = Column(VARCHAR(400))
    finance_money = Column(VARCHAR(400))
    finance_ratio = Column(VARCHAR(400))
    finance_investor = Column(VARCHAR(400))
    finance_source = Column(VARCHAR(400))
    mark = Column(NUMBER(6, 0, False), server_default=text("'0'"))
    add_time = Column(DateTime)
    agency_num = Column(VARCHAR(800))
    agency_name = Column(VARCHAR(800))
    batch = Column(VARCHAR(400))
    event_date = Column(VARCHAR(100))

class TycQyfzSmjj(Base):
    __tablename__ = 'tyc_qyfz_smjj'
    
    id = Column(NUMBER(24, 0, False), primary_key=True)
    txt_id = Column(VARCHAR(300))
    company_name = Column(VARCHAR(500))
    administrator_name = Column(VARCHAR(300))
    legal_representative = Column(VARCHAR(100))
    institutional_type = Column(VARCHAR(200))
    registration_number = Column(VARCHAR(100))
    establish_date = Column(VARCHAR(100))
    detail = Column(Text)
    mark = Column(NUMBER(6, 0, False))
    add_time = Column(DateTime)
    agency_num = Column(VARCHAR(300))
    agency_name = Column(VARCHAR(300))
    batch = Column(VARCHAR(150))

class TycQyfzTzjg(Base):
    __tablename__ = 'tyc_qyfz_tzjg'
    
    id = Column(NUMBER(24, 0, False), primary_key=True)
    txt_id = Column(VARCHAR(300))
    company_name = Column(VARCHAR(500))
    invest_institution = Column(VARCHAR(300))
    establish_date = Column(VARCHAR(100))
    origin_place = Column(VARCHAR(50))
    abstract = Column(VARCHAR(1000))
    mark = Column(NUMBER(6, 0, False))
    add_time = Column(DateTime)
    agency_num = Column(VARCHAR(300))
    agency_name = Column(VARCHAR(300))
    batch = Column(VARCHAR(150))

class TycQyfzTzsj(Base):
    __tablename__ = 'tyc_qyfz_tzsj'
    
    id = Column(NUMBER(24, 0, False), primary_key=True)
    txt_id = Column(VARCHAR(800), index=True)
    company_name = Column(VARCHAR(1000), index=True)
    touzi_date = Column(VARCHAR(400))
    touzi_round = Column(VARCHAR(400))
    touzi_money = Column(VARCHAR(400))
    touzi_ent = Column(VARCHAR(4000))
    touzi_product = Column(VARCHAR(400))
    touzi_area = Column(VARCHAR(400))
    touzi_industry = Column(VARCHAR(400))
    touzi_business = Column(VARCHAR(4000))
    mark = Column(NUMBER(6, 0, False), server_default=text("'0'"))
    add_time = Column(DateTime)
    agency_num = Column(VARCHAR(800))
    agency_name = Column(VARCHAR(800))
    batch = Column(VARCHAR(400))

class TycSffxBzxr(Base):
    __tablename__ = 'tyc_sffx_bzxr'
    
    id = Column(NUMBER(24, 0, False), primary_key=True)
    record_date = Column(VARCHAR(300))
    execute_underlying = Column(VARCHAR(80))
    case_number = Column(VARCHAR(400))
    court = Column(VARCHAR(400))
    txt_id = Column(VARCHAR(500), index=True)
    company_name = Column(VARCHAR(1000), index=True)
    add_time = Column(DateTime)
    mark = Column(NUMBER(6, 0, False), server_default=text("'0'"))
    agency_num = Column(VARCHAR(800))
    agency_name = Column(VARCHAR(800))
    batch = Column(VARCHAR(400))
    detail = Column(Text)

class TycSffxFls(Base):
    __tablename__ = 'tyc_sffx_flss'
    
    id = Column(NUMBER(24, 0, False), primary_key=True)
    judgment_date = Column(VARCHAR(300))
    judgment_document = Column(Text)
    case_type = Column(VARCHAR(200))
    case_number = Column(VARCHAR(400))
    document_url = Column(VARCHAR(800))
    txt_id = Column(VARCHAR(500), index=True)
    company_name = Column(VARCHAR(1000), index=True)
    add_time = Column(DateTime)
    detail_status = Column(NUMBER(6, 0, False), server_default=text("'0'"))
    mark = Column(NUMBER(6, 0, False), server_default=text("'0'"))
    case_identity = Column(VARCHAR(1020))
    agency_num = Column(VARCHAR(800))
    agency_name = Column(VARCHAR(800))
    batch = Column(VARCHAR(400))
    judgment_name = Column(VARCHAR(500))

class TycSffxFygg(Base):
    __tablename__ = 'tyc_sffx_fygg'
    
    id = Column(NUMBER(24, 0, False), primary_key=True)
    txt_id = Column(VARCHAR(500), index=True)
    company_name = Column(VARCHAR(1000), index=True)
    announcement_date = Column(VARCHAR(240))
    plaintiff = Column(VARCHAR(800))
    defendant = Column(VARCHAR(4000))
    announcement_type = Column(VARCHAR(400))
    court = Column(VARCHAR(800))
    detail_info = Column(Text)
    mark = Column(NUMBER(6, 0, False), server_default=text("'0'"))
    add_time = Column(DateTime)
    agency_num = Column(VARCHAR(800))
    agency_name = Column(VARCHAR(800))
    batch = Column(VARCHAR(400))

class TycSffxKtgg(Base):
    __tablename__ = 'tyc_sffx_ktgg'
    
    id = Column(NUMBER(24, 0, False), primary_key=True)
    txt_id = Column(VARCHAR(300))
    company_name = Column(VARCHAR(500))
    add_time = Column(DateTime)
    agency_num = Column(VARCHAR(300))
    batch = Column(VARCHAR(150))
    trial_date = Column(VARCHAR(100))
    cause_action = Column(VARCHAR(100))
    plaintiff = Column(VARCHAR(500))
    defendant = Column(VARCHAR(200))
    detail = Column(Text)
    mark = Column(NUMBER(6, 0, False), server_default=text("'0'"))
    agency_name = Column(VARCHAR(300))
    reference_num = Column(VARCHAR(100))

class TycSffxLaxx(Base):
    __tablename__ = 'tyc_sffx_laxx'
    
    id = Column(NUMBER(24, 0, False), primary_key=True)
    txt_id = Column(VARCHAR(300))
    company_name = Column(VARCHAR(500))
    filing_date = Column(VARCHAR(100))
    case_number = Column(VARCHAR(400))
    case_action = Column(VARCHAR(300))
    plaintiff = Column(VARCHAR(300))
    defendant = Column(VARCHAR(300))
    detail = Column(Text)
    mark = Column(NUMBER(6, 0, False))
    add_time = Column(DateTime)
    agency_num = Column(VARCHAR(300))
    agency_name = Column(VARCHAR(300))
    batch = Column(VARCHAR(150))

class TycSffxSfxz(Base):
    __tablename__ = 'tyc_sffx_sfxz'
    
    id = Column(NUMBER(24, 0, False), primary_key=True)
    txt_id = Column(VARCHAR(300))
    company_name = Column(VARCHAR(500))
    add_time = Column(DateTime)
    mark = Column(NUMBER(6, 0, False), server_default=text("0"))
    agency_num = Column(VARCHAR(300))
    agency_name = Column(VARCHAR(300))
    batch = Column(VARCHAR(150))
    enforcement_person = Column(VARCHAR(50))
    equity_amount = Column(VARCHAR(50))
    executive_court = Column(VARCHAR(150))
    approval_num = Column(VARCHAR(150))
    status = Column(VARCHAR(100))
    detail = Column(Text)

class TycSffxSxr(Base):
    __tablename__ = 'tyc_sffx_sxr'
    
    id = Column(NUMBER(24, 0, False), primary_key=True)
    case_date = Column(VARCHAR(160))
    case_number = Column(VARCHAR(4000))
    execution_court = Column(VARCHAR(800))
    performance_state = Column(VARCHAR(80))
    execute_number = Column(VARCHAR(800))
    detail_info = Column(Text)
    txt_id = Column(VARCHAR(800), index=True)
    company_name = Column(VARCHAR(1000), index=True)
    add_time = Column(DateTime)
    mark = Column(NUMBER(6, 0, False), server_default=text("'0'"))
    agency_num = Column(VARCHAR(800))
    agency_name = Column(VARCHAR(800))
    batch = Column(VARCHAR(400))

class TycYearDwtz(Base):
    __tablename__ = 'tyc_year_dwtz'
    
    mark = Column(NUMBER(6, 0, False), server_default=text("'0'"))
    add_time = Column(DateTime)
    year = Column(VARCHAR(100))
    id = Column(NUMBER(scale=0, asdecimal=False), primary_key=True)
    txt_id = Column(VARCHAR(500))
    company_name = Column(VARCHAR(1000))
    outbound_company = Column(VARCHAR(200))
    credit_num = Column(VARCHAR(200))
    agency_num = Column(VARCHAR(300))
    agency_name = Column(VARCHAR(300))
    batch = Column(VARCHAR(150))

class TycYearGdczxx(Base):
    __tablename__ = 'tyc_year_gdczxx'
    
    mark = Column(NUMBER(6, 0, False), server_default=text("'0'"))
    add_time = Column(DateTime)
    year = Column(VARCHAR(100))
    id = Column(NUMBER(scale=0, asdecimal=False), primary_key=True)
    txt_id = Column(VARCHAR(500))
    company_name = Column(VARCHAR(1000))
    shareholder = Column(VARCHAR(300))
    subscribe_contribution = Column(VARCHAR(300))
    contribution_time = Column(VARCHAR(300))
    contribution_style = Column(VARCHAR(300))
    actual_contribution = Column(VARCHAR(300))
    actual_time = Column(VARCHAR(300))
    actual_style = Column(VARCHAR(300))
    agency_num = Column(VARCHAR(300))
    agency_name = Column(VARCHAR(300))
    batch = Column(VARCHAR(200))

class TycYearGqbg(Base):
    __tablename__ = 'tyc_year_gqbg'
    
    id = Column(NUMBER(24, 0, False), primary_key=True)
    txt_id = Column(VARCHAR(300))
    company_name = Column(VARCHAR(500))
    shareholder = Column(VARCHAR(100))
    before_equity_ratio = Column(VARCHAR(20))
    after_equity_ratio = Column(VARCHAR(20))
    equity_change_date = Column(VARCHAR(100))
    mark = Column(NUMBER(6, 0, False))
    add_time = Column(DateTime)
    agency_num = Column(VARCHAR(300))
    agency_name = Column(VARCHAR(300))
    batch = Column(VARCHAR(150))
    year = Column(VARCHAR(60))

class TycYearJbxx(Base):
    __tablename__ = 'tyc_year_jbxx'
    
    mark = Column(NUMBER(6, 0, False), server_default=text("'0'"))
    add_time = Column(DateTime)
    year = Column(VARCHAR(100))
    id = Column(NUMBER(scale=0, asdecimal=False), primary_key=True)
    txt_id = Column(VARCHAR(500))
    company_name = Column(VARCHAR(1000))
    credit_num = Column(VARCHAR(300))
    ent_name = Column(VARCHAR(1000))
    company_tel = Column(VARCHAR(300))
    postal_code = Column(VARCHAR(300))
    manager_state = Column(VARCHAR(100))
    people_count = Column(VARCHAR(300))
    email = Column(VARCHAR(300))
    website = Column(VARCHAR(300))
    company_address = Column(VARCHAR(300))
    buy_equity = Column(VARCHAR(300))
    agency_num = Column(VARCHAR(300))
    agency_name = Column(VARCHAR(300))
    batch = Column(VARCHAR(150))

class TycYearSbxx(Base):
    __tablename__ = 'tyc_year_sbxx'
    
    id = Column(NUMBER(24, 0, False), primary_key=True)
    txt_id = Column(VARCHAR(300))
    company_name = Column(VARCHAR(500))
    endowment_insurance = Column(VARCHAR(20))
    medical_insurance = Column(VARCHAR(20))
    birth_insurance = Column(VARCHAR(20))
    unemployment_insurance = Column(VARCHAR(20))
    commercial_insurance = Column(VARCHAR(20))
    mark = Column(NUMBER(6, 0, False), server_default=text("'0'"))
    add_time = Column(DateTime)
    agency_num = Column(VARCHAR(300))
    agency_name = Column(VARCHAR(300))
    batch = Column(VARCHAR(150))
    year = Column(VARCHAR(60))

class TycYearWzhwdxx(Base):
    __tablename__ = 'tyc_year_wzhwdxx'
    
    mark = Column(NUMBER(6, 0, False), server_default=text("'0'"))
    add_time = Column(DateTime)
    year = Column(VARCHAR(150))
    id = Column(NUMBER(scale=0, asdecimal=False), primary_key=True)
    txt_id = Column(VARCHAR(500))
    company_name = Column(VARCHAR(1000))
    website_type = Column(VARCHAR(300))
    web_name = Column(VARCHAR(300))
    web_url = Column(VARCHAR(300))
    agency_num = Column(VARCHAR(300))
    agency_name = Column(VARCHAR(300))
    batch = Column(VARCHAR(150))

class TycYearXgsx(Base):
    __tablename__ = 'tyc_year_xgsx'
    
    id = Column(NUMBER(24, 0, False), primary_key=True)
    txt_id = Column(VARCHAR(300))
    company_name = Column(VARCHAR(500))
    date_changed = Column(VARCHAR(100))
    modification_matters = Column(VARCHAR(300))
    before_modification = Column(VARCHAR(100))
    after_modification = Column(VARCHAR(100))
    mark = Column(NUMBER(6, 0, False))
    add_time = Column(DateTime)
    agency_num = Column(VARCHAR(300))
    agency_name = Column(VARCHAR(300))
    batch = Column(VARCHAR(150))
    year = Column(VARCHAR(60))

class TycYearZczk(Base):
    __tablename__ = 'tyc_year_zczk'
    
    mark = Column(NUMBER(6, 0, False), server_default=text("'0'"))
    add_time = Column(DateTime)
    year = Column(VARCHAR(520))
    id = Column(NUMBER(scale=0, asdecimal=False), primary_key=True)
    txt_id = Column(VARCHAR(500))
    company_name = Column(VARCHAR(1000))
    total_assets = Column(VARCHAR(300))
    total_sales = Column(VARCHAR(300))
    operation_income = Column(VARCHAR(300))
    total_tax = Column(VARCHAR(300))
    total_income = Column(VARCHAR(300))
    total_profit = Column(VARCHAR(300))
    net_profit = Column(VARCHAR(300))
    total_debt = Column(VARCHAR(300))
    agency_num = Column(VARCHAR(300))
    agency_name = Column(VARCHAR(300))
    batch = Column(VARCHAR(150))

class TycZscqSbxx(Base):
    __tablename__ = 'tyc_zscq_sbxx'
    
    add_time = Column(DateTime)
    id = Column(NUMBER(scale=0, asdecimal=False), primary_key=True)
    apply_date = Column(VARCHAR(200))
    trademark = Column(VARCHAR(300))
    trademark_name = Column(VARCHAR(500))
    registration_number = Column(VARCHAR(300))
    type = Column(VARCHAR(150))
    status = Column(VARCHAR(200))
    txt_id = Column(VARCHAR(500))
    company_name = Column(VARCHAR(1000))
    mark = Column(CHAR(5))
    agency_num = Column(VARCHAR(300))
    agency_name = Column(VARCHAR(300))
    batch = Column(VARCHAR(150))
    detail = Column(Text)

class TycZscqWzba(Base):
    __tablename__ = 'tyc_zscq_wzba'
    
    id = Column(NUMBER(24, 0, False), primary_key=True)
    audit_date = Column(VARCHAR(240))
    web_name = Column(VARCHAR(500))
    web_homepage = Column(VARCHAR(4000))
    domain_name = Column(VARCHAR(500))
    record_number = Column(VARCHAR(300))
    status = Column(VARCHAR(150))
    department_type = Column(VARCHAR(200))
    txt_id = Column(VARCHAR(500), index=True)
    company_name = Column(VARCHAR(1000), index=True)
    add_time = Column(DateTime)
    mark = Column(NUMBER(6, 0, False), server_default=text("'0'"))
    agency_num = Column(VARCHAR(800))
    agency_name = Column(VARCHAR(800))
    batch = Column(VARCHAR(400))

class TycZscqZl(Base):
    __tablename__ = 'tyc_zscq_zl'
    
    id = Column(NUMBER(24, 0, False), primary_key=True)
    apply_publish_date = Column(VARCHAR(300))
    patent_name = Column(VARCHAR(1000))
    apply_number = Column(VARCHAR(400))
    apply_publish_number = Column(VARCHAR(400))
    detail_info = Column(Text)
    txt_id = Column(VARCHAR(500), index=True)
    company_name = Column(VARCHAR(1000), index=True)
    add_time = Column(DateTime)
    mark = Column(NUMBER(6, 0, False), server_default=text("'0'"))
    agency_num = Column(VARCHAR(800))
    agency_name = Column(VARCHAR(800))
    batch = Column(VARCHAR(400))
    patent_type = Column(VARCHAR(100))

class TycZscqZpzzq(Base):
    __tablename__ = 'tyc_zscq_zpzzq'
    
    add_time = Column(DateTime)
    id = Column(NUMBER(scale=0, asdecimal=False), primary_key=True)
    company_name = Column(VARCHAR(1000))
    mark = Column(CHAR(1))
    txt_id = Column(VARCHAR(500))
    works_name = Column(VARCHAR(300))
    register_name = Column(VARCHAR(300))
    type = Column(VARCHAR(150))
    create_date = Column(VARCHAR(150))
    register_date = Column(VARCHAR(150))
    firstpublish_date = Column(VARCHAR(150))
    agency_num = Column(VARCHAR(300))
    agency_name = Column(VARCHAR(300))
    batch = Column(VARCHAR(150))

class TycZscqZzq(Base):
    __tablename__ = 'tyc_zscq_zzq'
    
    id = Column(NUMBER(24, 0, False), primary_key=True)
    approval_date = Column(VARCHAR(300))
    software_name = Column(VARCHAR(400))
    software_referred = Column(VARCHAR(400))
    registration_number = Column(VARCHAR(400))
    type_number = Column(VARCHAR(200))
    version_number = Column(VARCHAR(400))
    detail_info = Column(Text)
    txt_id = Column(VARCHAR(500))
    company_name = Column(VARCHAR(1000), index=True)
    add_time = Column(DateTime)
    mark = Column(NUMBER(6, 0, False), server_default=text("'0'"))
    agency_num = Column(VARCHAR(800))
    agency_name = Column(VARCHAR(800))
    batch = Column(VARCHAR(400))

def check_obj(cls_spider, cls_standard):
    cls_spider_dict = cls_spider.__dict__
    cls_standard_dict = cls_standard.__dict__
    change_dict = {}
    for k, v in cls_spider_dict.items():
        if v == cls_standard_dict[k]:
            pass
        else:
            change_dict[k] = v
    return change_dict

if __name__ == '__main__':
    our_user = single_oracle_orm.query(CompanyBasicInfo).filter_by(id=334).first()
    # print(our_user.__dict__)
    other = single_oracle_orm.query(CompanyBasicInfo).filter_by(id=335).first()
    check_result_dict = check_obj(our_user, other)
    print(check_result_dict)
