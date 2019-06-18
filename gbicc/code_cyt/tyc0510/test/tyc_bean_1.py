# -*- coding:utf-8 -*-


# 公司列表搜索信息
class CompanyBasicInfo(object):
    search_name = ""
    ent_name = ""
    legal_representative = ""
    registered_capital = ""
    location = ""
    registration_date = ""
    score = ""
    status_type = ""
    url = ""
    txt_id = ""
    add_time = ""
    mark = ""
    agency_num = ""
    agency_name = ""
    batch = ""
    branch = ""
    table_name = "company_basic_info"
    column_name = "(branch,txt_id,search_name,company_name,legal_representative,registered_capital,registration_date,location,score,status_type,url,page_spider,parsed,mark,agency_num,agency_name,batch,add_time)"
    
    # sql = "insert into company_basic_info (branch,txt_id,search_name,company_name,legal_representative,registered_capital,registration_date,location,score,status_type,url,page_spider,parsed,mark,add_time,agency_num,agency_name,batch) values ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}',{},{},{},{},'{}','{}','{}').formate(branch,txt_id,search_name,company_name,legal_representative,registered_capital,registration_date,location,score,status_type,url,page_spider,parsed,mark,add_time,agency_num,agency_name,batch)"

# 企业背景-->基本信息
class TycQybjJbxx(object):
    # mongodb文本ID
    txtId = ''
    # 所属公司名称
    entName = ''
    # 工商注册号
    registerNum = ''
    # 组织机构代码
    tissueNum = ''
    # 统一信用代码
    creditNum = ''
    # 企业类型
    companyType = ''
    # 纳税人识别号
    taxpayerNum = ''
    # 行业
    industry = ''
    # 营业期限
    businessTerm = ''
    # 核准日期
    checkDate = ''
    # 登记机关
    registerOffice = ''
    # 注册地址
    registerSite = ''
    # 注册资本
    registerFund = ''
    # 注册时间
    registerDate = ''
    # 企业状态
    companyStatus = ''
    # 经营范围
    businessScope = ''
    # 电话
    telephone = ''
    # 邮箱
    email = ''
    # 网址
    url = ''
    # 标记号
    mark = ''
    # 添加时间
    add_time = ''
    # 新增曾用名
    used_name = ''
    # 英文名称
    englishName = ''
    # 纳税人资质
    taxQualificate = ''
    # 人员规模
    persionSize = ''
    # 实缴资本
    paidCapital = ''
    # 参保人数
    insuredPersion = ''
    # 机构号
    agency_num = ''
    # 机构名称
    agency_name = ''
    # 批次
    batch = ''
    # 银行分支机构号
    branch = ''
    table_name = "tyc_qybj_jbxx"
    column_name = "(insured_person,taxpayer_qualificate,person_size,paid_capital,txt_id,company_name,register_num,tissue_num,credit_num,company_type,taxpayer_num,industry,business_term,check_date,register_office,register_site,register_fund,register_date,company_status,business_scope,telephone,email,url,used_name,english_name,mark,agency_num,agency_name,batch,industry_4,branch,address_1,address_2,address_3,business_term_begin,business_term_end, add_time)"
    
    # sql = "insert into tyc_qybj_jbxx (insured_person,taxpayer_qualificate,person_size,paid_capital,txt_id,company_name,register_num,tissue_num,credit_num,company_type,taxpayer_num,industry,business_term,check_date,register_office,register_site,register_fund,register_date,company_status,business_scope,telephone,email,url,english_name,mark,add_time,agency_num,agency_name,batch,industry_4,branch) values ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}',{},{},'{}','{}','{}','{}','{}')".formate(insured_person,taxpayer_qualificate,person_size,paid_capital,txt_id,company_name,register_num,tissue_num,credit_num,company_type,taxpayer_num,industry,business_term,check_date,register_office,register_site,register_fund,register_date,company_status,business_scope,telephone,email,url,english_name,mark,add_time,agency_num,agency_name,batch,industry_4,branch)

# 企业背景-->主要人员
class TycQybjZyry(object):
    # mongodb文本ID
    txtId = ''
    # 所属公司名称
    entName = ''
    # 职位
    position = ''
    # 姓名
    name = ''
    # 标记号
    mark = ''
    # 添加时间
    add_time = ''
    # 机构号
    agency_num = ''
    # 机构名称
    agency_name = ''
    # 批次
    batch = ''
    table_name = "tyc_qybj_zyry"
    column_name = "(txt_id,company_name,position,person_name,mark,agency_num,agency_name,batch,add_time)"
    
    # sql = "insert into tyc_qybj_zyry (main_personal,txt_id,ent_name,position,name,mark,add_time,agency_num,agency_name,batch) values ('{}','{}','{}','{}','{}',{},{},'{}','{}','{}')".formate(main_personal,txt_id,ent_name,position,name,mark,add_time,agency_num,agency_name,batch)

# 企业背景-->股东信息
class TycQybjGdxx(object):
    # mongodb文本ID
    txtId = ''
    # 所属公司名称
    entName = ''
    # 股东
    shareholder = ''
    # 出资比例
    fundRatio = ''
    # 认缴出资
    fundSubcribe = ''
    # 出资时间
    fundTime = ''
    # 标记号
    mark = ''
    # 添加时间
    add_time = ''
    # 机构号
    agency_num = ''
    # 机构名称
    agency_name = ''
    # 批次
    batch = ''
    table_name = "tyc_qybj_gdxx"
    column_name = "(fund_time,txt_id,company_name,shareholder,fund_ratio,fund_subcribe,mark,agency_num,agency_name,batch,add_time)"
    
    # sql = "insert into tyc_qybj_gdxx (fund_time,txt_id,company_name,shareholder,fund_ratio,fund_subcribe,mark,add_time,agency_num,agency_name,batch) values ('{}','{}','{}','{}','{}','{}',{},{},'{}','{}','{}')".formate(fund_time,txt_id,company_name,shareholder,fund_ratio,fund_subcribe,mark,add_time,agency_num,agency_name,batch)

# 企业背景-->对外投资
class TycQybjDwtz(object):
    # mongodb文本ID
    txtId = ''
    # 所属公司名称
    entName = ''
    # 被投资企业名称
    investCompany = ''
    # 被投资法定代表人
    investPerson = ''
    # 注册资本
    investFund = ''
    # 投资数额
    investAmount = ''
    # 投资占比
    investRatio = ''
    # 注册时间
    investDate = ''
    # 状态
    investStatus = ''
    # 标记号
    mark = ''
    # 添加时间
    add_time = ''
    # 机构号
    agency_num = ''
    # 机构名称
    agency_name = ''
    # 批次
    batch = ''
    table_name = "tyc_qybj_dwtz"
    column_name = "(txt_id,company_name,invest_company,invest_person,invest_fund,invest_amount,invest_ratio,invest_date,invest_status,mark,agency_num,agency_name,batch,add_time)"
    
    # sql = "insert into tyc_qybj_dwtz (txt_id,company_name,invest_company,invest_person,invest_fund,invest_amount,invest_ratio,invest_date,invest_status,mark,add_time,agency_num,agency_name,batch) values ('{}','{}','{}','{}','{}','{}','{}','{}','{}',{},{},'{}','{}','{}')".formate(txt_id,company_name,invest_company,invest_person,invest_fund,invest_amount,invest_ratio,invest_date,invest_status,mark,add_time,agency_num,agency_name,batch)

# 企业背景-->变更记录
class TycQybjBgjl(object):
    # mongodb文本ID
    txtId = ''
    # 所属公司名称
    entName = ''
    # 变更时间
    alterDate = ''
    # 变更项目
    alterProject = ''
    # 变更前
    alterBefor = ''
    # 变更后
    alterAfter = ''
    # 标记号
    mark = ''
    # 添加时间
    add_time = ''
    # 机构号
    agency_num = ''
    # 机构名称
    agency_name = ''
    # 批次
    batch = ''
    table_name = "tyc_qybj_bgjl"
    column_name = "(txt_id,company_name,alter_date,alter_project,alter_befor,alter_after,mark,agency_num,agency_name,batch,add_time)"
    
    # sql = "insert into tyc_qybj_bgjl (txt_id,company_name,alter_date,alter_project,alter_befor,alter_after,mark,add_time,agency_num,agency_name,batch) values ('{}','{}','{}','{}','{}','{}',{},{},'{}','{}','{}')".formate(txt_id,company_name,alter_date,alter_project,alter_befor,alter_after,mark,add_time,agency_num,agency_name,batch)

