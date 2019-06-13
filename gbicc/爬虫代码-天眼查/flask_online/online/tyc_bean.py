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
    branch=""
    table_name = "company_basic_info"
    column_name = "(search_name,ent_name,legal_representative,registered_capital,registration_date,location,score,status_type,url,txt_id,add_time,mark,agency_num,agency_name,batch,branch)"


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
    addtime = ''
    # 英文名称
    englishName = ''
    # 机构号
    agency_num = ''
    #机构名称
    agency_name = ''
    #批次
    batch = ''
    #银行分支机构号
    branch=''
    table_name = "tyc_qybj_jbxx"
    column_name = "(txt_id,ent_name,register_num,tissue_num,credit_num,company_type,taxpayer_num,industry,business_term,check_date,register_office,english_name,register_site,register_fund,register_date,company_status,business_scope,telephone," \
                  "email,url,mark,addtime,agency_num,agency_name,batch,branch)"

#企业背景-->主要人员
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
    addtime = ''
    # 机构号
    agency_num = ''
    #机构名称
    agency_name = ''
    #批次
    batch = ''
    table_name = "tyc_qybj_zyry"
    column_name = "(txt_id,ent_name,position,name,mark,addtime,agency_num,agency_name,batch)"


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
    # 标记号
    mark = ''
    # 添加时间
    addtime = ''
    # 机构号
    agency_num = ''
    #机构名称
    agency_name = ''
    #批次
    batch = ''
    table_name = "tyc_qybj_gdxx"
    column_name = "(txt_id,ent_name,shareholder,fund_ratio,fund_subcribe,mark,addtime,agency_num,agency_name,batch)"


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
    addtime = ''
    # 机构号
    agency_num = ''
    #机构名称
    agency_name = ''
    #批次
    batch = ''
    table_name = "tyc_qybj_dwtz"
    column_name = "(txt_id,ent_name,invest_company,invest_person,invest_fund,invest_amount,invest_ratio,invest_date,invest_status,mark,addtime,agency_num,agency_name,batch)"


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
    addtime = ''
    # 机构号
    agency_num = ''
    #机构名称
    agency_name = ''
    #批次
    batch = ''
    table_name = "tyc_qybj_bgjl"
    column_name = "(txt_id,ent_name,alter_date,alter_project,alter_befor,alter_after,mark,addtime,agency_num,agency_name,batch)"


# 企业背景-->分支机构
class TycQybjFzjg(object):
    # 企业名称
    company_name = ""
    # 法定代表人
    legal_representative = ""
    # 状态
    status = ""
    # 注册时间
    registered_date = ""
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
    table_name = "tyc_qybj_fzjg"
    column_name = "(company_name,legal_representative,status,registered_date,txt_id,ent_name,add_time,mark,agency_num,agency_name,batch)"


# 企业发展-->融资历史
class TycQyfzRzls(object):
    # mongodb文本ID
    txtId = ''
    # 所属公司名称
    entName = ''
    # 时间
    financeDate = ''
    # 轮次
    financeRound = ''
    # 估值
    financeValue = ''
    # 金额
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
    addtime = ''
    # 机构号
    agency_num = ''
    #机构名称
    agency_name = ''
    #批次
    batch = ''
    table_name = "tyc_qyfz_rzls"
    column_name = "(txt_id,ent_name,finance_date,finance_round,finance_value,finance_money,finance_ratio,finance_investor,finance_source,mark,addtime,agency_num,agency_name,batch)"


# 企业发展-->核心团队
class TycQyfzHxtd(object):
    # mongodb文本ID
    txtId = ''
    # 所属公司名称
    entName = ''
    # 人物名称
    personName = ''
    # 人物介绍
    personInfo = ''
    # 标记号
    mark = ''
    # 添加时间
    addtime = ''
    # 机构号
    agency_num = ''
    #机构名称
    agency_name = ''
    #批次
    batch = ''
    table_name = "tyc_qyfz_hxtd"
    column_name = "(txt_id,ent_name,person_name,person_info,mark,addtime,agency_num,agency_name,batch)"


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
    addtime = ''
    # 机构号
    agency_num = ''
    #机构名称
    agency_name = ''
    #批次
    batch = ''
    table_name = "tyc_qyfz_qyyw"
    column_name = "(txt_id,ent_name,business_name,business_quale,business_info,mark,addtime,agency_num,agency_name,batch)"


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
    addtime = ''
    # 机构号
    agency_num = ''
    #机构名称
    agency_name = ''
    #批次
    batch = ''
    table_name = "tyc_qyfz_tzsj"
    column_name = "(txt_id,ent_name,touzi_date,touzi_round,touzi_money,touzi_ent,touzi_product,touzi_area,touzi_industry,touzi_business,mark,addtime,agency_num,agency_name,batch)"


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
    addtime = ''
    # 机构号
    agency_num = ''
    #机构名称
    agency_name = ''
    #批次
    batch = ''
    table_name = "tyc_qyfz_jpxx"
    column_name = "(txt_id,ent_name,jp_product,jp_area,jp_round,jp_industry,jp_business,jp_date,jp_value,mark,addtime,agency_num,agency_name,batch)"


