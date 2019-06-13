# coding: utf-8
from sqlalchemy import CHAR, Column, DateTime, Float, Table, Text, VARCHAR, text, create_engine
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
engine = create_engine('oracle://tyc:tyc@10.10.82.12:1521/tycprd', echo=True)
Database= sessionmaker(bind=engine)
single_oracle_orm=Database()
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


class CheckResult(Base):
    __tablename__ = 'check_result'

    id = Column(NUMBER(asdecimal=False), primary_key=True, server_default=text("0    "))
    add_time = Column(DateTime, nullable=False)
    table_name = Column(VARCHAR(200))
    table_field = Column(VARCHAR(2000), nullable=False)
    field_value_true = Column(VARCHAR(2000))
    field_value_false = Column(VARCHAR(2000))
    version = Column(VARCHAR(200))


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


t_company_11315_v = Table(
    'company_11315_v', metadata,
    Column('company_number', NUMBER(24, 0, False)),
    Column('url', VARCHAR(800)),
    Column('company_name', VARCHAR(1000)),
    Column('company_industry', VARCHAR(1600)),
    Column('address_1', VARCHAR(800)),
    Column('address_2', VARCHAR(800)),
    Column('address_3', VARCHAR(800)),
    Column('company_area', VARCHAR(2400)),
    Column('company_address', VARCHAR(2400)),
    Column('add_time', DateTime),
    Column('searched', NUMBER(6, 0, False)),
    Column('error', NUMBER(6, 0, False)),
    Column('parse', NUMBER(6, 0, False)),
    Column('mark', NUMBER(6, 0, False)),
    Column('branch', VARCHAR(300))
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


t_ogg_data_r_001_br_v = Table(
    'ogg_data_r_001_br_v', metadata,
    Column('data_date', DateTime),
    Column('branch_id', VARCHAR(12)),
    Column('jbxx_tab', VARCHAR(50)),
    Column('jbxx_count', NUMBER(asdecimal=False)),
    Column('jbxx_add_count', NUMBER(asdecimal=False)),
    Column('qyzx_tab', VARCHAR(50)),
    Column('qyzx_count', NUMBER(asdecimal=False)),
    Column('qyzx_add_count', NUMBER(asdecimal=False))
)


t_ogg_data_r_001_mth_v = Table(
    'ogg_data_r_001_mth_v', metadata,
    Column('data_date', DateTime),
    Column('branch', VARCHAR(12)),
    Column('tab', VARCHAR(50)),
    Column('cnt', NUMBER(asdecimal=False))
)


t_ogg_data_r_001_today_v = Table(
    'ogg_data_r_001_today_v', metadata,
    Column('data_date', DateTime),
    Column('branch', VARCHAR(12)),
    Column('tab', VARCHAR(50)),
    Column('cnt', NUMBER(asdecimal=False)),
    Column('add_cnt', NUMBER(asdecimal=False))
)


t_ogg_data_r_001_v = Table(
    'ogg_data_r_001_v', metadata,
    Column('data_date', DateTime),
    Column('branch_id', VARCHAR(12)),
    Column('jbxx_tab', VARCHAR(50)),
    Column('fre_fllag', CHAR(3)),
    Column('cnt', NUMBER(asdecimal=False)),
    Column('today_cnt', NUMBER(asdecimal=False))
)


t_ogg_data_r_001_year_v = Table(
    'ogg_data_r_001_year_v', metadata,
    Column('data_date', DateTime),
    Column('branch', VARCHAR(12)),
    Column('tab', VARCHAR(50)),
    Column('cnt', NUMBER(asdecimal=False))
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
    aquity_amount = Column(Float, server_default=text("'0.00'"))
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
    aquity_amount = Column(Float, server_default=text("'0.00'"))
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


t_tyc_jyfx_hbcf = Table(
    'tyc_jyfx_hbcf', metadata,
    Column('id', NUMBER(24, 0, False), nullable=False),
    Column('txt_id', VARCHAR(300)),
    Column('company_name', VARCHAR(500)),
    Column('departure_date', VARCHAR(100)),
    Column('decision_num', VARCHAR(100)),
    Column('punishment_cause', VARCHAR(500)),
    Column('penalty_result', VARCHAR(1000)),
    Column('penalty_unites', VARCHAR(300)),
    Column('detail', Text),
    Column('mark', NUMBER(6, 0, False)),
    Column('add_time', DateTime),
    Column('agency_num', VARCHAR(300)),
    Column('agency_name', VARCHAR(300)),
    Column('batch', VARCHAR(150))
)


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


t_tyc_jyfx_sswf = Table(
    'tyc_jyfx_sswf', metadata,
    Column('id', NUMBER(24, 0, False), nullable=False),
    Column('txt_id', VARCHAR(300)),
    Column('company_name', VARCHAR(500)),
    Column('taxpayer', VARCHAR(500)),
    Column('tax_authority', VARCHAR(300)),
    Column('case_character', VARCHAR(100)),
    Column('detail', Text),
    Column('mark', NUMBER(6, 0, False)),
    Column('add_time', DateTime),
    Column('agency_num', VARCHAR(300)),
    Column('agency_name', VARCHAR(300)),
    Column('batch', VARCHAR(150))
)


t_tyc_jyfx_tddy = Table(
    'tyc_jyfx_tddy', metadata,
    Column('id', NUMBER(24, 0, False), nullable=False),
    Column('txt_id', VARCHAR(300)),
    Column('company_name', VARCHAR(500)),
    Column('located', VARCHAR(500)),
    Column('start_end_time', VARCHAR(200)),
    Column('administrative_area', VARCHAR(50)),
    Column('mortgage_area', VARCHAR(50)),
    Column('mortgage_land_use', VARCHAR(200)),
    Column('detail', Text),
    Column('mark', NUMBER(6, 0, False)),
    Column('add_time', DateTime),
    Column('agency_num', VARCHAR(300)),
    Column('agency_name', VARCHAR(300)),
    Column('batch', VARCHAR(150))
)


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


t_tyc_jyfx_xzch_xyzg = Table(
    'tyc_jyfx_xzch_xyzg', metadata,
    Column('id', NUMBER(24, 0, False), nullable=False),
    Column('txt_id', VARCHAR(300)),
    Column('company_name', VARCHAR(500)),
    Column('decision_date', VARCHAR(100)),
    Column('decision_num', VARCHAR(200)),
    Column('punishment_cause', VARCHAR(1000)),
    Column('penalty_result', VARCHAR(1000)),
    Column('punishment_organ', VARCHAR(300)),
    Column('detail', Text),
    Column('mark', NUMBER(6, 0, False)),
    Column('add_time', DateTime),
    Column('agency_num', VARCHAR(300)),
    Column('agency_name', VARCHAR(300)),
    Column('batch', VARCHAR(150))
)


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


t_tyc_jyzk_ccjc = Table(
    'tyc_jyzk_ccjc', metadata,
    Column('add_time', DateTime),
    Column('id', NUMBER(scale=0, asdecimal=False)),
    Column('type', VARCHAR(150)),
    Column('result', VARCHAR(300)),
    Column('check_department', VARCHAR(150)),
    Column('txt_id', VARCHAR(500)),
    Column('company_name', VARCHAR(1000)),
    Column('mark', CHAR(1)),
    Column('agency_num', VARCHAR(300)),
    Column('agency_name', VARCHAR(300)),
    Column('batch', VARCHAR(150)),
    Column('check_date', VARCHAR(50))
)


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


t_tyc_jyzk_dkgs = Table(
    'tyc_jyzk_dkgs', metadata,
    Column('id', NUMBER(24, 0, False), nullable=False),
    Column('txt_id', VARCHAR(300)),
    Column('company_name', VARCHAR(500)),
    Column('release_date', VARCHAR(100)),
    Column('site_location', VARCHAR(1000)),
    Column('administrative_area', VARCHAR(200)),
    Column('acreage', VARCHAR(50)),
    Column('land_use', VARCHAR(100)),
    Column('publish_organ', VARCHAR(300)),
    Column('detail', Text),
    Column('mark', NUMBER(6, 0, False)),
    Column('add_time', DateTime),
    Column('agency_num', VARCHAR(300)),
    Column('agency_name', VARCHAR(300)),
    Column('batch', VARCHAR(150))
)


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


t_tyc_jyzk_gys = Table(
    'tyc_jyzk_gys', metadata,
    Column('id', NUMBER(24, 0, False), nullable=False),
    Column('txt_id', VARCHAR(300)),
    Column('company_name', VARCHAR(500)),
    Column('provider', VARCHAR(500)),
    Column('purchase_proportion', VARCHAR(20)),
    Column('purchase_amount', VARCHAR(20)),
    Column('report_period', VARCHAR(100)),
    Column('data_sources', VARCHAR(100)),
    Column('incidence_relation', VARCHAR(100)),
    Column('mark', NUMBER(6, 0, False)),
    Column('add_time', DateTime),
    Column('agency_num', VARCHAR(300)),
    Column('agency_name', VARCHAR(300)),
    Column('batch', VARCHAR(150))
)


class TycJyzkJckxy(Base):
    __tablename__ = 'tyc_jyzk_jckxy'

    id = Column(NUMBER(24, 0, False), primary_key=True)
    txt_id = Column(VARCHAR(500))
    company_name = Column(VARCHAR(1000))
    register_customs = Column(VARCHAR(300))
    customs_number = Column(VARCHAR(400))
    manager_type = Column(VARCHAR(400))
    detail_info = Column(Text)
    mark = Column(NUMBER(6, 0, False))
    add_time = Column(DateTime)
    agency_num = Column(VARCHAR(800))
    agency_name = Column(VARCHAR(800))
    batch = Column(VARCHAR(400))
    id_ktl = Column(NUMBER(scale=0, asdecimal=False))
    industry_category = Column(VARCHAR(50))
    register_date = Column(VARCHAR(100))


t_tyc_jyzk_kh = Table(
    'tyc_jyzk_kh', metadata,
    Column('id', NUMBER(24, 0, False), nullable=False),
    Column('txt_id', VARCHAR(300)),
    Column('company_name', VARCHAR(500)),
    Column('client', VARCHAR(500)),
    Column('sale_proportion', VARCHAR(20)),
    Column('sale_amount', VARCHAR(20)),
    Column('report_period', VARCHAR(100)),
    Column('data_sources', VARCHAR(100)),
    Column('incidence_relation', VARCHAR(100)),
    Column('mark', NUMBER(6, 0, False)),
    Column('add_time', DateTime),
    Column('agency_num', VARCHAR(300)),
    Column('agency_name', VARCHAR(300)),
    Column('batch', VARCHAR(150))
)


t_tyc_jyzk_swpj = Table(
    'tyc_jyzk_swpj', metadata,
    Column('add_time', DateTime),
    Column('year', VARCHAR(150)),
    Column('id', NUMBER(scale=0, asdecimal=False)),
    Column('tax_rating', VARCHAR(150)),
    Column('tax_type', VARCHAR(150)),
    Column('tax_identification_number', VARCHAR(300)),
    Column('evaluate_department', VARCHAR(300)),
    Column('txt_id', VARCHAR(500)),
    Column('company_name', VARCHAR(1000)),
    Column('mark', CHAR(1)),
    Column('agency_num', VARCHAR(300)),
    Column('agency_name', VARCHAR(300)),
    Column('batch', VARCHAR(150))
)


t_tyc_jyzk_tdzr = Table(
    'tyc_jyzk_tdzr', metadata,
    Column('id', NUMBER(24, 0, False), nullable=False),
    Column('txt_id', VARCHAR(300)),
    Column('company_name', VARCHAR(500)),
    Column('trade_date', VARCHAR(100)),
    Column('located', VARCHAR(500)),
    Column('land_area', VARCHAR(20)),
    Column('former_land_user', VARCHAR(500)),
    Column('current_land_user', VARCHAR(500)),
    Column('transfer_price', VARCHAR(20)),
    Column('detail', Text),
    Column('mark', NUMBER(6, 0, False)),
    Column('add_time', DateTime),
    Column('agency_num', VARCHAR(300)),
    Column('agency_name', VARCHAR(300)),
    Column('batch', VARCHAR(150))
)


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
    mark = Column(NUMBER(6, 0, False))
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


t_tyc_qybj_dwtz = Table(
    'tyc_qybj_dwtz', metadata,
    Column('invest_company', VARCHAR(800)),
    Column('invest_person', VARCHAR(800)),
    Column('invest_fund', VARCHAR(800)),
    Column('invest_amount', VARCHAR(800)),
    Column('invest_ratio', VARCHAR(800)),
    Column('invest_date', VARCHAR(800)),
    Column('invest_status', VARCHAR(800)),
    Column('mark', NUMBER(6, 0, False)),
    Column('add_time', DateTime),
    Column('agency_num', VARCHAR(800)),
    Column('agency_name', VARCHAR(800)),
    Column('batch', VARCHAR(400)),
    Column('id', VARCHAR(50)),
    Column('txt_id', VARCHAR(500)),
    Column('company_name', VARCHAR(1000)),
    Column('invest_company_ktl', VARCHAR(200))
)


t_tyc_qybj_fzjg = Table(
    'tyc_qybj_fzjg', metadata,
    Column('add_time', DateTime),
    Column('mark', NUMBER(6, 0, False)),
    Column('id', VARCHAR(60)),
    Column('company_name', VARCHAR(1000)),
    Column('legal_representative', VARCHAR(500)),
    Column('status', VARCHAR(300)),
    Column('register_date', VARCHAR(200)),
    Column('txt_id', VARCHAR(500)),
    Column('ent_name', VARCHAR(1000)),
    Column('agency_num', VARCHAR(300)),
    Column('agency_name', VARCHAR(300)),
    Column('batch', VARCHAR(300))
)


t_tyc_qybj_gdxx = Table(
    'tyc_qybj_gdxx', metadata,
    Column('shareholder', VARCHAR(800)),
    Column('fund_ratio', VARCHAR(800)),
    Column('fund_subcribe', VARCHAR(800)),
    Column('mark', VARCHAR(32)),
    Column('agency_num', VARCHAR(800)),
    Column('agency_name', VARCHAR(800)),
    Column('batch', VARCHAR(800)),
    Column('id', VARCHAR(100)),
    Column('txt_id', VARCHAR(500)),
    Column('company_name', VARCHAR(1000)),
    Column('fund_time', VARCHAR(100)),
    Column('add_time', DateTime)
)


t_tyc_qybj_gsgs = Table(
    'tyc_qybj_gsgs', metadata,
    Column('id', NUMBER(24, 0, False), nullable=False),
    Column('txt_id', VARCHAR(300)),
    Column('company_name', VARCHAR(500)),
    Column('shareholder_sponsor', VARCHAR(500)),
    Column('shareholder_proportion', VARCHAR(50)),
    Column('subscribe_contribution', VARCHAR(100)),
    Column('subscribe_date', VARCHAR(100)),
    Column('actual_contribution', VARCHAR(100)),
    Column('contribution_date', VARCHAR(100)),
    Column('detail', Text),
    Column('mark', NUMBER(6, 0, False)),
    Column('add_time', DateTime),
    Column('agency_num', VARCHAR(300)),
    Column('agency_name', VARCHAR(300)),
    Column('batch', VARCHAR(150))
)


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


t_tyc_qybj_qynb = Table(
    'tyc_qybj_qynb', metadata,
    Column('add_time', DateTime),
    Column('mark', NUMBER(6, 0, False)),
    Column('year', VARCHAR(100)),
    Column('id', VARCHAR(50)),
    Column('txt_id', VARCHAR(500)),
    Column('detail_url', VARCHAR(300)),
    Column('agency_num', VARCHAR(300)),
    Column('agency_name', VARCHAR(300)),
    Column('batch', VARCHAR(200)),
    Column('company_name', VARCHAR(1000)),
    Column('detail_url_ktl', VARCHAR(300))
)


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


t_tyc_qybj_zgs = Table(
    'tyc_qybj_zgs', metadata,
    Column('id', NUMBER(24, 0, False), nullable=False),
    Column('txt_id', VARCHAR(300)),
    Column('company_name', VARCHAR(500)),
    Column('head_office_name', VARCHAR(500)),
    Column('legal_representative', VARCHAR(300)),
    Column('register_fund', VARCHAR(300)),
    Column('establish_date', VARCHAR(100)),
    Column('status', VARCHAR(60)),
    Column('mark', NUMBER(6, 0, False)),
    Column('add_time', DateTime),
    Column('agency_num', VARCHAR(300)),
    Column('agency_name', VARCHAR(300)),
    Column('batch', VARCHAR(150))
)


t_tyc_qybj_zyry = Table(
    'tyc_qybj_zyry', metadata,
    Column('mark', NUMBER(6, 0, False), server_default=text("'0'")),
    Column('add_time', DateTime),
    Column('person_name', VARCHAR(200)),
    Column('id', NUMBER(scale=0, asdecimal=False)),
    Column('txt_id', VARCHAR(500)),
    Column('company_name', VARCHAR(1000)),
    Column('position', VARCHAR(200)),
    Column('agency_num', VARCHAR(300)),
    Column('agency_name', VARCHAR(300)),
    Column('batch', VARCHAR(200))
)


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


t_tyc_qyfz_smjj = Table(
    'tyc_qyfz_smjj', metadata,
    Column('id', NUMBER(24, 0, False), nullable=False),
    Column('txt_id', VARCHAR(300)),
    Column('company_name', VARCHAR(500)),
    Column('administrator_name', VARCHAR(300)),
    Column('legal_representative', VARCHAR(100)),
    Column('institutional_type', VARCHAR(200)),
    Column('registration_number', VARCHAR(100)),
    Column('establish_date', VARCHAR(100)),
    Column('detail', Text),
    Column('mark', NUMBER(6, 0, False)),
    Column('add_time', DateTime),
    Column('agency_num', VARCHAR(300)),
    Column('agency_name', VARCHAR(300)),
    Column('batch', VARCHAR(150))
)


t_tyc_qyfz_tzjg = Table(
    'tyc_qyfz_tzjg', metadata,
    Column('id', NUMBER(24, 0, False), nullable=False),
    Column('txt_id', VARCHAR(300)),
    Column('company_name', VARCHAR(500)),
    Column('invest_institution', VARCHAR(300)),
    Column('establish_date', VARCHAR(100)),
    Column('origin_place', VARCHAR(50)),
    Column('abstract', VARCHAR(1000)),
    Column('mark', NUMBER(6, 0, False)),
    Column('add_time', DateTime),
    Column('agency_num', VARCHAR(300)),
    Column('agency_name', VARCHAR(300)),
    Column('batch', VARCHAR(150))
)


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
    text_info = Column(Text)
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
    mark = Column(NUMBER(6, 0, False))
    agency_name = Column(VARCHAR(300))
    reference_num = Column(VARCHAR(100))


t_tyc_sffx_laxx = Table(
    'tyc_sffx_laxx', metadata,
    Column('id', NUMBER(24, 0, False), nullable=False),
    Column('txt_id', VARCHAR(300)),
    Column('company_name', VARCHAR(500)),
    Column('filing_date', VARCHAR(100)),
    Column('case_number', VARCHAR(400)),
    Column('case_action', VARCHAR(300)),
    Column('plaintiff', VARCHAR(300)),
    Column('defendant', VARCHAR(300)),
    Column('detail', Text),
    Column('mark', NUMBER(6, 0, False)),
    Column('add_time', DateTime),
    Column('agency_num', VARCHAR(300)),
    Column('agency_name', VARCHAR(300)),
    Column('batch', VARCHAR(150))
)


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


t_tyc_year_dwtz = Table(
    'tyc_year_dwtz', metadata,
    Column('mark', NUMBER(6, 0, False), server_default=text("'0'")),
    Column('add_time', DateTime),
    Column('year', VARCHAR(100)),
    Column('id', NUMBER(scale=0, asdecimal=False)),
    Column('txt_id', VARCHAR(500)),
    Column('company_name', VARCHAR(1000)),
    Column('outbound_company', VARCHAR(200)),
    Column('credit_num', VARCHAR(200)),
    Column('agency_num', VARCHAR(300)),
    Column('agency_name', VARCHAR(300)),
    Column('batch', VARCHAR(150))
)


t_tyc_year_gdczxx = Table(
    'tyc_year_gdczxx', metadata,
    Column('mark', NUMBER(6, 0, False), server_default=text("'0'")),
    Column('add_time', DateTime),
    Column('year', VARCHAR(100)),
    Column('id', NUMBER(scale=0, asdecimal=False)),
    Column('txt_id', VARCHAR(500)),
    Column('company_name', VARCHAR(1000)),
    Column('shareholder', VARCHAR(300)),
    Column('subscribe_contribution', VARCHAR(300)),
    Column('contribution_time', VARCHAR(300)),
    Column('contribution_style', VARCHAR(300)),
    Column('actual_contribution', VARCHAR(300)),
    Column('actual_time', VARCHAR(300)),
    Column('actual_style', VARCHAR(300)),
    Column('agency_num', VARCHAR(300)),
    Column('agency_name', VARCHAR(300)),
    Column('batch', VARCHAR(200))
)


t_tyc_year_gqbg = Table(
    'tyc_year_gqbg', metadata,
    Column('id', NUMBER(24, 0, False), nullable=False),
    Column('txt_id', VARCHAR(300)),
    Column('company_name', VARCHAR(500)),
    Column('shareholder', VARCHAR(100)),
    Column('before_equity_ratio', VARCHAR(20)),
    Column('after_equity_ratio', VARCHAR(20)),
    Column('equity_change_date', VARCHAR(100)),
    Column('mark', NUMBER(6, 0, False)),
    Column('add_time', DateTime),
    Column('agency_num', VARCHAR(300)),
    Column('agency_name', VARCHAR(300)),
    Column('batch', VARCHAR(150)),
    Column('year', VARCHAR(60))
)


t_tyc_year_jbxx = Table(
    'tyc_year_jbxx', metadata,
    Column('mark', NUMBER(6, 0, False), server_default=text("'0'")),
    Column('add_time', DateTime),
    Column('year', VARCHAR(100)),
    Column('id', NUMBER(scale=0, asdecimal=False)),
    Column('txt_id', VARCHAR(500)),
    Column('company_name', VARCHAR(1000)),
    Column('credit_num', VARCHAR(300)),
    Column('ent_name', VARCHAR(1000)),
    Column('company_tel', VARCHAR(300)),
    Column('postal_code', VARCHAR(300)),
    Column('manager_state', VARCHAR(100)),
    Column('people_count', VARCHAR(300)),
    Column('email', VARCHAR(300)),
    Column('website', VARCHAR(300)),
    Column('company_address', VARCHAR(300)),
    Column('buy_equity', VARCHAR(300)),
    Column('agency_num', VARCHAR(300)),
    Column('agency_name', VARCHAR(300)),
    Column('batch', VARCHAR(150))
)


t_tyc_year_sbxx = Table(
    'tyc_year_sbxx', metadata,
    Column('id', NUMBER(24, 0, False), nullable=False),
    Column('txt_id', VARCHAR(300)),
    Column('company_name', VARCHAR(500)),
    Column('endowment_insurance', VARCHAR(20)),
    Column('medical_insurance', VARCHAR(20)),
    Column('birth_insurance', VARCHAR(20)),
    Column('unemployment_insurance', VARCHAR(20)),
    Column('commercial_insurance', VARCHAR(20)),
    Column('mark', NUMBER(6, 0, False)),
    Column('add_time', DateTime),
    Column('agency_num', VARCHAR(300)),
    Column('agency_name', VARCHAR(300)),
    Column('batch', VARCHAR(150)),
    Column('year', VARCHAR(60))
)


t_tyc_year_wzhwdxx = Table(
    'tyc_year_wzhwdxx', metadata,
    Column('mark', NUMBER(6, 0, False), server_default=text("'0'")),
    Column('add_time', DateTime),
    Column('year', VARCHAR(150)),
    Column('id', NUMBER(scale=0, asdecimal=False)),
    Column('txt_id', VARCHAR(500)),
    Column('company_name', VARCHAR(1000)),
    Column('website_type', VARCHAR(300)),
    Column('web_name', VARCHAR(300)),
    Column('web_url', VARCHAR(300)),
    Column('agency_num', VARCHAR(300)),
    Column('agency_name', VARCHAR(300)),
    Column('batch', VARCHAR(150))
)


t_tyc_year_xgsx = Table(
    'tyc_year_xgsx', metadata,
    Column('id', NUMBER(24, 0, False), nullable=False),
    Column('txt_id', VARCHAR(300)),
    Column('company_name', VARCHAR(500)),
    Column('date_changed', VARCHAR(100)),
    Column('modification_matters', VARCHAR(300)),
    Column('before_modification', VARCHAR(100)),
    Column('after_modification', VARCHAR(100)),
    Column('mark', NUMBER(6, 0, False)),
    Column('add_time', DateTime),
    Column('agency_num', VARCHAR(300)),
    Column('agency_name', VARCHAR(300)),
    Column('batch', VARCHAR(150)),
    Column('year', VARCHAR(60))
)


t_tyc_year_zczk = Table(
    'tyc_year_zczk', metadata,
    Column('mark', NUMBER(6, 0, False), server_default=text("'0'")),
    Column('add_time', DateTime),
    Column('year', VARCHAR(520)),
    Column('id', NUMBER(scale=0, asdecimal=False)),
    Column('txt_id', VARCHAR(500)),
    Column('company_name', VARCHAR(1000)),
    Column('total_assets', VARCHAR(300)),
    Column('total_sales', VARCHAR(300)),
    Column('operation_income', VARCHAR(300)),
    Column('total_tax', VARCHAR(300)),
    Column('total_income', VARCHAR(300)),
    Column('total_profit', VARCHAR(300)),
    Column('net_profit', VARCHAR(300)),
    Column('total_debt', VARCHAR(300)),
    Column('agency_num', VARCHAR(300)),
    Column('agency_name', VARCHAR(300)),
    Column('batch', VARCHAR(150))
)


t_tyc_zscq_sbxx = Table(
    'tyc_zscq_sbxx', metadata,
    Column('add_time', DateTime),
    Column('id', NUMBER(scale=0, asdecimal=False)),
    Column('apply_date', VARCHAR(200)),
    Column('trademark', VARCHAR(300)),
    Column('trademark_name', VARCHAR(500)),
    Column('registration_number', VARCHAR(300)),
    Column('type', VARCHAR(150)),
    Column('status', VARCHAR(200)),
    Column('txt_id', VARCHAR(500)),
    Column('company_name', VARCHAR(1000)),
    Column('mark', CHAR(5)),
    Column('agency_num', VARCHAR(300)),
    Column('agency_name', VARCHAR(300)),
    Column('batch', VARCHAR(150)),
    Column('detail', Text)
)


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


t_tyc_zscq_zpzzq = Table(
    'tyc_zscq_zpzzq', metadata,
    Column('add_time', DateTime),
    Column('id', NUMBER(scale=0, asdecimal=False)),
    Column('company_name', VARCHAR(1000)),
    Column('mark', CHAR(1)),
    Column('txt_id', VARCHAR(500)),
    Column('works_name', VARCHAR(300)),
    Column('register_name', VARCHAR(300)),
    Column('type', VARCHAR(150)),
    Column('create_date', VARCHAR(150)),
    Column('register_date', VARCHAR(150)),
    Column('firstpublish_date', VARCHAR(150)),
    Column('agency_num', VARCHAR(300)),
    Column('agency_name', VARCHAR(300)),
    Column('batch', VARCHAR(150))
)


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


def check_obj(cls_spider,cls_standard):
    cls_spider_dict=cls_spider.__dict__
    cls_standard_dict=cls_standard.__dict__
    change_dict={}
    for k,v in cls_spider_dict.items():
        if v==cls_standard_dict[k]:
            pass
        else:
            change_dict[k]=v
    return change_dict

if __name__ == '__main__':
    our_user = single_oracle_orm.query(CompanyBasicInfo).filter_by(id=334).first()
    # print(our_user.__dict__)
    other=single_oracle_orm.query(CompanyBasicInfo).filter_by(id=335).first()
    check_result_dict=check_obj(our_user,other)
    print(check_result_dict)
        