# 企业背景-->分支机构
class TycQybjFzjg(object):
    # 企业名称
    ent_name = ""
    # 法定代表人
    legal_representative = ""
    # 状态
    status = ""
    # 注册时间
    registered_date = ""
    # mongodb文本ID
    txt_id = ""
    # 所属公司名称
    company_name = ""
    # 添加时间
    add_time = ""
    # 标记号
    mark = ""
    # 机构号
    agency_num = ''
    # 机构名称
    agency_name = ''
    # 批次
    batch = ''
    table_name = "tyc_qybj_fzjg"
    column_name = "(txt_id,company_name,ent_name,legal_representative,status,register_date,mark,agency_num,agency_name,batch,add_time)"
    # sql = "insert into tyc_qybj_fzjg (txt_id,ent_name,company_name,legal_representative,status,registered_date,mark,add_time,agency_num,agency_name,batch) values ('{}','{}','{}','{}','{}',{},{},{},'{}','{}','{}')".formate(txt_id,ent_name,company_name,legal_representative,status,registered_date,mark,add_time,agency_num,agency_name,batch)

# 企业发展-->融资历史
class TycQyfzRzls(object):
    # mongodb文本ID
    txtId = ''
    # 所属公司名称
    entName = ''
    # 披露日期
    financeDate = ''
    # 事件事件
    event_date = ''
    # 融资轮次
    financeRound = ''
    # 估值
    financeValue = ''
    # 交易金额
    financeMoney = ''
    # 比例
    financeRatio = ''
    # 投资方
    financeInvestor = ''
    # 新闻来源
    financeSource = ''
    # 标记号
    mark = ''
    # 添加时间
    add_time = ''
    # 机构号
    agency_num = ''
    # 机构名称
    agency_name = ''
    # 批次
    batch = ''
    table_name = "tyc_qyfz_rzls"
    column_name = "(batch,agency_name,agency_num,mark,finance_source,finance_investor,finance_ratio,finance_money,finance_value,finance_round,finance_date,event_date,company_name,txt_id,add_time)"
    
    # sql =  "insert into tyc_qyfz_rzls (batch,agency_name,agency_num,add_time,mark,finance_source,finance_investor,finance_ratio,finance_money,finance_value,finance_round,finance_date,ent_name,txt_id) values ('{}','{}','{}',{},{},'{}','{}','{}','{}','{}','{}','{}','{}','{}')".formate(batch,agency_name,agency_num,add_time,mark,finance_source,finance_investor,finance_ratio,finance_money,finance_value,finance_round,finance_date,ent_name,txt_id)

# 企业发展-->核心团队
class TycQyfzHxtd(object):
    # mongodb文本ID
    txtId = ''
    # 所属公司名称
    entName = ''
    # 人物名称
    personName = ''
    # 职位
    position = ''
    # 人物介绍
    personInfo = ''
    # 标记号
    mark = ''
    # 添加时间
    add_time = ''
    # 机构号
    agency_num = ''
    # 机构名称
    agency_name = ''
    # 批次
    batch = ''
    table_name = "tyc_qyfz_hxtd"
    column_name = "(txt_id,company_name,person_name,position,person_info,mark,agency_num,agency_name,batch,add_time)"
    
    # sql = "insert into tyc_qyfz_hxtd (txt_id,company_name,person_name,person_info,mark,add_time,agency_num,agency_name,batch) values ('{}','{}','{}','{}',{},{},'{}','{}','{}')".formate(txt_id,company_name,person_name,person_info,mark,add_time,agency_num,agency_name,batch)

# 企业发展-->企业业务
class TycQyfzQyyw(object):
    # mongodb文本ID
    txtId = ''
    # 所属公司名称
    entName = ''
    # 业务名称
    businessName = ''
    # 业务性质
    businessQuale = ''
    # 业务简介
    businessInfo = ''
    # 标记号
    mark = ''
    # 添加时间
    add_time = ''
    # 机构号
    agency_num = ''
    # 机构名称
    agency_name = ''
    # 批次
    batch = ''
    table_name = "tyc_qyfz_qyyw"
    column_name = "(batch,agency_name,agency_num,mark,business_info,business_quale,business_name,company_name,txt_id,add_time)"
    
    # sql = "insert into tyc_qyfz_qyyw (batch,agency_name,agency_num,add_time,mark,business_info,business_quale,business_name,company_name,txt_id) values ('{}','{}','{}',{},{},'{}','{}','{}','{}','{}')".formate(batch,agency_name,agency_num,add_time,mark,business_info,business_quale,business_name,company_name,txt_id)

# 企业发展-->投资事件
class TycQyfzTzsj(object):
    # mongodb文本ID
    txtId = ''
    # 所属公司名称
    entName = ''
    # 时间
    touziDate = ''
    # 轮次
    touziRound = ''
    # 金额
    touziMoney = ''
    # 投资方
    touziEnt = ''
    # 产品
    touziProduct = ''
    # 地区
    touziArea = ''
    # 行业
    touziIndustry = ''
    # 业务
    touziBusiness = ''
    # 标记号
    mark = ''
    # 添加时间
    add_time = ''
    # 机构号
    agency_num = ''
    # 机构名称
    agency_name = ''
    # 批次
    batch = ''
    table_name = "tyc_qyfz_tzsj"
    column_name = "(txt_id,company_name,touzi_date,touzi_round,touzi_money,touzi_ent,touzi_product,touzi_area,touzi_industry,touzi_business,mark,agency_num,agency_name,batch,add_time)"
    
    # sql = "insert into tyc_qyfz_tzsj (txt_id,company_name,touzi_date,touzi_round,touzi_money,touzi_ent,touzi_product,touzi_area,touzi_industry,touzi_business,mark,add_time,agency_num,agency_name,batch) values ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}',{},{},'{}','{}','{}')".formate(txt_id,company_name,touzi_date,touzi_round,touzi_money,touzi_ent,touzi_product,touzi_area,touzi_industry,touzi_business,mark,add_time,agency_num,agency_name,batch)

# 企业发展-->竞品信息
class TycQyfzJpxx(object):
    # mongodb文本ID
    txtId = ''
    # 所属公司名称
    entName = ''
    # 产品
    jpProduct = ''
    # 地区
    jpArea = ''
    # 当前轮次
    jpRound = ''
    # 行业
    jpIndustry = ''
    # 业务
    jpBusiness = ''
    # 成立时间
    jpDate = ''
    # 估值
    jpValue = ''
    # 标记号
    mark = ''
    # 添加时间
    add_time = ''
    # 机构号
    agency_num = ''
    # 机构名称
    agency_name = ''
    # 批次
    batch = ''
    table_name = "tyc_qyfz_jpxx"
    column_name = "(txt_id,company_name,jp_product,jp_area,jp_round,jp_industry,jp_business,jp_date,jp_value,mark,agency_num,agency_name,batch,add_time)"
    
    # sql = "insert into tyc_qyfz_jpxx (txt_id,company_name,jp_product,jp_area,jp_round,jp_industry,jp_business,jp_date,jp_value,mark,add_time,agency_num,agency_name,batch) values ('{}','{}','{}','{}','{}','{}','{}','{}','{}',{},{},'{}','{}','{}')".formate(txt_id,company_name,jp_product,jp_area,jp_round,jp_industry,jp_business,jp_date,jp_value,mark,add_time,agency_num,agency_name,batch)

# 法律诉讼
class TycSffxFlss(object):
    # mongodb文本ID
    txt_id = ""
    # 所属公司名称
    company_name = ""
    # 日期
    judgment_date = ""
    # 案件名称
    judgment_name = ""
    # 判决文书
    judgment_document = ""
    # 案件类型
    case_type = ""
    # 案件身份
    case_identity = ""
    # 案件号
    case_number = ""
    # 文书连接
    document_url = ""
    # 标记号
    mark = ""
    # 添加时间
    add_time = ""
    # 文书抓取状态
    detail_status = ''
    # 机构号
    agency_num = ''
    # 机构名称
    agency_name = ''
    # 批次
    batch = ''

    table_name = "tyc_sffx_flss"
    column_name = "(txt_id, company_name, judgment_date, judgment_name, judgment_document, case_type, case_identity, case_number, document_url, mark, detail_status, agency_num, agency_name, batch, add_time)"

    # sql = "insert into tyc_sffx_flss (text_info,batch,agency_name,agency_num,detail_status,mark,document_url,case_number,case_identity,case_type,judgment_document,company_name,txt_id,case_action,add_time,judgment_date) values ('{}','{}','{}','{}',{},{},'{}','{}','{}','{}','{}','{}','{}','{}',{},'{}')".formate(text_info,batch,agency_name,agency_num,detail_status,mark,document_url,case_number,case_identity,case_type,judgment_document,company_name,txt_id,case_action,add_time,judgment_date)