# 法律诉讼
class TycSffxFlss(object):
    # 日期
    judgment_date = ""
    # 判决文书
    judgment_document = ""
    # 案件类型
    case_type = ""
    # 案件号
    case_number = ""
    # 文书连接
    document_url = ""
    # mongodb文本ID
    txt_id = ""
    # 所属公司名称
    ent_name = ""
    # 添加时间
    add_time = ""
    # 标记号
    mark = ""
    # 判决书内容
    text_info = ""

    # 案件身份
    case_identity=""
    # 机构号
    agency_num = ''
    #机构名称
    agency_name = ''
    #批次
    batch = ''

    table_name = "tyc_sffx_flss"
    column_name = "(judgment_date, judgment_document, case_type, case_identity,case_number, document_url, txt_id, ent_name, add_time, mark,text_info,agency_num,agency_name,batch)"


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
    #机构名称
    agency_name = ''
    #批次
    batch = ''
    table_name = "tyc_sffx_fygg"
    column_name = "(announcement_date, plaintiff, defendant, announcement_type, court, detail_info, txt_id, ent_name, add_time, mark,agency_num,agency_name,batch)"


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
    #机构名称
    agency_name = ''
    #批次
    batch = ''
    table_name = "tyc_sffx_bzxr"
    column_name = "(record_date, Execute_underlying, case_number, court, txt_id, ent_name, add_time, mark,agency_num,agency_name,batch)"


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
    #机构名称
    agency_name = ''
    #批次
    batch = ''
    table_name = "tyc_jyfx_gqcz"
    column_name = "(announcement_date, registration_number, pledgor, pledgee, status, detail_info, txt_id, ent_name, add_time, mark,agency_num,agency_name,batch)"


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
    #机构名称
    agency_name = ''
    #批次
    batch = ''
    table_name = "tyc_jyzk_ztb"
    column_name = "(publish_date, title, title_url, procurement, txt_id, ent_name, add_time, mark,agency_num,agency_name,batch)"


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
    #机构名称
    agency_name = ''
    #批次
    batch = ''

    table_name = "tyc_jyzk_zp"
    column_name = "(publish_date, recruitment_job, salary, work_year, recruitment_numbers, work_city, detail_info, txt_id, ent_name, add_time, mark,agency_num,agency_name,batch)"


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
    #机构名称
    agency_name = ''
    #批次
    batch = ''

    table_name = "tyc_jyzk_swpj"
    column_name = "(year, tax_rating, tax_type, tax_identification_number, evaluate_department, txt_id, ent_name, add_time, mark,agency_num,agency_name,batch)"


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
    #机构名称
    agency_name = ''
    #批次
    batch = ''

    table_name = "tyc_jyzk_ccjc"
    column_name = "(date, type, result, check_department, txt_id, ent_name, add_time, mark ,agency_num,agency_name,batch)"


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
    #机构名称
    agency_name = ''
    #批次
    batch = ''

    table_name = "tyc_jyzk_cpxx"
    column_name = "(product_name, product_referred, product_classification, field, detail_info, txt_id, ent_name, add_time, mark ,agency_num,agency_name,batch)"


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

    table_name = "tyc_zscq_sbxx"
    column_name = "(apply_date, trademark, trademark_name, registration_number, type, status, txt_id, ent_name, add_time, mark ,agency_num,agency_name,batch)"
    def __str__(self):
        return '(\"'+self.apply_date+'\",\"'+ self.trademark+'\",\"'+ self.trademark_name+'\",\"'+self.registration_number+'\",\"'+ \
               self.type+'\",\"'+ self.status+'\",\"'+ self.txt_id+'\",\"'+ self.ent_name+'\",\"'+ self.add_time+'\",'+ self.mark +',\"'\
               +self.agency_num+'\",\"'+self.agency_name+'\",\"'+self.batch+'\")'


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
    #机构名称
    agency_name = ''
    #批次
    batch = ''

    table_name = "tyc_zscq_zl"
    column_name = "(apply_publish_date, patent_name, apply_number, apply_publish_number, detail_info, txt_id, ent_name, add_time, mark ,agency_num,agency_name,batch)"


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
    #机构名称
    agency_name = ''
    #批次
    batch = ''

    table_name = "tyc_zscq_zzq"
    column_name = "(approval_date, software_name, software_referred, registration_number, type_number, version_number, detail_info, txt_id, ent_name, add_time, mark ,agency_num,agency_name,batch)"


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
    #机构名称
    agency_name = ''
    #批次
    batch = ''

    table_name = "tyc_zscq_wzba"
    column_name = "(audit_date, web_name, web_homepage, domain_name, record_number, status, department_type, txt_id, ent_name, add_time, mark ,agency_num,agency_name,batch)"


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

    table_name = "tyc_sffx_sxr"
    column_name = "(case_date, case_number, execution_court, performance_state, execute_number, detail_info, txt_id, ent_name, add_time, mark ,agency_num,agency_name,batch)"