# 法院公告
class TycSffxFygg(object):
    # 公告时间
    announcement_date = ""
    # 上诉方
    plaintiff = ""
    # 被诉方
    defendant = ""
    # 公告类型
    announcement_type = ""
    # 法院
    court = ""
    # 详情
    detail_info = ""
    # mongodb文本ID
    txt_id = ""
    # 所属公司名称
    ent_name = ""
    # 添加时间
    add_time = ""
    # 标记号
    mark = ""
    # 机构号
    agency_num = ''
    # 机构名称
    agency_name = ''
    # 批次
    batch = ''
    table_name = "tyc_sffx_fygg"
    column_name = "(txt_id,company_name,announcement_date,plaintiff,defendant,announcement_type,court,detail_info,mark,agency_num,agency_name,batch,add_time)"
    
    # sql = "insert into tyc_sffx_fygg (txt_id,company_name,announcement_date,plaintiff,defendant,announcement_type,court,detail_info,mark,add_time,agency_num,agency_name,batch) values ('{}','{}',{},'{}','{}','{}','{}','{}',{},{},'{}','{}','{}')".formate(txt_id,company_name,announcement_date,plaintiff,defendant,announcement_type,court,detail_info,mark,add_time,agency_num,agency_name,batch)

# 被执行人
class TycSffxBzxr(object):
    # 立案日期
    record_date = ""
    # 执行标的
    Execute_underlying = ""
    # 案号
    case_number = ""
    # 法院
    court = ""
    # mongodb文本ID
    txt_id = ""
    # 所属公司名称
    ent_name = ""
    # 添加时间
    add_time = ""
    # 标记号
    mark = ""
    # 机构号
    agency_num = ''
    # 机构名称
    agency_name = ''
    # 批次
    batch = ''
    # 详情
    detail = ''

    table_name = "tyc_sffx_bzxr"
    column_name = "(agency_num,agency_name,batch,txt_id,company_name,record_date,execute_underlying,case_number,court,mark, detail,add_time)"
    
    # sql = "insert into tyc_sffx_bzxr (agency_num,agency_name,batch,txt_id,company_name,record_date,execute_underlying,case_number,court,mark,add_time) values ('{}','{}','{}','{}','{}','{}','{}','{}','{}',{},{})".formate(agency_num,agency_name,batch,txt_id,company_name,record_date,execute_underlying,case_number,court,mark,add_time)

# 股权出质
class TycJyfxGqcz(object):
    # 公告时间
    announcement_date = ""
    # 登记编号
    registration_number = ""
    # 出质人
    pledgor = ""
    # 质权人
    pledgee = ""
    # 状态
    status = ""
    # 出质股权数额
    pledged_amount = ""
    # 详情
    detail_info = ""
    # mongodb文本ID
    txt_id = ""
    # 所属公司名称
    ent_name = ""
    # 添加时间
    add_time = ""
    # 标记号
    mark = ""
    # 机构号
    agency_num = ''
    # 机构名称
    agency_name = ''
    # 批次
    batch = ''
    table_name = "tyc_jyfx_gqcz"
    column_name = "(announcement_date,registration_number,pledgor,pledgee,status,pledged_amount,detail_info,txt_id,company_name,mark,agency_num,agency_name,batch,add_time)"
    
    # sql = "insert into tyc_jyfx_gqcz (batch,agency_name,agency_num,aquity_amount,add_time,mark,detail_info,status,pledgee,pledgor,registration_number,announcement_date,company_name,txt_id) values ('{}','{}','{}',{},{},{},'{}','{}','{}','{}','{}','{}','{}','{}')".formate(batch,agency_name,agency_num,aquity_amount,add_time,mark,detail_info,status,pledgee,pledgor,registration_number,announcement_date,company_name,txt_id)

# 招投标
class TycJyzkZtb(object):
    # 发布时间
    publish_date = ""
    # 标题
    title = ""
    # 标题url
    title_url = ""
    # 采购人
    procurement = ""
    # mongodb文本ID
    txt_id = ""
    # 所属公司名称
    ent_name = ""
    # 添加时间
    add_time = ""
    # 标记号
    mark = ""
    # 机构号
    agency_num = ''
    # 机构名称
    agency_name = ''
    # 批次
    batch = ''
    table_name = "tyc_jyzk_ztb"
    column_name = "(txt_id,company_name,publish_date,title,title_url,procurement,mark,agency_num,agency_name,batch,add_time)"
    
    # sql = "insert into tyc_jyzk_ztb (txt_id,company_name,publish_date,title,title_url,procurement,mark,add_time,agency_num,agency_name,batch) values ('{}','{}',{},'{}','{}','{}',{},{},'{}','{}','{}')".formate(txt_id,company_name,publish_date,title,title_url,procurement,mark,add_time,agency_num,agency_name,batch)

# 招聘
class TycJyzkZp(object):
    # 发布时间
    publish_date = ""
    # 招聘职位
    recruitment_job = ""
    # 薪资
    salary = ""
    # 工作经验
    work_year = ""
    # 招聘人数
    recruitment_numbers = ""
    # 所在城市
    work_city = ""
    # 详情
    detail_info = ""
    # mongodb文本ID
    txt_id = ""
    # 所属公司名称
    ent_name = ""
    # 添加时间
    add_time = ""
    # 标记号
    mark = ""
    # 机构号
    agency_num = ''
    # 机构名称
    agency_name = ''
    # 批次
    batch = ''
    # 学历
    education = ''
    table_name = "tyc_jyzk_zp"
    column_name = "(work_city,detail_info,education,mark,agency_num,agency_name,batch,txt_id,company_name,publish_date,recruitment_job,salary,work_year,recruitment_numbers,add_time)"
    
    # sql = "insert into tyc_jyzk_zp (work_city,detail_info,mark,add_time,agency_num,agency_name,batch,txt_id,company_name,publish_date,recruitment_job,salary,work_year,recruitment_numbers) values ('{}','{}',{},{},'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".formate(work_city,detail_info,mark,add_time,agency_num,agency_name,batch,txt_id,company_name,publish_date,recruitment_job,salary,work_year,recruitment_numbers)

# 税务评级
class TycJyzkSwpj(object):
    # 年份
    year = ""
    # 纳税评级
    tax_rating = ""
    # 类型
    tax_type = ""
    # 纳税人识别号
    tax_identification_number = ""
    # 评价单位
    evaluate_department = ""
    # mongodb文本ID
    txt_id = ""
    # 所属公司名称
    ent_name = ""
    # 添加时间
    add_time = ""
    # 标记号
    mark = ""
    # 机构号
    agency_num = ''
    # 机构名称
    agency_name = ''
    # 批次
    batch = ''
    
    table_name = "tyc_jyzk_swpj"
    column_name = "(txt_id,company_name,year,tax_rating,tax_type,tax_identification_number,evaluate_department,mark,agency_num,agency_name,batch,add_time)"
    # sql = "insert into tyc_jyzk_swpj (txt_id,company_name,year,tax_rating,tax_type,tax_identification_number,evaluate_department,mark,add_time,agency_num,agency_name,batch) values ('{}','{}','{}','{}','{}','{}','{}',{},{},'{}','{}','{}')".formate(txt_id,company_name,year,tax_rating,tax_type,tax_identification_number,evaluate_department,mark,add_time,agency_num,agency_name,batch)

# 抽查检查
class TycJyzkCcjc(object):
    # 日期
    date = ""
    # 类型
    type = ""
    # 结果
    result = ""
    # 检查实施机关
    check_department = ""
    # mongodb文本ID
    txt_id = ""
    # 所属公司名称
    ent_name = ""
    # 添加时间
    add_time = ""
    # 标记号
    mark = ""
    # 机构号
    agency_num = ''
    # 机构名称
    agency_name = ''
    # 批次
    batch = ''
    
    table_name = "tyc_jyzk_ccjc"
    column_name = "(check_date, type, result, check_department, txt_id, company_name, mark ,agency_num,agency_name,batch,add_time)"
    
    # sql = "insert into tyc_jyzk_ccjc (agency_num,agency_name,batch,txt_id,company_name,register_date,company_type,result,check_department,mark,add_time) values ('{}','{}','{}','{}','{}','{}','{}','{}','{}',{},{})".formate(agency_num,agency_name,batch,txt_id,company_name,register_date,company_type,result,check_department,mark,add_time)

# 产品信息
class TycJyzkCpxx(object):
    # 产品名称
    product_name = ""
    # 产品简称
    product_referred = ""
    # 产品分类
    product_classification = ""
    # 领域
    field = ""
    # 详情
    detail_info = ""
    # mongodb文本ID
    txt_id = ""
    # 所属公司名称
    ent_name = ""
    # 添加时间
    add_time = ""
    # 标记号
    mark = ""
    # 机构号
    agency_num = ''
    # 机构名称
    agency_name = ''
    # 批次
    batch = ''
    
    table_name = "tyc_jyzk_cpxx"
    column_name = "(txt_id,company_name,product_name,product_referred,product_classification,field,detail_info,mark,agency_num,agency_name,batch,add_time)"
    
    # sql = "insert into tyc_jyzk_cpxx (txt_id,company_name,product_name,product_referred,product_classification,field,detail_info,mark,add_time,agency_num,agency_name,batch) values ('{}','{}','{}','{}','{}','{}','{}',{},{},'{}','{}','{}')".formate(txt_id,company_name,product_name,product_referred,product_classification,field,detail_info,mark,add_time,agency_num,agency_name,batch)

# 商标信息
class TycZscqSbxx(object):
    # 申请日期
    apply_date = ""
    # 商标
    trademark = ""
    # 商标名称
    trademark_name = ""
    # 注册号
    registration_number = ""
    # 类别
    type = ""
    # 状态
    status = ""
    # mongodb文本ID
    txt_id = ""
    # 详情
    detail = ''
    # 所属公司名称
    company_name = ""
    # 添加时间
    add_time = ""
    # 标记号
    mark = ""
    # 机构号
    agency_num = ''
    # 机构名称
    agency_name = ''
    # 批次
    batch = ''
    
    table_name = "tyc_zscq_sbxx"
    column_name = "(detail,txt_id,company_name,apply_date,trademark,trademark_name,registration_number,type,status,mark,agency_num,agency_name,batch,add_time)"
    
    def __str__(self):
        return '(\"' + self.apply_date + '\",\"' + self.trademark + '\",\"' + self.trademark_name + '\",\"' + self.registration_number + '\",\"' + \
               self.type + '\",\"' + self.status + '\",\"' + self.txt_id + '\",\"' + self.detail + '\",\"' + self.company_name + '\",\"' + self.add_time + '\",' + self.mark + ',\"' \
               + self.agency_num + '\",\"' + self.agency_name + '\",\"' + self.batch + '\")'
    
    # sql = "insert into tyc_zscq_sbxx (detail,txt_id,company_name,apply_date,trademark,trademark_name,registration_number,company_type,status,mark,add_time,agency_num,agency_name,batch) values ('{}','{}','{}','{}','{}','{}','{}','{}','{}',{},{},'{}','{}','{}')".formate(detail,txt_id,company_name,apply_date,trademark,trademark_name,registration_number,company_type,status,mark,add_time,agency_num,agency_name,batch)

# 专利信息
class TycZscqZl(object):
    # 申请公布日
    apply_publish_date = ""
    # 专利名称
    patent_name = ""
    # 申请号
    apply_number = ""
    # 申请公布号
    apply_publish_number = ""
    # 专利类型
    patent_type = ""
    # 详情
    detail_info = ""
    # mongodb文本ID
    txt_id = ""
    # 所属公司名称
    ent_name = ""
    # 添加时间
    add_time = ""
    # 标记号
    mark = ""
    # 机构号
    agency_num = ''
    # 机构名称
    agency_name = ''
    # 批次
    batch = ''
    
    table_name = "tyc_zscq_zl"
    column_name = "(apply_publish_date,patent_name,apply_number,apply_publish_number,detail_info,txt_id,company_name,mark,agency_num,agency_name,batch,patent_type,add_time)"
    # sql = "insert into tyc_zscq_zl (txt_id,apply_publish_number,batch,patent_type,ent_name,apply_publish_date,patent_name,apply_number,detail_info,mark,add_time,agency_num,agency_name) values ('{}','{}','{}','{}','{}','{}','{}','{}','{}',{},{},'{}','{}')".formate(txt_id,apply_publish_number,batch,patent_type,ent_name,apply_publish_date,patent_name,apply_number,detail_info,mark,add_time,agency_num,agency_name)

# 著作权
class TycZscqZzq(object):
    # 批准日期
    approval_date = ""
    # 软件全称
    software_name = ""
    # 软件简称
    software_referred = ""
    # 登记号
    registration_number = ""
    # 分类号
    type_number = ""
    # 版本号
    version_number = ""
    # 详情
    detail_info = ""
    # mongodb文本ID
    txt_id = ""
    # 所属公司名称
    ent_name = ""
    # 添加时间
    add_time = ""
    # 标记号
    mark = ""
    # 机构号
    agency_num = ''
    # 机构名称
    agency_name = ''
    # 批次
    batch = ''
    
    table_name = "tyc_zscq_zzq"
    column_name = "(batch,agency_num,mark,detail_info,version_number,type_number,software_referred,software_name,company_name,txt_id,approval_date,agency_name,registration_number,add_time)"
    
    # sql = "insert into tyc_zscq_zzq (batch,agency_num,add_time,mark,detail_info,version_number,type_number,software_referred,software_name,company_name,txt_id,approval_date,agency_name,registration_number) values ('{}','{}',{},{},'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".formate(batch,agency_num,add_time,mark,detail_info,version_number,type_number,software_referred,software_name,ent_name,txt_id,approval_date,agency_name,registration_number)

# 网站备案
class TycZscqWzba(object):
    # 审核时间
    audit_date = ""
    # 网站名称
    web_name = ""
    # 网站首页
    web_homepage = ""
    # 域名
    domain_name = ""
    # 备案号
    record_number = ""
    # 状态
    status = ""
    # 单位性质
    department_type = ""
    
    # mongodb文本ID
    txt_id = ""
    # 所属公司名称
    ent_name = ""
    # 添加时间
    add_time = ""
    # 标记号
    mark = ""
    # 机构号
    agency_num = ''
    # 机构名称
    agency_name = ''
    # 批次
    batch = ''
    
    table_name = "tyc_zscq_wzba"
    column_name = "(txt_id,domain_name,agency_num,company_name,audit_date,web_name,web_homepage,record_number,status,department_type,mark,agency_name,batch,add_time)"
    
    # sql = "insert into tyc_zscq_wzba (txt_id,domain_name,agency_num,company_name,audit_date,web_name,web_homepage,record_number,status,department_type,mark,add_time,agency_name,batch) values ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}',{},{},'{}','{}')".formate(txt_id,domain_name,agency_num,company_name,audit_date,web_name,web_homepage,record_number,status,department_type,mark,add_time,agency_name,batch)

# 失信人
class TycSffxSxr(object):
    # 立案日期
    case_date = ""
    # 案号
    case_number = ""
    # 执行法院
    execution_court = ""
    # 履行状态
    performance_state = ""
    # 执行依据文号
    execute_number = ""
    # 详情
    detail_info = ""
    # mongodb文本ID
    txt_id = ""
    # 所属公司名称
    company_name = ""
    # 添加时间
    add_time = ""
    # 标记号
    mark = ""
    # 机构号
    agency_num = ''
    # 机构名称
    agency_name = ''
    # 批次
    batch = ''
    
    table_name = "tyc_sffx_sxr"
    column_name = "(txt_id,company_name,case_date,case_number,execution_court,performance_state,execute_number,detail_info,mark,agency_num,agency_name,batch,add_time)"
    
    # sql = "insert into tyc_sffx_sxr (txt_id,company_name,case_date,case_number,execution_court,performance_state,execute_number,detail_info,mark,add_time,agency_num,agency_name,batch) values ('{}','{}','{}','{}','{}','{}','{}','{}',{},{},'{}','{}','{}')".formate(txt_id,company_name,case_date,case_number,execution_court,performance_state,execute_number,detail_info,mark,add_time,agency_num,agency_name,batch)

# 经营异常
class TycJyfxJyyc(object):
    # 列入日期
    insert_date = ""
    # 列入原因
    insert_cause = ""
    # 决定机关
    insert_department = ""
    # 移除日期
    out_date = ""
    # 移除原因
    out_case = ""
    # 移除机关
    out_department = ""
    # mongodb文本ID
    txt_id = ""
    # 所属公司名称
    ent_name = ""
    # 添加时间
    add_time = ""
    # 标记号
    mark = ""
    # 机构号
    agency_num = ''
    # 机构名称
    agency_name = ''
    # 批次
    batch = ''
    
    table_name = "tyc_jyfx_jyyc"
    column_name = "(txt_id,company_name,insert_date,insert_cause,insert_department,mark,agency_num,agency_name,batch,out_date,out_cause,out_department,add_time)"
    
    # sql = "insert into tyc_jyfx_jyyc (txt_id,company_name,insert_date,insert_cause,insert_department,mark,add_time,agency_num,agency_name,batch,out_cause,out_department) values ('{}','{}','{}','{}','{}',{},{},'{}','{}','{}','{}','{}')".formate(txt_id,company_name,insert_date,insert_cause,insert_department,mark,add_time,agency_num,agency_name,batch,out_cause,out_department)