# 经营异常
class TycJyfxJyyc(object):
    # 列入日期
    insert_date = ""
    # 列入原因
    insert_cause = ""
    # 决定机关
    insert_department = ""
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

    table_name = "tyc_jyfx_jyyc"
    column_name = "(insert_date, insert_cause, insert_department,txt_id, ent_name, add_time, mark,agency_num,agency_name,batch)"


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
    #机构名称
    agency_name = ''
    #批次
    batch = ''
    guarantee_amount=''
    table_name = "tyc_jyfx_dcdy"
    column_name = "(registration_date, registration_number, guarantee_type,guarantee_amount, registration_department, status, detail_info, txt_id, ent_name, add_time, mark ,agency_num,agency_name,batch)"


# 行政处罚
class TycJyfxXzcf(object):
    # 决定日期
    decision_date = ""
    # 决定书文号
    decision_number = ""
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

    table_name = "tyc_jyfx_xzcf"
    column_name = "(decision_date, decision_number, type, decision_department, detail_info, punishment_name, punishment_area,txt_id, ent_name, add_time, mark ,agency_num,agency_name,batch)"


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
    #机构名称
    agency_name = ''
    #批次
    batch = ''

    table_name = "tyc_jyzk_zqxx"
    column_name = '(publish_date, bond_name, bond_code, bond_type, latest_rating, detail_info, txt_id, ent_name, add_time, mark ,agency_num,agency_name,batch)'


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
     # 标记号
    mark = ''
    # 添加时间
    addtime = ''
    # 机构号
    agency_num = ''
    #机构名称
    agency_name = ''
    #批次
    batch = ''
    table_name = "tyc_jyfx_yzwf"
    column_name = "(txt_id,ent_name,illegal_date,illegal_reason,office,mark,addtime ,agency_num,agency_name,batch)"


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
    # 标记号
    mark = ''
    # 添加时间
    addtime = ''
    # 机构号
    agency_num = ''
    #机构名称
    agency_name = ''
    #批次
    batch = ''
    table_name = "tyc_jyfx_qsgg"
    column_name = "(txt_id,ent_name,taxes_date,taxes_num,taxes_type,taxes_money,taxes_balance,taxes_office,mark,addtime,agency_num,agency_name,batch)"


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
    # 标记号
    mark = ''
    # 添加时间
    addtime = ''
    # 机构号
    agency_num = ''
    #机构名称
    agency_name = ''
    #批次
    batch = ''
    table_name = "tyc_jyzk_gdxx"
    column_name = "(txt_id,ent_name,gd_sign_date,gd_num,gd_act_date,gd_area,gd_region,gd_operate,mark,addtime,agency_num,agency_name,batch)"


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
    addtime = ''
    # 机构号
    agency_num = ''
    #机构名称
    agency_name = ''
    #批次
    batch = ''
    table_name = "tyc_jyzk_zzzs"
    column_name = "(txt_id,ent_name,certificate_type,certificate_num,send_date,off_date,mark,addtime ,agency_num,agency_name,batch)"


# 企业年报
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
    #机构名称
    agency_name = ''
    #批次
    batch = ''
    table_name = "tyc_qybj_qynb"
    column_name = "(year, detail_url, txt_id, ent_name, add_time, mark ,agency_num,agency_name,batch)"

# 作品著作权
class TycZscqZpzzq(object):
    # mongodb文本ID
    txtId =""
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
    register_date =''
    # 首期发布日期
    firstpublish_date =''
    # 标记号
    mark = ''
    # 添加时间
    add_time = ''
    # 机构号
    agency_num = ''
    #机构名称
    agency_name = ''
    #批次
    batch = ''
    # 对应表
    table_name = "tyc_zscq_zpzzq"
    # 加入数据库

    column_name = "(works_name, register_name, type, creat_date, register_date, firstpublish_date, txt_id, ent_name, add_time, mark ,agency_num,agency_name,batch)"