# 动产抵押
class tycJyfxDcdy(object):
    # 登记日期
    registration_date = ""
    # 登记号
    registration_number = ""
    # 被担保债权类型
    guarantee_type = ""
    # 登记机关
    registration_department = ""
    # 状态
    status = ""
    # 详情
    detail_info = ""
    # mongodb文本ID
    txt_id = ""
    # 所属公司名称
    ent_name = ""
    # 添加时间
    add_time = ""
    # 标记号
    mark = ""
    # 机构号
    agency_num = ''
    # 机构名称
    agency_name = ''
    # 批次
    batch = ''
    guarantee_amount = ''
    table_name = "tyc_jyfx_dcdy"
    column_name = "(registration_date, registration_number, guarantee_type,guarantee_amount, registration_department, status, detail_info, txt_id, company_name, mark ,agency_num,agency_name,batch,add_time)"
    
    # sql = "insert into tyc_jyfx_dcdy (txt_id,company_name,registration_date,registration_number,guarantee_type,guarantee_amount,registration_department,status,detail_info,mark,add_time,aquity_amount,agency_num,agency_name,batch) values ('{}','{}','{}','{}','{}','{}','{}','{}','{}',{},{},{},'{}','{}','{}')".formate(registration_date, registration_number, guarantee_type,guarantee_amount, registration_department, status, detail_info, txt_id, company_name, add_time, mark ,agency_num,agency_name,batch)


# 行政处罚(工商局)
class TycJyfxXzcf(object):
    # 决定日期
    decision_date = ""
    # 决定书文号
    decision_number = ""
    # 行政处罚内容
    punishment_contents = ""
    # 类型
    type = ""
    # 决定机关
    decision_department = ""
    # 详情
    detail_info = ""
    # 处罚名称
    punishment_name = ""
    # 地域
    punishment_area = ""
    # mongodb文本ID
    txt_id = ""
    # 所属公司名称
    ent_name = ""
    # 添加时间
    add_time = ""
    # 标记号
    mark = ""
    # 机构号
    agency_num = ''
    #机构名称
    agency_name = ''
    #批次
    batch = ''

    table_name ="tyc_jyfx_xzcf"
    column_name = "(txt_id, company_name, decision_date, decision_number, punishment_contents, type,decision_department, detail_info, punishment_name, punishment_area, mark, agency_num, agency_name, batch, add_time)"


    # sql = "insert into tyc_jyfx_xzcf (punishment_department,txt_id,company_name,decision_date,decision_number,type,decision_department,detail_info,punishment_name,punishment_area,mark,add_time,agency_num,agency_name,batch) values ('{}','{}','{}',{},'{}','{}','{}','{}','{}','{}',{},{},'{}','{}','{}')".formate(punishment_department,txt_id,company_name,decision_date,decision_number,type,decision_department,detail_info,punishment_name,punishment_area,mark,add_time,agency_num,agency_name,batch)

# 债券信息
class TycJyzkZqxx(object):
    # 发行日期
    publish_date = ""
    # 债券名称
    bond_name = ""
    # 债券代码
    bond_code = ""
    # 债券类型
    bond_type = ""
    # 最新评级
    latest_rating = ""
    # 详情
    detail_info = ""
    # mongodb文本ID
    txt_id = ""
    # 所属公司名称
    ent_name = ""
    # 添加时间
    add_time = ""
    # 标记号
    mark = ""
    # 机构号
    agency_num = ''
    # 机构名称
    agency_name = ''
    # 批次
    batch = ''
    
    table_name = "tyc_jyzk_zqxx"
    column_name = "(batch,agency_name,agency_num,mark,detail_info,latest_rating,bond_type,bond_code,bond_name,publish_date,company_name,txt_id,add_time)"
    
    # sql = "insert into tyc_jyzk_zqxx (batch,agency_name,agency_num,add_time,mark,detail_info,latest_rating,bond_type,bond_code,bond_name,publish_date,company_name,txt_id) values ('{}','{}','{}',{},{},'{}','{}','{}','{}','{}','{}','{}','{}')".formate(batch,agency_name,agency_num,add_time,mark,detail_info,latest_rating,bond_type,bond_code,bond_name,publish_date,company_name,txt_id)

# 经营风险--严重违法
class TycJyfxYzwf(object):
    # mongodb文本ID
    txtId = ''
    # 所属公司名称
    entName = ''
    # 列入日期
    illegalDate = ''
    # 列入原因
    illegalReason = ''
    # 决定机关
    office = ''
    # 移除日期
    out_date = ''
    # 移除原因
    out_reason = ''
    # 移出决定机关
    out_department = ''
    # 标记号
    mark = ''
    # 添加时间
    add_time = ''
    # 机构号
    agency_num = ''
    # 机构名称
    agency_name = ''
    # 批次
    batch = ''
    table_name = "tyc_jyfx_yzwf"
    column_name = "(out_date,out_reason,out_department,txt_id,company_name,illegal_date,illegal_reason,office,mark,agency_num,agency_name,batch,add_time)"
    
    # sql = "insert into tyc_jyfx_yzwf (out_date,out_reason,out_department,txt_id,company_name,illegal_date,illegal_reason,office,mark,add_time,agency_num,agency_name,batch) values ('{}','{}','{}','{}','{}',{},'{}','{}',{},{},'{}','{}','{}')".formate(out_date,out_reason,out_department,txt_id,company_name,illegal_date,illegal_reason,office,mark,add_time,agency_num,agency_name,batch)

# 经营风险--欠税公告
class TycJyfxQsgg(object):
    # mongodb文本ID
    txtId = ''
    # 所属公司名称
    entName = ''
    # 发布日期
    taxesDate = ''
    # 纳税人识别号
    taxesNum = ''
    # 欠税税种
    taxesType = ''
    # 当前发生的欠税额
    taxesMoney = ''
    # 欠税余额
    taxesBalance = ''
    # 税务机关
    taxesOffice = ''
    # 详情
    detail = ''
    # 标记号
    mark = ''
    # 添加时间
    add_time = ''
    # 机构号
    agency_num = ''
    # 机构名称
    agency_name = ''
    # 批次
    batch = ''
    table_name = "tyc_jyfx_qsgg"
    column_name = "(detail,batch,agency_name,agency_num,mark,taxes_office,taxes_balance,taxes_money,taxes_type,taxes_num,taxes_date,company_name,txt_id,add_time)"
    
    # sql = "insert into tyc_jyfx_qsgg (detail,diving_amount,batch,agency_name,agency_num,add_time,mark,taxes_office,taxes_balance,taxes_money,taxes_type,taxes_num,taxes_date,company_name,txt_id) values ('{}','{}','{}','{}','{}',{},{},'{}','{}','{}','{}','{}',{},'{}','{}')".formate(detail,diving_amount,batch,agency_name,agency_num,add_time,mark,taxes_office,taxes_balance,taxes_money,taxes_type,taxes_num,taxes_date,company_name,txt_id)

# 经营状况--购地信息
class TycJyzkGdxx(object):
    # mongodb文本ID
    txtId = ''
    # 所属公司名称
    entName = ''
    # 签订日期
    gdSignDate = ''
    # 电子监管号
    gdNum = ''
    # 约定动工日
    gdActDate = ''
    # 供地总面积
    gdArea = ''
    # 行政区
    gdRegion = ''
    # 操作
    gdOperate = ''
    # 土地坐落
    located = ''
    # 土地用途
    land_use = ''
    # 供应方式
    supply_method = ''
    # 标记号
    mark = ''
    # 添加时间
    add_time = ''
    # 机构号
    agency_num = ''
    # 机构名称
    agency_name = ''
    # 批次
    batch = ''
    # 购地信息详情
    gd_info = ''

    table_name = "tyc_jyzk_gdxx"
    column_name = "(txt_id,company_name,gd_sign_date,gd_num,gd_act_date,gd_area,gd_region,gd_operate,located,land_use,supply_method,mark,agency_num,agency_name,batch,gd_info, add_time)"
    
    # sql = "insert into tyc_jyzk_gdxx (txt_id,company_name,gd_sign_date,gd_num,gd_act_date,gd_area,gd_region,gd_operate,located,land_use,supply_method,mark,add_time,agency_num,agency_name,batch) values ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}',{},{},'{}','{}','{}')".formate(txt_id,company_name,gd_sign_date,gd_num,gd_act_date,gd_area,gd_region,gd_operate,located,land_use,supply_method,mark,add_time,agency_num,agency_name,batch)