# 微信公众号
class TycJyzkWxgzh(object):
    # mongodb文本ID
    txtId = ''
    # 所属公司名称
    ent_name = ''
    # 公众号名称
    mp_name = ''
    # 微信号
    mp_number=''
    # 公众号简介
    mp_info=''
    # 添加时间
    addtime = ""
    # 标记号
    mark = ""
    # 机构号
    agency_num = ''
    #机构名称
    agency_name = ''
    #批次
    batch = ''
    # 对应表
    table_name = "tyc_jyzk_wxgzh"

    # 加入数据库
    column_name = "(mp_name,mp_number,mp_info,txt_Id,ent_name,mark,addtime ,agency_num,agency_name,batch)"

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
    # 经营类别
    manger_type = ''
    # 详情
    detail_info = ''
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
     # 对应表
    table_name = "tyc_jyzk_jckxy"
    # 加入数据库
    column_name = "(register_customs,customs_number,manger_type,detail_info,txt_Id,ent_name,mark,addtime ,agency_num,agency_name,batch)"

# 年报基本信息
class TycYearJbxx(object):

    # mongodb文本ID
    txtId = ''
    # 所属公司名称
    entName = ''
    # 年份
    year = ''
    # 公司名称
    ent_name = ''
    # 统一社会信用代码
    credit_num = ''
    # 企业名称
    company_name = ''
    # 企业联系电话
    company_tel = ''
    # 邮政编码
    postal_code = ''
    # 企业经营状态
    manger_state = ''
    # 从业人数
    people_count =''
    # 电子邮箱
    email =''
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
    #机构名称
    agency_name = ''
    #批次
    batch = ''
    # 对应的表
    table_name = "tyc_year_jbxx"
    # 加入数据库

    column_name = "(credit_num,company_name,company_tel,postal_code,manger_state,people_count,email,website,company_address,buy_equity,year,txt_id,ent_name,add_time,mark,agency_num,agency_name,batch)"

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
    #名称
    web_name = ''
    # 网址
    web_url=''
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
    # 对应的表
    table_name = "tyc_year_wzhwdxx"
    # 加入数据库
    column_name = "(website_type,web_name,web_url,year,txt_id,ent_name,add_time,mark,agency_num,agency_name,batch)"



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
    contribution_style =''
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
    #机构名称
    agency_name = ''
    #批次
    batch = ''
    # 对应的表
    table_name = "tyc_year_gdczxx"
    # 加入数据库
    column_name = "(shareholder,subscirbe_contribution,contribution_time,contribution_style,actual_contribution,actual_time,actual_style,year,txt_id,ent_name,add_time,mark,agency_num,agency_name,batch)"

class TycYearZczk(object):

    # mongodb文本ID
    txtId = ''
    # 所属公司名称
    entName = ''
    # 年份
    year = ''
    # 资产总额
    total_assets =''
    # 销售总额
    total_sales = ''
    # 营业总收入中主营业务收入
    operation_income = ''
    # 纳税总额
    total_tax =''
    # 所有者权益合计
    total_income = ''
    # 利润总额
    total_profit =''
    # 净利润
    net_profit = ''
    # 负债总额
    total_debt =''
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
    # 对应的表
    table_name = "tyc_year_zczk"
    # 加入数据库

    column_name = "(total_assets,total_income,total_sales,total_profit,operation_income,net_profit,total_tax,total_debt,year,txt_id,ent_name,add_time,mark,agency_num,agency_name,batch)"
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
    #机构名称
    agency_name = ''
    #批次
    batch = ''
    # 对应的表
    table_name = "tyc_year_dwtz"
    # 加入数据库
    column_name = "(credit_num,outbound_company,year,txt_id,ent_name,add_time,mark,agency_num,agency_name,batch)"

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

    column_name = '(batch,end_time)'

class Batch_Detail(object):
    company_number=""
    mark=""
    company_name=""
    company_address=""
    searched=""
    error=""
    add_time=""
    agency_num=""
    agency_name=""
    batch=""
    txt_id=""
    data_type=""
    table_name = 'batch_detail'
    column_name="company_number,mark,company_name,company_address,searched,error,add_time,agency_num,agency_name,batch,txt_id,data_type"


if __name__=="__main__":
    ss=TycZscqSbxx()
    print str(ss)