# 经营状况--资质证书
class TycJyzkZzzs(object):
    # mongodb文本ID
    txtId = ''
    # 所属公司名称
    entName = ''
    # 证书类型
    certificateType = ''
    # 发证日期
    sendDate = ''
    # 截止日期
    offDate = ''
    # 证书编号
    certificateNum = ''
    # 标记号
    mark = ''
    # 添加时间
    add_time = ''
    # 机构号
    agency_num = ''
    # 机构名称
    agency_name = ''
    # 批次
    batch = ''
    detail = ''
    table_name = "tyc_jyzk_zzzs"
    column_name = "(detail,txt_id,company_name,certificate_num,certificate_type,send_date,off_date,mark,agency_num,agency_name,batch,add_time)"
    
    # sql = "insert into tyc_jyzk_zzzs (detail,txt_id,company_name,certificate_num,certificate_type,send_date,off_date,mark,add_time,agency_num,agency_name,batch) values ('{}','{}','{}','{}','{}','{}','{}',{},{},'{}','{}','{}')".formate(detail,txt_id,company_name,certificate_num,certificate_type,send_date,off_date,mark,add_time,agency_num,agency_name,batch)

# 企业年报  TODO: 新增字段
class TycQybjQynb(object):
    # 年份
    year = ""
    # 详情链接
    detail_url = ""
    # mongodb文本ID
    txtId = ''
    # 所属公司名称
    entName = ''
    # 标记号
    mark = ''
    # 添加时间
    add_time = ''
    # 机构号
    agency_num = ''
    # 机构名称
    agency_name = ''
    # 批次
    batch = ''
    table_name = "tyc_qybj_qynb"
    column_name = "(txt_id,company_name,detail_url,year,mark,agency_num,agency_name,batch,add_time)"
    
    # sql = "insert into tyc_qybj_qynb (txt_id,company_name,detail_url,year,mark,add_time,agency_num,agency_name,batch) values ('{}','{}','{}','{}',{},{},'{}','{}','{}')".formate(txt_id,company_name,detail_url,year,mark,add_time,agency_num,agency_name,batch)

# 作品著作权
class TycZscqZpzzq(object):
    # mongodb文本ID
    txtId = ""
    # 所属公司名称
    entName = ''
    # 作品名称
    works_name = ''
    # 登记号
    register_name = ''
    # 类别
    type = ''
    # 创造完成日期
    creat_date = ''
    # 登记日期
    register_date = ''
    # 首期发布日期
    firstpublish_date = ''
    # 标记号
    mark = ''
    # 添加时间
    add_time = ''
    # 机构号
    agency_num = ''
    # 机构名称
    agency_name = ''
    # 批次
    batch = ''
    # 对应表
    table_name = "tyc_zscq_zpzzq"
    # 加入数据库
    
    column_name = "(works_name,mark,txt_id,company_name,register_name,type,create_date,register_date,firstpublish_date,agency_num,agency_name,batch,add_time)"
    
    # sql = "insert into tyc_zscq_zpzzq (works_name,mark,txt_id,company_name,register_name,company_type,create_date,register_date,firstpublish_date,add_time,agency_num,agency_name,batch) values ('{}',{},'{}','{}','{}','{}','{}','{}','{}',{},'{}','{}','{}')".formate(works_name,mark,txt_id,company_name,register_name,company_type,create_date,register_date,firstpublish_date,add_time,agency_num,agency_name,batch)

# 微信公众号
class TycJyzkWxgzh(object):
    # mongodb文本ID
    txtId = ''
    # 所属公司名称
    company_name = ''
    # 公众号名称
    mp_name = ''
    # 微信号
    mp_number = ''
    # 公众号简介
    mp_info = ''
    # 添加时间
    add_time = ""
    # 标记号
    mark = ""
    # 详情
    detail = ''
    # 机构号
    agency_num = ''
    # 机构名称
    agency_name = ''
    # 批次
    batch = ''
    # 对应表
    table_name = "tyc_jyzk_wxgzh"
    
    # 加入数据库
    column_name = "(txt_id,company_name,mp_name,mp_number,mp_info,mark,detail,agency_num,agency_name,batch,add_time)"
    # sql = "insert into tyc_jyzk_wxgzh (txt_id,company_name,mp_name,mp_number,mp_info,mark,add_time,agency_num,agency_name,batch) values ('{}','{}','{}','{}','{}',{},{},'{}','{}','{}')".formate(txt_id,company_name,mp_name,mp_number,mp_info,mark,add_time,agency_num,agency_name,batch)

# 进出口信用
class TycJyzkJckxy(object):
    # mongodb文本ID
    txtId = ''
    # 所属公司名称
    entName = ''
    # 注册海关
    register_customs = ''
    # 海关编号
    customs_number = ''
    # 行业种类
    industry_category = ''
    # 经营类别
    manger_type = ''
    # 注册日期
    register_date = ''
    # 详情
    detail_info = ''
    # 添加时间
    add_time = ""
    # 标记号
    mark = ""
    # 机构号
    agency_num = ''
    # 机构名称
    agency_name = ''
    # 批次
    batch = ''
    # 对应表
    table_name = "tyc_jyzk_jckxy"
    # 加入数据库
    column_name = "(txt_id,company_name,register_customs,customs_number,industry_category,manager_type,register_date,detail_info,mark,agency_num,agency_name,batch,add_time)"

    # sql = "insert into tyc_jyzk_jckxy (txt_id,company_name,register_customs,customs_number,manager_type,detail_info,mark,add_time,agency_num,agency_name,batch) values ('{}','{}','{}','{}','{}','{}',{},{},'{}','{}','{}')".formate(txt_id,company_name,register_customs,customs_number,manager_type,detail_info,mark,add_time,agency_num,agency_name,batch)

# 年报基本信息
class TycYearJbxx(object):
    # mongodb文本ID
    txtId = ''
    
    # 年份
    year = ''
    # 公司名称
    company_name = ''
    # 统一社会信用代码
    credit_num = ''
    # 企业名称
    ent_name = ''
    # 企业联系电话
    company_tel = ''
    # 邮政编码
    postal_code = ''
    # 企业经营状态
    manager_state = ''
    # 从业人数
    people_count = ''
    # 电子邮箱
    email = ''
    # 是否有网站或网店
    website = ''
    # 企业通信地址
    company_address = ''
    # 企业是否有投资信息或购买其他公司股权
    buy_equity = ''
    # 添加时间
    add_time = ""
    # 标记号
    mark = ""
    # 机构号
    agency_num = ''
    # 机构名称
    agency_name = ''
    # 批次
    batch = ''
    # 对应的表
    table_name = "tyc_year_jbxx"
    # 加入数据库
    
    column_name = "(credit_num,company_name,company_tel,postal_code,manager_state,people_count,email,website,company_address,buy_equity,year,txt_id,ent_name,mark,agency_num,agency_name,batch,add_time)"
    
    # sql = "insert into tyc_year_jbxx (batch,agency_name,agency_num,add_time,mark,company_address,website,email,people_count,manager_state,company_tel,company_name,credit_num,ent_name,year,txt_id,buy_equity,postal_code) values ('{}','{}','{}',{},{},'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".formate(credit_num,company_name,company_tel,postal_code,manager_state,people_count,email,website,company_address,buy_equity,year,txt_id,ent_name,add_time,mark,agency_num,agency_name,batch)

# 网站或网店信息
class TycYearWzhwdxx(object):
    # mongodb文本ID
    txtId = ''
    # 所属公司名称
    entName = ''
    # 年份
    year = ''
    # 类型
    website_type = ''
    # 名称
    web_name = ''
    # 网址
    web_url = ''
    # 添加时间
    add_time = ""
    # 标记号
    mark = ""
    # 机构号
    agency_num = ''
    # 机构名称
    agency_name = ''
    # 批次
    batch = ''
    # 对应的表
    table_name = "tyc_year_wzhwdxx"
    # 加入数据库
    column_name = "(website_type,web_name,web_url,year,txt_id,company_name,mark,agency_num,agency_name,batch,add_time)"
    # sql = "insert into tyc_year_wzhwdxx (txt_id,web_url,year,company_name,website_type,web_name,mark,add_time,agency_num,agency_name,batch) values ('{}','{}','{}','{}','{}','{}',{},{},'{}','{}','{}')".formate(txt_id,web_url,year,company_name,website_type,web_name,mark,add_time,agency_num,agency_name,batch)

class TycYearGdczxx(object):
    # mongodb文本ID
    txtId = ''
    # 所属公司名称
    entName = ''
    # 年份
    year = ''
    #  股东
    shareholder = ''
    # 认缴出资额(万元)
    subscirbe_contribution = ''
    # 认缴出资时间
    contribution_time = ''
    # 认缴出资方式
    contribution_style = ''
    # 实缴出资额(万元）
    actual_contribution = ''
    # 实缴出资时间
    actual_time = ''
    # 实缴出资方式
    actual_style = ''
    # 添加时间
    add_time = ""
    # 标记号
    mark = ""
    # 机构号
    agency_num = ''
    # 机构名称
    agency_name = ''
    # 批次
    batch = ''
    # 对应的表
    table_name = "tyc_year_gdczxx"
    # 加入数据库
    column_name = "(txt_id,company_name,year,shareholder,subscribe_contribution,contribution_time,contribution_style,actual_contribution,actual_time,actual_style,mark,agency_num,agency_name,batch,add_time)"
    
    # sql = "insert into tyc_year_gdczxx (txt_id,company_name,year,shareholder,subscirbe_contribution,contribution_time,contribution_style,actual_contribution,actual_time,actual_style,mark,add_time,agency_num,agency_name,batch) values ('{}','{}','{}','{}','{}',{},'{}','{}',{},'{}',{},{},'{}','{}','{}')".formate(txt_id,company_name,year,shareholder,subscirbe_contribution,contribution_time,contribution_style,actual_contribution,actual_time,actual_style,mark,add_time,agency_num,agency_name,batch)

class TycYearZczk(object):
    # mongodb文本ID
    txtId = ''
    # 所属公司名称
    entName = ''
    # 年份
    year = ''
    # 资产总额
    total_assets = ''
    # 销售总额
    total_sales = ''
    # 营业总收入中主营业务收入
    operation_income = ''
    # 纳税总额
    total_tax = ''
    # 所有者权益合计
    total_income = ''
    # 利润总额
    total_profit = ''
    # 净利润
    net_profit = ''
    # 负债总额
    total_debt = ''
    # 添加时间
    add_time = ""
    # 标记号
    mark = ""
    # 机构号
    agency_num = ''
    # 机构名称
    agency_name = ''
    # 批次
    batch = ''
    # 对应的表
    table_name = "tyc_year_zczk"
    # 加入数据库
    
    column_name = "(batch,agency_name,agency_num,mark,total_debt,net_profit,total_profit,total_income,total_tax,operation_income,total_sales,total_assets,year,company_name,txt_id,add_time)"
    
    # sql = "insert into tyc_year_zczk (batch,agency_name,agency_num,add_time,mark,total_debt,net_profit,total_profit,total_income,total_tax,operation_income,total_sales,total_assets,year,company_name,txt_id) values ('{}','{}','{}',{},{},'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".formate(batch,agency_name,agency_num,add_time,mark,total_debt,net_profit,total_profit,total_income,total_tax,operation_income,total_sales,total_assets,year,company_name,txt_id)

#
class TycYearDwtz(object):
    # mongodb文本ID
    txtId = ''
    # 所属公司名称
    entName = ''
    # 年份
    year = ''
    # 对外投资企业名称
    outbound_company = ''
    # 统一信用代码
    credit_num = ''
    # 添加时间
    add_time = ""
    # 标记号
    mark = ""
    # 机构号
    agency_num = ''
    # 机构名称
    agency_name = ''
    # 批次
    batch = ''
    # 对应的表
    table_name = "tyc_year_dwtz"
    # 加入数据库
    column_name = "(txt_id,mark,outbound_company,company_name,year,credit_num,agency_num,agency_name,batch,add_time)"
    
    # sql = "insert into tyc_year_dwtz (txt_id,mark,outbound_company,company_name,year,credit_num,add_time,agency_num,agency_name,batch) values ('{}',{},'{}','{}','{}','{}',{},'{}','{}','{}')".formate(txt_id,mark,outbound_company,company_name,year,credit_num,add_time,agency_num,agency_name,batch)

class BatchList(object):
    mark = ''
    
    company_name = ''
    
    company_address = ''
    
    searched = ''
    
    error = ''
    
    add_time = ''
    
    agency_num = ''
    
    agency_name = ''
    
    batch = ''
    
    end_time = ''
    
    table_name = 'batch_list'
    
    column_name = '(mark,company_name,searched,error,company_number,company_address,agency_num,agency_name,batch,end_time,batch_type,add_time)'
    
    # sql = "insert into batch_list (mark,company_name,searched,error,company_number,company_address,add_time,agency_num,agency_name,batch,end_time,batch_type) values ('{}',{},'{}','{}','{}','{}','{}','{}','{}')".formate(mark,company_name,searched,error,company_number,company_address,add_time,agency_num,agency_name,batch,end_time,batch_type)

class Batch_Detail(object):
    company_number = ""
    mark = ""
    company_name = ""
    company_address = ""
    searched = ""
    error = ""
    add_time = ""
    agency_num = ""
    agency_name = ""
    batch = ""
    txt_id = ""
    batch_type = ""
    table_name = 'batch_detail'
    column_name = " (company_number,mark,company_name,company_address,searched,error,agency_num,agency_name,batch,txt_id,batch_type,add_time) "
    
    # sql = "insert into batch_detail (company_number,mark,add_time,company_name,company_address,searched,error,agency_num,agency_name,batch,txt_id,batch_type) values ({},'{}','{}','{}','{}','{}','{}','{}','{}')".formate(company_number,mark,add_time,company_name,company_address,searched,error,agency_num,agency_name,batch,txt_id,batch_type)

# # 企业背景——最终受益人
class TycQybjZzsyr():
    # mongodb文本ID
    txtId = ''
    # 所属公司名称
    entName = ''
    # 最终受益人名称
    beneficiaryName = ''
    # 持股比例
    shareholderProportion = ''
    # 股权链
    equityChain = ''
    # 添加时间
    add_time = ""
    # 标记号
    mark = ""
    # 机构号
    agency_num = ''
    # 机构名称
    agency_name = ''
    # 批次
    batch = ''
    
    table_name = 'tyc_qybj_zzsyr'
    column_name = " (txt_id,company_name,mark,agency_num,agency_name,batch,beneficiary_name,shareholder_proportion,equity_chain,add_time) "
    
    # sql = "insert into tyc_qybj_zzsyr (txt_id,company_name,add_time,mark,agency_num,agency_name,batch,beneficiary_name,shareholder_proportion,equity_chain) values ('{}','{}',{},{},'{}','{}','{}','{}','{}','{}')".formate(txt_id,company_name,add_time,mark,agency_num,agency_name,batch,beneficiary_name,shareholder_proportion,equity_chain)

# 企业背景-->实际控制权
class TycQybjSjkzq():
    # mongodb文本ID
    txtId = ''
    # 所属公司名称
    entName = ''
    # 控股企业名称
    holdingName = ''
    # 持股比例
    investProportion = ''
    # 股权链
    equityChain = ''
    # 添加时间
    add_time = ""
    # 标记号
    mark = ""
    # 机构号
    agency_num = ''
    # 机构名称
    agency_name = ''
    # 批次
    batch = ''
    table_name = 'tyc_qybj_sjkzq'
    column_name = " (txt_id,company_name,mark,agency_num,agency_name,batch,holding_name,invest_proportion,equity_chain,add_time)"
    
    # sql = "insert into tyc_qybj_sjkzq (txt_id,company_name,add_time,mark,agency_num,agency_name,batch,holding_name,invest_proportion,equity_chain) values ('{}','{}',{},{},'{}','{}','{}','{}','{}','{}')".formate(txt_id,company_name,add_time,mark,agency_num,agency_name,batch,holding_name,invest_proportion,equity_chain)

# 司法风险-->开庭公告
class TycSffxKtgg():
    # mongodb文本ID
    txtId = ''
    # 所属公司名称
    entName = ''
    # 开庭日期
    trialDate = ''
    # 案号
    reference_num = ''
    # 案由
    causeAction = ''
    # 原告/上诉人
    plaintiff = ''
    # 被告/被上诉人
    defendant = ''
    # 详情
    detail = ''
    # 添加时间
    add_time = ""
    # 标记号
    mark = ""
    # 机构号
    agency_num = ''
    # 机构名称
    agency_name = ''
    # 批次
    batch = ''
    
    table_name = 'tyc_sffx_ktgg'
    column_name = "(detail,defendant,plaintiff,reference_num,cause_action,trial_date,batch,agency_name,agency_num,mark,company_name,txt_id,add_time)"
    
    # sql = "insert into tyc_sffx_ktgg (detail,defendant,plaintiff,cause_action,trial_date,batch,agency_name,agency_num,mark,add_time,company_name,txt_id) values ('{}','{}','{}','{}','{}','{}','{}','{}',{},{},'{}','{}')".formate(detail,defendant,plaintiff,cause_action,trial_date,batch,agency_name,agency_num,mark,add_time,company_name,txt_id)

# 司法风险-->司法协助
class TycSffxSfxz():
    id = ''
    # mongodb文本ID
    txtId = ''
    # 所属公司名称
    entName = ''
    # 被执行人
    enforcementPerson = ''
    # 股权数额
    equityAmount = ''
    # 执行法院
    executiveCourt = ''
    # 执行通知文号
    approvalNum = ''
    # 类型|状态
    status = ''
    # 详情
    detail = ''
    # 添加时间
    add_time = ""
    # 标记号
    mark = ""
    # 机构号
    agency_num = ''
    # 机构名称
    agency_name = ''
    # 批次
    batch = ''
    
    table_name = 'tyc_sffx_sfxz'
    column_name = "(txt_id,company_name,mark,agency_num,agency_name,batch,enforcement_person,equity_amount,executive_court,approval_num,status,detail,add_time)"
    
    # sql = "insert into tyc_sffx_sfxz (txt_id,company_name,add_time,mark,agency_num,agency_name,batch,enforcement_person,equity_amount,executive_court,approval_num,status,detail) values ('{}','{}',{},{},'{}','{}','{}','{}','{}','{}','{}','{}','{}')".formate(txt_id,company_name,add_time,mark,agency_num,agency_name,batch,enforcement_person,equity_amount,executive_court,approval_num,status,detail)

# 经营风险-->公示催告
class TycJyfxGscg():
    id = ''
    # mongodb文本ID
    txtId = ''
    # 所属公司名称
    company_name = ''
    # 票据号
    billNumber = ''
    # 票据类型
    billType = ''
    # 票面金额
    denomination = ''
    # 发布机构
    publishAuthority = ''
    # 公告日期
    announcementDate = ''
    # 详情
    detail = ''
    # 添加时间
    add_time = ""
    # 标记号
    mark = ""
    # 机构号
    agency_num = ''
    # 机构名称
    agency_name = ''
    # 批次
    batch = ''
    
    table_name = 'tyc_jyfx_gscg'
    column_name = "(txt_id,company_name,bill_number,bill_type,denomination,publish_authority,announcement_date,detail,mark,agency_num,agency_name,batch,add_time)"
    
    # sql = "insert into tyc_jyfx_gscg (txt_id,company_name,bill_number,bill_type,denomination,publish_authority,announcement_date,detail,mark,agency_num,agency_name,batch,add_time) values ('{}','{}','{}','{}','{}','{}','{}','{}',{},'{}','{}','{}',{})".formate(txt_id,company_name,bill_number,bill_type,denomination,publish_authority,announcement_date,detail,mark,agency_num,agency_name,batch,add_time)

# 经营风险-->司法拍卖
class TycJyfxSfpm():
    id = ''
    # mongodb文本ID
    txtId = ''
    # 所属公司名称
    entName = ''
    # 拍卖公告
    auctionNotice = ''
    # 公告日期
    auctionDate = ''
    # 执行法院
    executeCourt = ''
    # 拍卖标的
    auctionTarget = ''
    # 拍卖详情
    auctionDetail = ''
    
    # 添加时间
    add_time = ""
    # 标记号
    mark = ""
    # 机构号
    agency_num = ''
    # 机构名称
    agency_name = ''
    # 批次
    batch = ''
    
    table_name = 'tyc_jyfx_sfpm'
    column_name = "(auction_detail,txt_id,company_name,auction_notice,auction_date,execute_court,auction_target,mark,agency_num,agency_name,batch,add_time)"
    
    # sql = "insert into tyc_jyfx_sfpm (auction_detail,txt_id,company_name,auction_notice,auction_date,execute_court,auction_target,mark,add_time,agency_num,agency_name,batch) values ('{}','{}','{}','{}','{}','{}','{}',{},{},'{}','{}','{}')".formate(auction_detail,txt_id,company_name,auction_notice,auction_date,execute_court,auction_target,mark,add_time,agency_num,agency_name,batch)

# 经营风险-->清算信息
class TycJyfxQsxx():
    # mongodb文本ID
    txtId = ''
    # 所属公司名称
    entName = ''
    # 清算组负责人
    principal = ''
    # 清算组成员
    member = ''
    
    # 添加时间
    add_time = ""
    # 标记号
    mark = ""
    # 机构号
    agency_num = ''
    # 机构名称
    agency_name = ''
    # 批次
    batch = ''
    
    table_name = 'tyc_jyfx_qsxx'
    column_name = "(member,principal,batch,agency_name,agency_num,mark,company_name,txt_id,add_time)"
    
    # sql = "insert into tyc_jyfx_qsxx (member,principal,batch,agency_name,agency_num,mark,add_time,company_name,txt_id) values ('{}','{}','{}','{}','{}',{},{},'{}','{}')".formate(member,principal,batch,agency_name,agency_num,mark,add_time,company_name,txt_id)

# 经营状况-->行政许可【工商局】
class TycJyzkGsj():
    id = ''
    # mongodb文本ID
    txtId = ''
    # 所属公司名称
    entName = ''
    # 许可书文编号
    licenseDocNum = ''
    # 许可文件名称
    licenseDocName = ''
    # 有效期自
    validityBegin = ''
    # 有效期至
    validityEnd = ''
    # 许可机关
    licenseAuthority = ''
    # 许可内容
    licenseContent = ''
    
    # 添加时间
    add_time = ""
    # 标记号
    mark = ""
    # 机构号
    agency_num = ''
    # 机构名称
    agency_name = ''
    # 批次
    batch = ''
    
    table_name = 'tyc_jyzk_gsj'
    column_name = "(batch,agency_name,agency_num,mark,license_content,license_authority,validity_end,validity_begin,license_document_name,license_documet_num,company_name,txt_id,add_time)"
    
    # sql = "insert into tyc_jyzk_gsj (batch,agency_name,agency_num,add_time,mark,license_content,license_authority,validity_end,validity_begin,license_documcompany_name,license_documet_num,company_name,txt_id) values ('{}','{}','{}',{},{},'{}','{}','{}','{}','{}','{}','{}','{}')".formate(batch,agency_name,agency_num,add_time,mark,license_content,license_authority,validity_end,validity_begin,license_documcompany_name,license_documet_num,company_name,txt_id)

# 经营状况-->行政许可【信用中国】
class TycJyzkXyzg():
    # mongodb文本ID
    txtId = ''
    # 所属公司名称
    entName = ''
    # 行政许可文书号
    licenseDocNum = ''
    # 许可决定机关
    licenseAuthority = ''
    # 许可决定日期
    licenseDate = ''
    # 详情
    detail = ''
    
    # 添加时间
    add_time = ""
    # 标记号
    mark = ""
    # 机构号
    agency_num = ''
    # 机构名称
    agency_name = ''
    # 批次
    batch = ''
    
    table_name = 'tyc_jyzk_xyzg'
    column_name = "(txt_id,company_name,license_documet_num,license_authority,license_date,detail,mark,agency_num,agency_name,batch,add_time)"
    
    # sql = "insert into tyc_jyzk_xyzg (txt_id,company_name,license_documet_num,license_authority,license_date,detail,mark,add_time,agency_num,agency_name,batch) values ('{}','{}','{}','{}','{}','{}',{},{},'{}','{}','{}')".formate(txt_id,company_name,license_documet_num,license_authority,license_date,detail,mark,add_time,agency_num,agency_name,batch)

# 经营状况-->电信许可
class TycJyzkDxxk():
    id = ''
    # mongodb文本ID
    txtId = ''
    # 所属公司名称
    entName = ''
    # 许可证号
    licenseKey = ''
    # 业务范围
    businessSphere = ''
    # 是否有效
    available = ''
    # 详情
    detailInfo = ''
    
    # 添加时间
    add_time = ""
    # 标记号
    mark = ""
    # 机构号
    agency_num = ''
    # 机构名称
    agency_name = ''
    # 批次
    batch = ''
    
    table_name = 'tyc_jyzk_dxxk'
    column_name = "(txt_id,company_name,mark,license_key,business_sphere,available,detail_info,agency_num,agency_name,batch,add_time)"
    # sql = "insert into tyc_jyzk_dxxk (txt_id,company_name,license_key,business_sphere,available,detail_info,mark,add_time,agency_num,agency_name,batch) values ('{}','{}','{}','{}','{}','{}',{},{},'{}','{}','{}')".formate(txt_id,company_name,license_key,business_sphere,available,detail_info,mark,add_time,agency_num,agency_name,batch)

if __name__ == "__main__":
    ss = TycZscqSbxx()
    print(str(ss))
