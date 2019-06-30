# !/usr/bin/env python
import logging.config
import re
import sys
# import HTMLParser
from datetime import datetime

from bs4 import BeautifulSoup
from bson import ObjectId
# from cpca import *
from cpca import transform
from lxml import etree
from sqlalchemy import select
import copy
from util.replace_special_util import replace_special_chars
from util.try_and_except_util import try_and_text
from db import single_mongodb, single_oracle
from redis_cache import single_redis
# from tyc_bean_1 import *
from sqlalchemy import func

# reload(sys)
# sys.setdefaultencoding('utf-8')
from models import *

logging.config.fileConfig("../log_file/parse.conf")

logger = logging.getLogger("loggerText")

CURRENT_VERSION_NULL = '此版本无此信息'

NEXT_PAGE_DICT = {
    '北京百度网讯科技有限公司': {
        'tyc_zscq_wzba': '网站备案',
        'tyc_qybj_dwtz': '对外投资',
        'tyc_jyfx_xzcf': '行政处罚 工商局',
        'tyc_qybj_bgjl': '变更记录',
        'tyc_sffx_ktgg': '开庭公告',
        'tyc_sffx_flss': '法律诉讼',
        'tyc_sffx_fygg': '法院公告',
        'tyc_jyfx_gqcz': '股权出质',
        'tyc_qyfz_hxtd': '核心团队',
        'tyc_qyfz_qyyw': '企业业务',
        'tyc_qyfz_tzsj': '投资事件',
        'tyc_qyfz_jpxx': '竞品信息',
        'tyc_jyzk_zp': '招聘信息',
        'tyc_jyzk_gsj': '行政许可 工商局',
        'tyc_jyzk_ccjc': '抽查检查',
        'tyc_jyzk_zzzs': '资质证书',
        'tyc_jyzk_ztb': '招投标',
        'tyc_jyzk_cpxx': '产品信息',
        'tyc_jyzk_wxgzh': '微信公众号',
        'tyc_zscq_sbxx': '商标信息',
        'tyc_zscq_zl': '专利',
        'tyc_zscq_zzq': '软件著作权',
        'tyc_zscq_zpzzq': '作品著作权'},
    '中国移动通信集团广东有限公司': {
        'tyc_zscq_wzba': '网站备案',
        'tyc_qybj_bgjl': '变更记录',
        'tyc_qybj_fzjg': '分支机构',
        'tyc_sffx_ktgg': '开庭公告',
        'tyc_sffx_flss': '法律诉讼',
        'tyc_sffx_fygg': '法院公告',
        'tyc_jyzk_gsj': '行政许可 工商局',
        'tyc_jyzk_ztb': '招投标',
        'tyc_jyzk_wxgzh': '微信公众号',
        'tyc_jyzk_gdxx': '购地信息',
        'tyc_zscq_sbxx': '商标信息',
        'tyc_zscq_zl': '专利',
        'tyc_zscq_zzq': '软件著作权'},
    '佐源集团有限公司': {
        'tyc_sffx_sxr': '失信人',
        'tyc_sffx_bzxr': '被执行人',
        'tyc_sffx_sfxz': '司法协助',
        'tyc_qybj_bgjl': '变更记录',
        'tyc_sffx_ktgg': '开庭公告',
        'tyc_sffx_flss': '法律诉讼',
        'tyc_sffx_fygg': '法院公告',
        'tyc_jyfx_qsgg': '欠税公告',
        'tyc_zscq_sbxx': '商标信息',
        'tyc_zscq_zl': '专利'},
    '乐视控股（北京）有限公司': {
        'tyc_qybj_dwtz': '对外投资',
        'tyc_sffx_sxr': '失信人',
        'tyc_sffx_bzxr': '被执行人',
        'tyc_qybj_bgjl': '变更记录',
        'tyc_sffx_ktgg': '开庭公告',
        'tyc_sffx_flss': '法律诉讼',
        'tyc_sffx_fygg': '法院公告',
        'tyc_sffx_sfxz': '司法协助',
        'tyc_jyfx_gqcz': '股权出质',
        'tyc_qyfz_jpxx': '竞品信息'},
    '北京京东世纪贸易有限公司': {
        'tyc_qybj_dwtz': '对外投资',
        'tyc_jyzk_ccjc': '抽查检查',
        'tyc_jyzk_xyzg': '行政许可 信用中国',
        'tyc_qybj_bgjl': '变更记录',
        'tyc_sffx_ktgg': '开庭公告',
        'tyc_sffx_flss': '法律诉讼',
        'tyc_sffx_fygg': '法院公告',
        'tyc_jyfx_xzcf': '行政处罚 工商局',
        'tyc_jyfx_sfpm': '司法拍卖',
        'tyc_qyfz_tzsj': '投资事件',
        'tyc_qyfz_jpxx': '竞品信息',
        'tyc_jyzk_zp': '招聘信息',
        'tyc_jyzk_zzzs': '资质证书',
        'tyc_jyzk_ztb': '招投标',
                        'tyc_jyzk_wxgzh': '微信公众号',
                        'tyc_zscq_sbxx': '商标信息',
                        'tyc_zscq_zl': '专利',
                        'tyc_zscq_zzq': '软件著作权',
                        'tyc_zscq_zpzzq': '作品著作权'},
    '武汉品口科技有限责任公司': {},
    '浙江海正动物保健品有限公司': {
        'tyc_jyzk_gsj': '行政许可 工商局',
        'tyc_zscq_zl': '专利'},
    '河南丰利环保科技有限公司': {
        'tyc_qybj_bgjl': '变更记录',
        'tyc_sffx_fygg': '法院公告',
        'tyc_zscq_sbxx': '商标信息',
    }}


def check_next_page(company_name, table_name):
    '''
    翻页解析方法正确执行时，从全局翻页页面的字典中去掉当前模块，最终剩余id则为未执行分页解析的模块
    :param table_name: 当前模块对应的表名;company_name:当前解析的企业名称
    :return: 无
    '''
    global NEXT_PAGE_DICT
    try:
        if table_name in NEXT_PAGE_DICT[company_name] and NEXT_PAGE_DICT[company_name].get(
                table_name):
            del NEXT_PAGE_DICT[company_name][table_name]
    except Exception as e:
        print('check next page errot:{}'.format(e))


def check_company_next_page(NEXT_PAGE_DICT,search_name):
    '''
    汇总结算当前公司所有翻页模块是否正常解析，把未正常翻页的模块对应表名入库check_result
    :param NEXT_PAGE_DICT: 标杆企业有分页的表格键值对
    :param search_name: 当前公司名称
    :return: 无
    '''
    # global NEXT_PAGE_DICT
    if NEXT_PAGE_DICT[search_name]:
        # 记录未成功解析的企业和对应的模块，并入库记录
        # not_parse_table_names = str(list(NEXT_PAGE_DICT[search_name].values()))[1:-1].replace('\'',
        #                                                                                       '')  # 得出未解析的模块名称拼接字符串
        next_page_parse = CheckResult()
        next_page_parse.company_name = search_name
        next_page_parse.add_time = func.now()
        # next_page_parse.different_reason = '分页未解析模块:' + not_parse_table_names
        # next_page_parse.table_name = str(list(NEXT_PAGE_DICT[search_name].keys()))[1:-1].replace('\'', '')
        next_page_parse.table_field = '-'
        next_page_parse.standard_value = '-'
        next_page_parse.current_value = '-'
        next_page_parse.risk_level = 1
        next_page_parse.standard_version = 1
        try:
            print('next_page_parse=================', next_page_parse.__dict__)
            for one_table_name,one_table_show in NEXT_PAGE_DICT[search_name].items():
                next_page_parse.table_name = one_table_name
                next_page_parse.different_reason = '分页解析异常模块:' + one_table_show
                single_oracle_orm.add(next_page_parse)
                single_oracle_orm.commit()
        except Exception as e:
            single_oracle_orm.rollback()
            print('分页未解析模块提交异常：{}'.format(e), '\n', next_page_parse.different_reason)


def check_parse(flss, add_result, unique_field):
    '''
    检测解析字段是否有误，检测到第一个有误的，只记录第一条然后停止检测
    :param add_result: check_result对象
    :param current_table:当前模块的表名
    :param unique_field:当前模块对应库表可做唯一值的字段
    :param flss:当前模块对象
    :return:
    '''
    print(
        '开始核对字段解析是否有误:{}==={}'.format(
            flss.company_name,
            add_result.table_name))
    flss_dict = flss.__dict__
    if flss_dict:
        #print('check_parse flss_dict=============', flss_dict)
        for table_field, current_value in flss_dict.items():

            if current_value == '解析有误':
                add_result.table_field = table_field
                add_result.current_value = current_value
                add_result.different_reason = '页面解析异常'
                qurey_import_and_standard(add_result, unique_field)
                print('解析有误查询标准值>>>>>>>>>', table_field, current_value)
                return 1


def qurey_import_and_standard(add_result, unique_field):
    '''
    查询该字段重要等级，和标准值
    :param add_result: check_result对象
    :param current_table:当前模块的表名
    :param unique_field:当前模块对应库表可做唯一值的字段
    :return:
    '''
    orc_conn = engine.connect()
    table_field = add_result.table_field
    check_import_field = CheckImportField  # 关键字表的model类名
    current_table = add_result.table_name  # 当前表名
    unique_field_name = unique_field[0]  # 唯一值字段名
    unique_field_value = unique_field[1]  # 唯一值
    print('开始查询该字段重要等级，和标准值', add_result.__dict__)
    try:
        add_result.risk_level = single_oracle_orm.query(check_import_field).filter_by(
            column_name=table_field).first().column_level  # 查询当前字段的重要等级
    except Exception as e:
        add_result.risk_level = 2
        print('CheckImportField not found === {}'.format(e))
    try:
        query_sql = "select " + table_field + " from " + current_table + \
            " WHERE " + unique_field_name + " = '" + unique_field_value + "'"
        add_result.standard_value = orc_conn.execute(
            query_sql).fetchone()[0]  # 查询当前字段的唯一标准值
        print('查询的标准值：', add_result.standard_value)
    except Exception as e:
        print('CheckImportField search error === {}'.format(e))
    try:
        single_oracle_orm.add(add_result)
        single_oracle_orm.commit()
    except Exception as e:
        print('查询标准值后插入对应标准值有误：{}'.format(e))


def check_obj(cls_spider, cls_standard):
    '''
    对比爬虫解析对象和标准库对象各字段值（detail详情clob除外）
    :param cls_spider: 解析字段的对象
    :param cls_standard: 标准库对象
    :return: 不同于标准库的字段
    '''
    cls_spider_dict = cls_spider.__dict__
    cls_standard_dict = cls_standard.__dict__
    change_dict = {}
    pass_k = [
        'detail',
        'txt_id',
        'batch',
        'id',
        'agency_name',
        'agency_num',
        '_sa_instance_state',
        'add_time',
        'judgment_document',
        'standard_version',
        'detail_status',
        'mark',
        'detail_info']
    for k, v in cls_spider_dict.items():
        if 'detail' in k:
            if not v:  # 判断detail字段是否不为空
                return 1  # 如果detail为空则，返回True，认为该行数据不是全字段匹配
        if k in pass_k:
            continue
        if v == cls_standard_dict[k]:
            pass
        else:
            change_dict[k] = v
    return change_dict


def check_all_data(add_result, cls_spider, current_class):
    '''
    页面解析第一条和标准库每一条进行对比，有一条匹配则通过，没有匹配则认为：全字段不匹配
    :param cls_spider: 页面解析的数据对象
    :param cls_standard: 表中库对象
    :return:有无匹配到数据：1 匹配到，None 未匹配
    '''
    print(
        '开始核对首页全字段数据：{}==={}'.format(
            cls_spider.company_name,
            add_result.table_name))
    change_flag = 0
    company_name = cls_spider.company_name
    standard_datas = single_oracle_orm.query(
        current_class).filter_by(company_name=company_name).all()

    for cls_standard in standard_datas:

        check_res = check_obj(cls_spider, cls_standard)
        # print('逐一对比字段后有不匹配的字段：{}'.format(check_res))
        if check_res:
            # 全字段不匹配
            pass
        else:
            # 有匹配到的行
            change_flag += 1
    if change_flag >= 1:
        return 1  # 匹配到数据
    else:
        return 0  # 没匹配到数据


def check_thead(table, thead_list):
    '''
    核对表头信息是否增加，删除，改变
    :param table: xpath定位到table的对象
    :param table_list: 存放表头信息的列表
    :return: 携带核对结果信息的字典
    '''

    ths = table[0].xpath('./thead/tr//text()')
    if '查看实际控股人 >' in ths:
        ths.remove('查看实际控股人 >')
    result_dict = {}
    if ths:
        # 列数增加
        if len(ths) > len(thead_list):
            mesg = '表头信息增加的列为：{}'.format(
                list(set(ths).difference(set(thead_list))))
            result_dict['res'] = 'False'
            result_dict['mesg'] = mesg
        # 列数减少
        elif len(ths) < len(thead_list):
            mesg = '表头信息减少的列为：{}'.format(
                list(set(thead_list).difference(set(ths))))
            result_dict['res'] = 'False'
            result_dict['mesg'] = mesg
        elif len(ths) == len(thead_list):
            for i in range(len(ths)):
                # 表头信息改动
                if ths[i] not in thead_list:
                    mesg = '有变动的表头信息为：{}'.format(
                        list(set(thead_list).difference(set(ths))))
                    result_dict['res'] = 'False'
                    result_dict['mesg'] = mesg
                # 表头信息次序变动
                elif ths[i] in thead_list and ths[i] != thead_list[i]:
                    result_dict['res'] = 'False'
                    result_dict['mesg'] = '表头信息次序改变'
                else:
                    return True

        return result_dict


def insert_result(company_name, table_name, result_dict):
    '''
    将表头信息核对结果插入到check_result表中
    :param table_name: 表名
    :param message:  携带有表头核对结果信息的字典
    :return:
    '''
    if result_dict:
        pass
    else:
        checkResult = CheckResult()
        checkResult.company_name = company_name
        checkResult.table_name = table_name
        checkResult.add_time = func.now()
        checkResult.standard_version = 1
        checkResult.risk_level = 1
        checkResult.task_status = 0

        if result_dict['res'] == 'False':
            # print(result_dict['mesg'])5
            checkResult.different_reason = result_dict['mesg']
        print(checkResult.different_reason)
        single_oracle_orm.add(checkResult)
        single_oracle_orm.commit()


###########################################################################

def decode_dict_date(word, dicts):
    logger.debug('decode_dict_date  yuan==='.format(word))
    try:
        new_word = ''
        for i in word:
            if i in dicts.keys():
                new_word += dicts[i]
            else:
                new_word += i
        logger.debug('decode_dict_date  xin====={}'.format(new_word))
        return new_word
    except Exception as e:
        logger.debug(e)
        new_word = word
    return new_word


def create_insert_sql(table_name, table_column, column_count):
    insert_sql = 'insert into ' + table_name + ' ' + table_column + ' values('
    for i in range(1, column_count):
        insert_sql += ':' + str(i) + ','
    insert_sql += 'sysdate)'
    return insert_sql


class TycDetailParse(object):
    txt_id = ''
    entName = ''
    agency_num = ''
    agency_name = ''
    batch = ''
    soup = None
    selector = None
    detail_info = None

    def __init__(self, mongo, oracle, search_name):
        self.single_mongodb = mongo
        single_oracle = oracle
        self.dicts = {}
        self.search_name = search_name
        ############################################################

    # 解析：企业背景-->基本信息(工商信息)
    def html_parse_baseinfo(self):

        logger.debug("Parse detail info 基本信息 {}".format(self.search_name))
        top = self.selector.xpath('//div[@id="company_web_top"]')

        table_lists = (self.selector.xpath(
            '//div[contains(@id,"_container_baseInfo")]//table'))
        # text_list = table_lists[0].xpath('string(.)')
        # text_list2 = table_lists[0].xpath('string(.)')
        if top:
            baseinfo = TycQybjJbxx()
            key = self.search_name
            top = top[0]
            # 新增异常捕获，无邮箱信息无class=email
            try:
                email = top.xpath('.//span[@class="pl5"]/script/text()')
                # print('email', email[0])
                if not email:
                    email = top.xpath('.//span[@class="email"]/text()')
                email = email[0]
            except BaseException:
                email = 'NA'
            baseinfo.email = email.replace(
                u'"', u'').replace(
                u'[', u'').replace(
                u']', u'')
            # print(baseinfo.email)
            detail_basic = top.xpath(
                './/div[@class="box -company-box "]/div[@class="content"]/div[contains(@class,"detail")]')
            if detail_basic:
                insert_value = ""
                detail_basic = detail_basic[0]
                # #logger.debug(detail_basic.xpath('string()'))
                telephone = detail_basic.xpath('./div/div/span//script/text()')
                if not telephone:
                    telephone = detail_basic.xpath(
                        './div[position()=1]/div[position()=1]/span[2]/text()')

                baseinfo.telephone = telephone[0].replace(
                    u'"', u'').replace(u'[', u'').replace(u']', u'')
                urls = detail_basic.xpath(
                    './div[position()=2]//a[@class="company-link"][position()=1]/text()')
                baseinfo.url = urls[0] if urls else 'NA'

            if table_lists:
                # string_list=table[0].xpath('/string()')

                trs0 = table_lists[0].xpath('./tbody/tr')
                trs1 = table_lists[1].xpath('./tbody/tr')
                if trs0 and trs1:
                    # dict_list
                    logger.debug('Traceback: lenth()={}'.format(len(trs1)))
                    dicts = self.dicts
                    try:
                        registerFund = trs1[0].xpath(
                            './td/div/@title')[0] or 'NA'

                    except BaseException:
                        registerFund = trs1[0].xpath('./td//text()')[0]
                    baseinfo.register_fund = registerFund

                    baseinfo.company_status = trs1[1].xpath(
                        './td[2]//text()')[0]
                    baseinfo.register_num = trs1[1].xpath('./td[4]//text()')[0]
                    baseinfo.tissue_num = trs1[2].xpath(
                        './td[position()=4]/text()')[0]
                    baseinfo.credit_num = trs1[2].xpath(
                        './td[position()=2]/text()')[0]
                    baseinfo.company_type = trs1[3].xpath(
                        './td[4]')[0].xpath('string(.)')
                    baseinfo.taxpayer_num = trs1[3].xpath(
                        './td[2]')[0].xpath('string(.)')
                    baseinfo.industry = trs1[4].xpath(
                        './td[4]')[0].xpath('string(.)')
                    businessTerm = trs1[4].xpath(
                        './td[2]')[0].xpath('string(.)')
                    if businessTerm == '-' or businessTerm == '未公开':
                        business_term_begin = business_term_end = '-'
                    else:
                        business_term_begin = businessTerm.split('至')[0]
                        business_term_end = businessTerm.split('至')[1]
                        if business_term_end == '无固定期限':
                            business_term_end = '2999-12-31'
                    baseinfo.business_term_begin = business_term_begin
                    baseinfo.business_term_end = business_term_end

                    registerDate = try_and_text(
                        "variable[0].xpath('./td[4]')[0].xpath('string(.)')", trs1)
                    # 新增 纳税人资质
                    taxQualificate = try_and_text(
                        "variable[5].xpath('./td[2]')[0].xpath('string(.)')", trs1)
                    baseinfo.taxpayer_qualificate = taxQualificate[0] if taxQualificate else 'NA'

                    checkDate = try_and_text(
                        "variable[5].xpath('./td[4]')[0].xpath('string(.)')", trs1)
                    #
                    regDate = ''.join(registerDate.strip('-'))
                    checDate = ''.join(checkDate.strip('-'))
                    if self.dicts:
                        if checDate > '20191231' or checDate < '19500101':
                            checkDate = decode_dict_date(checkDate, dicts)
                        if regDate > '20191231' or regDate < '19500101':
                            registerDate = decode_dict_date(
                                registerDate, dicts)
                    #
                    baseinfo.business_term = businessTerm
                    baseinfo.register_date = registerDate
                    baseinfo.check_date = checkDate

                    baseinfo.english_name = try_and_text(
                        "variable[8].xpath('./td[4]')[0].xpath('string(.)')", trs1)
                    # 此处改为曾用名
                    baseinfo.used_name = try_and_text(
                        "variable[8].xpath('./td[2]')[0].xpath('string(.)')",
                        trs1).replace(
                        '查看更多',
                        '')
                    baseinfo.register_site = try_and_text(
                        "variable[9].xpath('./td[2]')[0].xpath('string(.)')",
                        trs1).replace(
                        '附近公司',
                        '')
                    address_1 = address_2 = address_3 = 'NA'

                    df = transform([baseinfo.register_site], cut=False)
                    for addr in df.index:
                        print(addr)
                        baseinfo.address_1 = df.loc[addr].values[0]
                        baseinfo.address_2 = df.loc[addr].values[1]
                        baseinfo.address_3 = df.loc[addr].values[2]

                    businessScope = replace_special_chars(try_and_text(
                        "variable[10].xpath('./td[2]')[0].xpath('string(.)')", trs1))
                    baseinfo.business_scope = businessScope.replace(
                        "'", '') if businessScope else 'NA'

                    # 人员规模
                    baseinfo.person_size = try_and_text(
                        "variable[6].xpath('./td[4]')[0].xpath('string(.)')", trs1)
                    # 实缴资本：
                    baseinfo.paid_capital = try_and_text(
                        "variable[6].xpath('./td[2]')[0].xpath('string(.)')", trs1)
                    # 参保人数：
                    baseinfo.insured_person = try_and_text(
                        "variable[7].xpath('./td[2]')[0].xpath('string(.)')", trs1)
                    baseinfo.register_office = try_and_text(
                        "variable[7].xpath('./td[4]')[0].xpath('string(.)')", trs1)
                    baseinfo.txt_id = self.txt_id or 'NA'
                    baseinfo.company_name = key
                    baseinfo.mark = 0
                    baseinfo.add_time = func.now()
                    baseinfo.agency_num = self.agency_num
                    baseinfo.agency_name = self.agency_name
                    baseinfo.batch = self.batch
                    baseinfo.industry_4 = 'NA'

                    print('正在核实的公司是{}'.format(key))
                    standard_data = single_oracle_orm.query(
                        TycQybjJbxx).filter_by(company_name=key).first()
                    try:
                        change_dict = check_obj(baseinfo, standard_data)
                        print('核对结果为：', change_dict)

                        checkResult = CheckResult()
                        checkResult.company_name = key
                        checkResult.add_time = func.now()
                        checkResult.standard_version = 1
                        checkResult.task_status = 0
                        for k, v in change_dict.items():
                            checkResult.current_value = v
                            checkResult.table_name = baseinfo.__tablename__
                            checkResult.table_field = k
                            checkResult.standard_value = standard_data.__dict__[
                                k]
                            checkResult.different_reason = '{}表中字段{}的值未核对成功'.format(
                                key, k)
                            import_field = single_oracle.oracle_find_by_param_all(
                                "select column_name from check_import_field where table_name = '{}'".format(
                                    checkResult.table_name))
                            # print(import_field)
                            for col_name in import_field:
                                if k == col_name:
                                    checkResult.risk_level = 1
                                else:
                                    checkResult.risk_level = 2
                            single_oracle_orm.add(checkResult)
                            single_oracle_orm.commit()
                    except Exception as e:
                        print(e)
                        # check_obj(baseinfo,standard_data)
                        # print('核对结果为：',change_dict)

    # 解析：企业背景-->主要人员
    def html_parse_mainPerson(self):

        logger.debug("Parse detail info 主要人员 {}".format(self.search_name))
        mainPerson = TycQybjZyry()
        table_name = mainPerson.__tablename__

        table = self.selector.xpath('//div[@id="_container_staff"]/div/table')
        if table:
            thead_list = ['序号', '姓名', '职位']
            # thead_list = ['序号', '姓名']
            result_dict = check_thead(table, thead_list)
            table_name = mainPerson.__tablename__
            print('表头核对结果为.....：', result_dict)
            if result_dict:
                trs = table[0].xpath('./tbody/tr')

                # print(trs)
                first_parse_data = None
                if trs:
                    # mainPerson = TycQybjZyry()
                    key = self.search_name
                    # trs = trs[0]

                    add_result = CheckResult()
                    add_result.company_name = key
                    add_result.add_time = func.now()
                    # add_result.table_name = 'tyc_qybj_jbxx'  # 当前表名
                    add_result.table_name = table_name  # 当前表名
                    current_class = TycQybjZyry  # 当前模块对象名

                    check_flag = 0  # 检测首页是否有匹配到的一行数据
                    check_first = 0  # 检测首页是否有匹配到的第一行数据

                    for div in trs:
                        insert_value = ""
                        # logger.debug(div)
                        # xuhao = .xpath('./td')[0].xpath('string(.)')
                        position = div.xpath('./td[3]//text()')

                        mainPerson.position = ''.join(position).replace(
                            '\n', '').replace(
                            "'", '') if position else 'NA'
                        name = div.xpath('./td[2]//div//a/text()')
                        try:
                            mainPerson.person_name = name[0].replace(
                                '\n', '').replace(
                                "'", '') if name else 'NA'
                        except BaseException:
                            mainPerson.person_name = 'ERROR'
                        mainPerson.txt_id = self.txt_id
                        mainPerson.company_name = key
                        mainPerson.mark = 0
                        mainPerson.add_time = func.now()
                        mainPerson.agency_num = self.agency_num
                        mainPerson.agency_name = self.agency_name
                        mainPerson.batch = self.batch

                        unique_field = [
                            'company_name', mainPerson.company_name]  # 该模块中唯一值字段名和值
                        check_parse(mainPerson, add_result, unique_field)

                        # 验证首页解析
                        check_result = check_all_data(
                            add_result, mainPerson, current_class)
                        if not first_parse_data:
                            first_parse_data = mainPerson  # 保存第一条解析的数据
                        print('check_result+++++++++======:', check_result)
                        check_first += 1
                        if check_result:
                            check_flag = 1  # 匹配到数据
                            break
                        else:
                            check_flag = 0  # 没有匹配到
                    if not check_flag:
                        # 如果首页没有匹配到，则保存首页第一条数据到标准库，并记录其中一个字段
                        print('首页没有匹配到数据》》》》》》》》》')
                        try:

                            add_result.table_field = 'position'  # 保存第一各异常字段名   各模块手动添加
                            add_result.current_value = first_parse_data.position  # 保存第一各异常字段值   各模块手动添加
                            add_result.different_reason = '该页信息都不匹配，请通知数据管理员'
                            add_result.risk_level, add_result.standard_version = 1, 1
                            standard_value = single_oracle_orm.query(current_class).filter_by(  # 各表不同
                                company_name=first_parse_data.company_name).first()
                            add_result.standard_value = standard_value.position if standard_value else '-'
                            single_oracle_orm.add(add_result)
                            single_oracle_orm.commit()
                        except Exception as e:
                            print('check all datas error===={}'.format(e))
                    elif check_first > 1 and check_flag:
                        # 匹配到但不是第一条，更新页面第一条到标准库
                        unique_line = single_oracle_orm.query(
                            current_class).first()
                        single_oracle_orm.delete(unique_line)
                        single_oracle_orm.add(first_parse_data)
                        single_oracle_orm.commit()
                        print(
                            '首页已匹配到数据，但不是第一条,更新为当前页第一条》》》》》》》！{}'.format(key))
            else:
                insert_result(self.search_name, table_name, result_dict)

    # 解析：企业背景-->股东信息
    def html_parse_shareholderInfo(self, index):
        logger.debug("Parse detail info 股东信息 {}".format(self.search_name))

        shareholderInfo = TycQybjGdxx()
        if index == 1 and not isinstance(self.selector, int):
            # 分页是否解析：传入当前公司名称和当前模块对应的数据表名
            check_next_page(self.search_name, 'tyc_qybj_gdxx')
        else:
            table = self.selector.xpath('//div[@id="_container_holder"]/table')
            if table:
                thead_list = ['序号', '股东（发起人）', '出资比例', '认缴出资额', '认缴出资日期']
                result_dict = check_thead(table, thead_list)
                print('表头核对结果为.....：', result_dict)
                table_name = shareholderInfo.__tablename__
                if result_dict:

                    # print(table_name)
                    # insert_result(self.search_name, table_name, result_dict)
                    trs = table[0].xpath('./tbody/tr')

                    # trs = (self.selector.xpath(
                    #     '//div[@id="_container_holder"]/table/tbody/tr'))

                    if trs:
                        # shareholderInfo = TycQybjGdxx()
                        key = self.search_name
                        # 创建新增对象 TODO: 测试核对第一条数据
                        add_result = CheckResult()
                        add_result.company_name = key
                        add_result.add_time = func.now()
                        # add_result.table_name = 'tyc_qybj_jbxx'  # 当前表名
                        add_result.table_name = table_name  # 当前表名
                        current_class = TycQybjGdxx  # 当前模块对象名
                        first_parse_data = None
                        check_flag = 0  # 检测首页是否有匹配到的一行数据
                        check_first = 0  # 检测首页是否有匹配到的第一行数据

                        for tr in trs:
                            insert_value = ""
                            tds = tr.xpath('./td')
                            shareholderInfo.shareholder = try_and_text(
                                "variable[1].xpath('.//a/text()')[0]", tds)
                            shareholderInfo.fund_ratio = try_and_text(
                                "variable[2].xpath('.//text()')[0]", tds)
                            shareholderInfo.fund_subcribe = try_and_text(
                                "variable[3].xpath('.//text()')[0]", tds)
                            shareholderInfo.txt_id = self.txt_id
                            shareholderInfo.company_name = key
                            shareholderInfo.mark = 0
                            shareholderInfo.add_time = func.now()
                            shareholderInfo.agency_num = self.agency_num
                            shareholderInfo.agency_name = self.agency_name
                            shareholderInfo.batch = self.batch

                            # 增加 出资时间
                            fundTime = try_and_text(
                                "variable[4].xpath('.//text()')", tds)
                            shareholderInfo.fund_time = fundTime[0] if fundTime else 'NA'
                            #

                            unique_field = [
                                'company_name', shareholderInfo.company_name]  # 该模块中唯一值字段名和值
                            check_parse(
                                shareholderInfo, add_result, unique_field)

                            # 验证首页解析
                            check_result = check_all_data(
                                add_result, shareholderInfo, current_class)
                            if not first_parse_data:
                                first_parse_data = shareholderInfo  # 保存第一条解析的数据
                            print('check_result+++++++++======:', check_result)
                            check_first += 1
                            if check_result:
                                check_flag = 1  # 匹配到数据
                                break
                            else:
                                check_flag = 0  # 没有匹配到
                        if not check_flag:
                            # 如果首页没有匹配到，则保存首页第一条数据到标准库，并记录其中一个字段
                            print('首页没有匹配到数据》》》》》》》》》')

                            try:

                                add_result.table_field = 'shareholder'  # 保存第一各异常字段名   各模块手动添加
                                add_result.current_value = first_parse_data.shareholder  # 保存第一各异常字段值   各模块手动添加
                                add_result.different_reason = '该页信息都不匹配，请通知数据管理员'
                                add_result.risk_level, add_result.standard_version = 1, 1
                                standard_value = single_oracle_orm.query(current_class).filter_by(  # 各表不同
                                    company_name=first_parse_data.company_name).first()
                                add_result.standard_value = standard_value.shareholder if standard_value else '-'
                                single_oracle_orm.add(add_result)
                                single_oracle_orm.commit()
                            except Exception as e:
                                print('check all datas error===={}'.format(e))
                        elif check_first > 1 and check_flag:
                            # 匹配到但不是第一条，更新页面第一条到标准库
                            unique_line = single_oracle_orm.query(
                                current_class).first()
                            single_oracle_orm.delete(unique_line)
                            single_oracle_orm.add(first_parse_data)
                            single_oracle_orm.commit()
                            print(
                                '首页已匹配到数据，但不是第一条,更新为当前页第一条》》》》》》》！{}'.format(key))

                else:
                    insert_result(self.search_name, table_name, result_dict)

    # 解析：企业背景-->对外投资
    def html_parse_investInfo(self, index):
        logger.debug("Parse detail info 对外投资 {}".format(self.search_name))
        investInfo = TycQybjDwtz()
        if index == 1 and not isinstance(self.selector, int):
            # 分页是否解析：传入当前公司名称和当前模块对应的数据表名
            check_next_page(self.search_name, 'tyc_qybj_dwtz')
        else:
            table = self.selector.xpath('//div[@id="_container_invest"]/table')
            if table:
                thead_list = [
                    '序号',
                    '被投资企业名称',
                    '被投资法定代表人',
                    '投资占比',
                    '注册资本',
                    '成立日期',
                    '经营状态']
                result_dict = check_thead(table, thead_list)
                table_name = investInfo.__tablename__
                print('表头核对结果为.....：', result_dict)
                if result_dict:

                    # print(table_name)
                    # insert_result(self.search_name, table_name, result_dict)
                    trs = table[0].xpath('./tbody/tr')

                    # trs = self.selector.xpath(
                    #     '//div[@id="_container_invest"]/table/tbody/tr')
            # //div[@class="out-investment-container"]/table/tbody/tr
                    if trs:
                        # investInfo = TycQybjDwtz()
                        key = self.search_name
                        # 创建新增对象 TODO: 测试核对第一条数据
                        add_result = CheckResult()
                        add_result.company_name = key
                        add_result.add_time = func.now()
                        # add_result.table_name = 'tyc_qybj_jbxx'  # 当前表名
                        add_result.table_name = table_name  # 当前表名
                        current_class = TycQybjDwtz  # 当前模块对象名
                        first_parse_data = None
                        check_flag = 0  # 检测首页是否有匹配到的一行数据
                        check_first = 0  # 检测首页是否有匹配到的第一行数据
                        for tr in trs:
                            insert_value = ""
                            tds = tr.xpath('./td')
                            try:
                                investInfo.invest_company = try_and_text(
                                    "variable[1].xpath('.//text()')[-1]", tds)
                            except BaseException:
                                investInfo.invest_company = 'ERROR'
                            try:
                                investInfo.invest_person = try_and_text(
                                    "variable[2].xpath('.//a')[0].xpath('./text()')[0]", tds)
                            except BaseException:
                                investInfo.invest_person = 'ERROR'
                            investInfo.invest_ratio = try_and_text(
                                "variable[3].xpath('.//text()')[0]", tds)
                            # investInfo.investAmount = tds[4].xpath('string(.)')
                            investInfo.invest_amount = CURRENT_VERSION_NULL
                            investInfo.invest_fund = try_and_text(
                                "variable[4].xpath('.//text()')[0]", tds)
                            investInfo.invest_date = try_and_text(
                                "variable[5].xpath('.//text()')[0]", tds)
                            investInfo.invest_status = try_and_text(
                                "variable[6].xpath('.//text()')[0]", tds)
                            investInfo.txt_id = self.txt_id
                            investInfo.company_name = key
                            investInfo.mark = 0
                            investInfo.add_time = func.now()
                            investInfo.agency_num = self.agency_num
                            investInfo.agency_name = self.agency_name
                            investInfo.batch = self.batch

                            unique_field = [
                                'company_name', investInfo.company_name]  # 该模块中唯一值字段名和值
                            check_parse(investInfo, add_result, unique_field)
                            # 验证首页解析
                            check_result = check_all_data(
                                add_result, investInfo, current_class)
                            if not first_parse_data:
                                first_parse_data = investInfo  # 保存第一条解析的数据
                            print('check_result+++++++++======:', check_result)
                            check_first += 1
                            if check_result:
                                check_flag = 1  # 匹配到数据
                                break
                            else:
                                check_flag = 0  # 没有匹配到
                        if not check_flag:
                            # 如果首页没有匹配到，则保存首页第一条数据到标准库，并记录其中一个字段
                            print('首页没有匹配到数据》》》》》》》》》')

                            try:

                                add_result.table_field = 'invest_company'  # 保存第一各异常字段名   各模块手动添加
                                add_result.current_value = first_parse_data.invest_company  # 保存第一各异常字段值   各模块手动添加
                                add_result.different_reason = '该页信息都不匹配，请通知数据管理员'
                                add_result.risk_level, add_result.standard_version = 1, 1
                                standard_value = single_oracle_orm.query(current_class).filter_by(  # 各表不同
                                    company_name=first_parse_data.company_name).first()
                                add_result.standard_value = standard_value.invest_company if standard_value else '-'
                                single_oracle_orm.add(add_result)
                                single_oracle_orm.commit()
                            except Exception as e:
                                print('check all datas error===={}'.format(e))
                        elif check_first > 1 and check_flag:
                            # 匹配到但不是第一条，更新页面第一条到标准库
                            unique_line = single_oracle_orm.query(
                                current_class).first()
                            single_oracle_orm.delete(unique_line)
                            single_oracle_orm.add(first_parse_data)
                            single_oracle_orm.commit()
                            print(
                                '首页已匹配到数据，但不是第一条,更新为当前页第一条》》》》》》》！{}'.format(key))

                            # value_list = [
                            #     investInfo.txt_id,
                            #     investInfo.company_name,
                            #     investInfo.investCompany,
                            #     investInfo.investPerson,
                            #     investInfo.investFund,
                            #     investInfo.investAmount,
                            #     investInfo.investRatio,
                            #     investInfo.investDate,
                            #     investInfo.investStatus,
                            #     investInfo.mark,
                            #     investInfo.agency_num,
                            #     investInfo.agency_name,
                            #     investInfo.batch]

                else:
                    insert_result(self.search_name, table_name, result_dict)

    # 解析：企业背景-->变更记录
    def html_parse_alterRecord(self, index):
        logger.debug("Parse detail info 变更记录 {}".format(self.search_name))
        alterRecord = TycQybjBgjl()
        if index == 1 and not isinstance(self.selector, int):
            # 分页是否解析：传入当前公司名称和当前模块对应的数据表名
            check_next_page(self.search_name, 'tyc_qybj_bgjl')
        else:
            table = self.selector.xpath(
                '//div[@id="_container_changeinfo"]/table')
            if table:
                thead_list = ['序号', '变更日期', '变更项目', '变更前', '变更后']
                result_dict = check_thead(table, thead_list)
                print('核对结果为....', result_dict)
                table_name = alterRecord.__tablename__
                print('表头核对结果为.....：', result_dict)
                if result_dict:

                    # print(table_name)
                    # insert_result(self.search_name, table_name, result_dict)
                    trs = table[0].xpath('./tbody/tr')
                    # trs = self.selector.xpath(
                    #     '//div[@id="_container_changeinfo"]//table/tbody/tr')

                    if trs:
                        logger.debug(
                            '环境编码：{}'.format(
                                sys.getdefaultencoding()))
                        key = self.search_name
                        # 创建新增对象 TODO: 测试核对第一条数据
                        add_result = CheckResult()
                        add_result.company_name = key
                        add_result.add_time = func.now()
                        # add_result.table_name = 'tyc_qybj_jbxx'  # 当前表名
                        add_result.table_name = table_name  # 当前表名
                        current_class = TycQybjBgjl  # 当前模块对象名
                        first_parse_data = None
                        check_flag = 0  # 检测首页是否有匹配到的一行数据
                        check_first = 0  # 检测首页是否有匹配到的第一行数据

                        for tr in trs:
                            insert_value = ""
                            # alterRecord = TycQybjBgjl()
                            tds = tr.xpath('./td')
                            tds_len = len(tds)
                            alterDate = try_and_text(
                                "variable[1].xpath('./text()')", tds)
                            alterRecord.alter_date = alterDate[0] if alterDate else 'NA'
                            alterProject = try_and_text(
                                "variable[2].xpath('./text()')", tds)
                            alterRecord.alter_project = alterProject[0] if alterProject else 'NA'
                            alterBefor = try_and_text(
                                "variable[3].xpath('./div')[0].xpath('string(.)')", tds)

                            try:
                                alterBefor = replace_special_chars(alterBefor)
                            except BaseException:
                                alterBefor = replace_special_chars(alterBefor)
                            alterRecord.alter_befor = alterBefor
                            alterAfter = try_and_text(
                                "variable[4].xpath('./div')[0].xpath('string(.)')", tds)
                            # alterAfter = replace_special_chars(alterAfter)

                            alterAfter = replace_special_chars(alterAfter)

                            alterRecord.alter_after = alterAfter
                            # <em><font color="#EF5644">长</font></em>
                            alterRecord.txt_id = self.txt_id
                            alterRecord.company_name = key
                            # alterRecord.company_name = key
                            alterRecord.mark = 0
                            alterRecord.add_time = func.now()
                            alterRecord.agency_num = self.agency_num
                            alterRecord.agency_name = self.agency_name
                            alterRecord.batch = self.batch

                            unique_field = [
                                'company_name', alterRecord.company_name]  # 该模块中唯一值字段名和值
                            check_parse(alterRecord, add_result, unique_field)
                            # 验证首页解析
                            check_result = check_all_data(
                                add_result, alterRecord, current_class)
                            if not first_parse_data:
                                first_parse_data = alterRecord  # 保存第一条解析的数据
                            print('check_result+++++++++======:', check_result)
                            check_first += 1
                            if check_result:
                                check_flag = 1  # 匹配到数据
                                break
                            else:
                                check_flag = 0  # 没有匹配到
                        if not check_flag:
                            # 如果首页没有匹配到，则保存首页第一条数据到标准库，并记录其中一个字段
                            print('首页没有匹配到数据》》》》》》》》》')

                            try:

                                add_result.table_field = 'alter_date'  # 保存第一各异常字段名   各模块手动添加
                                add_result.current_value = first_parse_data.alter_date  # 保存第一各异常字段值   各模块手动添加
                                add_result.different_reason = '该页信息都不匹配，请通知数据管理员'
                                add_result.risk_level, add_result.standard_version = 1, 1
                                standard_value = single_oracle_orm.query(current_class).filter_by(  # 各表不同
                                    company_name=first_parse_data.company_name).first()
                                add_result.standard_value = standard_value.alter_date if standard_value else '-'
                                single_oracle_orm.add(add_result)
                                single_oracle_orm.commit()
                            except Exception as e:
                                print('check all datas error===={}'.format(e))
                        elif check_first > 1 and check_flag:
                            # 匹配到但不是第一条，更新页面第一条到标准库
                            unique_line = single_oracle_orm.query(
                                current_class).first()
                            single_oracle_orm.delete(unique_line)
                            single_oracle_orm.add(first_parse_data)
                            single_oracle_orm.commit()
                            print(
                                '首页已匹配到数据，但不是第一条,更新为当前页第一条》》》》》》》！{}'.format(key))

                else:
                    insert_result(self.search_name, table_name, result_dict)

    # 年报 企业基本信息 第一个table
    def html_parse_year_jbxx(self, year_selector, year):
        logger.debug("Parse detail info 年报基本解析 {}".format(self.search_name))
        # 获得大标签
        if year_selector:
            year_selector = year_selector.replace(u'企业基本信息', 'year_basic_info')
            year_selector = etree.HTML(year_selector)
        trs = year_selector.xpath(
            '// div[text()="year_basic_info"]/parent::*/div/table/tr')
        insert_value = ""
        if trs:
            flss = TycYearJbxx()
            key = self.search_name

            # root_div = root_div[0]
            # 一行是一个tr

            flss.credit_num = try_and_text(
                'variable[0].xpath("./td[2]/text()")[0]', trs)
            flss.ent_name = try_and_text(
                'variable[0].xpath("./td[4]/text()")[0]', trs)
            flss.company_tel = try_and_text(
                'variable[1].xpath("./td[2]/text()")[0]', trs)
            flss.postal_code = try_and_text(
                'variable[1].xpath("./td[4]/text()")[0]', trs)
            flss.manager_state = try_and_text(
                'variable[2].xpath("./td[2]/text()")[0]', trs)
            flss.people_count = try_and_text(
                'variable[2].xpath("./td[4]/text()")[0]', trs)
            flss.email = try_and_text(
                'variable[3].xpath("./td[2]/text()")[0]', trs)
            flss.website = try_and_text(
                'variable[3].xpath("./td[4]/text()")[0]', trs)
            flss.company_address = try_and_text(
                'variable[4].xpath("./td[2]/text()")[0]', trs)
            flss.buy_equity = try_and_text(
                'variable[4].xpath("./td[4]/text()")[0]', trs)
            flss.year = year
            flss.txt_id = self.txt_id
            flss.company_name = key
            flss.add_time = func.now()
            flss.mark = 0
            flss.agency_num = self.agency_num
            flss.agency_name = self.agency_name
            flss.batch = self.batch

            print('正在核实的公司是{}'.format(key))
            # print('该公司的实际信息是： {}'.format(baseinfo.__dict__))
            # single_oracle_orm.add(flss)
            # print('年报基本信息：============',flss.__dict__)
            # y2017 = single_oracle_orm.query(TycYearJbxx).filter_by(year=2017,company_name='佐源集团有限公司').first()
            # single_oracle_orm.delete()
            # single_oracle_orm.commit()
            standard_data = single_oracle_orm.query(
                TycYearJbxx).filter_by(company_name=key).first()

            try:
                change_dict = check_obj(flss, standard_data)
                print('核对结果为：', change_dict)
                checkResult = CheckResult()
                checkResult.company_name = key
                checkResult.add_time = func.now()
                checkResult.standard_version = 1
                checkResult.task_status = 0
                for k, v in change_dict.items():
                    checkResult.current_value = v
                    checkResult.table_field = k
                    checkResult.table_name = 'tyc_year_jbxx'
                    checkResult.standard_value = standard_data.__dict__[k]
                    checkResult.different_reason = '{}表中字段{}的值未核对成功'.format(
                        key, k)
                    import_field = single_oracle.oracle_find_by_param_all(
                        "select column_name from check_import_field where table_name = '{}'".format(
                            flss.__tablename__))

                    for col_name in import_field:
                        if k == col_name[0]:
                            checkResult.risk_level = 1
                        else:
                            checkResult.risk_level = 2
                    single_oracle_orm.add(checkResult)
                    single_oracle_orm.commit()

            except Exception as e:
                print(e)

    # 解析年报网站信息
    def html_parse_year_wzhwdxx(self, year_selector, year):
        logger.debug("Parse detail info 企业年报网站信息 {}".format(self.search_name))
        website = TycYearWzhwdxx()
        year_selector = year_selector.replace(u'网站或网店信息', 'year_wangzhan')
        if year_selector:
            year_selector = etree.HTML(year_selector)
            # trs = year_selector.xpath('//div[contains(text(),"year_wangzhan")//table/tbody/tr')

            # 表头信息
            root_div = year_selector.xpath(
                '//div[text()="year_wangzhan"]/parent::*//table')
            if root_div:
                thead_list = ['类型', '名称', '网址']
                result_dict = check_thead(root_div, thead_list)
                print(result_dict)
                table_name = website.__tablename__
                print('表头核对结果为.....：', result_dict)
                if result_dict:

                    # table_name = website.__tablename__
                    # print(table_name)
                    # insert_result(self.search_name, table_name, result_dict)

                    # trs = year_selector.xpath(
                    #     '//div[text()="year_wangzhan"]/parent::*//table/tbody/tr')
                    trs = root_div[0].xpath('./tbody/tr')
                # root_div = soup_year.find("div", attrs={"class": "report_website"})
                    if trs:
                        # 一行是一个tr
                        website = TycYearWzhwdxx()
                        key = self.search_name
                        # 创建新增对象 TODO: 测试核对第一条数据
                        add_result = CheckResult()
                        add_result.company_name = key
                        add_result.add_time = func.now()
                        # add_result.table_name = 'tyc_qybj_jbxx'  # 当前表名
                        add_result.table_name = table_name  # 当前表名
                        current_class = TycYearWzhwdxx  # 当前模块对象名
                        first_parse_data = None
                        check_flag = 0  # 检测首页是否有匹配到的一行数据
                        check_first = 0  # 检测首页是否有匹配到的第一行数据

                        # root_div = root_div[0]
                        # trs = root_div.find("table").find("tbody").find_all("tr")

                        for tr in trs:
                            insert_value = ""
                            tds = tr.xpath("./td")
                            website.website_type = try_and_text(
                                'variable[0].xpath(".//text()")[0]', tds)
                            website.web_name = try_and_text(
                                'variable[1].xpath(".//text()")[0]', tds)
                            web_url = try_and_text(
                                'variable[2].xpath(".//text()")', tds)
                            logger.debug(
                                'web_url={} {}'.format(
                                    web_url, type(web_url)))
                            if web_url:
                                web_url = web_url[0] or 'NA'
                            website.web_url = web_url or 'NA'
                            website.year = year
                            website.txt_id = self.txt_id
                            website.company_name = key
                            website.add_time = func.now()
                            website.mark = 0
                            website.agency_num = self.agency_num
                            website.agency_name = self.agency_name
                            website.batch = self.batch

                            unique_field = [
                                'company_name', website.company_name]  # 该模块中唯一值字段名和值
                            check_parse(website, add_result, unique_field)

                            # 验证首页解析
                            check_result = check_all_data(
                                add_result, website, current_class)
                            if not first_parse_data:
                                first_parse_data = website  # 保存第一条解析的数据
                            print('check_result+++++++++======:', check_result)
                            check_first += 1
                            if check_result:
                                check_flag = 1  # 匹配到数据
                                break
                            else:
                                check_flag = 0  # 没有匹配到
                        if not check_flag:
                            # 如果首页没有匹配到，则保存首页第一条数据到标准库，并记录其中一个字段
                            print('首页没有匹配到数据》》》》》》》》》')

                            try:

                                add_result.table_field = 'website_type'  # 保存第一各异常字段名   各模块手动添加
                                add_result.current_value = first_parse_data.website_type  # 保存第一各异常字段值   各模块手动添加
                                add_result.different_reason = '该页信息都不匹配，请通知数据管理员'
                                add_result.risk_level, add_result.standard_version = 1, 1
                                standard_value = single_oracle_orm.query(current_class).filter_by(  # 各表不同
                                    company_name=first_parse_data.company_name).first()
                                add_result.standard_value = standard_value.website_type if standard_value else '-'
                                add_result.table_name = table_name
                                single_oracle_orm.add(add_result)
                                single_oracle_orm.commit()
                            except Exception as e:
                                print('check all datas error===={}'.format(e))
                        elif check_first > 1 and check_flag:
                            # 匹配到但不是第一条，更新页面第一条到标准库
                            unique_line = single_oracle_orm.query(
                                current_class).first()
                            single_oracle_orm.delete(unique_line)
                            single_oracle_orm.add(first_parse_data)
                            single_oracle_orm.commit()
                            print(
                                '首页已匹配到数据，但不是第一条,更新为当前页第一条》》》》》》》！{}'.format(key))
                else:
                    insert_result(self.search_name, table_name, result_dict)

    # 年报 股东及出资信息
    def html_parse_year_gdczxx(self, year_selector, year):
        logger.debug("Parse detail info 股份出资信息 {}".format(self.search_name))
        gdcz = TycYearGdczxx()
        # 获得分支机构大标签
        year_selector = year_selector.replace(u'股东及出资信息', 'year_gudongchuzi')
        if year_selector:
            year_selector = etree.HTML(year_selector)

        print('正在进行的表格为：{}'.format(gdcz.__tablename__))
        # 表头信息
        root_div = year_selector.xpath(
            '//div[text()="year_gudongchuzi"]/parent::*//table')
        if root_div:
            thead_list = [
                '股东',
                '认缴出资额(万元)',
                '认缴出资时间',
                '认缴出资方式',
                '实缴出资额(万元)',
                '实缴出资时间',
                '实缴出资方式']
            result_dict = check_thead(root_div, thead_list)
            print(result_dict)
            table_name = gdcz.__tablename__
            print('表头核对结果为.....：', result_dict)
            if result_dict:
                # print(table_name)

                # trs = year_selector.xpath(
                #     '//div[text()="year_gudongchuzi"]/parent::*//table/tbody/tr')
                trs = root_div[0].xpath('./tbody/tr')
                if trs:
                    # gdcz = TycYearGdczxx()
                    key = self.search_name
                    # 一行是一个tr
                    # 创建新增对象 TODO: 测试核对第一条数据
                    add_result = CheckResult()
                    add_result.company_name = key
                    add_result.add_time = func.now()
                    # add_result.table_name = 'tyc_qybj_jbxx'  # 当前表名
                    add_result.table_name = table_name  # 当前表名
                    current_class = TycYearGdczxx  # 当前模块对象名
                    first_parse_data = None
                    check_flag = 0  # 检测首页是否有匹配到的一行数据
                    check_first = 0  # 检测首页是否有匹配到的第一行数据
                    for tr in trs:
                        insert_value = ""
                        tds = tr.xpath("./td")

                        gdcz.shareholder = try_and_text(
                            "variable[0].xpath('.//text()')[0]", tds)
                        gdcz.subscirbe_contribution = try_and_text(
                            "variable[1].xpath('./text()')[0]", tds)

                        gdcz.contribution_time = try_and_text(
                            "variable[2].xpath('./text()')[0]", tds)
                        gdcz.contribution_style = try_and_text(
                            "variable[3].xpath('./text()')[0]", tds)
                        actual_contribution = try_and_text(
                            "variable[4].xpath('./text()')", tds)
                        gdcz.actual_contribution = 'NA'
                        if actual_contribution:
                            gdcz.actual_contribution = actual_contribution[0]
                        gdcz.actual_time = try_and_text(
                            "variable[5].xpath('./text()')[0]", tds)
                        gdcz.actual_style = try_and_text(
                            "variable[6].xpath('./text()')[0]", tds)
                        gdcz.year = year
                        gdcz.txt_id = self.txt_id
                        gdcz.company_name = key
                        gdcz.add_time = func.now()
                        gdcz.mark = 0
                        gdcz.agency_num = self.agency_num
                        gdcz.agency_name = self.agency_name
                        gdcz.batch = self.batch

                        unique_field = [
                            'company_name', gdcz.company_name]  # 该模块中唯一值字段名和值
                        check_parse(gdcz, add_result, unique_field)

                        # 验证首页解析
                        check_result = check_all_data(
                            add_result, gdcz, current_class)
                        if not first_parse_data:
                            first_parse_data = gdcz  # 保存第一条解析的数据
                        print('check_result+++++++++======:', check_result)
                        check_first += 1
                        if check_result:
                            check_flag = 1  # 匹配到数据
                            break
                        else:
                            check_flag = 0  # 没有匹配到
                    if not check_flag:
                        # 如果首页没有匹配到，则保存首页第一条数据到标准库，并记录其中一个字段
                        print('首页没有匹配到数据》》》》》》》》》')

                        try:

                            add_result.table_field = 'shareholder'  # 保存第一各异常字段名   各模块手动添加
                            add_result.current_value = first_parse_data.shareholder  # 保存第一各异常字段值   各模块手动添加
                            add_result.different_reason = '该页信息都不匹配，请通知数据管理员'
                            add_result.risk_level, add_result.standard_version = 1, 1
                            standard_value = single_oracle_orm.query(current_class).filter_by(  # 各表不同
                                company_name=first_parse_data.company_name).first()
                            add_result.standard_value = standard_value.shareholder if standard_value else '-'
                            single_oracle_orm.add(add_result)
                            single_oracle_orm.commit()
                        except Exception as e:
                            print('check all datas error===={}'.format(e))
                    elif check_first > 1 and check_flag:
                        # 匹配到但不是第一条，更新页面第一条到标准库
                        unique_line = single_oracle_orm.query(
                            current_class).first()
                        single_oracle_orm.delete(unique_line)
                        single_oracle_orm.add(first_parse_data)
                        single_oracle_orm.commit()
                        print(
                            '首页已匹配到数据，但不是第一条,更新为当前页第一条》》》》》》》！{}'.format(key))

            else:
                insert_result(self.search_name, table_name, result_dict)

    # 年报 企业资产状况信息
    def html_parse_year_zczk(self, year_selector, year):
        logger.debug("Parse detail info 资产状况 {}".format(self.search_name))
        # 获得大标签
        year_selector = year_selector.replace(
            u'企业资产状况信息', 'year_ent_money_info')
        if year_selector:
            year_selector = etree.HTML(year_selector)
        info = u'企业资产状况信息'
        trs = year_selector.xpath(
            '//div[text()="year_ent_money_info"]/parent::*//table//tr')
        insert_value = ""
        if trs:
            flss = TycYearZczk()
            key = self.search_name
            # root_div = root_div[2]
            # 一行是一个tr

            flss.total_assets = try_and_text(
                "variable[0].xpath('./td[position()=2]/text()')[0]", trs)
            flss.total_income = try_and_text(
                "variable[0].xpath('td[position()=4]/text()')[0]", trs)
            flss.total_sales = try_and_text(
                "variable[1].xpath('td[position()=2]/text()')[0]", trs)
            flss.total_profit = try_and_text(
                "variable[1].xpath('td[position()=4]/text()')[0]", trs)
            flss.operation_income = try_and_text(
                "variable[2].xpath('td[position()=2]/text()')[0]", trs)
            flss.net_profit = try_and_text(
                "variable[2].xpath('td[position()=4]/text()')[0]", trs)
            flss.total_tax = try_and_text(
                "variable[3].xpath('td[position()=2]/text()')[0]", trs)
            flss.total_debt = try_and_text(
                "variable[3].xpath('td[position()=4]/text()')[0]", trs)

            flss.year = year
            flss.txt_id = self.txt_id
            flss.company_name = key
            flss.add_time = func.now()
            flss.mark = 0
            flss.agency_num = self.agency_num
            flss.agency_name = self.agency_name
            flss.batch = self.batch

            print('正在核实的公司是{}'.format(key))
            # print('该公司的实际信息是： {}'.format(baseinfo.__dict__))
            # single_oracle_orm.add(flss)
            # print('企业资产状况信息：============', flss.__dict__)
            # y2017 = single_oracle_orm.query(TycYearJbxx).filter_by(year=2017, company_name='佐源集团有限公司').first()
            # single_oracle_orm.delete()
            # single_oracle_orm.commit()
            standard_data = single_oracle_orm.query(
                TycQybjJbxx).filter_by(company_name=key).first()

            try:
                change_dict = check_obj(flss, standard_data)
                print('核对结果为：', change_dict)

                checkResult = CheckResult()
                checkResult.company_name = key
                checkResult.add_time = func.now()
                checkResult.standard_version = 1
                checkResult.task_status = 0
                for k, v in change_dict.items():
                    checkResult.current_value = v
                    checkResult.table_name = flss.__tablename__
                    checkResult.table_field = k
                    checkResult.standard_value = standard_data.__dict__[k]
                    checkResult.different_reason = '{}表中字段{}的值未核对成功'.format(
                        key, k)
                    import_field = single_oracle.oracle_find_by_param_all(
                        "select column_name from check_import_field where table_name = {}".format(
                            checkResult.table_name))
                    for col_name in import_field:
                        if k == col_name[0]:
                            checkResult.risk_level = 1
                        else:
                            checkResult.risk_level = 2
                    single_oracle_orm.add(checkResult)
                    single_oracle_orm.commit()
            except Exception as e:
                print(e)

    # 年报 对外投资
    def html_parse_year_dwtz(self, year_selector, year):
        logger.debug("Parse detail info 对外投资 {}".format(self.search_name))

        dwtz = TycYearDwtz()

        year_selector = year_selector.replace(
            u'对外投资信息', 'year_outbound_company')
        if year_selector:
            year_selector = etree.HTML(year_selector)
            # trs = year_selector.xpath('//div[contains(text(),"year_outbound_company")')

        # 表头信息
        root_div = year_selector.xpath(
            '//div[text()="year_outbound_company"]/parent::*//table')
        if root_div:
            thead_list = ['注册号/统一社会信用代码', '对外投资企业名称']
            result_dict = check_thead(root_div, thead_list)
            print(result_dict)
            table_name = dwtz.__tablename__
            print('表头核对结果为.....：', result_dict)
            if result_dict:

                # print(table_name)
                # trs = year_selector.xpath(
                #     '//div[text()="year_outbound_company"]/parent::*//table/tbody/tr')
                trs = root_div[0].xpath('./tbody/tr')

                if trs:
                    # dwtz = TycYearDwtz()
                    key = self.search_name
                    # 一行是一个tr
                    # 创建新增对象 TODO: 测试核对第一条数据
                    add_result = CheckResult()
                    add_result.company_name = key
                    add_result.add_time = func.now()
                    # add_result.table_name = 'tyc_qybj_jbxx'  # 当前表名
                    add_result.table_name = table_name  # 当前表名
                    current_class = TycYearDwtz  # 当前模块对象名
                    first_parse_data = None
                    check_flag = 0  # 检测首页是否有匹配到的一行数据
                    check_first = 0  # 检测首页是否有匹配到的第一行数据

                    for tr in trs:
                        insert_value = ""
                        tds = tr.xpath("./td")
                        dwtz.credit_num = try_and_text(
                            "variable[0].xpath('string(.)')", tds)
                        dwtz.outbound_company = try_and_text(
                            "variable[1].xpath('string(.)')", tds)

                        dwtz.year = year
                        dwtz.txt_id = self.txt_id
                        dwtz.company_name = key
                        dwtz.add_time = func.now()
                        dwtz.mark = 0
                        dwtz.agency_num = self.agency_num
                        dwtz.agency_name = self.agency_name
                        dwtz.batch = self.batch

                        unique_field = [
                            'company_name', dwtz.company_name]  # 该模块中唯一值字段名和值
                        check_parse(dwtz, add_result, unique_field)

                        # 验证首页解析
                        check_result = check_all_data(
                            add_result, dwtz, current_class)
                        if not first_parse_data:
                            first_parse_data = dwtz  # 保存第一条解析的数据
                        print('check_result+++++++++======:', check_result)
                        check_first += 1
                        if check_result:
                            check_flag = 1  # 匹配到数据
                            break
                        else:
                            check_flag = 0  # 没有匹配到
                    if not check_flag:
                        # 如果首页没有匹配到，则保存首页第一条数据到标准库，并记录其中一个字段
                        print('首页没有匹配到数据》》》》》》》》》')

                        try:

                            add_result.table_field = 'credit_num'  # 保存第一各异常字段名   各模块手动添加
                            add_result.current_value = first_parse_data.credit_num  # 保存第一各异常字段值   各模块手动添加
                            add_result.different_reason = '该页信息都不匹配，请通知数据管理员'
                            add_result.risk_level, add_result.standard_version = 1, 1
                            standard_value = single_oracle_orm.query(current_class).filter_by(  # 各表不同
                                company_name=first_parse_data.company_name).first()
                            add_result.standard_value = standard_value.credit_num if standard_value else '-'
                            single_oracle_orm.add(add_result)
                            single_oracle_orm.commit()
                        except Exception as e:
                            print('check all datas error===={}'.format(e))
                    elif check_first > 1 and check_flag:
                        # 匹配到但不是第一条，更新页面第一条到标准库
                        unique_line = single_oracle_orm.query(
                            current_class).first()
                        single_oracle_orm.delete(unique_line)
                        single_oracle_orm.add(first_parse_data)
                        single_oracle_orm.commit()
                        print(
                            '首页已匹配到数据，但不是第一条,更新为当前页第一条》》》》》》》！{}'.format(key))

            else:
                insert_result(self.search_name, table_name, result_dict)

    # 分支机构
    def html_parse_branch(self, index):
        key = self.search_name
        logger.debug("Parse detail info 分支机构 {}".format(self.search_name))
        flss = TycQybjFzjg()

        if index == 1 and not isinstance(self.selector, int):
            # 分页是否解析：传入当前公司名称和当前模块对应的数据表名
            check_next_page(self.search_name, 'tyc_qybj_fzjg')
        else:
            # 获得分支机构大标签
            root_div = self.selector.xpath(
                '//div[@id="_container_branch"]/table')

            if root_div:

                # 表头信息
                thead_list = ['序号', '企业名称', '负责人', '成立日期', '经营状态']
                result_dict = check_thead(root_div, thead_list)
                table_name = flss.__tablename__
                print('表头核对结果为.....：', result_dict)
                if result_dict:

                    # print(table_name)

                    # 一行是一个tr
                    root_div = root_div[0]
                    trs = root_div.xpath("./tbody/tr")

                    # 创建新增对象 TODO: 测试核对第一条数据
                    add_result = CheckResult()
                    add_result.company_name = key
                    add_result.add_time = func.now()
                    # add_result.table_name = 'tyc_qybj_jbxx'  # 当前表名
                    add_result.table_name = table_name  # 当前表名
                    current_class = TycQybjFzjg  # 当前模块对象名
                    first_parse_data = None
                    check_flag = 0  # 检测首页是否有匹配到的一行数据
                    check_first = 0  # 检测首页是否有匹配到的第一行数据

                    for tr in trs:

                        insert_value = ""
                        tds = tr.xpath("./td")
                        ent_name = try_and_text(
                            "variable[1].xpath('.//td/a/text()')", tds)
                        flss.company_name = ent_name[0] if ent_name else self.search_name

                        flss.registere_date = try_and_text(
                            "variable[3].xpath('.//text()')[0]", tds)
                        flss.status = 'NA'

                        flss.status = try_and_text(
                            "variable[4].xpath('.//text()')[0]", tds)

                        legal_representative = try_and_text(
                            "variable[2].xpath('./div/div[2]/a/text()')", tds)
                        logger.debug(
                            '负责人={} type={}'.format(
                                legal_representative,
                                type(legal_representative)))
                        if legal_representative:
                            flss.legal_representative = legal_representative[0]
                        else:
                            flss.legal_representative = 'NA'
                        flss.txt_id = self.txt_id
                        flss.company_name = key
                        flss.add_time = func.now()
                        flss.mark = 0
                        flss.agency_num = self.agency_num
                        flss.agency_name = self.agency_name
                        flss.batch = self.batch

                        unique_field = [
                            'company_name', flss.company_name]  # 该模块中唯一值字段名和值
                        check_parse(flss, add_result, unique_field)

                        # 验证首页解析
                        check_result = check_all_data(
                            add_result, flss, current_class)
                        if not first_parse_data:
                            first_parse_data = flss  # 保存第一条解析的数据
                        print('check_result+++++++++======:', check_result)
                        check_first += 1
                        if check_result:
                            check_flag = 1  # 匹配到数据
                            break
                        else:
                            check_flag = 0  # 没有匹配到
                    if not check_flag:
                        # 如果首页没有匹配到，则保存首页第一条数据到标准库，并记录其中一个字段
                        print('首页没有匹配到数据》》》》》》》》》')

                        try:

                            add_result.table_field = 'company_name'  # 保存第一各异常字段名   各模块手动添加
                            add_result.current_value = first_parse_data.company_name  # 保存第一各异常字段值   各模块手动添加
                            add_result.different_reason = '该页信息都不匹配，请通知数据管理员'
                            add_result.risk_level, add_result.standard_version = 1, 1
                            standard_value = single_oracle_orm.query(current_class).filter_by(  # 各表不同
                                company_name=first_parse_data.company_name).first()
                            add_result.standard_value = standard_value.company_name if standard_value else '-'
                            single_oracle_orm.add(add_result)
                            single_oracle_orm.commit()
                        except Exception as e:
                            print('check all datas error===={}'.format(e))
                    elif check_first > 1 and check_flag:
                        # 匹配到但不是第一条，更新页面第一条到标准库
                        unique_line = single_oracle_orm.query(
                            current_class).first()
                        single_oracle_orm.delete(unique_line)
                        single_oracle_orm.add(first_parse_data)
                        single_oracle_orm.commit()
                        print(
                            '首页已匹配到数据，但不是第一条,更新为当前页第一条》》》》》》》！{}'.format(key))

                else:
                    insert_result(self.search_name, table_name, result_dict)

    # 司法风险
    # 解析：司法风险-->开庭公告
    def html_parse_ktgg(self, index):
        logger.debug("Parse detail info 开庭公告 {}".format(self.search_name))
        ktggInfo = TycSffxKtgg()

        if index == 1 and not isinstance(self.selector, int):
            # 分页是否解析：传入当前公司名称和当前模块对应的数据表名
            check_next_page(self.search_name, 'tyc_sffx_ktgg')
        else:
            # 表头信息
            table = self.selector.xpath(
                '//div[@id="_container_announcementcourt"]/table')
            if table:
                thead_list = [
                    '序号',
                    '开庭日期',
                    '案号',
                    '案由',
                    '公诉人/原告/上诉人/申请人',
                    '被告人/被告/被上诉人/被申请人',
                    '操作']
                result_dict = check_thead(table, thead_list)
                table_name = ktggInfo.__tablename__
                print('表头核对结果为.....：', result_dict)
                if result_dict:

                    # print(table_name)

                    trs = self.selector.xpath(
                        '//div[@id="_container_announcementcourt"]/table/tbody/tr')

                    if trs:
                        # ktggInfo = TycSffxKtgg()

                        key = self.search_name

                        # 创建新增对象 TODO: 测试核对第一条数据
                        add_result = CheckResult()
                        add_result.company_name = key
                        add_result.add_time = func.now()
                        # add_result.table_name = 'tyc_qybj_jbxx'  # 当前表名
                        add_result.table_name = table_name  # 当前表名
                        current_class = TycSffxKtgg  # 当前模块对象名
                        first_parse_data = None
                        check_flag = 0  # 检测首页是否有匹配到的一行数据
                        check_first = 0  # 检测首页是否有匹配到的第一行数据

                        for tr in trs:
                            insert_value = ""
                            tds = tr.xpath('./td')

                            # 开庭日期
                            ktggInfo.trial_date = try_and_text(
                                "variable[1].xpath('./text()')[0]", tds)
                            # 案号
                            ktggInfo.reference_num = try_and_text(
                                "variable[2].xpath('.//text()')[0]", tds)
                            # 案由
                            ktggInfo.cause_action = try_and_text(
                                "variable[3].xpath('.//text()')[0]", tds)
                            # 原告/上诉人
                            plaintiff = try_and_text(
                                "variable[4].xpath('string(.)')", tds)
                            ktggInfo.plaintiff = plaintiff if plaintiff else 'NA'
                            # 被告/被上诉人
                            ktggInfo.defendant = 'NA'
                            try:
                                ktggInfo.defendant = '、'.join(
                                    tds[5].xpath('./div//text()'))
                            except Exception as e:
                                logger.debug(e)
                            # 详情 \u003C\u002Fa\u003E

                            detail = try_and_text(
                                "variable[6].xpath('./script/text()')[0]", tds)
                            ktggInfo.detail = replace_special_chars(detail)

                            ktggInfo.txt_id = self.txt_id
                            ktggInfo.company_name = key
                            ktggInfo.mark = 0
                            ktggInfo.add_time = datetime.now()
                            ktggInfo.agency_num = self.agency_num
                            ktggInfo.agency_name = self.agency_name
                            ktggInfo.batch = self.batch

                            unique_field = [
                                'company_name', ktggInfo.company_name]  # 该模块中唯一值字段名和值
                            check_parse(ktggInfo, add_result, unique_field)

                            # 验证首页解析
                            check_result = check_all_data(
                                add_result, ktggInfo, current_class)
                            if not first_parse_data:
                                first_parse_data = ktggInfo  # 保存第一条解析的数据
                            print('check_result+++++++++======:', check_result)
                            check_first += 1
                            if check_result:
                                check_flag = 1  # 匹配到数据
                                break
                            else:
                                check_flag = 0  # 没有匹配到
                        if not check_flag:
                            # 如果首页没有匹配到，则保存首页第一条数据到标准库，并记录其中一个字段
                            print('首页没有匹配到数据》》》》》》》》》')

                            try:

                                add_result.table_field = 'trial_date'  # 保存第一各异常字段名   各模块手动添加
                                add_result.current_value = first_parse_data.trial_date  # 保存第一各异常字段值   各模块手动添加
                                add_result.different_reason = '该页信息都不匹配，请通知数据管理员'
                                add_result.risk_level, add_result.standard_version = 1, 1
                                standard_value = single_oracle_orm.query(current_class).filter_by(  # 各表不同
                                    company_name=first_parse_data.company_name).first()
                                add_result.standard_value = standard_value.trial_date if standard_value else '-'
                                single_oracle_orm.add(add_result)
                                single_oracle_orm.commit()
                            except Exception as e:
                                print('check all datas error===={}'.format(e))
                        elif check_first > 1 and check_flag:
                            # 匹配到但不是第一条，更新页面第一条到标准库
                            unique_line = single_oracle_orm.query(
                                current_class).first()
                            single_oracle_orm.delete(unique_line)
                            single_oracle_orm.add(first_parse_data)
                            single_oracle_orm.commit()
                            print(
                                '首页已匹配到数据，但不是第一条,更新为当前页第一条》》》》》》》！{}'.format(key))

                else:
                    insert_result(self.search_name, table_name, result_dict)

    # 法律诉讼
    def html_parse_lawsuit(self, index):
        logger.debug("Parse detail info 法律诉讼 {}".format(self.search_name))
        flss = TycSffxFls()
        if index == 1:
            # 分页是否解析：传入当前公司名称和当前模块对应的数据表名
            check_next_page(self.search_name, 'tyc_sffx_flss')
        else:
            table = self.selector.xpath(
                '//div[@id="_container_lawsuit"]/table')
            if table:
                thead_list = ['序号', '日期', '案件名称', '案由', '案件身份', '案号']
                result_dict = check_thead(table, thead_list)
                table_name = flss.__tablename__
                print('表头核对结果为.....：', result_dict)
                if result_dict:

                    # print(table_name)

                    root_div = self.selector.xpath(
                        '//div[@id="_container_lawsuit"]/table/tbody/tr')
                    if root_div:
                        # flss = TycSffxFlss()
                        key = self.search_name

                        # 一行是一个tr

                        # 创建新增对象 TODO: 测试核对第一条数据
                        add_result = CheckResult()
                        add_result.company_name = key
                        add_result.add_time = func.now()
                        # add_result.table_name = 'tyc_qybj_jbxx'  # 当前表名
                        add_result.table_name = table_name  # 当前表名
                        current_class = TycSffxFls  # 当前模块对象名
                        first_parse_data = None
                        check_flag = 0  # 检测首页是否有匹配到的一行数据
                        check_first = 0  # 检测首页是否有匹配到的第一行数据

                        law_count = 0
                        for tr in root_div:
                            insert_value = ""
                            tds = tr.xpath("./td")
                            if tds:
                                flss.judgment_date = try_and_text(
                                    "variable[1].xpath('./span/text()')[0]", tds)
                                # flss.judgment_document = try_and_text("variable[2].xpath('./a/text()')[0]", tds)

                                tds_href = try_and_text(
                                    "variable[2].xpath('./a/@href')[0]", tds)
                                flss.judgment_name = try_and_text(
                                    "variable[2].xpath('./a//text()')[0]", tds)
                                name = try_and_text(
                                    "variable[2].xpath('./a/text()')[0]", tds)
                                flss.document_url = tds_href if tds_href else 'NA'
                                case_type = try_and_text(
                                    "variable[3].xpath('./span/text()')", tds)
                                flss.case_type = case_type[0] if case_type else 'NA'
                                # case_identity = try_and_text("variable[4].xpath('.//text()')", tds)
                                # flss.case_identity = ','.join(
                                #     case_identity) if case_identity else 'NA'
                                s1 = s2 = ''
                                plaintiff = try_and_text(
                                    "variable[4].xpath('./div[position()=1]//text()')", tds)
                                defendant = try_and_text(
                                    "variable[4].xpath('./div[position()=2]//text()')", tds)
                                if len(plaintiff) != 0:
                                    for i in plaintiff:
                                        s1 += i
                                if len(defendant) != 0:
                                    for j in defendant:
                                        s2 += j
                                flss.case_identity = s1 + ';' + s2

                                case_number = try_and_text(
                                    "variable[5].xpath('./span/text()')", tds)
                                flss.case_number = case_number[0] if case_number else 'NA'
                                flss.txt_id = self.txt_id

                                flss.company_name = key
                                flss.add_time = func.now()
                                flss.mark = 0
                                flss.agency_num = self.agency_num
                                flss.agency_name = self.agency_name
                                # 区别key
                                flss.batch = self.batch
                                text_info = 'NA'
                                try:
                                    text_info = self.detail_info['_container_lawsuit'][tds_href.split(
                                        r'/')[-1]]
                                except BaseException:
                                    pass

                                flss.judgment_document = replace_special_chars(
                                    text_info)

                                unique_field = [
                                    'company_name', flss.company_name]  # 该模块中唯一值字段名和值
                                check_parse(flss, add_result, unique_field)

                                # 验证首页解析
                                check_result = check_all_data(
                                    add_result, flss, current_class)
                                if not first_parse_data:
                                    first_parse_data = flss  # 保存第一条解析的数据
                                print(
                                    'check_result+++++++++======法律诉讼:', check_result)
                                check_first += 1
                                if check_result:
                                    check_flag = 1  # 匹配到数据
                                    break
                                else:
                                    check_flag = 0  # 没有匹配到
                        print(
                            '法律诉讼：check_flag：{}-----check_first:{}'.format(check_flag, check_first))
                        if not check_flag:
                            # 如果首页没有匹配到，则保存首页第一条数据到标准库，并记录其中一个字段
                            print('首页没有匹配到数据》》》》》》》》》')

                            try:

                                add_result.table_field = 'judgment_date'  # 保存第一各异常字段名   各模块手动添加
                                add_result.current_value = first_parse_data.judgment_date  # 保存第一各异常字段值   各模块手动添加
                                add_result.different_reason = '该页信息都不匹配，请通知数据管理员'
                                add_result.risk_level, add_result.standard_version = 1, 1
                                standard_value = single_oracle_orm.query(current_class).filter_by(  # 各表不同
                                    company_name=first_parse_data.company_name).first()
                                add_result.standard_value = standard_value.judgment_date if standard_value else '-'
                                single_oracle_orm.add(add_result)
                                single_oracle_orm.commit()
                            except Exception as e:
                                print('check all datas error===={}'.format(e))
                        elif check_first > 1 and check_flag:
                            # 匹配到但不是第一条，更新页面第一条到标准库
                            unique_line = single_oracle_orm.query(
                                current_class).first()
                            single_oracle_orm.delete(unique_line)
                            single_oracle_orm.add(first_parse_data)
                            single_oracle_orm.commit()
                            print(
                                '首页已匹配到数据，但不是第一条,更新为当前页第一条》》》》》》》！{}'.format(key))

                else:
                    insert_result(self.search_name, table_name, result_dict)

    # 法院公告
    def html_parse_announcement(self, index):
        logger.debug("Parse detail info 法院公告 {}".format(self.search_name))
        flss = TycSffxFygg()
        if index == 1 and not isinstance(self.selector, int):
            # 分页是否解析：传入当前公司名称和当前模块对应的数据表名
            check_next_page(self.search_name, 'tyc_sffx_fygg')
        else:
            # 获得法院公告大标签
            root_div = self.selector.xpath(
                '//div[@id="_container_court"]/table')
            thead_list = ['序号', '刊登日期', '上诉方', '被诉方', '公告类型', '法院', '操作']
            result_dict = check_thead(root_div, thead_list)
            print(result_dict)
            table_name = flss.__tablename__
            print('表头核对结果为.....：', result_dict)
            if result_dict:

                # print(table_name)

                if root_div:
                    # flss = TycSffxFygg()
                    key = self.search_name
                    # 一行是一个tr
                    # 创建新增对象 TODO: 测试核对第一条数据
                    add_result = CheckResult()
                    add_result.company_name = key
                    add_result.add_time = func.now()
                    # add_result.table_name = 'tyc_qybj_jbxx'  # 当前表名
                    add_result.table_name = table_name  # 当前表名
                    current_class = TycSffxFygg  # 当前模块对象名
                    first_parse_data = None
                    check_flag = 0  # 检测首页是否有匹配到的一行数据
                    check_first = 0  # 检测首页是否有匹配到的第一行数据

                    root_div = root_div[0]
                    trs = root_div.xpath("./tbody/tr")

                    for tr in trs:
                        insert_value = ""
                        tds = tr.xpath("./td")
                        flss.announcement_date = try_and_text(
                            "variable[1].xpath('./text()')[0]", tds)
                        plaintiff = try_and_text(
                            "variable[2].xpath('string(.)')", tds)
                        if plaintiff:
                            flss.plaintiff = plaintiff
                        defendant = try_and_text(
                            "variable[3].xpath('string(.)')", tds)
                        flss.defendant = defendant if defendant else 'NA'

                        flss.announcement_type = try_and_text(
                            "variable[4].xpath('string(.)')", tds)
                        flss.court = try_and_text(
                            "variable[5].xpath('string(.)')", tds)
                        text_info = try_and_text(
                            "variable[6].xpath('./script/text()')[0]", tds)
                        text_info = replace_special_chars(text_info)
                        flss.detail_info = text_info
                        flss.txt_id = self.txt_id
                        flss.company_name = key
                        flss.add_time = func.now()
                        flss.mark = 0
                        flss.agency_num = self.agency_num
                        flss.agency_name = self.agency_name
                        flss.batch = self.batch

                        unique_field = [
                            'company_name', flss.company_name]  # 该模块中唯一值字段名和值
                        check_parse(flss, add_result, unique_field)

                        # 验证首页解析
                        check_result = check_all_data(
                            add_result, flss, current_class)
                        if not first_parse_data:
                            first_parse_data = flss  # 保存第一条解析的数据
                        print('check_result+++++++++======:', check_result)
                        check_first += 1
                        if check_result:
                            check_flag = 1  # 匹配到数据
                            break
                        else:
                            check_flag = 0  # 没有匹配到
                    if not check_flag:
                        # 如果首页没有匹配到，则保存首页第一条数据到标准库，并记录其中一个字段
                        print('首页没有匹配到数据》》》》》》》》》')

                        try:

                            add_result.table_field = 'announcement_date'  # 保存第一各异常字段名   各模块手动添加
                            add_result.current_value = first_parse_data.announcement_date  # 保存第一各异常字段值   各模块手动添加
                            add_result.different_reason = '该页信息都不匹配，请通知数据管理员'
                            add_result.risk_level, add_result.standard_version = 1, 1
                            standard_value = single_oracle_orm.query(current_class).filter_by(  # 各表不同
                                company_name=first_parse_data.company_name).first()
                            add_result.standard_value = standard_value.announcement_date if standard_value else '-'
                            single_oracle_orm.add(add_result)
                            single_oracle_orm.commit()
                        except Exception as e:
                            print('check all datas error===={}'.format(e))
                    elif check_first > 1 and check_flag:
                        # 匹配到但不是第一条，更新页面第一条到标准库
                        unique_line = single_oracle_orm.query(
                            current_class).first()
                        single_oracle_orm.delete(unique_line)
                        single_oracle_orm.add(first_parse_data)
                        single_oracle_orm.commit()
                        print(
                            '首页已匹配到数据，但不是第一条,更新为当前页第一条》》》》》》》！{}'.format(key))

            else:
                insert_result(self.search_name, table_name, result_dict)

    # 失信人
    def html_parse_shixinren(self, index):
        logger.debug("Parse detail info 失信人{}".format(self.search_name))
        if index == 1 and not isinstance(self.selector, int):
            # 分页是否解析：传入当前公司名称和当前模块对应的数据表名
            check_next_page(self.search_name, 'tyc_sffx_sxr')
        else:
            # 获得失信人大标签
            root_div = self.selector.xpath(
                '//div[@id="_container_dishonest"][position()=1]/table')

            if root_div:
                flss = TycSffxSxr()
                key = self.search_name
                # 表头信息
                thead_list = [
                    '序号',
                    '立案日期',
                    '案号',
                    '执行法院',
                    '履行状态',
                    '执行依据文号',
                    '操作']
                result_dict = check_thead(root_div, thead_list)
                table_name = flss.__tablename__
                print('表头核对结果为.....：', result_dict)
                if result_dict:

                    # print(table_name)

                    # 一行是一个tr

                    # 创建新增对象 TODO: 测试核对第一条数据
                    add_result = CheckResult()
                    add_result.company_name = key
                    add_result.add_time = func.now()
                    # add_result.table_name = 'tyc_qybj_jbxx'  # 当前表名
                    add_result.table_name = table_name  # 当前表名
                    current_class = TycSffxSxr  # 当前模块对象名
                    first_parse_data = None
                    check_flag = 0  # 检测首页是否有匹配到的一行数据
                    check_first = 0  # 检测首页是否有匹配到的第一行数据

                    root_div = root_div[0]
                    trs = root_div.xpath("./tbody/tr")

                    for tr in trs:
                        insert_value = ""
                        tds = tr.xpath("./td")
                        case_date = try_and_text(
                            "variable[1].xpath('.//text()')", tds)
                        case_number = try_and_text(
                            "variable[2].xpath('.//text()')", tds)
                        execution_court = try_and_text(
                            "variable[3].xpath('.//text()')", tds)
                        performance_state = try_and_text(
                            "variable[4].xpath('.//text()')", tds)
                        execute_number = try_and_text(
                            "variable[5].xpath('.//text()')", tds)

                        flss.case_date = case_date[0] if case_date else 'NA'
                        flss.case_number = case_number[0] if case_number else 'NA'
                        flss.execution_court = execution_court[0] if execution_court else 'NA'
                        flss.performance_state = performance_state[0] if performance_state else 'NA'
                        flss.execute_number = execute_number[0] if execute_number else 'NA'
                        href = try_and_text(
                            "variable[6].xpath('./span/@onclick')[0]", tds)
                        res = re.search(r'"(.*?)"', href).groups(1)
                        href = res[0]
                        text_info = 'NA'
                        try:
                            text_info = self.detail_info["_container_dishonest"][href]
                            text_info = replace_special_chars(text_info)
                        except BaseException:
                            pass
                        flss.detail_info = text_info

                        flss.txt_id = self.txt_id
                        flss.company_name = key
                        flss.add_time = func.now()
                        flss.mark = 0
                        flss.agency_num = self.agency_num
                        flss.agency_name = self.agency_name
                        flss.batch = self.batch

                        unique_field = [
                            'company_name', flss.company_name]  # 该模块中唯一值字段名和值
                        check_parse(flss, add_result, unique_field)

                        # 验证首页解析
                        check_result = check_all_data(
                            add_result, flss, current_class)
                        if not first_parse_data:
                            first_parse_data = flss  # 保存第一条解析的数据
                        print('check_result+++++++++======:', check_result)
                        check_first += 1
                        if check_result:
                            check_flag = 1  # 匹配到数据
                            break
                        else:
                            check_flag = 0  # 没有匹配到
                    if not check_flag:
                        # 如果首页没有匹配到，则保存首页第一条数据到标准库，并记录其中一个字段
                        print('首页没有匹配到数据》》》》》》》》》')

                        try:

                            add_result.table_field = 'case_date'  # 保存第一各异常字段名   各模块手动添加
                            add_result.current_value = first_parse_data.case_date  # 保存第一各异常字段值   各模块手动添加
                            add_result.different_reason = '该页信息都不匹配，请通知数据管理员'
                            add_result.risk_level, add_result.standard_version = 1, 1
                            standard_value = single_oracle_orm.query(current_class).filter_by(  # 各表不同
                                company_name=first_parse_data.company_name).first()
                            add_result.standard_value = standard_value.case_date if standard_value else '-'
                            single_oracle_orm.add(add_result)
                            single_oracle_orm.commit()
                        except Exception as e:
                            print('check all datas error===={}'.format(e))
                    elif check_first > 1 and check_flag:
                        # 匹配到但不是第一条，更新页面第一条到标准库
                        unique_line = single_oracle_orm.query(
                            current_class).first()
                        single_oracle_orm.delete(unique_line)
                        single_oracle_orm.add(first_parse_data)
                        single_oracle_orm.commit()
                        print(
                            '首页已匹配到数据，但不是第一条,更新为当前页第一条》》》》》》》！{}'.format(key))

                else:
                    insert_result(self.search_name, table_name, result_dict)

    # 被执行人
    def html_parse_executed(self, index):
        logger.debug("Parse detail info 被执行人{}".format(self.search_name))
        if index == 1 and not isinstance(self.selector, int):
            # 分页是否解析：传入当前公司名称和当前模块对应的数据表名
            check_next_page(self.search_name, 'tyc_sffx_bzxr')
        else:
            # 获得被执行人大标签
            root_div = self.selector.xpath(
                '//div[@id="_container_zhixing"][position()=1]/table')
            if root_div:
                flss = TycSffxBzxr()
                key = self.search_name
                # 表头信息
                thead_list = ['序号', '立案日期', '执行标的', '案号', '执行法院', '操作']
                result_dict = check_thead(root_div, thead_list)
                table_name = flss.__tablename__
                print('表头核对结果为.....：', result_dict)
                if result_dict:

                    # print(table_name)

                    root_div = root_div[0]
                    # 一行是一个tr
                    trs = root_div.xpath("./tbody/tr")

                    for tr in trs:

                        # 创建新增对象 TODO: 测试核对第一条数据
                        add_result = CheckResult()
                        add_result.company_name = key
                        add_result.add_time = func.now()
                        # add_result.table_name = 'tyc_qybj_jbxx'  # 当前表名
                        add_result.table_name = table_name  # 当前表名
                        current_class = TycSffxBzxr  # 当前模块对象名
                        first_parse_data = None
                        check_flag = 0  # 检测首页是否有匹配到的一行数据
                        check_first = 0  # 检测首页是否有匹配到的第一行数据

                        insert_value = ""
                        tds = tr.xpath("./td")
                        flss.record_date = try_and_text(
                            "variable[1].xpath('./text()')[0]", tds)
                        flss.execute_underlying = try_and_text(
                            "variable[2].xpath('./text()')[0]", tds)
                        flss.case_number = try_and_text(
                            "variable[3].xpath('./text()')[0]", tds)
                        flss.court = try_and_text(
                            "variable[4].xpath('./text()')[0]", tds)
                        href = try_and_text(
                            "variable[5].xpath('./span/@onclick')[0]", tds)
                        res = re.search(r'"(.*?)"', href).groups(1)
                        href = res[0]
                        text_info = 'NA'
                        try:
                            text_info = self.detail_info["_container_zhixing"][href]
                            text_info = replace_special_chars(text_info)
                        except BaseException:
                            pass
                        flss.detail = text_info

                        flss.txt_id = self.txt_id
                        flss.company_name = key
                        flss.add_time = func.now()
                        flss.mark = 0
                        flss.agency_num = self.agency_num
                        flss.agency_name = self.agency_name
                        flss.batch = self.batch

                        unique_field = [
                            'company_name', flss.company_name]  # 该模块中唯一值字段名和值
                        check_parse(flss, add_result, unique_field)

                        # 验证首页解析
                        check_result = check_all_data(
                            add_result, flss, current_class)
                        if not first_parse_data:
                            first_parse_data = flss  # 保存第一条解析的数据
                        print('check_result+++++++++======:', check_result)
                        check_first += 1
                        if check_result:
                            check_flag = 1  # 匹配到数据
                            break
                        else:
                            check_flag = 0  # 没有匹配到
                    if not check_flag:
                        # 如果首页没有匹配到，则保存首页第一条数据到标准库，并记录其中一个字段
                        print('首页没有匹配到数据》》》》》》》》》')

                        try:

                            add_result.table_field = 'record_date'  # 保存第一各异常字段名   各模块手动添加
                            add_result.current_value = first_parse_data.record_date  # 保存第一各异常字段值   各模块手动添加
                            add_result.different_reason = '该页信息都不匹配，请通知数据管理员'
                            add_result.risk_level, add_result.standard_version = 1, 1
                            standard_value = single_oracle_orm.query(current_class).filter_by(  # 各表不同
                                company_name=first_parse_data.company_name).first()
                            add_result.standard_value = standard_value.record_date if standard_value else '-'
                            single_oracle_orm.add(add_result)
                            single_oracle_orm.add(add_result)
                            single_oracle_orm.commit()
                        except Exception as e:
                            print('check all datas error===={}'.format(e))
                    elif check_first > 1 and check_flag:
                        # 匹配到但不是第一条，更新页面第一条到标准库
                        unique_line = single_oracle_orm.query(
                            current_class).first()
                        single_oracle_orm.delete(unique_line)
                        single_oracle_orm.add(first_parse_data)
                        single_oracle_orm.commit()
                        print(
                            '首页已匹配到数据，但不是第一条,更新为当前页第一条》》》》》》》！{}'.format(key))
                else:
                    insert_result(self.search_name, table_name, result_dict)

    # 解析：司法风险-->司法协助
    def html_parse_sfxz(self, index):
        logger.debug("Parse detail info 司法协助 {}".format(self.search_name))
        sfxzInfo = TycSffxSfxz()
        if index == 1 and not isinstance(self.selector, int):
            # 分页是否解析：传入当前公司名称和当前模块对应的数据表名
            check_next_page(self.search_name, 'tyc_sffx_sfxz')
            print('佐源集团司法协助来了。。。。。。。。。。。。。。。。')
        else:
            root_div = self.selector.xpath(
                '//div[@id="_container_judicialAid"]/table')

            # 表头信息
            thead_list = [
                '序号',
                '被执行人',
                '股权数额',
                '执行法院',
                '执行通知书文号',
                '类型|状态',
                '操作']
            if root_div:
                result_dict = check_thead(root_div, thead_list)
                table_name = sfxzInfo.__tablename__
                print('表头核对结果为.....：', result_dict)
                if result_dict:

                    # print(table_name)

                    trs = self.selector.xpath(
                        '//div[@id="_container_judicialAid"]/table/tbody/tr')
                    if trs:
                        # sfxzInfo = TycSffxSfxz()

                        key = self.search_name  # 创建新增对象

                        add_result = CheckResult()
                        add_result.company_name = key
                        add_result.add_time = func.now()
                        # add_result.table_name = 'tyc_qybj_jbxx'  # 当前表名
                        add_result.table_name = table_name  # 当前表名
                        current_class = TycSffxSfxz  # 当前模块对象名
                        first_parse_data = None
                        check_flag = 0  # 检测首页是否有匹配到的一行数据
                        check_first = 0  # 检测首页是否有匹配到的第一行数据

                        for tr in trs:
                            insert_value = ""
                            tds = tr.xpath('./td')
                            # 被执行人
                            sfxzInfo.enforcement_person = try_and_text(
                                "variable[1].xpath('./text()')[0]", tds)
                            # 股权数额
                            sfxzInfo.equity_amount = try_and_text(
                                "variable[2].xpath('./text()')[0]", tds)
                            # 执行法院
                            sfxzInfo.executive_court = try_and_text(
                                "variable[3].xpath('./text()')[0]", tds)
                            # sfxzInfo.executive_court = '解析有误'
                            # 执行通知文号
                            sfxzInfo.approval_num = try_and_text(
                                "variable[4].xpath('./text()')[0]", tds)
                            # 类型|状态
                            sfxzInfo.status = try_and_text(
                                "variable[5].xpath('./text()')[0]", tds)
                            href = try_and_text(
                                "variable[6].xpath('./span/@onclick')[0]", tds)
                            res = re.search(r'"(.*?)"', href).groups(1)
                            href = res[0]
                            text_info = 'NA'
                            try:
                                text_info = self.detail_info["_container_judicialAid"][href]
                                text_info = replace_special_chars(text_info)
                            except BaseException:
                                pass
                            sfxzInfo.detail = text_info
                            sfxzInfo.txt_id = self.txt_id
                            sfxzInfo.company_name = key
                            sfxzInfo.mark = 0
                            sfxzInfo.add_time = datetime.now()
                            sfxzInfo.agency_num = self.agency_num
                            sfxzInfo.agency_name = self.agency_name
                            sfxzInfo.batch = self.batch

                            unique_field = [
                                'company_name', sfxzInfo.company_name]  # 该模块中唯一值字段名和值
                            check_parse(sfxzInfo, add_result, unique_field)

                            # 验证首页解析
                            check_result = check_all_data(
                                add_result, sfxzInfo, current_class)
                            if not first_parse_data:
                                first_parse_data = sfxzInfo  # 保存第一条解析的数据
                            print('check_result+++++++++======:', check_result)
                            check_first += 1
                            if check_result:
                                check_flag = 1  # 匹配到数据
                                break
                            else:
                                check_flag = 0  # 没有匹配到
                        if not check_flag:
                            # 如果首页没有匹配到，则保存首页第一条数据到标准库，并记录其中一个字段
                            print('首页没有匹配到数据》》》》》》》》》')

                            try:

                                add_result.table_field = 'enforcement_person'  # 保存第一各异常字段名   各模块手动添加
                                add_result.current_value = first_parse_data.enforcementPerson  # 保存第一各异常字段值   各模块手动添加
                                add_result.different_reason = '该页信息都不匹配，请通知数据管理员'
                                add_result.risk_level, add_result.standard_version = 1, 1
                                standard_value = single_oracle_orm.query(current_class).filter_by(  # 各表不同
                                    company_name=first_parse_data.company_name).first().enforcement_person
                                single_oracle_orm.add(add_result)
                                single_oracle_orm.commit()
                            except Exception as e:
                                print('check all datas error===={}'.format(e))
                        elif check_first > 1 and check_flag:
                            # 匹配到但不是第一条，更新页面第一条到标准库
                            unique_line = single_oracle_orm.query(
                                current_class).first()
                            single_oracle_orm.delete(unique_line)
                            single_oracle_orm.add(first_parse_data)
                            single_oracle_orm.commit()
                            print(
                                '首页已匹配到数据，但不是第一条,更新为当前页第一条》》》》》》》！{}'.format(key))

                else:
                    insert_result(self.search_name, table_name, result_dict)

    # 经营风险
    # 经营异常
    def html_parse_abnormal(self, index):
        logger.debug("Parse detail info 经营异常 {}".format(self.search_name))
        flss = TycJyfxJyyc()
        if index == 1 and not isinstance(self.selector, int):
            # # 分页是否解析：传入当前公司名称和当前模块对应的数据表名
            # check_next_page(self.search_name, 'tyc_jyfx_jyyc')
            pass
        else:
            table = self.selector.xpath(
                '//div[@id= "_container_abnormal"]/table')
            if table:
                # 表头信息
                thead_list = ['序号', '列入日期', '列入经营异常名录原因', '列入决定机关']
                result_dict = check_thead(table, thead_list)
                table_name = flss.__tablename__
                print('表头核对结果为.....：', result_dict)
                if result_dict:

                    # print(table_name)

                    # 获得经营异常大标签
                    # root_div = self.selector.xpath(
                    # '//div[@id= "_container_abnormal"]/table/tbody/tr')
                    root_div = table[0].xpath('./tbody/tr')
                    if root_div:
                        # flss = TycJyfxJyyc()
                        key = self.search_name

                        add_result = CheckResult()
                        add_result.company_name = key
                        add_result.add_time = func.now()
                        # add_result.table_name = 'tyc_qybj_jbxx'  # 当前表名
                        add_result.table_name = table_name  # 当前表名
                        current_class = TycJyfxJyyc  # 当前模块对象名
                        first_parse_data = None
                        check_flag = 0  # 检测首页是否有匹配到的一行数据
                        check_first = 0  # 检测首页是否有匹配到的第一行数据

                        for tr in root_div:
                            insert_value = ""
                            tds = tr.xpath("./td")
                            # 加入
                            insert_date = try_and_text(
                                "variable[1].xpath('.//text()')[0]", tds)
                            flss.insert_date = insert_date
                            insert_cause = try_and_text(
                                "variable[2].xpath('.//text()')[0]", tds)
                            logger.debug(
                                '列入原因={} type={}'.format(
                                    insert_cause,
                                    type(insert_cause)))
                            flss.insert_cause = insert_cause
                            insert_department = 'NA'
                            insert_department = try_and_text(
                                "variable[3].xpath('.//text()')[0]", tds)
                            flss.insert_department = insert_department

                            flss.out_date = CURRENT_VERSION_NULL
                            flss.out_cause = CURRENT_VERSION_NULL
                            flss.out_department = CURRENT_VERSION_NULL
                            # 新增 移除日期
                            try:
                                out_date = try_and_text(
                                    "variable[4].xpath('.//text()')[0]", tds)
                                flss.out_date = out_date if out_date else 'NA'
                                # 新增  移除原因
                                out_cause = try_and_text(
                                    "variable[5].xpath('.//text()')[0]", tds)
                                flss.out_cause = out_cause if out_cause else 'NA'
                                # 新增 移除机关
                                out_department = try_and_text(
                                    "variable[6].xpath('.//text()')[0]", tds)
                                flss.out_department = out_department if out_department else 'NA'
                            except BaseException:
                                pass

                            flss.txt_id = self.txt_id
                            flss.company_name = key
                            flss.add_time = func.now()
                            flss.mark = 0
                            flss.agency_num = self.agency_num
                            flss.agency_name = self.agency_name
                            flss.batch = self.batch

                            unique_field = [
                                'company_name', flss.company_name]  # 该模块中唯一值字段名和值
                            check_parse(flss, add_result, unique_field)

                            # 验证首页解析
                            check_result = check_all_data(
                                add_result, flss, current_class)
                            if not first_parse_data:
                                first_parse_data = flss  # 保存第一条解析的数据
                            print('check_result+++++++++======:', check_result)
                            check_first += 1
                            if check_result:
                                check_flag = 1  # 匹配到数据
                                break
                            else:
                                check_flag = 0  # 没有匹配到
                        if not check_flag:
                            # 如果首页没有匹配到，则保存首页第一条数据到标准库，并记录其中一个字段
                            print('首页没有匹配到数据》》》》》》》》》')

                            try:

                                add_result.table_field = 'insert_date'  # 保存第一各异常字段名   各模块手动添加
                                add_result.current_value = first_parse_data.insert_date  # 保存第一各异常字段值   各模块手动添加
                                add_result.different_reason = '该页信息都不匹配，请通知数据管理员'
                                add_result.risk_level, add_result.standard_version = 1, 1
                                standard_value = single_oracle_orm.query(current_class).filter_by(  # 各表不同
                                    company_name=first_parse_data.company_name).first()
                                add_result.standard_value = standard_value.insert_date if standard_value else '-'
                                single_oracle_orm.add(add_result)
                                single_oracle_orm.commit()
                            except Exception as e:
                                print('check all datas error===={}'.format(e))
                        elif check_first > 1 and check_flag:
                            # 匹配到但不是第一条，更新页面第一条到标准库
                            unique_line = single_oracle_orm.query(
                                current_class).first()
                            single_oracle_orm.delete(unique_line)
                            single_oracle_orm.add(first_parse_data)
                            single_oracle_orm.commit()
                            print(
                                '首页已匹配到数据，但不是第一条,更新为当前页第一条》》》》》》》！{}'.format(key))

                else:
                    insert_result(self.search_name, table_name, result_dict)

    # 行政处罚
    def html_parse_xingzhengchufa(self, index):
        logger.debug("Parse detail info 行政处罚{}".format(self.search_name))
        flss = TycJyfxXzcf()
        if index == 1 and not isinstance(self.selector, int):
            # 分页是否解析：传入当前公司名称和当前模块对应的数据表名
            check_next_page(self.search_name, 'tyc_jyfx_xzcf')
        else:
            # 获得行政处罚大标

            root_div = self.selector.xpath(
                '//div[@id="_container_punish"][position()=1]/table')

        if root_div:
            # flss = TycJyfxXzcf()
            key = self.search_name

            # 表头信息
            thead_list = ['序号', '公示日期', '决定书文号', '行政处罚内容', '决定机关', '操作']
            result_dict = check_thead(root_div, thead_list)
            table_name = flss.__tablename__
            print('表头核对结果为.....：', result_dict)
            if result_dict:

                # print(table_name)

                # 一行是一个tr
                root_div = root_div[0]
                trs = root_div.xpath("./tbody/tr")

                for tr in trs:

                    add_result = CheckResult()
                    add_result.company_name = key
                    add_result.add_time = func.now()
                    # add_result.' = 'tyc_qybj_jbxx'  # 当前表名
                    add_result.table_name = table_name  # 当前表名
                    current_class = TycJyfxXzcf  # 当前模块对象名
                    first_parse_data = None
                    check_flag = 0  # 检测首页是否有匹配到的一行数据
                    check_first = 0  # 检测首页是否有匹配到的第一行数据

                    insert_value = ""
                    tds = tr.xpath("./td")

                    try:
                        flss.punishment_name = CURRENT_VERSION_NULL
                        flss.punishment_area = CURRENT_VERSION_NULL
                        flss.decision_date = try_and_text(
                            "variable[1].xpath('./text()')[0]", tds)
                        flss.decision_number = try_and_text(
                            "variable[2].xpath('./text()')[0]", tds)
                        flss.punishment_contents = try_and_text(
                            "variable[3].xpath('./text()')[0]", tds)
                        # flss.type = try_and_text("variable[4].xpath('./text()')[0]",tds)
                        flss.type = CURRENT_VERSION_NULL
                        flss.decision_department = try_and_text(
                            "variable[4].xpath('./text()')[0]", tds)
                        flss.detail_info = try_and_text(
                            "variable[5].xpath('./script/text()')[0]", tds)
                        # tds[5].text.replace("详情 》", "").strip().replace("'", '\\"')
                    except BaseException:
                        flss.decision_date = ""
                        flss.decision_number = ""
                        flss.type = ""
                        flss.decision_department = ""
                        flss.punishment_name = try_and_text(
                            "variable[1].xpath('text()')[0]", tds)
                        flss.punishment_area = try_and_text(
                            "variable[2].xpath('text()')[0]", tds)
                        flss.detail_info = try_and_text(
                            "variable[3].xpath('./script/text()')[0]", tds)
                        # tds[3].text.replace("详情 》", "").strip().replace("'", '\\"')
                    flss.txt_id = self.txt_id
                    try:
                        flss.company_name = key
                    except BaseException:
                        flss.company_name = key

                    flss.add_time = func.now()
                    flss.mark = 0
                    flss.agency_num = self.agency_num
                    flss.agency_name = self.agency_name
                    flss.batch = self.batch

                    unique_field = [
                        'company_name', flss.company_name]  # 该模块中唯一值字段名和值
                    check_parse(flss, add_result, unique_field)

                    # 验证首页解析
                    check_result = check_all_data(
                        add_result, flss, current_class)
                    if not first_parse_data:
                        first_parse_data = flss  # 保存第一条解析的数据
                    print('check_result+++++++++======:', check_result)
                    check_first += 1
                    if check_result:
                        check_flag = 1  # 匹配到数据
                        break
                    else:
                        check_flag = 0  # 没有匹配到
                if not check_flag:
                    # 如果首页没有匹配到，则保存首页第一条数据到标准库，并记录其中一个字段
                    print('首页没有匹配到数据》》》》》》》》》')

                    try:

                        add_result.table_field = 'decision_date'  # 保存第一各异常字段名   各模块手动添加
                        add_result.current_value = first_parse_data.decision_date  # 保存第一各异常字段值   各模块手动添加
                        add_result.different_reason = '该页信息都不匹配，请通知数据管理员'
                        add_result.risk_level, add_result.standard_version = 1, 1
                        standard_value = single_oracle_orm.query(current_class).filter_by(  # 各表不同
                            company_name=first_parse_data.company_name).first()
                        add_result.standard_value = standard_value.decision_date if standard_value else '-'
                        single_oracle_orm.add(add_result)
                        single_oracle_orm.commit()
                    except Exception as e:
                        print('check all datas error===={}'.format(e))
                elif check_first > 1 and check_flag:
                    # 匹配到但不是第一条，更新页面第一条到标准库
                    unique_line = single_oracle_orm.query(
                        current_class).first()
                    single_oracle_orm.delete(unique_line)
                    single_oracle_orm.add(first_parse_data)
                    single_oracle_orm.commit()
                    print('首页已匹配到数据，但不是第一条,更新为当前页第一条》》》》》》》！{}'.format(key))

            else:
                insert_result(self.search_name, table_name, result_dict)

    # 解析：经营风险--严重违法
    def html_parse_illegalSerious(self):
        logger.debug("Parse detail info 严重违法 {}".format(self.search_name))
        illegalSerious = TycJyfxYzwf()

        # 表头信息
        root_div = self.selector.xpath('//div[@id="_container_illegal"]/table')
        if root_div:
            thead_list = ['序号', '列入日期', '列入严重违法失信企业名单原因', '列入决定机关']
            result_dict = check_thead(root_div, thead_list)
            table_name = illegalSerious.__tablename__
            print('表头核对结果为.....：', result_dict)
            if result_dict:

                # trs = self.selector.xpath(
                #     '//div[@id="_container_illegal"]/table/tbody/tr')
                trs = root_div[0].xpath('./tbody/tr')
                if trs:

                    key = self.search_name

                    add_result = CheckResult()
                    add_result.company_name = key
                    add_result.add_time = func.now()
                    # add_result.table_name = 'tyc_qybj_jbxx'  # 当前表名
                    add_result.table_name = table_name  # 当前表名
                    current_class = TycJyfxYzwf  # 当前模块对象名
                    first_parse_data = None
                    check_flag = 0  # 检测首页是否有匹配到的一行数据
                    check_first = 0  # 检测首页是否有匹配到的第一行数据

                    for tr in trs:
                        insert_value = ""
                        # illegalSerious = TycJyfxYzwf()
                        tds = tr.xpath('./td')
                        illegalSerious.illegal_date = try_and_text(
                            "variable[1].xpath('text()')[0]", tds)
                        illegalSerious.illegal_reason = try_and_text(
                            "variable[2].xpath('text()')[0] ", tds)
                        illegalSerious.office = try_and_text(
                            "variable[3].xpath('text()')[0]", tds)

                        # 移出日期
                        try:
                            out_date = tds[4].xpath('./text()')[0]
                            illegalSerious.out_date = out_date[0] if out_date else 'NA'
                            # 移出原因
                            out_reason = try_and_text(
                                "variable[5].xpath('./text()')[0]", tds)
                            illegalSerious.out_reason = out_reason[0] if out_reason else 'NA'
                            # 移出决定机关
                            out_department = try_and_text(
                                "variable[6].xpath('./text()')[0]", tds)
                            illegalSerious.out_department = out_department[0] if out_department else 'NA'
                        except BaseException:
                            # 新增移出
                            illegalSerious.out_date = CURRENT_VERSION_NULL
                            illegalSerious.out_reason = CURRENT_VERSION_NULL
                            illegalSerious.out_department = CURRENT_VERSION_NULL

                        illegalSerious.txt_id = self.txt_id
                        illegalSerious.company_name = key
                        illegalSerious.mark = 0
                        illegalSerious.add_time = func.now()
                        illegalSerious.agency_num = self.agency_num
                        illegalSerious.agency_name = self.agency_name
                        illegalSerious.batch = self.batch

                        unique_field = [
                            'company_name', illegalSerious.company_name]  # 该模块中唯一值字段名和值
                        check_parse(illegalSerious, add_result, unique_field)

                        # 验证首页解析
                        check_result = check_all_data(
                            add_result, illegalSerious, current_class)
                        if not first_parse_data:
                            first_parse_data = illegalSerious  # 保存第一条解析的数据
                        print('check_result+++++++++======:', check_result)
                        check_first += 1
                        if check_result:
                            check_flag = 1  # 匹配到数据
                            break
                        else:
                            check_flag = 0  # 没有匹配到
                    if not check_flag:
                        # 如果首页没有匹配到，则保存首页第一条数据到标准库，并记录其中一个字段
                        print('首页没有匹配到数据》》》》》》》》》')

                        try:

                            add_result.table_field = 'illegal_date'  # 保存第一各异常字段名   各模块手动添加
                            add_result.current_value = first_parse_data.illegal_date  # 保存第一各异常字段值   各模块手动添加
                            add_result.different_reason = '该页信息都不匹配，请通知数据管理员'
                            add_result.risk_level, add_result.standard_version = 1, 1
                            standard_value = single_oracle_orm.query(current_class).filter_by(  # 各表不同
                                company_name=first_parse_data.company_name).first()
                            add_result.standard_value = standard_value.illegal_date if standard_value else '-'
                            single_oracle_orm.add(add_result)
                            single_oracle_orm.commit()
                        except Exception as e:
                            print('check all datas error===={}'.format(e))
                    elif check_first > 1 and check_flag:
                        # 匹配到但不是第一条，更新页面第一条到标准库
                        unique_line = single_oracle_orm.query(
                            current_class).first()
                        single_oracle_orm.delete(unique_line)
                        single_oracle_orm.add(first_parse_data)
                        single_oracle_orm.commit()
                        print(
                            '首页已匹配到数据，但不是第一条,更新为当前页第一条》》》》》》》！{}'.format(key))

            else:
                insert_result(self.search_name, table_name, result_dict)

    # 股权出质
    def html_parse_pledge(self, index):
        # 无变化
        logger.debug("Parse detail info 股权出质{}".format(self.search_name))
        flss = TycJyfxGqcz()

        if index == 1 and not isinstance(self.selector, int):
            # 分页是否解析：传入当前公司名称和当前模块对应的数据表名
            check_next_page(self.search_name, 'tyc_jyfx_gqcz')
        elif index == 0:
            # 获得股权出质大标签  nav-main-equityCount
            table = self.selector.xpath('//div[@id="_container_equity"]/table')
            thead_list = [
                '序号',
                '公示日期',
                '登记编号',
                '出质人',
                '质权人',
                '状态',
                '出质股权数额',
                '操作']
            if table:
                result_dict = check_thead(table, thead_list)
                table_name = flss.__tablename__
                print('表头核对结果为.....：', result_dict)
                if result_dict:

                    # print(table_name)
                    insert_result(self.search_name, table_name, result_dict)
                else:

                    # root_div = self.selector.xpath(
                    #     '//div[@id="_container_equity"]/table/tbody/tr')
                    root_div = table[0].xpath('./tbody/tr')
                    if root_div:
                        logger.debug(
                            'cccc有股权出质。。。。。。。。。。。。。。。。。{}'.format(
                                self.search_name))
                        # flss = TycJyfxGqcz()
                        key = self.search_name
                        # 一行是一个tr
                        # TODO: 测试核对第一条数据
                        add_result = CheckResult()
                        add_result.company_name = key
                        add_result.add_time = func.now()
                        # add_result.table_name = 'tyc_qybj_jbxx'  # 当前表名
                        add_result.table_name = table_name  # 当前表名
                        current_class = TycJyfxGqcz  # 当前模块对象名
                        first_parse_data = None
                        check_flag = 0  # 检测首页是否有匹配到的一行数据
                        check_first = 0  # 检测首页是否有匹配到的第一行数据

                        for tr in root_div:
                            insert_value = ""
                            tds = tr.xpath("./td")
                            # #logger.debug(tds.xpath('text()'))
                            flss.announcement_date = try_and_text(
                                "variable[1].xpath('.//text()')[0]", tds)
                            flss.registration_number = try_and_text(
                                "variable[2].xpath('.//text()')[0]", tds)

                            flss.pledgor = try_and_text(
                                "variable[3].xpath('.//text()')[0]", tds)
                            flss.pledgee = try_and_text(
                                "variable[4].xpath('.//text()')[0]", tds)
                            flss.status = try_and_text(
                                "variable[5].xpath('.//text()')[0]", tds)
                            flss.pledged_amount = try_and_text(
                                "variable[6].xpath('.//text()')[0]", tds)
                            text_info = try_and_text(
                                "variable[7].xpath('./script/text()')[0]", tds)
                            text_info = replace_special_chars(text_info)
                            flss.detail_info = text_info
                            # tds[6].text.replace("详情 》", "").strip().replace("'", '\\"')
                            flss.txt_id = self.txt_id
                            flss.company_name = key
                            flss.add_time = func.now()
                            flss.mark = 0
                            flss.agency_num = self.agency_num
                            flss.agency_name = self.agency_name
                            flss.batch = self.batch

                            # TODO:
                            unique_field = [
                                'company_name', flss.company_name]  # 该模块中唯一值字段名和值
                            check_parse(flss, add_result, unique_field)

                            # 验证首页解析
                            check_result = check_all_data(
                                add_result, flss, current_class)
                            if not first_parse_data:
                                first_parse_data = flss  # 保存第一条解析的数据
                            print('check_result+++++++++======:', check_result)
                            check_first += 1
                            if check_result:
                                check_flag = 1  # 匹配到数据
                                break
                            else:
                                check_flag = 0  # 没有匹配到
                        if not check_flag:
                            # 如果首页没有匹配到，则保存首页第一条数据到标准库，并记录其中一个字段
                            print('首页没有匹配到数据》》》》》》》》》')

                            try:
                                # TODO :
                                add_result.table_field = 'announcement_date'  # 保存第一各异常字段名   各模块手动添加
                                add_result.current_value = first_parse_data.announcement_date  # 保存第一各异常字段值   各模块手动添加
                                add_result.different_reason = '该页信息都不匹配，请通知数据管理员'
                                add_result.risk_level, add_result.standard_version = 1, 1
                                standard_value = single_oracle_orm.query(current_class).filter_by(  # 各表不同
                                    company_name=first_parse_data.company_name).first()
                                add_result.standard_value = standard_value.announcement_date if standard_value else '-'
                                single_oracle_orm.add(add_result)
                                single_oracle_orm.commit()
                            except Exception as e:
                                print('check all datas error===={}'.format(e))
                        elif check_first > 1 and check_flag:
                            # 匹配到但不是第一条，更新页面第一条到标准库
                            unique_line = single_oracle_orm.query(
                                current_class).first()
                            single_oracle_orm.delete(unique_line)
                            single_oracle_orm.add(first_parse_data)
                            single_oracle_orm.commit()
                            print(
                                '首页已匹配到数据，但不是第一条,更新为当前页第一条》》》》》》》！{}'.format(key))

    # 动产抵押
    def html_parse_dongchandiya(self, index):
        logger.debug("Parse detail info 动产抵押{}".format(self.search_name))
        flss = TycJyfxDcdy()
        if index == 1 and not isinstance(self.selector, int):
            pass
            # # 分页是否解析：传入当前公司名称和当前模块对应的数据表名
            # check_next_page(self.search_name, 'tyc_qybj_dwtz')
        else:
            table = self.selector.xpath(
                '//div[@id="_container_mortgage"]/table')
            thead_list = [
                '序号',
                '登记日期',
                '登记号',
                '被担保债权类型',
                '被担保债权数额',
                '登记机关',
                '状态',
                '操作']
            if table:
                result_dict = check_thead(table, thead_list)
                table_name = flss.__tablename__
                print('表头核对结果为.....：', result_dict)
                if result_dict:

                    # print(table_name)

                    # 获得动产抵押大标签
                    # root_div = self.selector.xpath(
                    #             #     "//div[@id='_container_mortgage']/table/tbody/tr")
                    root_div = table[0].xpath('./tbody/tr')
                    if root_div:
                        logger.debug(
                            'cccc有动产抵押。。。。。。。。。。。。。。。。。{}'.format(
                                self.search_name))

                        key = self.search_name
                        # 一行是一个tr
                        # TODO: 测试核对第一条数据
                        add_result = CheckResult()
                        add_result.company_name = key
                        add_result.add_time = func.now()
                        # add_result.table_name = 'tyc_qybj_jbxx'  # 当前表名
                        add_result.table_name = table_name  # 当前表名
                        current_class = TycJyfxDcdy  # 当前模块对象名
                        first_parse_data = None
                        check_flag = 0  # 检测首页是否有匹配到的一行数据
                        check_first = 0  # 检测首页是否有匹配到的第一行数据

                        for tr in root_div:
                            # flss = tycJyfxDcdy()
                            insert_value = ""
                            tds = tr.xpath('./td')
                            flss.registration_date = try_and_text(
                                "variable[1].xpath('./text()')[0]", tds)
                            flss.registration_number = try_and_text(
                                "variable[2].xpath('./text()')[0]", tds)
                            flss.guarantee_amount = try_and_text(
                                "variable[4].xpath('./text()')[0]", tds)
                            flss.guarantee_type = try_and_text(
                                "variable[3].xpath('./text()')[0]", tds)
                            flss.registration_department = try_and_text(
                                "variable[5].xpath('./text()')[0]", tds)
                            flss.status = try_and_text(
                                "variable[6].xpath('./text()')[0]", tds)

                            detail_info = try_and_text(
                                "variable[7].xpath('.//script/text()')[0]", tds)
                            # tds[7].text.replace("详情 》", "").strip().replace("'", '\\"')
                            flss.detail_info = replace_special_chars(
                                detail_info)
                            flss.txt_id = self.txt_id
                            flss.company_name = key
                            flss.add_time = func.now()
                            flss.mark = 0
                            flss.agency_num = self.agency_num
                            flss.agency_name = self.agency_name
                            flss.batch = self.batch

                            # TODO:
                            unique_field = [
                                'company_name', flss.company_name]  # 该模块中唯一值字段名和值
                            check_parse(flss, add_result, unique_field)

                            # 验证首页解析
                            check_result = check_all_data(
                                add_result, flss, current_class)
                            if not first_parse_data:
                                first_parse_data = flss  # 保存第一条解析的数据
                            print('check_result+++++++++======:', check_result)
                            check_first += 1
                            if check_result:
                                check_flag = 1  # 匹配到数据
                                break
                            else:
                                check_flag = 0  # 没有匹配到
                        if not check_flag:
                            # 如果首页没有匹配到，则保存首页第一条数据到标准库，并记录其中一个字段
                            print('首页没有匹配到数据》》》》》》》》》')

                            try:
                                # TODO :
                                add_result.table_field = 'registration_date'  # 保存第一各异常字段名   各模块手动添加
                                add_result.current_value = first_parse_data.registration_date  # 保存第一各异常字段值   各模块手动添加
                                add_result.different_reason = '该页信息都不匹配，请通知数据管理员'
                                add_result.risk_level, add_result.standard_version = 1, 1
                                standard_value = single_oracle_orm.query(current_class).filter_by(  # 各表不同
                                    company_name=first_parse_data.company_name).first()
                                add_result.standard_value = standard_value.registration_date if standard_value else '-'
                                single_oracle_orm.add(add_result)
                                single_oracle_orm.commit()
                            except Exception as e:
                                print('check all datas error===={}'.format(e))
                        elif check_first > 1 and check_flag:
                            # 匹配到但不是第一条，更新页面第一条到标准库
                            unique_line = single_oracle_orm.query(
                                current_class).first()
                            single_oracle_orm.delete(unique_line)
                            single_oracle_orm.add(first_parse_data)
                            single_oracle_orm.commit()
                            print(
                                '首页已匹配到数据，但不是第一条,更新为当前页第一条》》》》》》》！{}'.format(key))

                else:
                    insert_result(self.search_name, table_name, result_dict)

    # 解析：经营风险--欠税公告
    def html_parse_taxesNotice(self, index):
        logger.debug("Parse detail info 欠税公告{}".format(self.search_name))
        taxesNotice = TycJyfxQsgg()
        if index == 1 and not isinstance(self.selector, int):
            # 分页是否解析：传入当前公司名称和当前模块对应的数据表名
            check_next_page(self.search_name, 'tyc_jyfx_qsgg')
            # print('经营风险--欠税公告来了。。。。。。：{}'.format(self.search_name))
        else:
            # 表头信息
            root_div = self.selector.xpath(
                '//div[@id="_container_towntax"][position()=1]//table')
            thead_list = [
                '序号',
                '发布日期',
                '纳税人识别号',
                '欠税税种',
                '当前新发生的欠税余额',
                '欠税余额',
                '税务机关',
                '操作']
            if root_div:
                result_dict = check_thead(root_div, thead_list)
                table_name = taxesNotice.__tablename__
                print('表头核对结果为.....：', result_dict)
                if result_dict:
                    # print(table_name)

                    # trs = self.selector.xpath(
                    #     '//div[@id="_container_towntax"][position()=1]//table[position()=1]/tbody/tr')
                    trs = root_div[0].xpath('./tbody/tr')
                    if trs:

                        key = self.search_name
                        # taxesNotice = TycJyfxQsgg()

                        # TODO: 测试核对第一条数据
                        add_result = CheckResult()
                        add_result.company_name = key
                        add_result.add_time = func.now()
                        # add_result.table_name = 'tyc_qybj_jbxx'  # 当前表名
                        add_result.table_name = table_name  # 当前表名
                        current_class = TycJyfxQsgg  # 当前模块对象名
                        first_parse_data = None
                        check_flag = 0  # 检测首页是否有匹配到的一行数据
                        check_first = 0  # 检测首页是否有匹配到的第一行数据

                        for tr in trs:
                            insert_value = ""
                            tds = tr.xpath('./td')
                            taxesNotice.taxes_date = try_and_text(
                                "variable[1].xpath('text()')[0]", tds)
                            taxesNotice.taxes_num = try_and_text(
                                "variable[2].xpath('text()')[0]", tds)
                            taxesNotice.taxes_type = try_and_text(
                                "variable[3].xpath('text()')[0]", tds)
                            taxesNotice.taxes_money = try_and_text(
                                "variable[4].xpath('text()')[0]", tds)
                            taxesNotice.taxes_balance = try_and_text(
                                "variable[5].xpath('text()')[0]", tds)
                            taxesNotice.taxes_office = try_and_text(
                                "variable[6].xpath('text()')[0]", tds)
                            # 新增 详情
                            taxesNotice.detail = try_and_text(
                                "variable[7].xpath('./script/text()')[0]", tds)

                            taxesNotice.txt_id = self.txt_id
                            taxesNotice.company_name = key
                            taxesNotice.mark = 0
                            taxesNotice.add_time = func.now()
                            taxesNotice.agency_num = self.agency_num
                            taxesNotice.agency_name = self.agency_name
                            taxesNotice.batch = self.batch

                            # TODO:
                            unique_field = [
                                'company_name', taxesNotice.company_name]  # 该模块中唯一值字段名和值
                            check_parse(taxesNotice, add_result, unique_field)

                            # 验证首页解析
                            check_result = check_all_data(
                                add_result, taxesNotice, current_class)
                            if not first_parse_data:
                                first_parse_data = taxesNotice  # 保存第一条解析的数据
                            print('check_result+++++++++======:', check_result)
                            check_first += 1
                            if check_result:
                                check_flag = 1  # 匹配到数据
                                break
                            else:
                                check_flag = 0  # 没有匹配到
                        if not check_flag:
                            # 如果首页没有匹配到，则保存首页第一条数据到标准库，并记录其中一个字段
                            print('首页没有匹配到数据》》》》》》》》》')

                            try:
                                # TODO :
                                add_result.table_field = 'taxes_date'  # 保存第一各异常字段名   各模块手动添加
                                add_result.current_value = first_parse_data.taxes_date  # 保存第一各异常字段值   各模块手动添加
                                add_result.different_reason = '该页信息都不匹配，请通知数据管理员'
                                add_result.risk_level, add_result.standard_version = 1, 1
                                standard_value = single_oracle_orm.query(current_class).filter_by(  # 各表不同
                                    company_name=first_parse_data.company_name).first()
                                add_result.standard_value = standard_value.taxes_date if standard_value else '-'
                                single_oracle_orm.add(add_result)
                                single_oracle_orm.commit()
                            except Exception as e:
                                print('check all datas error===={}'.format(e))
                        elif check_first > 1 and check_flag:
                            # 匹配到但不是第一条，更新页面第一条到标准库
                            unique_line = single_oracle_orm.query(
                                current_class).first()
                            single_oracle_orm.delete(unique_line)
                            single_oracle_orm.add(first_parse_data)
                            single_oracle_orm.commit()
                            print(
                                '首页已匹配到数据，但不是第一条,更新为当前页第一条》》》》》》》！{}'.format(key))

                else:
                    insert_result(self.search_name, table_name, result_dict)

    # 解析：经营风险-->司法拍卖
    def html_parse_sfpm(self, index):
        logger.debug("Parse detail info 司法拍卖 {}".format(self.search_name))
        sfpaInfo = TycJyfxSfpm()
        if index == 1 and not isinstance(self.selector, int):
            # 分页是否解析：传入当前公司名称和当前模块对应的数据表名
            check_next_page(self.search_name, 'tyc_jyfx_sfpm')
        else:
            # 表头信息
            root_div = self.selector.xpath(
                '//div[@id="_container_judicialSale"]/table')
            thead_list = ['序号', '拍卖公告', '公告日期', '执行法院', '拍卖标的']
            if root_div:
                result_dict = check_thead(root_div, thead_list)
                table_name = sfpaInfo.__tablename__
                print('表头核对结果为.....：', result_dict)
                if result_dict:
                    # print(table_name)

                    # trs = self.selector.xpath(
                    #     '//div[@id="_container_judicialSale"]/table/tbody/tr')
                    trs = root_div[0].xpath('./tbody/tr')
                    if trs:
                        # sfpaInfo = TycJyfxSfpm()

                        key = self.search_name

                        # TODO: 测试核对第一条数据
                        add_result = CheckResult()
                        add_result.company_name = key
                        add_result.add_time = func.now()
                        # add_result.table_name = 'tyc_qybj_jbxx'  # 当前表名
                        add_result.table_name = table_name  # 当前表名
                        current_class = TycJyfxSfpm  # 当前模块对象名
                        first_parse_data = None
                        check_flag = 0  # 检测首页是否有匹配到的一行数据
                        check_first = 0  # 检测首页是否有匹配到的第一行数据

                        for tr in trs:
                            insert_value = ""
                            tds = tr.xpath('./td')
                            # 拍卖公告
                            sfpaInfo.auction_notice = try_and_text(
                                "variable[1].xpath('./a/text()')[0]", tds)
                            # 公告日期
                            sfpaInfo.auction_date = try_and_text(
                                "variable[2].xpath('./text()')[0]", tds)
                            # 执行法院
                            sfpaInfo.execute_court = try_and_text(
                                "variable[3].xpath('./text()')[0]", tds)
                            # 拍卖标的
                            sfpaInfo.auction_target = try_and_text(
                                "variable[4].xpath('string(.)')", tds)
                            text_info = 'NA'
                            href = try_and_text(
                                "variable[1].xpath('./a/@href')[0]", tds)
                            # 新增 详情 brand  TODO:详情
                            try:
                                text_info = self.detail_info["_container_judicialSale"][href.split(
                                    '/')[-1].replace('.', '_')]
                            except BaseException:
                                pass
                            sfpaInfo.auction_detail = replace_special_chars(
                                text_info)

                            # sfpaInfo.auction_detail = '详情'

                            sfpaInfo.txt_id = self.txt_id
                            sfpaInfo.company_name = key
                            sfpaInfo.mark = 0
                            sfpaInfo.add_time = datetime.now()
                            sfpaInfo.agency_num = self.agency_num
                            sfpaInfo.agency_name = self.agency_name
                            sfpaInfo.batch = self.batch

                            # TODO:
                            unique_field = [
                                'company_name', sfpaInfo.company_name]  # 该模块中唯一值字段名和值
                            check_parse(sfpaInfo, add_result, unique_field)

                            # 验证首页解析
                            check_result = check_all_data(
                                add_result, sfpaInfo, current_class)
                            if not first_parse_data:
                                first_parse_data = sfpaInfo  # 保存第一条解析的数据
                            print('check_result+++++++++======:', check_result)
                            check_first += 1
                            if check_result:
                                check_flag = 1  # 匹配到数据
                                break
                            else:
                                check_flag = 0  # 没有匹配到
                        if not check_flag:
                            # 如果首页没有匹配到，则保存首页第一条数据到标准库，并记录其中一个字段
                            print('首页没有匹配到数据》》》》》》》》》')

                            try:
                                # TODO :
                                add_result.table_field = 'auction_notice'  # 保存第一各异常字段名   各模块手动添加
                                add_result.current_value = first_parse_data.auction_notice  # 保存第一各异常字段值   各模块手动添加
                                add_result.different_reason = '该页信息都不匹配，请通知数据管理员'
                                add_result.risk_level, add_result.standard_version = 1, 1
                                standard_value = single_oracle_orm.query(current_class).filter_by(  # 各表不同
                                    company_name=first_parse_data.company_name).first()
                                add_result.standard_value = standard_value.auction_notice if standard_value else '-'
                                single_oracle_orm.add(add_result)
                                single_oracle_orm.commit()
                            except Exception as e:
                                print('check all datas error===={}'.format(e))
                        elif check_first > 1 and check_flag:
                            # 匹配到但不是第一条，更新页面第一条到标准库
                            unique_line = single_oracle_orm.query(
                                current_class).first()
                            single_oracle_orm.delete(unique_line)
                            single_oracle_orm.add(first_parse_data)
                            single_oracle_orm.commit()
                            print(
                                '首页已匹配到数据，但不是第一条,更新为当前页第一条》》》》》》》！{}'.format(key))

                else:
                    insert_result(self.search_name, table_name, result_dict)

    # 解析：经营风险-->清算信息
    def html_parse_qsxx(self, index):
        logger.debug("Parse detail info 清算信息 {}".format(self.search_name))
        qsxxInfo = TycJyfxQsxx()

        if index == 1 and not isinstance(self.selector, int):
            # # 分页是否解析：传入当前公司名称和当前模块对应的数据表名
            # check_next_page(self.search_name, 'tyc_qybj_dwtz')
            pass
        else:

            trs = self.selector.xpath(
                '//div[@id="_container_clearingCount"]/table/tbody/tr')
            if trs:
                # qsxxInfo = TycJyfxQsxx()
                insert_value = ""
                key = self.search_name

                tds1 = trs[0].xpath('./td')
                tds2 = trs[1].xpath('./td')
                # 清算组负责人
                principal = try_and_text("variable[1].xpath('./text()')", tds1)
                qsxxInfo.principal = principal[0] if principal else 'NA'

                # 清算组成员
                member = try_and_text("variable[1].xpath('./text()')", tds2)
                qsxxInfo.member = member[0] if member else 'NA'

                qsxxInfo.txt_id = self.txt_id
                qsxxInfo.company_name = key
                qsxxInfo.mark = 0
                qsxxInfo.add_time = datetime.now()
                qsxxInfo.agency_num = self.agency_num
                qsxxInfo.agency_name = self.agency_name
                qsxxInfo.batch = self.batch

                print('正在核实的公司是{}'.format(key))
                # single_oracle_orm.add(qsxxInfo)
                # print('清算信息：============', qsxxInfo.__dict__)
                # y2017 = single_oracle_orm.query(TycYearJbxx).filter_by(year=2017, company_name='佐源集团有限公司').first()
                # single_oracle_orm.delete()
                # single_oracle_orm.commit()
                standard_data = single_oracle_orm.query(
                    TycJyfxQsxx).filter_by(company_name=key).first()

                try:
                    change_dict = check_obj(qsxxInfo, standard_data)
                    print('核对结果为：', change_dict)
                    checkResult = CheckResult()
                    checkResult.company_name = key
                    checkResult.add_time = func.now()
                    checkResult.standard_version = 1
                    checkResult.task_status = 0
                    for k, v in change_dict.items():
                        checkResult.table_name = qsxxInfo.__tablename__
                        checkResult.current_value = v
                        checkResult.table_field = k
                        checkResult.standard_value = standard_data.__dict__[k]
                        checkResult.different_reason = '{}表中字段{}的值未核对成功'.format(
                            key, k)
                        import_field = single_oracle.oracle_find_by_param_all(
                            "select column_name from check_import_field where table_name = {}".format(
                                checkResult.table_name))
                        for col_name in import_field:
                            if k == col_name[0]:
                                checkResult.risk_level = 1
                            else:
                                checkResult.risk_level = 2
                        single_oracle_orm.add(checkResult)
                        single_oracle_orm.commit()

                except Exception as e:
                    print(e)

    # 解析：经营风险-->公示催告
    def html_parse_gscg(self):
        logger.debug("Parse detail info 公示催告 {}".format(self.search_name))
        gscgInfo = TycJyfxGscg()
        # 表头信息
        root_div = self.selector.xpath(
            '//div[@id="_container_publicnoticeItem"]/table')
        if root_div:
            thead_list = ['序号', '票据号', '票据类型', '票面金额', '发布机构', '公告日期', '操作']
            if root_div:
                result_dict = check_thead(root_div, thead_list)
                table_name = gscgInfo.__tablename__
                print('表头核对结果为.....：', result_dict)
                if result_dict:
                    # print(table_name)

                    # trs = self.selector.xpath(
                    #     '//div[@id="_container_publicnoticeItem"]/table/tbody/tr')
                    trs = root_div[0].xpath('./tbody/tr')
                    if trs:
                        # gscgInfo = TycJyfxGscg()

                        key = self.search_name
                        # TODO: 测试核对第一条数据
                        add_result = CheckResult()
                        add_result.company_name = key
                        add_result.add_time = func.now()
                        # add_result.table_name = 'tyc_qybj_jbxx'  # 当前表名
                        add_result.table_name = table_name  # 当前表名
                        current_class = TycJyfxGscg  # 当前模块对象名
                        first_parse_data = None
                        check_flag = 0  # 检测首页是否有匹配到的一行数据
                        check_first = 0  # 检测首页是否有匹配到的第一行数据

                        for tr in trs:
                            insert_value = ""
                            tds = tr.xpath('./td')
                            # 票据号
                            gscgInfo.bill_number = try_and_text(
                                "variable[1].xpath('.//text()')[0]", tds)
                            # 票据类型
                            gscgInfo.bill_type = try_and_text(
                                "variable[2].xpath('.//text()')[0]", tds)
                            # 票面金额
                            gscgInfo.denomination = try_and_text(
                                "variable[3].xpath('.//text()')[0]", tds)
                            # 发布机构
                            gscgInfo.publish_authority = try_and_text(
                                "variable[4].xpath('.//text()')[0]", tds)
                            # 公告日期
                            gscgInfo.announcement_date = try_and_text(
                                "variable[5].xpath('.//text()')[0]", tds)
                            # 详情
                            text_info = try_and_text(
                                "variable[6].xpath('.//text()')[0]", tds)
                            text_info = replace_special_chars(text_info)
                            gscgInfo.detail = text_info

                            gscgInfo.txt_id = self.txt_id
                            gscgInfo.company_name = key
                            gscgInfo.mark = 0
                            gscgInfo.add_time = datetime.now()
                            gscgInfo.agency_num = self.agency_num
                            gscgInfo.agency_name = self.agency_name
                            gscgInfo.batch = self.batch

                            # TODO:
                            unique_field = [
                                'company_name', gscgInfo.company_name]  # 该模块中唯一值字段名和值
                            check_parse(gscgInfo, add_result, unique_field)

                            # 验证首页解析
                            check_result = check_all_data(
                                add_result, gscgInfo, current_class)
                            if not first_parse_data:
                                first_parse_data = gscgInfo  # 保存第一条解析的数据
                            print('check_result+++++++++======:', check_result)
                            check_first += 1
                            if check_result:
                                check_flag = 1  # 匹配到数据
                                break
                            else:
                                check_flag = 0  # 没有匹配到
                        if not check_flag:
                            # 如果首页没有匹配到，则保存首页第一条数据到标准库，并记录其中一个字段
                            print('首页没有匹配到数据》》》》》》》》》')

                            try:
                                # TODO :
                                add_result.table_field = 'bill_number'  # 保存第一各异常字段名   各模块手动添加
                                add_result.current_value = first_parse_data.bill_number  # 保存第一各异常字段值   各模块手动添加
                                add_result.different_reason = '该页信息都不匹配，请通知数据管理员'
                                add_result.risk_level, add_result.standard_version = 1, 1
                                standard_value = single_oracle_orm.query(current_class).filter_by(  # 各表不同
                                    company_name=first_parse_data.company_name).first()
                                add_result.standard_value = standard_value.bill_number if standard_value else '-'
                                single_oracle_orm.add(add_result)
                                single_oracle_orm.commit()
                            except Exception as e:
                                print('check all datas error===={}'.format(e))
                        elif check_first > 1 and check_flag:
                            # 匹配到但不是第一条，更新页面第一条到标准库
                            unique_line = single_oracle_orm.query(
                                current_class).first()
                            single_oracle_orm.delete(unique_line)
                            single_oracle_orm.add(first_parse_data)
                            single_oracle_orm.commit()
                            print(
                                '首页已匹配到数据，但不是第一条,更新为当前页第一条》》》》》》》！{}'.format(key))

                else:
                    insert_result(self.search_name, table_name, result_dict)

    # 解析：企业发展-->融资历史
    def html_parse_financeHistory(self):

        logger.debug("Parse detail info 融资历史 {}".format(self.search_name))
        table = (self.selector.xpath(
            '//div[@id="_container_rongzi"]/table'))
        flss = TycQyfzRzl()
        thead_list = [
            '序号',
            '披露日期',
            '事件日期',
            '交易金额',
            '融资轮次',
            '估值',
            '比例',
            '投资方',
            '新闻来源']
        if table:
            result_dict = check_thead(table, thead_list)
            table_name = flss.__tablename__
            print('表头核对结果为.....：', result_dict)
            if result_dict:
                # print(table_name)

                trs = table.xpath('./tbody/tr')
                if trs:

                    key = self.search_name
                    # 创建新增对象
                    add_result = CheckResult()
                    add_result.company_name = key
                    add_result.add_time = func.now()
                    add_result.table_name = 'tyc_qyfz_rzls'  # 当前表名     各表不同
                    current_class = TycQyfzRzl  # 当前模块对象名  各表不同
                    first_parse_data = None
                    check_flag = 0  # 检测首页是否有匹配到的一行数据
                    check_first = 0  # 检测首页是否有匹配到的第一行数据

                    for tr in trs:
                        insert_value = ""
                        tds = tr.xpath('./td')
                        flss.finance_date = try_and_text(
                            "variable[1].xpath('string(.)')", tds)
                        flss.event_date = try_and_text(
                            "variable[2].xpath('string(.)')", tds)
                        flss.finance_round = try_and_text(
                            "variable[4].xpath('string(.)')", tds)
                        flss.finance_value = try_and_text(
                            "variable[5].xpath('string(.)')", tds)
                        flss.finance_money = try_and_text(
                            "variable[3].xpath('string(.)')", tds)
                        flss.finance_ratio = try_and_text(
                            "variable[6].xpath('string(.)')", tds)
                        flss.finance_investor = try_and_text(
                            "','.join(variable[7].xpath('.//text()'))", tds)
                        source = try_and_text(
                            "variable[8].xpath('.//text()')[0]", tds)
                        flss.finance_source = source
                        flss.txt_id = self.txt_id
                        flss.company_name = key
                        flss.mark = 0
                        flss.add_time = func.now()
                        flss.agency_num = self.agency_num
                        flss.agency_name = self.agency_name
                        flss.batch = self.batch
                        # 解析判断
                        unique_field = [
                            'company_name', flss.company_name]  # 该模块中唯一值字段名和值  各表不同
                        check_parse(flss, add_result, unique_field)  # 解析有误判断

                        # 验证首页解析，匹配到数据返回True
                        check_result = check_all_data(
                            add_result, flss, current_class)
                        if not first_parse_data:
                            first_parse_data = copy.deepcopy(
                                flss)  # 保存第一条解析的数据
                        print('check_result+++++++++======:', check_result)
                        check_first += 1
                        if check_result:
                            check_flag = 1  # 匹配到数据
                            break
                        else:
                            check_flag = 0  # 没有匹配到
                    if not check_flag:
                        # 如果首页没有匹配到，则保存首页第一条数据到标准库，并记录其中一个字段
                        print('首页没有匹配到数据》》》》》》》》》')

                        try:
                            add_result.table_field = 'finance_date'  # 保存第一各异常字段名       各表不同
                            add_result.current_value = first_parse_data.finance_date  # 保存第一各异常字段值   各表不同
                            add_result.different_reason = '该页信息都不匹配，请通知数据管理员'
                            add_result.risk_level, add_result.standard_version = 1, 1
                            standard_value = single_oracle_orm.query(current_class).filter_by(  # 各表不同
                                company_name=first_parse_data.company_name).first()
                            add_result.standard_value = standard_value.finance_date if standard_value else '-'
                            add_result.standard_version = 1
                            single_oracle_orm.add(add_result)
                            single_oracle_orm.commit()
                        except Exception as e:
                            print('check all datas error===={}'.format(e))
                    elif check_first > 1 and check_flag:
                        # 匹配到但不是第一条，更新页面第一条到标准库
                        unique_line = single_oracle_orm.query(
                            current_class).first()
                        single_oracle_orm.delete(unique_line)
                        single_oracle_orm.add(first_parse_data)
                        single_oracle_orm.commit()
                        print(
                            '首页已匹配到数据，但不是第一条,更新为当前页第一条》》》》》》》！{}'.format(key))

            else:
                insert_result(self.search_name, table_name, result_dict)

    # 解析：企业背景--核心团队
    def html_parse_coreTeam(self, index):
        logger.debug("Parse detail info 核心团队 {}".format(self.search_name))
        flss = TycQyfzHxtd()
        if index == 1 and not isinstance(self.selector, int):
            # 分页是否解析：传入当前公司名称和当前模块对应的数据表名
            check_next_page(self.search_name, 'tyc_qyfz_hxtd')
        else:
            table = self.selector.xpath(
                '//div[@id="_container_teamMember"]/div/table')
            if table:
                thead_list = ['序号', '姓名', '职位', '简介']
                result_dict = check_thead(table, thead_list)
                print('核对结果为....{}'.format(result_dict))
                table_name = flss.__tablename__
                print('表头核对结果为.....：', result_dict)
                if result_dict:

                    trs = table[0].xpath('./tbody/tr')

                    if trs:

                        key = self.search_name
                        # 创建新增对象
                        add_result = CheckResult()
                        add_result.company_name = key
                        add_result.add_time = func.now()
                        add_result.table_name = 'tyc_qyfz_hxtd'  # 当前表名     各表不同
                        current_class = TycQyfzHxtd  # 当前模块对象名  各表不同
                        first_parse_data = None
                        check_flag = 0  # 检测首页是否有匹配到的一行数据
                        check_first = 0  # 检测首页是否有匹配到的第一行数据

                        # divs = divs[0]
                        # trs=divs[0].xpath()
                        for tr in trs:
                            insert_value = ""
                            tds = tr.xpath('./td')
                            if tds[1].xpath('.//a/text()'):
                                personName = tds[1].xpath('.//a/text()')[0]
                            else:
                                personName = tds[1].xpath('.//span/text()')[1]
                            flss.person_name = personName

                            flss.position = try_and_text(
                                "variable[2].xpath('.//text()')[0]", tds)
                            personInfo = try_and_text(
                                "variable[3].xpath('./div/div/text()')[0]", tds)

                            flss.person_info = ''.join(personInfo)
                            flss.txt_id = self.txt_id
                            flss.company_name = key
                            flss.mark = 0
                            flss.add_time = func.now()
                            flss.agency_num = self.agency_num
                            flss.agency_name = self.agency_name
                            flss.batch = self.batch
                            # 解析判断
                            unique_field = [
                                'company_name', flss.company_name]  # 该模块中唯一值字段名和值  各表不同
                            check_parse(
                                flss, add_result, unique_field)  # 解析有误判断

                            # 验证首页解析，匹配到数据返回True
                            check_result = check_all_data(
                                add_result, flss, current_class)
                            if not first_parse_data:
                                first_parse_data = copy.deepcopy(
                                    flss)  # 保存第一条解析的数据
                            print('check_result+++++++++======:', check_result)
                            check_first += 1
                            if check_result:
                                check_flag = 1  # 匹配到数据
                                break
                            else:
                                check_flag = 0  # 没有匹配到
                        if not check_flag:
                            # 如果首页没有匹配到，则保存首页第一条数据到标准库，并记录其中一个字段
                            print('首页没有匹配到数据》》》》》》》》》')
                            try:
                                add_result.table_field = 'person_name'  # 保存第一各异常字段名       各表不同
                                add_result.current_value = first_parse_data.person_name  # 保存第一各异常字段值   各表不同
                                add_result.different_reason = '该页信息都不匹配，请通知数据管理员'
                                add_result.risk_level, add_result.standard_version = 1, 1
                                standard_value = single_oracle_orm.query(current_class).filter_by(  # 各表不同
                                    company_name=first_parse_data.company_name).first()
                                add_result.standard_value = standard_value.person_name if standard_value else '-'
                                add_result.standard_version = 1
                                single_oracle_orm.add(add_result)
                                single_oracle_orm.commit()
                            except Exception as e:
                                print('check all datas error===={}'.format(e))
                        elif check_first > 1 and check_flag:
                            # 匹配到但不是第一条，更新页面第一条到标准库
                            unique_line = single_oracle_orm.query(
                                current_class).first()
                            single_oracle_orm.delete(unique_line)
                            single_oracle_orm.add(first_parse_data)
                            single_oracle_orm.commit()
                            print(
                                '首页已匹配到数据，但不是第一条,更新为当前页第一条》》》》》》》！{}'.format(key))

                else:
                    insert_result(self.search_name, table_name, result_dict)

    # 解析：企业背景--企业业务
    def html_parse_entBusiness(self, index):
        logger.debug("Parse detail info 企业业务 {}".format(self.search_name))
        flss = TycQyfzQyyw()
        if index == 1 and not isinstance(self.selector, int):
            # 分页是否解析：传入当前公司名称和当前模块对应的数据表名
            check_next_page(self.search_name, 'tyc_qyfz_qyyw')
        else:
            table = self.selector.xpath(
                '//div[@id="_container_firmProduct"]/table')
            thead_list = ['序号', '产品名称', '产品标签', '产品介绍']
            if table:
                result_dict = check_thead(table, thead_list)
                table_name = flss.__tablename__
                print('表头核对结果为.....：', result_dict)
                if result_dict:
                    # print(table_name)

                    trs = table.xpath('./tbody/tr')
                    if trs:

                        key = self.search_name
                        # 创建新增对象
                        add_result = CheckResult()
                        add_result.company_name = key
                        add_result.add_time = func.now()
                        add_result.table_name = 'tyc_qyfz_qyyw'  # 当前表名     各表不同
                        current_class = TycQyfzQyyw  # 当前模块对象名  各表不同
                        first_parse_data = None
                        check_flag = 0  # 检测首页是否有匹配到的一行数据
                        check_first = 0  # 检测首页是否有匹配到的第一行数据

                        # divs = divs[0]
                        for tr in trs:
                            tds = tr.xpath('./td')
                            insert_value = ""
                            flss.business_name = try_and_text(
                                "variable[1].xpath('.//td//text()')[-1]", tds)
                            flss.business_quale = try_and_text(
                                "variable[2].xpath('.//text()')[-1]", tds)
                            flss.business_info = try_and_text(
                                "variable[3].xpath('./div/div//text()')[0]", tds)
                            flss.txt_id = self.txt_id
                            flss.company_name = key
                            flss.mark = 0
                            flss.add_time = func.now()
                            flss.agency_num = self.agency_num
                            flss.agency_name = self.agency_name
                            flss.batch = self.batch
                            # 解析判断
                            unique_field = [
                                'company_name', flss.company_name]  # 该模块中唯一值字段名和值  各表不同
                            check_parse(
                                flss, add_result, unique_field)  # 解析有误判断

                            # 验证首页解析，匹配到数据返回True
                            check_result = check_all_data(
                                add_result, flss, current_class)
                            if not first_parse_data:
                                first_parse_data = copy.deepcopy(
                                    flss)  # 保存第一条解析的数据
                            print('check_result+++++++++======:', check_result)
                            check_first += 1
                            if check_result:
                                check_flag = 1  # 匹配到数据
                                break
                            else:
                                check_flag = 0  # 没有匹配到
                        if not check_flag:
                            # 如果首页没有匹配到，则保存首页第一条数据到标准库，并记录其中一个字段
                            print('首页没有匹配到数据》》》》》》》》》')
                            try:
                                add_result.table_field = 'business_name'  # 保存第一各异常字段名       各表不同
                                add_result.current_value = first_parse_data.business_name  # 保存第一各异常字段值   各表不同
                                add_result.different_reason = '该页信息都不匹配，请通知数据管理员'
                                add_result.risk_level, add_result.standard_version = 1, 1
                                standard_value = single_oracle_orm.query(TycQyfzQyyw).filter_by(  # 各表不同
                                    company_name=first_parse_data.company_name).first()
                                add_result.standard_value = standard_value.business_name if standard_value else '-'
                                add_result.standard_version = 1
                                single_oracle_orm.add(add_result)
                                single_oracle_orm.commit()
                            except Exception as e:
                                print('check all datas error===={}'.format(e))
                        elif check_first > 1 and check_flag:
                            # 匹配到但不是第一条，更新页面第一条到标准库
                            unique_line = single_oracle_orm.query(
                                current_class).first()
                            single_oracle_orm.delete(unique_line)
                            single_oracle_orm.add(first_parse_data)
                            single_oracle_orm.commit()
                            print(
                                '首页已匹配到数据，但不是第一条,更新为当前页第一条》》》》》》》！{}'.format(key))

                else:
                    insert_result(self.search_name, table_name, result_dict)

    # 解析：企业背景--投资事件
    def html_parse_investEvent(self, index):
        logger.debug("Parse detail info 投资事件 {}".format(self.search_name))
        flss = TycQyfzTzsj()
        if index == 1 and not isinstance(self.selector, int):
            # 分页是否解析：传入当前公司名称和当前模块对应的数据表名
            check_next_page(self.search_name, 'tyc_qyfz_tzsj')
        else:
            table = self.selector.xpath(
                '//div[@id="_container_touzi"]/table')
            thead_list = [
                '序号',
                '时间',
                '轮次',
                '金额',
                '投资方',
                '产品',
                '地区',
                '行业',
                '业务']
            if table:
                result_dict = check_thead(table, thead_list)
                table_name = flss.__tablename__
                print('表头核对结果为.....：', result_dict)
                if result_dict:
                    # print(table_name)

                    trs = table[0].xpath('./tbody/tr')
                    if trs:

                        key = self.search_name
                        # 创建新增对象
                        add_result = CheckResult()
                        add_result.company_name = key
                        add_result.add_time = func.now()
                        add_result.table_name = 'tyc_qyfz_tzsj'  # 当前表名     各表不同
                        current_class = TycQyfzTzsj  # 当前模块对象名  各表不同
                        first_parse_data = None
                        check_flag = 0  # 检测首页是否有匹配到的一行数据
                        check_first = 0  # 检测首页是否有匹配到的第一行数据

                        for tr in trs:
                            insert_value = ""
                            tds = tr.xpath('./td')
                            flss.touzi_date = try_and_text(
                                "variable[1].xpath('string(.)')", tds)
                            flss.touzi_round = try_and_text(
                                "variable[2].xpath('string(.)')", tds)
                            flss.touzi_money = try_and_text(
                                "variable[3].xpath('string(.)')", tds)
                            flss.touzi_ent = try_and_text(
                                "variable[4].xpath('string(.)')", tds)
                            flss.touzi_product = try_and_text(
                                "(variable[5].xpath('.//a/text()'))[0]", tds)
                            flss.touzi_area = try_and_text(
                                "variable[6].xpath('string(.)')", tds)
                            flss.touzi_industry = try_and_text(
                                "variable[7].xpath('string(.)')", tds)
                            flss.touzi_business = try_and_text(
                                "variable[8].xpath('string(.)')", tds)
                            flss.txt_id = self.txt_id
                            flss.company_name = key
                            flss.mark = 0
                            flss.add_time = func.now()
                            flss.agency_num = self.agency_num
                            flss.agency_name = self.agency_name
                            flss.batch = self.batch
                            # 解析判断
                            unique_field = [
                                'company_name', flss.company_name]  # 该模块中唯一值字段名和值  各表不同
                            check_parse(
                                flss, add_result, unique_field)  # 解析有误判断

                            # 验证首页解析，匹配到数据返回True
                            check_result = check_all_data(
                                add_result, flss, current_class)
                            if not first_parse_data:
                                first_parse_data = copy.deepcopy(
                                    flss)  # 保存第一条解析的数据
                            print('check_result+++++++++======:', check_result)
                            check_first += 1
                            if check_result:
                                check_flag = 1  # 匹配到数据
                                break
                            else:
                                check_flag = 0  # 没有匹配到
                        if not check_flag:
                            # 如果首页没有匹配到，则保存首页第一条数据到标准库，并记录其中一个字段
                            print('首页没有匹配到数据》》》》》》》》》')
                            try:
                                add_result.table_field = 'touzi_date'  # 保存第一各异常字段名       各表不同
                                add_result.current_value = first_parse_data.touzi_date  # 保存第一各异常字段值   各表不同
                                add_result.different_reason = '该页信息都不匹配，请通知数据管理员'
                                add_result.risk_level, add_result.standard_version = 1, 1
                                standard_value = single_oracle_orm.query(current_class).filter_by(  # 各表不同
                                    company_name=first_parse_data.company_name).first()
                                add_result.standard_value = standard_value.touzi_date if standard_value else '-'
                                add_result.standard_version = 1
                                single_oracle_orm.add(add_result)
                                single_oracle_orm.commit()
                            except Exception as e:
                                print('check all datas error===={}'.format(e))
                        elif check_first > 1 and check_flag:
                            # 匹配到但不是第一条，更新页面第一条到标准库
                            unique_line = single_oracle_orm.query(
                                current_class).first()
                            single_oracle_orm.delete(unique_line)
                            single_oracle_orm.add(first_parse_data)
                            single_oracle_orm.commit()
                            print(
                                '首页已匹配到数据，但不是第一条,更新为当前页第一条》》》》》》》！{}'.format(key))

                else:
                    insert_result(self.search_name, table_name, result_dict)

    # 解析：企业背景--竞品信息   docker cp /etc/localtime: 2 /etc/localtime
    def html_parse_jpInfo(self, index):

        logger.debug("Parse detail info 竞品信息 {}".format(self.search_name))
        flss = TycQyfzJpxx()
        if index == 1 and not isinstance(self.selector, int):
            # 分页是否解析：传入当前公司名称和当前模块对应的数据表名
            check_next_page(self.search_name, 'tyc_qyfz_jpxx')
        else:
            table = self.selector.xpath(
                '//div[@id="_container_jingpin"]/div/table')
            thead_list = ['序号', '产品', '地区', '当前融资轮次', '行业', '业务', '成立时间', '估值']
            if table:
                result_dict = check_thead(table, thead_list)
                table_name = flss.__tablename__
                print('表头核对结果为.....：', result_dict)
                if result_dict:
                    # print(table_name)

                    trs = table[0].xpath('./tbody/tr')

                    if trs:

                        key = self.search_name
                        # 创建新增对象
                        add_result = CheckResult()
                        add_result.company_name = key
                        add_result.add_time = func.now()
                        add_result.table_name = 'tyc_qyfz_jpxx'  # 当前表名     各表不同
                        current_class = TycQyfzJpxx  # 当前模块对象名  各表不同
                        first_parse_data = None
                        check_flag = 0  # 检测首页是否有匹配到的一行数据
                        check_first = 0  # 检测首页是否有匹配到的第一行数据

                        for tr in trs:
                            insert_value = ""
                            tds = tr.xpath('./td')
                            flss.jp_product = try_and_text(
                                "variable[1].xpath('.//a/text()')[0]", tds)
                            flss.jp_area = try_and_text(
                                "variable[2].xpath('.//text()')[0]", tds)
                            flss.jp_round = try_and_text(
                                "variable[3].xpath('.//text()')[0]", tds)
                            flss.jp_industry = try_and_text(
                                "variable[4].xpath('.//text()')[0]", tds)
                            flss.jp_business = try_and_text(
                                "variable[5].xpath('.//text()')[0]", tds)
                            flss.jp_date = try_and_text(
                                "variable[6].xpath('.//text()')[0]", tds)
                            flss.jp_value = try_and_text(
                                "variable[7].xpath('.//text()')[0]", tds)
                            flss.txt_id = self.txt_id
                            flss.company_name = key
                            flss.mark = 0
                            flss.add_time = func.now()
                            flss.agency_num = self.agency_num
                            flss.agency_name = self.agency_name
                            flss.batch = self.batch
                            # 解析判断
                            unique_field = [
                                'company_name', flss.company_name]  # 该模块中唯一值字段名和值  各表不同
                            check_parse(
                                flss, add_result, unique_field)  # 解析有误判断

                            # 验证首页解析，匹配到数据返回True
                            check_result = check_all_data(
                                add_result, flss, current_class)
                            if not first_parse_data:
                                first_parse_data = copy.deepcopy(
                                    flss)  # 保存第一条解析的数据
                            print('check_result+++++++++======:', check_result)
                            check_first += 1
                            if check_result:
                                check_flag = 1  # 匹配到数据
                                break
                            else:
                                check_flag = 0  # 没有匹配到
                        if not check_flag:
                            # 如果首页没有匹配到，则保存首页第一条数据到标准库，并记录其中一个字段
                            print('首页没有匹配到数据》》》》》》》》》')
                            try:
                                add_result.table_field = 'jp_product'  # 保存第一各异常字段名       各表不同
                                add_result.current_value = first_parse_data.jp_product  # 保存第一各异常字段值   各表不同
                                add_result.different_reason = '该页信息都不匹配，请通知数据管理员'
                                add_result.risk_level, add_result.standard_version = 1, 1
                                standard_value = single_oracle_orm.query(current_class).filter_by(  # 各表不同
                                    company_name=first_parse_data.company_name).first()
                                add_result.standard_value = standard_value.jp_product if standard_value else '-'
                                add_result.standard_version = 1
                                single_oracle_orm.add(add_result)
                                single_oracle_orm.commit()
                            except Exception as e:
                                print('check all datas error===={}'.format(e))
                        elif check_first > 1 and check_flag:
                            # 匹配到但不是第一条，更新页面第一条到标准库
                            unique_line = single_oracle_orm.query(
                                current_class).first()
                            single_oracle_orm.delete(unique_line)
                            single_oracle_orm.add(first_parse_data)
                            single_oracle_orm.commit()
                            print(
                                '首页已匹配到数据，但不是第一条,更新为当前页第一条》》》》》》》！{}'.format(key))

                else:
                    insert_result(self.search_name, table_name, result_dict)

    # 招聘
    def html_parse_recruitment(self, index):
        logger.debug("Parse detail info 招聘 {}".format(self.search_name))
        flss = TycJyzkZp()
        # 判断分页
        if index == 1 and not isinstance(self.selector, int):
            # 分页是否解析：传入当前公司名称和当前模块对应的数据表名
            check_next_page(self.search_name, 'tyc_jyzk_zp')
        else:
            root_div = ''
            table = self.selector.xpath(
                '//div[@id="_container_recruit"][position()=1]//table')
            thead_list = ['序号', '发布日期', '招聘职位', '月薪', '学历', '工作经验', '地区', '操作']
            if table:
                result_dict = check_thead(table, thead_list)
                table_name = flss.__tablename__
                print('表头核对结果为.....：', result_dict)
                if result_dict:
                    # print(table_name)
                    insert_result(self.search_name, table_name, result_dict)
                root_div = table
            if not root_div:
                table = self.selector.xpath(
                    '//div[@id="_container_baipin"]/table')
                thead_list = [
                    '序号',
                    '发布日期',
                    '招聘职位',
                    '月薪',
                    '学历',
                    '工作经验',
                    '地区',
                    '操作']
                if table:
                    result_dict = check_thead(table, thead_list)
                    table_name = flss.__tablename__
                    print('表头核对结果为.....：', result_dict)
                    if result_dict:
                        # print(table_name)
                        insert_result(
                            self.search_name, table_name, result_dict)
                    root_div = table[0].xpath('./tbody/tr')

            if root_div:
                # 一行是一个

                key = self.search_name
                # 创建新增对象
                add_result = CheckResult()
                add_result.company_name = key
                add_result.add_time = func.now()
                add_result.table_name = 'tyc_jyzk_zp'  # 当前表名     各表不同
                current_class = TycJyzkZp  # 当前模块对象名  各表不同
                first_parse_data = None
                check_flag = 0  # 检测首页是否有匹配到的一行数据
                check_first = 0  # 检测首页是否有匹配到的第一行数据

                # root_div = root_div[0]
                for tr in root_div:  # bodys
                    tds = tr.xpath('./td')
                    tr_hrefs = try_and_text(
                        'variable[7].xpath(".//a/@href")[0]', tds)
                    insert_value = ""
                    flss.publish_date = try_and_text(
                        "variable[1].xpath('.//text()')[0]", tds)
                    flss.recruitment_job = try_and_text(
                        "variable[2].xpath('.//text()')[0]", tds)
                    flss.salary = try_and_text(
                        "variable[3].xpath('.//text()')[0]", tds)
                    education = try_and_text(
                        "variable[4].xpath('.//text()')[0]", tds)
                    work_year = try_and_text(
                        "variable[5].xpath('.//text()')[0]", tds)
                    flss.work_city = try_and_text(
                        "variable[6].xpath('.//text()')[0]", tds)

                    flss.work_year = work_year
                    flss.recruitment_numbers = '无明确人数'
                    flss.education = education
                    href = tr_hrefs

                    # 新增 详情 brand
                    text_info = 'NA'
                    try:
                        text_info_key = href.split(r'/')[-1].replace('.', '_')
                        text_info = self.detail_info["_container_baipin"][text_info_key]
                    except BaseException:
                        text_info = '解析出错'
                    flss.detail_info = replace_special_chars(text_info)
                    flss.txt_id = self.txt_id
                    flss.company_name = key
                    flss.add_time = func.now()
                    flss.mark = 0
                    flss.agency_num = self.agency_num
                    flss.agency_name = self.agency_name
                    flss.batch = self.batch
                    # 解析判断
                    unique_field = [
                        'company_name',
                        flss.company_name]  # 该模块中唯一值字段名和值  各表不同
                    check_parse(flss, add_result, unique_field)  # 解析有误判断

                    # 验证首页解析，匹配到数据返回True
                    check_result = check_all_data(
                        add_result, flss, current_class)
                    if not first_parse_data:
                        first_parse_data = copy.deepcopy(flss)  # 保存第一条解析的数据
                    print('check_result+++++++++======:', check_result)
                    check_first += 1
                    if check_result:
                        check_flag = 1  # 匹配到数据
                        break
                    else:
                        check_flag = 0  # 没有匹配到
                if not check_flag:
                    # 如果首页没有匹配到，则保存首页第一条数据到标准库，并记录其中一个字段
                    print('首页没有匹配到数据》》》》》》》》》')

                    try:
                        add_result.table_field = 'recruitment_job'  # 保存第一各异常字段名       各表不同
                        add_result.current_value = first_parse_data.recruitment_job  # 保存第一各异常字段值   各表不同
                        add_result.different_reason = '该页信息都不匹配，请通知数据管理员'
                        add_result.risk_level, add_result.standard_version = 1, 1
                        standard_value = single_oracle_orm.query(current_class).filter_by(  # 各表不同
                            company_name=first_parse_data.company_name).first()
                        add_result.standard_value = standard_value.recruitment_job if standard_value else '-'
                        add_result.standard_version = 1
                        single_oracle_orm.add(add_result)
                        single_oracle_orm.commit()
                    except Exception as e:
                        print('check all datas error===={}'.format(e))
                elif check_first > 1 and check_flag:
                    # 匹配到但不是第一条，更新页面第一条到标准库
                    unique_line = single_oracle_orm.query(
                        current_class).first()
                    single_oracle_orm.delete(unique_line)
                    single_oracle_orm.add(first_parse_data)
                    single_oracle_orm.commit()
                    print('首页已匹配到数据，但不是第一条,更新为当前页第一条》》》》》》》！{}'.format(key))

    # 解析：经营状况-->行政许可【工商局】
    def html_parse_gsj(self, index):
        logger.debug("Parse detail info 工商局 {}".format(self.search_name))
        flss = TycJyzkGsj()
        if index == 1 and not isinstance(self.selector, int):
            # 分页是否解析：传入当前公司名称和当前模块对应的数据表名
            check_next_page(self.search_name, 'tyc_jyzk_gsj')
        else:
            table = self.selector.xpath(
                '//div[@id="_container_licensing"]/table')
            thead_list = [
                '序号',
                '许可文书编号',
                '许可文件名称',
                '有效期自',
                '有效期至',
                '许可机关',
                '许可内容']
            if table:
                result_dict = check_thead(table, thead_list)
                table_name = flss.__tablename__
                print('表头核对结果为.....：', result_dict)
                if result_dict:
                    # print(table_name)

                    trs = table[0].xpath('./tbody/tr')
                    if trs:

                        key = self.search_name
                        # 创建新增对象
                        add_result = CheckResult()
                        add_result.company_name = key
                        add_result.add_time = func.now()
                        add_result.table_name = 'tyc_jyzk_gsj'  # 当前表名     各表不同
                        current_class = TycJyzkGsj  # 当前模块对象名  各表不同
                        first_parse_data = None
                        check_flag = 0  # 检测首页是否有匹配到的一行数据
                        check_first = 0  # 检测首页是否有匹配到的第一行数据

                        for tr in trs:
                            insert_value = ""
                            tds = tr.xpath('./td')
                            # 许可书文编号
                            flss.license_documet_num = try_and_text(
                                "variable[1].xpath('./text()')[0]", tds)
                            # 许可文件名称
                            flss.license_document_name = try_and_text(
                                "variable[2].xpath('./text()')[0]", tds)
                            # 有效期自
                            flss.validity_begin = try_and_text(
                                "variable[3].xpath('./text()')[0]", tds)
                            # 有效期至
                            flss.validity_end = try_and_text(
                                "variable[4].xpath('./text()')[0]", tds)
                            # 许可机关
                            flss.license_authority = try_and_text(
                                "variable[5].xpath('./text()')[0]", tds)
                            # 许可内容
                            flss.license_content = try_and_text(
                                "variable[6].xpath('./text()')[0]", tds)

                            flss.txt_id = self.txt_id
                            flss.company_name = key
                            flss.mark = 0
                            flss.add_time = datetime.now()
                            flss.agency_num = self.agency_num
                            flss.agency_name = self.agency_name
                            flss.batch = self.batch
                            # 解析判断
                            unique_field = [
                                'company_name', flss.company_name]  # 该模块中唯一值字段名和值  各表不同
                            check_parse(
                                flss, add_result, unique_field)  # 解析有误判断

                            # 验证首页解析，匹配到数据返回True
                            check_result = check_all_data(
                                add_result, flss, current_class)
                            if not first_parse_data:
                                first_parse_data = copy.deepcopy(
                                    flss)  # 保存第一条解析的数据
                            print('check_result+++++++++======:', check_result)
                            check_first += 1
                            if check_result:
                                check_flag = 1  # 匹配到数据
                                break
                            else:
                                check_flag = 0  # 没有匹配到
                        if not check_flag:
                            # 如果首页没有匹配到，则保存首页第一条数据到标准库，并记录其中一个字段
                            print('首页没有匹配到数据》》》》》》》》》')
                            try:
                                add_result.table_field = 'license_documet_num'  # 保存第一各异常字段名       各表不同
                                add_result.current_value = first_parse_data.license_documet_num  # 保存第一各异常字段值   各表不同
                                add_result.different_reason = '该页信息都不匹配，请通知数据管理员'
                                add_result.risk_level, add_result.standard_version = 1, 1
                                standard_value = single_oracle_orm.query(current_class).filter_by(  # 各表不同
                                    company_name=first_parse_data.company_name).first()
                                add_result.standard_value = standard_value.license_documet_num if standard_value else '-'
                                add_result.standard_version = 1
                                single_oracle_orm.add(add_result)
                                single_oracle_orm.commit()
                            except Exception as e:
                                print('check all datas error===={}'.format(e))
                        elif check_first > 1 and check_flag:
                            # 匹配到但不是第一条，更新页面第一条到标准库
                            unique_line = single_oracle_orm.query(
                                current_class).first()
                            single_oracle_orm.delete(unique_line)
                            single_oracle_orm.add(first_parse_data)
                            single_oracle_orm.commit()
                            print(
                                '首页已匹配到数据，但不是第一条,更新为当前页第一条》》》》》》》！{}'.format(key))

                else:
                    insert_result(self.search_name, table_name, result_dict)

    # 解析：经营状况-->行政许可【信用中国】
    def html_parse_xyzg(self, index):
        logger.debug("Parse detail info 信用中国 {}".format(self.search_name))
        flss = TycJyzkXyzg()
        if index == 1 and not isinstance(self.selector, int):
            # 分页是否解析：传入当前公司名称和当前模块对应的数据表名
            check_next_page(self.search_name, 'tyc_jyzk_xyzg')
        else:
            table = self.selector.xpath(
                '//div[@id="_container_licensingXyzg"]//table')
            thead_list = ['序号', '行政许可文书号', '许可决定机关', '许可决定日期', '操作']
            if table:
                result_dict = check_thead(table, thead_list)
                table_name = flss.__tablename__
                print('表头核对结果为.....：', result_dict)
                if result_dict:
                    # print(table_name)

                    trs = table[0].xpath('./tbody/tr')
                    if trs:

                        key = self.search_name
                        # 创建新增对象
                        add_result = CheckResult()
                        add_result.company_name = key
                        add_result.add_time = func.now()
                        add_result.table_name = 'tyc_jyzk_xyzg'  # 当前表名     各表不同
                        current_class = TycJyzkXyzg  # 当前模块对象名  各表不同
                        first_parse_data = None
                        check_flag = 0  # 检测首页是否有匹配到的一行数据
                        check_first = 0  # 检测首页是否有匹配到的第一行数据

                        for tr in trs:
                            insert_value = ""
                            tds = tr.xpath('./td')
                            # 行政许可文书号
                            flss.license_documet_num = try_and_text(
                                "variable[1].xpath('.//text()')[0]", tds)
                            # 许可决定机关
                            flss.license_authority = try_and_text(
                                "variable[2].xpath('.//text()')[0]", tds)
                            # 许可决定日期
                            flss.license_date = try_and_text(
                                "variable[3].xpath( './/text()')[0]", tds)
                            # 详情
                            text_info = try_and_text(
                                "variable[4].xpath('.//script/text()')[0]", tds)
                            text_info = replace_special_chars(text_info)
                            flss.detail = text_info

                            flss.txt_id = self.txt_id
                            flss.company_name = key
                            flss.mark = 0
                            flss.add_time = datetime.now()
                            flss.agency_num = self.agency_num
                            flss.agency_name = self.agency_name
                            flss.batch = self.batch

                            # 解析判断
                            unique_field = [
                                'company_name', flss.company_name]  # 该模块中唯一值字段名和值  各表不同
                            check_parse(
                                flss, add_result, unique_field)  # 解析有误判断

                            # 验证首页解析，匹配到数据返回True
                            check_result = check_all_data(
                                add_result, flss, current_class)
                            if not first_parse_data:
                                first_parse_data = copy.deepcopy(
                                    flss)  # 保存第一条解析的数据
                            print('check_result+++++++++======:', check_result)
                            check_first += 1
                            if check_result:
                                check_flag = 1  # 匹配到数据
                                break
                            else:
                                check_flag = 0  # 没有匹配到
                        if not check_flag:
                            # 如果首页没有匹配到，则保存首页第一条数据到标准库，并记录其中一个字段
                            print('首页没有匹配到数据》》》》》》》》》')

                            try:
                                add_result.table_field = 'license_documet_num'  # 保存第一各异常字段名       各表不同
                                add_result.current_value = first_parse_data.license_documet_num  # 保存第一各异常字段值   各表不同
                                add_result.different_reason = '该页信息都不匹配，请通知数据管理员'
                                add_result.risk_level, add_result.standard_version = 1, 1
                                standard_value = single_oracle_orm.query(current_class).filter_by(  # 各表不同
                                    company_name=first_parse_data.company_name).first()
                                add_result.standard_value = standard_value.license_documet_num if standard_value else '-'
                                add_result.standard_version = 1
                                single_oracle_orm.add(add_result)
                                single_oracle_orm.commit()
                            except Exception as e:
                                print('check all datas error===={}'.format(e))
                        elif check_first > 1 and check_flag:
                            # 匹配到但不是第一条，更新页面第一条到标准库
                            unique_line = single_oracle_orm.query(
                                current_class).first()
                            single_oracle_orm.delete(unique_line)
                            single_oracle_orm.add(first_parse_data)
                            single_oracle_orm.commit()
                            print(
                                '首页已匹配到数据，但不是第一条,更新为当前页第一条》》》》》》》！{}'.format(key))

                else:
                    insert_result(self.search_name, table_name, result_dict)

    # 税务评级
    def html_parse_tax(self, index):
        logger.debug("Parse detail info 税务评级{}".format(self.search_name))
        flss = TycJyzkSwpj()
        if index == 1 and not isinstance(self.selector, int):
            # 分页是否解析：传入当前公司名称和当前模块对应的数据表名
            check_next_page(self.search_name, 'tyc_jyzk_swpj')
        else:
            # 获得税务评级大标签
            table = self.selector.xpath(
                '//div[@id="_container_taxcredit"][position()=1]/table')
            thead_list = ['序号', '评价年度', '纳税人信用级别', '类型', '纳税人识别号', '评价单位']
            if table:
                result_dict = check_thead(table, thead_list)
                table_name = flss.__tablename__
                print('表头核对结果为.....：', result_dict)
                if result_dict:
                    # print(table_name)

                    root_div = table
                    if root_div:

                        key = self.search_name
                        root_div = root_div[0]
                        # 创建新增对象
                        add_result = CheckResult()
                        add_result.company_name = key
                        add_result.add_time = func.now()
                        add_result.table_name = 'tyc_jyzk_swpj'  # 当前表名     各表不同
                        current_class = TycJyzkSwpj  # 当前模块对象名  各表不同
                        first_parse_data = None
                        check_flag = 0  # 检测首页是否有匹配到的一行数据
                        check_first = 0  # 检测首页是否有匹配到的第一行数据
                        # 一行是一个tr
                        trs = root_div.xpath("./tbody/tr")

                        for tr in trs:
                            insert_value = ""
                            tds = tr.xpath("td")
                            flss.year = try_and_text(
                                "variable[1].xpath('./text()')[0]", tds)
                            flss.tax_rating = try_and_text(
                                "variable[2].xpath('./text()')[0]", tds)
                            flss.tax_type = try_and_text(
                                "variable[3].xpath('./text()')[0]", tds)
                            flss.tax_identification_number = try_and_text(
                                "variable[4].xpath('./text()')[0]", tds)
                            flss.evaluate_department = try_and_text(
                                "variable[5].xpath('./text()')[0]", tds)
                            flss.txt_id = self.txt_id
                            flss.company_name = key
                            flss.add_time = func.now()
                            flss.mark = 0
                            flss.agency_num = self.agency_num
                            flss.agency_name = self.agency_name
                            flss.batch = self.batch
                            # 解析判断
                            unique_field = [
                                'company_name', flss.company_name]  # 该模块中唯一值字段名和值  各表不同
                            check_parse(
                                flss, add_result, unique_field)  # 解析有误判断

                            # 验证首页解析，匹配到数据返回True
                            check_result = check_all_data(
                                add_result, flss, current_class)
                            if not first_parse_data:
                                first_parse_data = copy.deepcopy(
                                    flss)  # 保存第一条解析的数据
                            print('check_result+++++++++======:', check_result)
                            check_first += 1
                            if check_result:
                                check_flag = 1  # 匹配到数据
                                break
                            else:
                                check_flag = 0  # 没有匹配到
                        if not check_flag:
                            # 如果首页没有匹配到，则保存首页第一条数据到标准库，并记录其中一个字段
                            print('首页没有匹配到数据》》》》》》》》》')
                            try:
                                add_result.table_field = 'year'  # 保存第一各异常字段名       各表不同
                                add_result.current_value = first_parse_data.year  # 保存第一各异常字段值   各表不同
                                add_result.different_reason = '该页信息都不匹配，请通知数据管理员'
                                add_result.risk_level, add_result.standard_version = 1, 1
                                standard_value = single_oracle_orm.query(current_class).filter_by(  # 各表不同
                                    company_name=first_parse_data.company_name).first()
                                add_result.standard_value = standard_value.year if standard_value else '-'
                                add_result.standard_version = 1
                                single_oracle_orm.add(add_result)
                                single_oracle_orm.commit()
                            except Exception as e:
                                print('check all datas error===={}'.format(e))
                        elif check_first > 1 and check_flag:
                            # 匹配到但不是第一条，更新页面第一条到标准库
                            unique_line = single_oracle_orm.query(
                                current_class).first()
                            single_oracle_orm.delete(unique_line)
                            single_oracle_orm.add(first_parse_data)
                            single_oracle_orm.commit()
                            print(
                                '首页已匹配到数据，但不是第一条,更新为当前页第一条》》》》》》》！{}'.format(key))

                else:
                    insert_result(self.search_name, table_name, result_dict)

    # 抽查检查
    def html_parse_check(self, index):
        logger.debug("Parse detail info 抽查检查 {}".format(self.search_name))
        flss = TycJyzkCcjc()
        if index == 1 and not isinstance(self.selector, int):
            # 分页是否解析：传入当前公司名称和当前模块对应的数据表名
            check_next_page(self.search_name, 'tyc_jyzk_ccjc')
        else:
            # 获得抽查检查大标签
            table = self.selector.xpath(
                '//div[@id="_container_check"]//table')
            thead_list = ['序号', '日期', '类型', '结果', '检查实施机关']
            if table:
                result_dict = check_thead(table, thead_list)
                table_name = flss.__tablename__
                print('表头核对结果为.....：', result_dict)
                if result_dict:
                    # print(table_name)

                    root_div = table.xpath('./tbody/tr')
                    if root_div:

                        key = self.search_name
                        # 创建新增对象
                        add_result = CheckResult()
                        add_result.company_name = key
                        add_result.add_time = func.now()
                        add_result.table_name = 'tyc_jyzk_ccjc'  # 当前表名     各表不同
                        current_class = TycJyzkCcjc  # 当前模块对象名  各表不同
                        first_parse_data = None
                        check_flag = 0  # 检测首页是否有匹配到的一行数据
                        check_first = 0  # 检测首页是否有匹配到的第一行数据
                        # 一行是一个tr
                        #
                        for tr in root_div:
                            insert_value = ""
                            tds = tr.xpath("./td")
                            flss.check_date = try_and_text(
                                "variable[1].xpath('.//text()')[0]", tds)
                            flss.type = try_and_text(
                                "variable[2].xpath('.//text()')[0]", tds)
                            flss.result = try_and_text(
                                "variable[3].xpath('.//text()')[0]", tds)
                            flss.check_department = try_and_text(
                                "variable[4].xpath('.//text()')[0]", tds)
                            flss.txt_id = self.txt_id
                            flss.company_name = key
                            flss.add_time = func.now()
                            flss.mark = 0
                            flss.agency_num = self.agency_num
                            flss.agency_name = self.agency_name
                            flss.batch = self.batch
                            # 解析判断
                            unique_field = [
                                'company_name', flss.company_name]  # 该模块中唯一值字段名和值  各表不同
                            check_parse(
                                flss, add_result, unique_field)  # 解析有误判断

                            # 验证首页解析，匹配到数据返回True
                            check_result = check_all_data(
                                add_result, flss, current_class)
                            if not first_parse_data:
                                first_parse_data = copy.deepcopy(
                                    flss)  # 保存第一条解析的数据
                            print('check_result+++++++++======:', check_result)
                            check_first += 1
                            if check_result:
                                check_flag = 1  # 匹配到数据
                                break
                            else:
                                check_flag = 0  # 没有匹配到
                        if not check_flag:
                            # 如果首页没有匹配到，则保存首页第一条数据到标准库，并记录其中一个字段
                            print('首页没有匹配到数据》》》》》》》》》')

                            try:
                                add_result.table_field = 'check_date'  # 保存第一各异常字段名       各表不同
                                add_result.current_value = first_parse_data.check_date  # 保存第一各异常字段值   各表不同
                                add_result.different_reason = '该页信息都不匹配，请通知数据管理员'
                                add_result.risk_level, add_result.standard_version = 1, 1
                                standard_value = single_oracle_orm.query(current_class).filter_by(  # 各表不同
                                    company_name=first_parse_data.company_name).first()
                                add_result.standard_value = standard_value.check_date if standard_value else '-'
                                add_result.standard_version = 1
                                single_oracle_orm.add(add_result)
                                single_oracle_orm.commit()
                            except Exception as e:
                                print('check all datas error===={}'.format(e))
                        elif check_first > 1 and check_flag:
                            # 匹配到但不是第一条，更新页面第一条到标准库
                            unique_line = single_oracle_orm.query(
                                current_class).first()
                            single_oracle_orm.delete(unique_line)
                            single_oracle_orm.add(first_parse_data)
                            single_oracle_orm.commit()
                            print(
                                '首页已匹配到数据，但不是第一条,更新为当前页第一条》》》》》》》！{}'.format(key))

                else:
                    insert_result(self.search_name, table_name, result_dict)

    # 解析：经营状况--资质证书
    def html_parse_certificateInfo(self, index):
        key = self.search_name
        logger.debug("Parse detail info 资质证书 {}".format(self.search_name))
        flss = TycJyzkZzz()
        if index == 1 and not isinstance(self.selector, int):
            # 分页是否解析：传入当前公司名称和当前模块对应的数据表名
            check_next_page(self.search_name, 'tyc_jyzk_zzzs')
        else:

            table = self.selector.xpath(
                '//div[@id="_container_certificate"][position()=1]//table[position()=1]')
            thead_list = ['序号', '证书类型', '证书编号', '发证日期', '截止日期']
            if table:
                result_dict = check_thead(table, thead_list)
                table_name = flss.__tablename__
                print('表头核对结果为.....：', result_dict)
                # print(table_name)
                if result_dict:

                    trs = table[0].xpath('./tbody/tr')
                    if trs:

                        # 创建新增对象
                        add_result = CheckResult()
                        add_result.company_name = key
                        add_result.add_time = func.now()
                        add_result.table_name = 'tyc_jyzk_zzzs'  # 当前表名     各表不同
                        current_class = TycJyzkZzz  # 当前模块对象名  各表不同
                        first_parse_data = None
                        check_flag = 0  # 检测首页是否有匹配到的一行数据
                        check_first = 0  # 检测首页是否有匹配到的第一行数据
                        for tr in trs:
                            insert_value = ""
                            tds = tr.xpath('./td')
                            flss.certificate_type = try_and_text(
                                "variable[1].xpath('./span/text()')[0]", tds)
                            flss.certificate_num = try_and_text(
                                "variable[2].xpath('./span/text()')[0]", tds)
                            flss.send_date = try_and_text(
                                "variable[3].xpath('./span/text()')[0]", tds)
                            flss.off_date = try_and_text(
                                "variable[4].xpath('./span/text()')[0]", tds)
                            # certificateInfo.deviceNum = tds[4].xpath('string(.)')
                            # certificateInfo.permitNum = tds[5].xpath('string(.)')
                            # 新增 证书详情
                            href = try_and_text(
                                "variable[1].xpath('./span/@onclick')[0]", tds)
                            res = re.search(
                                r"certificatePopup\('(.*?)'\)", href).groups(1)
                            href = res[0]
                            text_info = 'NA'
                            try:
                                text_info = self.detail_info["_container_certificate"][href]
                            except BaseException:
                                pass
                                flss.detail = replace_special_chars(text_info)
                            flss.txt_id = self.txt_id
                            flss.company_name = key
                            flss.mark = 0
                            flss.add_time = func.now()
                            flss.agency_num = self.agency_num
                            flss.agency_name = self.agency_name
                            flss.batch = self.batch
                            # 解析判断
                            unique_field = [
                                'company_name', flss.company_name]  # 该模块中唯一值字段名和值  各表不同
                            check_parse(
                                flss, add_result, unique_field)  # 解析有误判断

                            # 验证首页解析，匹配到数据返回True
                            check_result = check_all_data(
                                add_result, flss, current_class)
                            if not first_parse_data:
                                first_parse_data = copy.deepcopy(
                                    flss)  # 保存第一条解析的数据
                            print('check_result+++++++++======:', check_result)
                            check_first += 1
                            if check_result:
                                check_flag = 1  # 匹配到数据
                                break
                            else:
                                check_flag = 0  # 没有匹配到
                        if not check_flag:
                            # 如果首页没有匹配到，则保存首页第一条数据到标准库，并记录其中一个字段
                            print('首页没有匹配到数据》》》》》》》》》')
                            try:
                                add_result.table_field = 'certificate_type'  # 保存第一各异常字段名       各表不同
                                add_result.current_value = first_parse_data.certificate_type  # 保存第一各异常字段值   各表不同
                                add_result.different_reason = '该页信息都不匹配，请通知数据管理员'
                                add_result.risk_level, add_result.standard_version = 1, 1
                                standard_value = single_oracle_orm.query(current_class).filter_by(  # 各表不同
                                    company_name=first_parse_data.company_name).first()
                                add_result.standard_value = standard_value.certificate_type if standard_value else '-'
                                add_result.standard_version = 1
                                single_oracle_orm.add(add_result)
                                single_oracle_orm.commit()
                            except Exception as e:
                                print('check all datas error===={}'.format(e))
                        elif check_first > 1 and check_flag:
                            # 匹配到但不是第一条，更新页面第一条到标准库
                            unique_line = single_oracle_orm.query(
                                current_class).first()
                            single_oracle_orm.delete(unique_line)
                            single_oracle_orm.add(first_parse_data)
                            single_oracle_orm.commit()
                            print(
                                '首页已匹配到数据，但不是第一条,更新为当前页第一条》》》》》》》！{}'.format(key))

                else:
                    insert_result(self.search_name, table_name, result_dict)

    # 招投标
    def html_parse_bidding(self, index):
        logger.debug("Parse detail info 招投标{}".format(self.search_name))
        flss = TycJyzkZtb()
        if index == 1 and not isinstance(self.selector, int):
            # 分页是否解析：传入当前公司名称和当前模块对应的数据表名
            check_next_page(self.search_name, 'tyc_jyzk_ztb')
        else:
            # 获得招投标大标签
            table = self.selector.xpath(
                '//div[@id="_container_bid"][position()=1]/table')
            thead_list = ['序号', '发布日期', '标题', '采购人']
            if table:
                result_dict = check_thead(table, thead_list)
                table_name = flss.__tablename__
                print('表头核对结果为.....：', result_dict)
                if result_dict:
                    # print(table_name)

                    root_div = table
                    if root_div:

                        key = self.search_name
                        # 一行是一个tr
                        root_div = root_div[0]
                        trs = root_div.xpath("./tbody/tr")
                        # 创建新增对象
                        add_result = CheckResult()
                        add_result.company_name = key
                        add_result.add_time = func.now()
                        add_result.table_name = 'tyc_jyzk_ztb'  # 当前表名     各表不同
                        current_class = TycJyzkZtb  # 当前模块对象名  各表不同
                        first_parse_data = None
                        check_flag = 0  # 检测首页是否有匹配到的一行数据
                        check_first = 0  # 检测首页是否有匹配到的第一行数据

                        for tr in trs:
                            insert_value = ""
                            tds = tr.xpath("./td")
                            flss.publish_date = try_and_text(
                                "variable[1].xpath('./text()')[0]", tds)
                            flss.title = try_and_text(
                                "variable[2].xpath('./a/text()')[0]", tds)
                            flss.title_url = try_and_text(
                                "variable[2].xpath('./a/@href')[0]", tds)
                            flss.procurement = try_and_text(
                                "variable[3].xpath('./text()')[0]", tds)
                            flss.txt_id = self.txt_id
                            flss.company_name = key
                            flss.add_time = func.now()
                            flss.mark = 0
                            flss.agency_num = self.agency_num
                            flss.agency_name = self.agency_name
                            flss.batch = self.batch
                            # 解析判断
                            unique_field = [
                                'company_name', flss.company_name]  # 该模块中唯一值字段名和值  各表不同
                            check_parse(
                                flss, add_result, unique_field)  # 解析有误判断

                            # 验证首页解析，匹配到数据返回True
                            check_result = check_all_data(
                                add_result, flss, current_class)
                            if not first_parse_data:
                                first_parse_data = copy.deepcopy(
                                    flss)  # 保存第一条解析的数据
                            print('check_result+++++++++======:', check_result)
                            check_first += 1
                            if check_result:
                                check_flag = 1  # 匹配到数据
                                break
                            else:
                                check_flag = 0  # 没有匹配到
                        if not check_flag:
                            # 如果首页没有匹配到，则保存首页第一条数据到标准库，并记录其中一个字段
                            print('首页没有匹配到数据》》》》》》》》》')

                            try:
                                add_result.table_field = 'publish_date'  # 保存第一各异常字段名       各表不同
                                add_result.current_value = first_parse_data.publish_date  # 保存第一各异常字段值   各表不同
                                add_result.different_reason = '该页信息都不匹配，请通知数据管理员'
                                add_result.risk_level, add_result.standard_version = 1, 1
                                standard_value = single_oracle_orm.query(current_class).filter_by(  # 各表不同
                                    company_name=first_parse_data.company_name).first()
                                add_result.standard_value = standard_value.publish_date if standard_value else '-'
                                add_result.standard_version = 1
                                single_oracle_orm.add(add_result)
                                single_oracle_orm.commit()
                            except Exception as e:
                                print('check all datas error===={}'.format(e))
                        elif check_first > 1 and check_flag:
                            # 匹配到但不是第一条，更新页面第一条到标准库
                            unique_line = single_oracle_orm.query(
                                current_class).first()
                            single_oracle_orm.delete(unique_line)
                            single_oracle_orm.add(first_parse_data)
                            single_oracle_orm.commit()
                            print(
                                '首页已匹配到数据，但不是第一条,更新为当前页第一条》》》》》》》！{}'.format(key))

                else:
                    insert_result(self.search_name, table_name, result_dict)

    # 产品信息
    def html_parse_product(self, index):
        logger.debug("Parse detail info 产品信息 {}".format(self.search_name))
        flss = TycJyzkCpxx()
        if index == 1 and not isinstance(self.selector, int):
            # 分页是否解析：传入当前公司名称和当前模块对应的数据表名
            check_next_page(self.search_name, 'tyc_jyzk_cpxx')
        else:
            # 获得产品信息大标签
            table = self.selector.xpath(
                '//div[@id="_container_product"]/table')
            thead_list = ['序号', '产品名称', '产品简称', '产品分类', '领域', '操作']
            if table:
                result_dict = check_thead(table, thead_list)
                table_name = flss.__tablename__
                print('表头核对结果为.....：', result_dict)
                # print(table_name)
                if result_dict:

                    root_div = table.xpath('./tbody/tr')
                    if root_div:

                        key = self.search_name
                        # 创建新增对象
                        add_result = CheckResult()
                        add_result.company_name = key
                        add_result.add_time = func.now()
                        add_result.table_name = 'tyc_jyzk_cpxx'  # 当前表名     各表不同
                        current_class = TycJyzkCpxx  # 当前模块对象名  各表不同
                        first_parse_data = None
                        check_flag = 0  # 检测首页是否有匹配到的一行数据
                        check_first = 0  # 检测首页是否有匹配到的第一行数据
                        # 一行是一个tr
                        # root_div = root_div[0]
                        # trs = root_div.xpath("./tbody/tr")

                        for tr in root_div:
                            insert_value = ""
                            tds = tr.xpath("./td")
                            flss.product_name = try_and_text(
                                "variable[1].xpath('.//span/text()')[0]", tds)
                            flss.product_referred = try_and_text(
                                "variable[2].xpath('.//text()')[0]", tds)
                            flss.product_classification = try_and_text(
                                "variable[3].xpath('.//text()')[0]", tds)
                            flss.field = try_and_text(
                                "variable[4].xpath('.//text()')[0]", tds)
                            href = try_and_text(
                                "variable[5].xpath('./a/@href')[0]", tds)
                            text_info = 'NA'
                            try:
                                text_info = self.detail_info["_container_product"][href.split(
                                    r'/')[-1]]
                                text_info = replace_special_chars(text_info)
                            except BaseException:
                                pass
                            flss.detail_info = text_info
                            flss.txt_id = self.txt_id
                            flss.company_name = key
                            flss.add_time = func.now()
                            flss.mark = 0
                            flss.agency_num = self.agency_num
                            flss.agency_name = self.agency_name
                            flss.batch = self.batch
                            # 解析判断
                            unique_field = [
                                'company_name', flss.company_name]  # 该模块中唯一值字段名和值  各表不同
                            check_parse(
                                flss, add_result, unique_field)  # 解析有误判断

                            # 验证首页解析，匹配到数据返回True
                            check_result = check_all_data(
                                add_result, flss, current_class)
                            if not first_parse_data:
                                first_parse_data = copy.deepcopy(
                                    flss)  # 保存第一条解析的数据
                            print('check_result+++++++++======:', check_result)
                            check_first += 1
                            if check_result:
                                check_flag = 1  # 匹配到数据
                                break
                            else:
                                check_flag = 0  # 没有匹配到
                        if not check_flag:
                            # 如果首页没有匹配到，则保存首页第一条数据到标准库，并记录其中一个字段
                            print('首页没有匹配到数据》》》》》》》》》')

                            try:
                                add_result.table_field = 'product_name'  # 保存第一各异常字段名       各表不同
                                add_result.current_value = first_parse_data.product_name  # 保存第一各异常字段值   各表不同
                                add_result.different_reason = '该页信息都不匹配，请通知数据管理员'
                                add_result.risk_level, add_result.standard_version = 1, 1
                                standard_value = single_oracle_orm.query(current_class).filter_by(  # 各表不同
                                    company_name=first_parse_data.company_name).first()
                                add_result.standard_value = standard_value.product_name if standard_value else '-'
                                add_result.standard_version = 1
                                single_oracle_orm.add(add_result)
                                single_oracle_orm.commit()
                            except Exception as e:
                                print('check all datas error===={}'.format(e))
                        elif check_first > 1 and check_flag:
                            # 匹配到但不是第一条，更新页面第一条到标准库
                            unique_line = single_oracle_orm.query(
                                current_class).first()
                            single_oracle_orm.delete(unique_line)
                            single_oracle_orm.add(first_parse_data)
                            single_oracle_orm.commit()
                            print(
                                '首页已匹配到数据，但不是第一条,更新为当前页第一条》》》》》》》！{}'.format(key))

                else:
                    insert_result(self.search_name, table_name, result_dict)

    # 微信公众号解析
    def html_parse_entWechat(self, index):
        logger.debug("Parse detail info 微信公众号 {}".format(self.search_name))
        flss = TycJyzkWxgzh()
        if index:
            # 分页是否解析：传入当前公司名称和当前模块对应的数据表名
            check_next_page(self.search_name, 'tyc_jyzk_wxgzh')
        else:
            table = self.selector.xpath('//div[@id="_container_wechat"]/table')
            thead_list = ['序号', '微信公众号', '微信号', '二维码', '功能介绍', '操作']
            if table:
                result_dict = check_thead(table, thead_list)
                table_name = flss.__tablename__
                print('表头核对结果为.....：', result_dict)
                # print(table_name)
                if result_dict:

                    trs = table[0].xpath('./tbody/tr')
                    if trs:

                        key = self.search_name
                        # 创建新增对象
                        add_result = CheckResult()
                        add_result.company_name = key
                        add_result.add_time = func.now()
                        add_result.table_name = 'tyc_jyzk_wxgzh'  # 当前表名     各表不同
                        current_class = TycJyzkWxgzh  # 当前模块对象名  各表不同
                        first_parse_data = None
                        check_flag = 0  # 检测首页是否有匹配到的一行数据
                        check_first = 0  # 检测首页是否有匹配到的第一行数据

                        for tr in trs:
                            insert_value = ""
                            flss.mp_name = try_and_text(
                                "variable.xpath('./td')[1].xpath('.//span/text()')[1]", tr)
                            flss.mp_number = try_and_text(
                                "variable.xpath('./td')[2].xpath('./span/text()')[0]", tr)
                            flss.mp_info = try_and_text(
                                "variable.xpath('./td')[4].xpath('./div/div/text()')[0]", tr)
                            detail = try_and_text(
                                "variable.xpath('./td')[5].xpath('./script/text()')[0]", tr)  # 新增
                            flss.detail = detail.replace(
                                r'\u002F', '/')  # 0614修改
                            flss.txt_id = self.txt_id
                            flss.company_name = key
                            flss.mark = 0
                            flss.add_time = func.now()
                            flss.agency_num = self.agency_num
                            flss.agency_name = self.agency_name
                            flss.batch = self.batch
                            # 解析判断
                            unique_field = [
                                'company_name', flss.company_name]  # 该模块中唯一值字段名和值  各表不同
                            check_parse(
                                flss, add_result, unique_field)  # 解析有误判断

                            # 验证首页解析，匹配到数据返回True
                            check_result = check_all_data(
                                add_result, flss, current_class)
                            if not first_parse_data:
                                first_parse_data = copy.deepcopy(
                                    flss)  # 保存第一条解析的数据
                            print('check_result+++++++++======:', check_result)
                            check_first += 1
                            if check_result:
                                check_flag = 1  # 匹配到数据
                                break
                            else:
                                check_flag = 0  # 没有匹配到
                        if not check_flag:
                            # 如果首页没有匹配到，则保存首页第一条数据到标准库，并记录其中一个字段
                            print('首页没有匹配到数据》》》》》》》》》')
                            try:
                                add_result.table_field = 'mp_name'  # 保存第一各异常字段名       各表不同
                                add_result.current_value = first_parse_data.mp_name  # 保存第一各异常字段值   各表不同
                                add_result.different_reason = '该页信息都不匹配，请通知数据管理员'
                                add_result.risk_level, add_result.standard_version = 1, 1
                                standard_value = single_oracle_orm.query(current_class).filter_by(  # 各表不同
                                    company_name=first_parse_data.company_name).first()
                                add_result.standard_value = standard_value.mp_name if standard_value else '-'
                                add_result.standard_version = 1
                                single_oracle_orm.add(add_result)
                                single_oracle_orm.commit()
                            except Exception as e:
                                print('check all datas error===={}'.format(e))
                        elif check_first > 1 and check_flag:
                            # 匹配到但不是第一条，更新页面第一条到标准库
                            unique_line = single_oracle_orm.query(
                                current_class).first()
                            single_oracle_orm.delete(unique_line)
                            single_oracle_orm.add(first_parse_data)
                            single_oracle_orm.commit()
                            print(
                                '首页已匹配到数据，但不是第一条,更新为当前页第一条》》》》》》》！{}'.format(key))

                else:
                    insert_result(self.search_name, table_name, result_dict)

    # 进出口信用
    def html_parse_outputxy(self):
        logger.debug("Parse detail info 进出口信用 {}".format(self.search_name))
        flss = TycJyzkJckxy()
        # 获得大标签
        table = self.selector.xpath(
            '//div[@id="_container_importAndExport"]//table')
        thead_list = ['序号', '注册海关', '行业种类', '经营类别', '注册日期', '操作']
        if table:
            result_dict = check_thead(table, thead_list)
            table_name = flss.__tablename__
            print('表头核对结果为.....：', result_dict)
            # print(table_name)
            if result_dict:
                insert_result(self.search_name, table_name, result_dict)
                root_div = table[0].xpath('./tbody/tr')
                if root_div:

                    key = self.search_name
                    # 一行是一个tr
                    # 创建新增对象
                    add_result = CheckResult()
                    add_result.company_name = key
                    add_result.add_time = func.now()
                    add_result.table_name = 'tyc_jyzk_jckxy'  # 当前表名     各表不同
                    current_class = TycJyzkJckxy  # 当前模块对象名  各表不同
                    first_parse_data = None
                    check_flag = 0  # 检测首页是否有匹配到的一行数据
                    check_first = 0  # 检测首页是否有匹配到的第一行数据

                    for tr in root_div:
                        insert_value = ""
                        tds = tr.xpath("./td")
                        flss.register_customs = try_and_text(
                            "variable[1].xpath('./text()')[0]", tds)
                        flss.industry_category = try_and_text(
                            "variable[2].xpath('./text()')[0]", tds)
                        flss.manager_type = try_and_text(
                            "variable[3].xpath('./text()')[0]", tds)
                        flss.register_date = try_and_text(
                            "variable[4].xpath('./text()')[0]", tds)
                        flss.detail_info = 'NA'
                        detail_info = try_and_text(
                            "variable[5].xpath('.//script/text()')[0]", tds)
                        flss.detail_info = replace_special_chars(detail_info)
                        flss.txt_id = self.txt_id
                        flss.company_name = key
                        flss.add_time = func.now()
                        flss.mark = 0
                        flss.agency_num = self.agency_num
                        flss.agency_name = self.agency_name
                        flss.batch = self.batch
                        flss.customs_number = CURRENT_VERSION_NULL
                        # 解析判断
                        unique_field = [
                            'company_name', flss.company_name]  # 该模块中唯一值字段名和值  各表不同
                        check_parse(flss, add_result, unique_field)  # 解析有误判断

                        # 验证首页解析，匹配到数据返回True
                        check_result = check_all_data(
                            add_result, flss, current_class)
                        if not first_parse_data:
                            first_parse_data = copy.deepcopy(
                                flss)  # 保存第一条解析的数据
                        print('check_result+++++++++======:', check_result)
                        check_first += 1
                        if check_result:
                            check_flag = 1  # 匹配到数据
                            break
                        else:
                            check_flag = 0  # 没有匹配到
                    if not check_flag:
                        # 如果首页没有匹配到，则保存首页第一条数据到标准库，并记录其中一个字段
                        print('首页没有匹配到数据》》》》》》》》》')
                        try:
                            add_result.table_field = 'register_customs'  # 保存第一各异常字段名       各表不同
                            add_result.current_value = first_parse_data.register_customs  # 保存第一各异常字段值   各表不同
                            add_result.different_reason = '该页信息都不匹配，请通知数据管理员'
                            add_result.risk_level, add_result.standard_version = 1, 1
                            standard_value = single_oracle_orm.query(current_class).filter_by(  # 各表不同
                                company_name=first_parse_data.company_name).first()
                            add_result.standard_value = standard_value.register_customs if standard_value else '-'
                            add_result.standard_version = 1
                            single_oracle_orm.add(add_result)
                            single_oracle_orm.commit()
                        except Exception as e:
                            print('check all datas error===={}'.format(e))
                    elif check_first > 1 and check_flag:
                        # 匹配到但不是第一条，更新页面第一条到标准库
                        unique_line = single_oracle_orm.query(
                            current_class).first()
                        single_oracle_orm.delete(unique_line)
                        single_oracle_orm.add(first_parse_data)
                        single_oracle_orm.commit()
                        print(
                            '首页已匹配到数据，但不是第一条,更新为当前页第一条》》》》》》》！{}'.format(key))

            else:
                insert_result(self.search_name, table_name, result_dict)

    # 债券信息
    def html_parse_zhaiquan(self, index):
        logger.debug("Parse detail info 债券信息{}".format(self.search_name))
        flss = TycJyzkZqxx()
        if index == 1 and not isinstance(self.selector, int):
            # 分页是否解析：传入当前公司名称和当前模块对应的数据表名
            check_next_page(self.search_name, 'tyc_jyzk_zqxx')
        else:
            # 获得债券信息大标签
            table = self.selector.xpath('//div[@id="_container_bond"]/table')
            thead_list = ['序号', '发行日期', '债券名称', '债券代码', '债券类型', '最新评级', '操作']
            if table:
                result_dict = check_thead(table, thead_list)
                table_name = flss.__tablename__
                print('表头核对结果为.....：', result_dict)
                # print(table_name)
                if result_dict:

                    root_div = table
                    if root_div:

                        logger.debug(
                            'cccc有债券信息。。。。。。。。。。。。。。。。。{}'.format(
                                self.search_name))
                        key = self.search_name
                        # 一行是一个tr
                        root_div = root_div[0]
                        trs = root_div.xpath("./tbody/tr")
                        # 创建新增对象
                        add_result = CheckResult()
                        add_result.company_name = key
                        add_result.add_time = func.now()
                        add_result.table_name = 'tyc_jyzk_zqxx'  # 当前表名     各表不同
                        current_class = TycJyzkZqxx  # 当前模块对象名  各表不同
                        first_parse_data = None
                        check_flag = 0  # 检测首页是否有匹配到的一行数据
                        check_first = 0  # 检测首页是否有匹配到的第一行数据

                        for tr in trs:
                            insert_value = ""
                            tds = tr.xpath("./td")
                            flss.publish_date = try_and_text(
                                "variable[1].xpath('.//text()')[0]", tds)
                            flss.bond_name = try_and_text(
                                "variable[2].xpath('.//text()')[0]", tds)
                            flss.bond_code = try_and_text(
                                "variable[3].xpath('.//text()')[0]", tds)
                            flss.bond_type = try_and_text(
                                "variable[4].xpath('.//text()')[0]", tds)
                            flss.latest_rating = try_and_text(
                                "variable[5].xpath('.//text()')[0]", tds)
                            text_info = try_and_text(
                                "variable[6].xpath('.//script/text()')[0]", tds)
                            # text_info = replace_special_chars(text_info)
                            flss.text_info = text_info.replace(r'\u002F', '')
                            # tds[6].text.replace("详情 》", "").strip().replace("'", '\\"')
                            flss.txt_id = self.txt_id
                            flss.company_name = key
                            # flss.add_time = func.now()
                            flss.mark = 0
                            flss.agency_num = self.agency_num
                            flss.agency_name = self.agency_name
                            flss.batch = self.batch
                            # 解析判断
                            unique_field = [
                                'company_name', flss.company_name]  # 该模块中唯一值字段名和值  各表不同
                            check_parse(
                                flss, add_result, unique_field)  # 解析有误判断

                            # 验证首页解析，匹配到数据返回True
                            check_result = check_all_data(
                                add_result, flss, current_class)
                            if not first_parse_data:
                                first_parse_data = copy.deepcopy(
                                    flss)  # 保存第一条解析的数据
                            print('check_result+++++++++======:', check_result)
                            check_first += 1
                            if check_result:
                                check_flag = 1  # 匹配到数据
                                break
                            else:
                                check_flag = 0  # 没有匹配到
                        if not check_flag:
                            # 如果首页没有匹配到，则保存首页第一条数据到标准库，并记录其中一个字段
                            print('首页没有匹配到数据》》》》》》》》》')

                            try:
                                add_result.table_field = 'publish_date'  # 保存第一各异常字段名       各表不同
                                add_result.current_value = first_parse_data.publish_date  # 保存第一各异常字段值   各表不同
                                add_result.different_reason = '该页信息都不匹配，请通知数据管理员'
                                add_result.risk_level, add_result.standard_version = 1, 1
                                standard_value = single_oracle_orm.query(current_class).filter_by(  # 各表不同
                                    company_name=first_parse_data.company_name).first()
                                add_result.standard_value = standard_value.publish_date if standard_value else '-'
                                add_result.standard_version = 1
                                single_oracle_orm.add(add_result)
                                single_oracle_orm.commit()
                            except Exception as e:
                                print('check all datas error===={}'.format(e))
                        elif check_first > 1 and check_flag:
                            # 匹配到但不是第一条，更新页面第一条到标准库
                            unique_line = single_oracle_orm.query(
                                current_class).first()
                            single_oracle_orm.delete(unique_line)
                            single_oracle_orm.add(first_parse_data)
                            single_oracle_orm.commit()
                            print(
                                '首页已匹配到数据，但不是第一条,更新为当前页第一条》》》》》》》！{}'.format(key))

                else:
                    insert_result(self.search_name, table_name, result_dict)

    # 解析：经营状况--购地信息
    def html_parse_buyInfo(self, index):
        logger.debug("Parse detail info 购地信息 {}".format(self.search_name))
        flss = TycJyzkGdxx()
        if index == 1 and not isinstance(self.selector, int):
            # 分页是否解析：传入当前公司名称和当前模块对应的数据表名
            check_next_page(self.search_name, 'tyc_jyzk_gdxx')
        else:
            table = self.selector.xpath(
                '//div[@id="_container_purchaselandV2"]/table')
            thead_list = [
                '序号',
                '土地坐落',
                '土地用途',
                '总面积（公顷）',
                '行政区',
                '供应方式',
                '签订日期']
            if table:
                result_dict = check_thead(table, thead_list)
                table_name = flss.__tablename__
                print('表头核对结果为.....：', result_dict)
                # print(table_name)
                if result_dict:

                    trs = table[0].xpath('./tbody/tr')
                    if trs:
                        key = self.search_name
                        # 创建新增对象
                        add_result = CheckResult()
                        add_result.company_name = key
                        add_result.add_time = func.now()
                        add_result.table_name = 'tyc_jyzk_gdxx'  # 当前表名     各表不同
                        current_class = TycJyzkGdxx  # 当前模块对象名  各表不同
                        first_parse_data = None
                        check_flag = 0  # 检测首页是否有匹配到的一行数据
                        check_first = 0  # 检测首页是否有匹配到的第一行数据
                        for tr in trs:
                            insert_value = ""
                            tds = tr.xpath('./td')
                            # 签订日期
                            flss.gd_sign_date = try_and_text(
                                "variable[6].xpath('./text()')[0]", tds)
                            # 土地坐落
                            where = try_and_text(
                                "variable[1].xpath('./script/text()')[0]", tds)
                            # 土地用途
                            todo = try_and_text(
                                "variable[2].xpath('./text()')[0]", tds)
                            # 总面积（公顷）
                            gd_area = try_and_text(
                                "variable[3].xpath('./text()')[0]", tds)
                            # 行政区
                            gd_region = try_and_text(
                                "variable[4].xpath('./text()')[0]", tds)
                            # 供应方式
                            type = try_and_text(
                                "variable[5].xpath('./text()')[0]", tds)
                            flss.gd_num = CURRENT_VERSION_NULL
                            flss.gd_act_date = CURRENT_VERSION_NULL
                            flss.gd_area = str(gd_area) + '公顷'
                            flss.gd_region = gd_region
                            flss.gd_operate = CURRENT_VERSION_NULL

                            # 新增 土地坐落
                            flss.located = where
                            # 新增 土地用途
                            flss.land_use = todo
                            # 新增  供应方式
                            flss.supply_method = type
                            flss.txt_id = self.txt_id
                            flss.company_name = key
                            flss.mark = 0
                            flss.add_time = func.now()
                            flss.agency_num = self.agency_num
                            flss.agency_name = self.agency_name
                            flss.batch = self.batch

                            # 解析判断
                            unique_field = [
                                'company_name', flss.company_name]  # 该模块中唯一值字段名和值  各表不同
                            check_parse(
                                flss, add_result, unique_field)  # 解析有误判断

                            # 验证首页解析，匹配到数据返回True
                            check_result = check_all_data(
                                add_result, flss, current_class)
                            if not first_parse_data:
                                first_parse_data = copy.deepcopy(
                                    flss)  # 保存第一条解析的数据
                            print('check_result+++++++++======:', check_result)
                            check_first += 1
                            if check_result:
                                check_flag = 1  # 匹配到数据
                                break
                            else:
                                check_flag = 0  # 没有匹配到
                        if not check_flag:
                            # 如果首页没有匹配到，则保存首页第一条数据到标准库，并记录其中一个字段
                            print('首页没有匹配到数据》》》》》》》》》')

                            try:
                                add_result.table_field = 'located'  # 保存第一各异常字段名       各表不同
                                add_result.current_value = first_parse_data.located  # 保存第一各异常字段值   各表不同
                                add_result.different_reason = '该页信息都不匹配，请通知数据管理员'
                                add_result.risk_level, add_result.standard_version = 1, 1
                                standard_value = single_oracle_orm.query(TycJyzkGdxx).filter_by(  # 各表不同
                                    company_name=first_parse_data.company_name).first()
                                add_result.standard_value = standard_value.located if standard_value else '-'
                                add_result.standard_version = 1
                                single_oracle_orm.add(add_result)
                                single_oracle_orm.commit()
                            except Exception as e:
                                print('check all datas error===={}'.format(e))
                        elif check_first > 1 and check_flag:
                            # 匹配到但不是第一条，更新页面第一条到标准库
                            unique_line = single_oracle_orm.query(
                                current_class).first()
                            single_oracle_orm.delete(unique_line)
                            single_oracle_orm.add(first_parse_data)
                            single_oracle_orm.commit()
                            print(
                                '首页已匹配到数据，但不是第一条,更新为当前页第一条》》》》》》》！{}'.format(key))

                else:
                    insert_result(self.search_name, table_name, result_dict)

    # 解析：经营状况-->电信许可
    def html_parse_dxxk(self, index):
        logger.debug("Parse detail info 电信许可 {}".format(self.search_name))
        flss = TycJyzkDxxk()
        if index == 1 and not isinstance(self.selector, int):
            # 分页是否解析：传入当前公司名称和当前模块对应的数据表名
            check_next_page(self.search_name, 'tyc_jyzk_dxxk')
        else:
            table = self.selector.xpath(
                '//div[@id="_container_permission"]/table')
            thead_list = ['序号', '许可证号', '业务范围', '是否有效', '操作']
            if table:
                result_dict = check_thead(table, thead_list)
                table_name = flss.__tablename__
                print('表头核对结果为.....：', result_dict)
                # print(table_name)
                if result_dict:

                    trs = table[0].xpath('./tbody/tr')
                    if trs:

                        key = self.search_name
                        # 创建新增对象
                        add_result = CheckResult()
                        add_result.company_name = key
                        add_result.add_time = func.now()
                        add_result.table_name = 'tyc_jyzk_dxxk'  # 当前表名     各表不同
                        current_class = TycJyzkDxxk  # 当前模块对象名  各表不同
                        first_parse_data = None
                        check_flag = 0  # 检测首页是否有匹配到的一行数据
                        check_first = 0  # 检测首页是否有匹配到的第一行数据

                        for tr in trs:
                            insert_value = ""
                            tds = tr.xpath('./td')
                            # 许可证号
                            flss.license_key = try_and_text(
                                "variable[1].xpath('./text()')[0]", tds)
                            # 业务范围
                            flss.business_sphere = try_and_text(
                                "variable[2].xpath('./text()')[0]", tds)
                            # 是否有效
                            flss.available = try_and_text(
                                "variable[3].xpath('./text()')[0]", tds)
                            # 详情
                            text_info = try_and_text(
                                "variable[4].xpath('./script/text()')[0]", tds)
                            text_info = replace_special_chars(text_info)
                            flss.detail_info = text_info

                            flss.txt_id = self.txt_id
                            flss.company_name = key
                            flss.mark = 0
                            flss.add_time = datetime.now()
                            flss.agency_num = self.agency_num
                            flss.agency_name = self.agency_name
                            flss.batch = self.batch

                            # 解析判断
                            unique_field = [
                                'company_name', flss.company_name]  # 该模块中唯一值字段名和值  各表不同
                            check_parse(
                                flss, add_result, unique_field)  # 解析有误判断

                            # 验证首页解析，匹配到数据返回True
                            check_result = check_all_data(
                                add_result, flss, current_class)
                            if not first_parse_data:
                                first_parse_data = copy.deepcopy(
                                    flss)  # 保存第一条解析的数据
                            print('check_result+++++++++======:', check_result)
                            check_first += 1
                            if check_result:
                                check_flag = 1  # 匹配到数据
                                break
                            else:
                                check_flag = 0  # 没有匹配到
                        if not check_flag:
                            # 如果首页没有匹配到，则保存首页第一条数据到标准库，并记录其中一个字段
                            print('首页没有匹配到数据》》》》》》》》》')

                            try:
                                add_result.table_field = 'license_key'  # 保存第一各异常字段名       各表不同
                                add_result.current_value = first_parse_data.license_key  # 保存第一各异常字段值   各表不同
                                add_result.different_reason = '该页信息都不匹配，请通知数据管理员'
                                add_result.risk_level, add_result.standard_version = 1, 1
                                standard_value = single_oracle_orm.query(current_class).filter_by(  # 各表不同
                                    company_name=first_parse_data.company_name).first()
                                add_result.standard_value = standard_value.license_key if standard_value else '-'
                                add_result.standard_version = 1
                                single_oracle_orm.add(add_result)
                                single_oracle_orm.commit()
                            except Exception as e:
                                print('check all datas error===={}'.format(e))
                        elif check_first > 1 and check_flag:
                            # 匹配到但不是第一条，更新页面第一条到标准库
                            unique_line = single_oracle_orm.query(
                                current_class).first()
                            single_oracle_orm.delete(unique_line)
                            single_oracle_orm.add(first_parse_data)
                            single_oracle_orm.commit()
                            print(
                                '首页已匹配到数据，但不是第一条,更新为当前页第一条》》》》》》》！{}'.format(key))

                else:
                    insert_result(self.search_name, table_name, result_dict)

    # 商标信息
    def html_parse_trademark(self, index):
        logger.debug("Parse detail info 商标信息 {}".format(self.search_name))
        flss = TycZscqSbxx()
        if index == 1 and not isinstance(self.selector, int):
            # 分页是否解析：传入当前公司名称和当前模块对应的数据表名
            check_next_page(self.search_name, 'tyc_zscq_sbxx')
        else:
            # 获得商标信息大标签
            table = self.selector.xpath(
                '//div[@id= "_container_tmInfo"][position()=1]/div/table')
            thead_list = [
                '序号',
                '申请日期',
                '商标',
                '商标名称',
                '注册号',
                '国际分类',
                '商标状态',
                '操作']
            if table:
                result_dict = check_thead(table, thead_list)
                table_name = flss.__tablename__
                print('表头核对结果为.....：', result_dict)
                # print(table_name)
                if result_dict:

                    root_div = table
                    if root_div:

                        key = self.search_name
                        # 一行是一个tr

                        root_div = root_div[0]
                        trs = root_div.xpath("./tbody/tr")
                        # 创建新增对象
                        add_result = CheckResult()
                        add_result.company_name = key
                        add_result.add_time = func.now()
                        add_result.table_name = 'tyc_zscq_sbxx'  # 当前表名     各表不同
                        current_class = TycZscqSbxx  # 当前模块对象名  各表不同
                        first_parse_data = None
                        check_flag = 0  # 检测首页是否有匹配到的一行数据
                        check_first = 0  # 检测首页是否有匹配到的第一行数据

                        for tr in trs:
                            insert_value = ""
                            tds = tr.xpath("./td")
                            if tds:
                                flss.apply_date = try_and_text(
                                    "variable[1].xpath('.//text()')[0]", tds)
                                flss.trademark = try_and_text(
                                    "variable[2].xpath('.//img/@data-src')[0]", tds)
                                flss.trademark_name = try_and_text(
                                    "variable[3].xpath('.//text()')[0]", tds)
                                flss.registration_number = try_and_text(
                                    "variable[4].xpath('.//text()')[0]", tds)
                                flss.type = try_and_text(
                                    "variable[5].xpath('.//text()')[0]", tds)
                                flss.status = try_and_text(
                                    "variable[6].xpath('.//text()')[0]", tds)
                                href = try_and_text(
                                    "variable[7].xpath('./a/@href')[0]", tds)
                                # 新增 详情 brand
                                text_info = "NA"
                                try:
                                    text_info = self.detail_info["_container_tmInfo"][href.split(
                                        r'/')[-1]]
                                    text_info = replace_special_chars(
                                        text_info)
                                except BaseException:
                                    pass

                                flss.detail = text_info

                                flss.txt_id = self.txt_id
                                flss.company_name = key
                                flss.add_time = func.now()
                                flss.mark = 0
                                flss.agency_num = self.agency_num
                                flss.agency_name = self.agency_name
                                flss.batch = self.batch

                                # 解析判断
                                unique_field = [
                                    'company_name', flss.company_name]  # 该模块中唯一值字段名和值  各表不同
                                check_parse(
                                    flss, add_result, unique_field)  # 解析有误判断

                                # 验证首页解析，匹配到数据返回True
                                check_result = check_all_data(
                                    add_result, flss, current_class)
                                if not first_parse_data:
                                    first_parse_data = copy.deepcopy(
                                        flss)  # 保存第一条解析的数据
                                print(
                                    'check_result+++++++++======:', check_result)
                                check_first += 1
                                if check_result:
                                    check_flag = 1  # 匹配到数据
                                    break
                                else:
                                    check_flag = 0  # 没有匹配到
                        if not check_flag:
                            # 如果首页没有匹配到，则保存首页第一条数据到标准库，并记录其中一个字段
                            print('首页没有匹配到数据》》》》》》》》》')

                            try:
                                add_result.table_field = 'apply_date'  # 保存第一各异常字段名       各表不同
                                add_result.current_value = first_parse_data.apply_date  # 保存第一各异常字段值   各表不同
                                add_result.different_reason = '该页信息都不匹配，请通知数据管理员'
                                add_result.risk_level, add_result.standard_version = 1, 1
                                standard_value = single_oracle_orm.query(current_class).filter_by(  # 各表不同
                                    company_name=first_parse_data.company_name).first()
                                add_result.standard_value = standard_value.apply_date if standard_value else '-'
                                add_result.standard_version = 1
                                single_oracle_orm.add(add_result)
                                single_oracle_orm.commit()
                            except Exception as e:
                                print('check all datas error===={}'.format(e))
                        elif check_first > 1 and check_flag:
                            # 匹配到但不是第一条，更新页面第一条到标准库
                            unique_line = single_oracle_orm.query(
                                current_class).first()
                            single_oracle_orm.delete(unique_line)
                            single_oracle_orm.add(first_parse_data)
                            single_oracle_orm.commit()
                            print(
                                '首页已匹配到数据，但不是第一条,更新为当前页第一条》》》》》》》！{}'.format(key))

                else:
                    insert_result(self.search_name, table_name, result_dict)

    # 专利信息
    def html_parse_patent(self, index):
        logger.debug("Parse detail info 专利信息 {}".format(self.search_name))
        flss = TycZscqZl()
        if index == 1 and not isinstance(self.selector, int):
            # 分页是否解析：传入当前公司名称和当前模块对应的数据表名
            check_next_page(self.search_name, 'tyc_zscq_zl')
        else:
            # 获得专利信息大标签
            table = self.selector.xpath(
                '//div[@id="_container_patent"][position()=1]/table')
            thead_list = ['序号', '申请公布日', '专利名称', '申请号', '申请公布号', '专利类型', '操作']
            if table:
                result_dict = check_thead(table, thead_list)
                table_name = flss.__tablename__
                print('表头核对结果为.....：', result_dict)
                # print(table_name)
                if result_dict:

                    root_div = table
                    if root_div:

                        key = self.search_name
                        # 一行是一个tr
                        root_div = root_div[0]
                        trs = root_div.xpath("./tbody/tr")

                        # 创建新增对象
                        add_result = CheckResult()
                        add_result.company_name = key
                        add_result.add_time = func.now()
                        add_result.table_name = 'tyc_zscq_zl'  # 当前表名     各表不同
                        current_class = TycZscqZl  # 当前模块对象名  各表不同
                        first_parse_data = None
                        check_flag = 0  # 检测首页是否有匹配到的一行数据
                        check_first = 0  # 检测首页是否有匹配到的第一行数据

                        for tr in trs:
                            insert_value = ""
                            tds = tr.xpath("./td")
                            flss.apply_publish_date = try_and_text(
                                "variable[1].xpath('./span/text()')[0]", tds)
                            flss.patent_name = try_and_text(
                                "variable[2].xpath('./span/text()')[0]", tds)
                            flss.apply_number = try_and_text(
                                "variable[3].xpath('./span/text()')[0]", tds)
                            flss.apply_publish_number = try_and_text(
                                "variable[4].xpath('./span/text()')[0]", tds)

                            # 新增 专利类型
                            patent_type = try_and_text(
                                "variable[5].xpath('./span/text()')", tds)
                            flss.patent_type = patent_type[0] if patent_type else 'NA'

                            href = try_and_text(
                                "variable[6].xpath('./a/@href')[0]", tds)
                            # 新增 详情 brand
                            text_info = 'NA'
                            try:
                                text_info = self.detail_info["_container_patent"][href.split(
                                    r'/')[-1]]
                            except BaseException:
                                pass
                            flss.detail_info = replace_special_chars(text_info)
                            flss.txt_id = self.txt_id
                            flss.company_name = key
                            flss.add_time = func.now()
                            flss.mark = 0
                            flss.agency_num = self.agency_num
                            flss.agency_name = self.agency_name
                            flss.batch = self.batch

                            # 解析判断
                            unique_field = [
                                'company_name', flss.company_name]  # 该模块中唯一值字段名和值  各表不同
                            check_parse(
                                flss, add_result, unique_field)  # 解析有误判断

                            # 验证首页解析，匹配到数据返回True
                            check_result = check_all_data(
                                add_result, flss, current_class)
                            if not first_parse_data:
                                first_parse_data = copy.deepcopy(
                                    flss)  # 保存第一条解析的数据
                            print('check_result+++++++++======:', check_result)
                            check_first += 1
                            if check_result:
                                check_flag = 1  # 匹配到数据
                                break
                            else:
                                check_flag = 0  # 没有匹配到
                        if not check_flag:
                            # 如果首页没有匹配到，则保存首页第一条数据到标准库，并记录其中一个字段
                            print('首页没有匹配到数据》》》》》》》》》')
                            try:
                                add_result.table_field = 'apply_publish_date'  # 保存第一各异常字段名       各表不同
                                add_result.current_value = first_parse_data.apply_publish_date  # 保存第一各异常字段值   各表不同
                                add_result.different_reason = '该页信息都不匹配，请通知数据管理员'
                                add_result.risk_level, add_result.standard_version = 1, 1
                                standard_value = single_oracle_orm.query(current_class).filter_by(  # 各表不同
                                    company_name=first_parse_data.company_name).first()
                                add_result.standard_value = standard_value.apply_publish_date if standard_value else '-'
                                add_result.standard_version = 1
                                single_oracle_orm.add(add_result)
                                single_oracle_orm.commit()
                            except Exception as e:
                                print('check all datas error===={}'.format(e))

                        elif check_first > 1 and check_flag:
                            # 匹配到但不是第一条，更新页面第一条到标准库
                            unique_line = single_oracle_orm.query(
                                current_class).first()
                            single_oracle_orm.delete(unique_line)
                            single_oracle_orm.add(first_parse_data)
                            single_oracle_orm.commit()
                            print(
                                '首页已匹配到数据，但不是第一条,更新为当前页第一条》》》》》》》！{}'.format(key))

                else:
                    insert_result(self.search_name, table_name, result_dict)

    # 软件著作权
    def html_parse_copyright(self, index):
        logger.debug("Parse detail info 软件著作权 {}".format(self.search_name))
        flss = TycZscqZzq()
        if index == 1 and not isinstance(self.selector, int):
            # 分页是否解析：传入当前公司名称和当前模块对应的数据表名
            check_next_page(self.search_name, 'tyc_zscq_zzq')
        else:
            table = self.selector.xpath(
                '//div[@id="_container_copyright"][position()=1]/table')
        thead_list = ['序号', '批准日期', '软件全称', '软件简称', '登记号', '分类号', '版本号', '操作']
        if table:
            result_dict = check_thead(table, thead_list)
            table_name = flss.__tablename__
            print('表头核对结果为.....：', result_dict)
            # print(table_name)
            if result_dict:

                root_div = table

                if root_div:

                    key = self.search_name
                    # 一行是一个tr
                    root_div = root_div[0]
                    trs = root_div.xpath("./tbody/tr")

                    # 创建新增对象
                    add_result = CheckResult()
                    add_result.company_name = key
                    add_result.add_time = func.now()
                    add_result.table_name = 'tyc_zscq_zzq'  # 当前表名
                    current_class = TycZscqZzq  # 当前模块对象名
                    first_parse_data = None
                    check_flag = 0  # 检测首页是否有匹配到的一行数据
                    check_first = 0  # 检测首页是否有匹配到的第一行数据
                    for tr in trs:
                        insert_value = ""
                        tds = tr.xpath("./td")
                        flss.approval_date = try_and_text(
                            "variable[1].xpath('./span/text()')[0]", tds)
                        flss.software_name = try_and_text(
                            "variable[2].xpath('./span/text()')[0]", tds)
                        flss.software_referred = try_and_text(
                            "variable[3].xpath('./span/text()')[0]", tds)
                        flss.registration_number = try_and_text(
                            "variable[4].xpath('./span/text()')[0]", tds)
                        flss.type_number = try_and_text(
                            "variable[5].xpath('./span/text()')[0]", tds)
                        flss.version_number = try_and_text(
                            "variable[6].xpath('./span/text()')[0]", tds)
                        text_info = try_and_text(
                            "variable[7].xpath('./script/text()')[0]", tds)
                        text_info = replace_special_chars(text_info)
                        flss.detail_info = text_info

                        flss.txt_id = self.txt_id
                        flss.company_name = key
                        flss.add_time = func.now()
                        flss.mark = 0
                        flss.agency_num = self.agency_num
                        flss.agency_name = self.agency_name
                        flss.batch = self.batch

                        # 解析判断
                        unique_field = [
                            'company_name', flss.company_name]  # 该模块中唯一值字段名和值  各表不同
                        check_parse(flss, add_result, unique_field)  # 解析有误判断

                        # 验证首页解析，匹配到数据返回True
                        check_result = check_all_data(
                            add_result, flss, current_class)
                        if not first_parse_data:
                            first_parse_data = copy.deepcopy(
                                flss)  # 保存第一条解析的数据
                        print('check_result+++++++++======:', check_result)
                        check_first += 1
                        if check_result:
                            check_flag = 1  # 匹配到数据
                            break
                        else:
                            check_flag = 0  # 没有匹配到
                    if not check_flag:
                        # 如果首页没有匹配到，则保存首页第一条数据到标准库，并记录其中一个字段
                        print('首页没有匹配到数据》》》》》》》》》')
                        try:
                            add_result.table_field = 'approval_date'  # 保存第一各异常字段名       各表不同
                            add_result.current_value = first_parse_data.approval_date  # 保存第一各异常字段值   各表不同
                            add_result.different_reason = '该页信息都不匹配，请通知数据管理员'
                            add_result.risk_level, add_result.standard_version = 1, 1
                            standard_value = single_oracle_orm.query(current_class).filter_by(  # 各表不同
                                company_name=first_parse_data.company_name).first()
                            add_result.standard_value = standard_value.approval_date if standard_value else '-'
                            add_result.standard_version = 1
                            single_oracle_orm.add(add_result)
                            single_oracle_orm.commit()
                        except Exception as e:
                            print('check all datas error===={}'.format(e))

                    elif check_first > 1 and check_flag:
                        # 匹配到但不是第一条，更新页面第一条到标准库
                        unique_line = single_oracle_orm.query(
                            current_class).first()
                        single_oracle_orm.delete(unique_line)
                        single_oracle_orm.add(first_parse_data)
                        single_oracle_orm.commit()
                        print(
                            '首页已匹配到数据，但不是第一条,更新为当前页第一条》》》》》》》！{}'.format(key))

            else:
                insert_result(self.search_name, table_name, result_dict)

    # 作品著作权
    def html_parse_copyzzq(self, index):
        logger.debug("Parse detail info 作品著作权 {}".format(self.search_name))
        flss = TycZscqZpzzq()
        # 获得作品著作权大标签
        if index == 1 and not isinstance(self.selector, int):
            # 分页是否解析：传入当前公司名称和当前模块对应的数据表名
            check_next_page(self.search_name, 'tyc_zscq_zpzzq')
        else:
            table = self.selector.xpath(
                '//div[@id="_container_copyrightWorks"]/table')
            thead_list = [
                '序号',
                '作品名称',
                '登记号',
                '登记类别',
                '创作完成日期',
                '登记日期',
                '首次发布日期']
            if table:
                result_dict = check_thead(table, thead_list)
                table_name = flss.__tablename__
                print('表头核对结果为.....：', result_dict)
                # print(table_name)
                if result_dict:

                    root_div = table[0].xpath('./tbody/tr')
                    if root_div:

                        key = self.search_name
                        # root_div = root_div[0]
                        # trs = root_div.xpath(".")
                        #
                        # 创建新增对象
                        add_result = CheckResult()
                        add_result.company_name = key
                        add_result.add_time = func.now()
                        add_result.table_name = 'tyc_zscq_zpzzq'  # 当前表名
                        current_class = TycZscqZpzzq  # 当前模块对象名
                        first_parse_data = None
                        check_flag = 0  # 检测首页是否有匹配到的一行数据
                        check_first = 0  # 检测首页是否有匹配到的第一行数据

                        for tr in root_div:
                            insert_value = ""
                            # 作品名称	登记号	类别	 创作完成日期	登记日期	首次发布日期
                            tds = tr.xpath("./td")
                            flss.works_name = try_and_text(
                                "variable[1].xpath('.//text()')[0]", tds)
                            flss.register_name = try_and_text(
                                "variable[2].xpath('.//text()')[0]", tds)
                            flss.type = try_and_text(
                                "variable[3].xpath('.//text()')[0]", tds)
                            flss.create_date = try_and_text(
                                "variable[4].xpath('.//text()')[0]", tds)
                            flss.register_date = try_and_text(
                                "variable[5].xpath('.//text()')[0]", tds)
                            flss.firstpublish_date = try_and_text(
                                "variable[6].xpath('.//text()')[0]", tds)
                            flss.txt_id = self.txt_id
                            flss.company_name = key
                            flss.add_time = func.now()
                            flss.mark = 0
                            flss.agency_num = self.agency_num
                            flss.agency_name = self.agency_name
                            flss.batch = self.batch

                            # 解析判断
                            unique_field = [
                                'company_name', flss.company_name]  # 该模块中唯一值字段名和值  各表不同
                            check_parse(
                                flss, add_result, unique_field)  # 解析有误判断

                            # 验证首页解析，匹配到数据返回True
                            check_result = check_all_data(
                                add_result, flss, current_class)
                            if not first_parse_data:
                                first_parse_data = copy.deepcopy(
                                    flss)  # 保存第一条解析的数据
                            print('check_result+++++++++======:', check_result)
                            check_first += 1
                            if check_result:
                                check_flag = 1  # 匹配到数据
                                break
                            else:
                                check_flag = 0  # 没有匹配到
                        if not check_flag:
                            # 如果首页没有匹配到，则保存首页第一条数据到标准库，并记录其中一个字段
                            print('首页没有匹配到数据》》》》》》》》》')

                            try:
                                add_result.table_field = 'works_name'  # 保存第一各异常字段名       各表不同
                                add_result.current_value = first_parse_data.works_name  # 保存第一各异常字段值   各表不同
                                add_result.different_reason = '该页信息都不匹配，请通知数据管理员'
                                add_result.risk_level, add_result.standard_version = 1, 1
                                standard_value = single_oracle_orm.query(current_class).filter_by(  # 各表不同
                                    company_name=first_parse_data.company_name).first()
                                add_result.standard_value = standard_value.works_name if standard_value else '-'
                                add_result.standard_version = 1
                                single_oracle_orm.add(add_result)
                                single_oracle_orm.commit()
                            except Exception as e:
                                print('check all datas error===={}'.format(e))
                        elif check_first > 1 and check_flag:
                            # 匹配到但不是第一条，更新页面第一条到标准库
                            unique_line = single_oracle_orm.query(
                                current_class).first()
                            single_oracle_orm.delete(unique_line)
                            single_oracle_orm.add(first_parse_data)
                            single_oracle_orm.commit()
                            print(
                                '首页已匹配到数据，但不是第一条,更新为当前页第一条》》》》》》》！{}'.format(key))

                else:
                    insert_result(self.search_name, table_name, result_dict)

    # 网站备案
    def html_parse_website(self, index):
        logger.debug("Parse detail info 网站备案 {}".format(self.search_name))
        flss = TycZscqWzba()
        if index == 1 and not isinstance(self.selector, int):
            # 分页是否解析：传入当前公司名称和当前模块对应的数据表名
            check_next_page(self.search_name, 'tyc_zscq_wzba')

        else:
            # 获得网站备案大标签
            table = self.selector.xpath('//div[@id="_container_icp"]/table')
            thead_list = ['序号', '审核日期', '网站名称', '网站首页', '域名', '网站备案/许可证号']
            if table:
                result_dict = check_thead(table, thead_list)
                table_name = flss.__tablename__
                print('表头核对结果为.....：', result_dict)
                # print(table_name)
                if result_dict:

                    root_div = table
                    if root_div:

                        key = self.search_name
                        root_div = root_div[0]
                        # 一行是一个tr
                        trs = root_div.xpath("./tbody/tr")

                        # 创建新增对象
                        add_result = CheckResult()
                        add_result.company_name = key
                        add_result.add_time = func.now()
                        add_result.table_name = 'tyc_zscq_wzba'  # 当前表名     各表不同
                        current_class = TycZscqWzba  # 当前模块对象名  各表不同
                        first_parse_data = None
                        check_flag = 0  # 检测首页是否有匹配到的一行数据
                        check_first = 0  # 检测首页是否有匹配到的第一行数据

                        for tr in trs:
                            insert_value = ""
                            tds = tr.xpath('./td')
                            flss.audit_date = try_and_text(
                                "variable[1].xpath('./span/text()')[0]", tds)
                            flss.web_name = try_and_text(
                                "variable[2].xpath('./span/text()')[0]", tds)
                            flss.web_homepage = try_and_text(
                                "variable[3].xpath('.//a//text()')[0]", tds)
                            domain_name = try_and_text(
                                "variable[4].xpath('./text()')[0]", tds)
                            flss.domain_name = domain_name if domain_name else 'NA'
                            record_number = try_and_text(
                                "variable[5].xpath('./span/text()')[0]", tds)
                            flss.record_number = record_number if record_number else 'NA'
                            flss.txt_id = self.txt_id
                            flss.company_name = key
                            flss.add_time = func.now()
                            flss.mark = 0
                            flss.agency_num = self.agency_num
                            flss.agency_name = self.agency_name
                            flss.batch = self.batch

                            # 解析判断
                            unique_field = [
                                'company_name', flss.company_name]  # 该模块中唯一值字段名和值  各表不同
                            check_parse(
                                flss, add_result, unique_field)  # 解析有误判断

                            # 验证首页解析，匹配到数据返回True
                            check_result = check_all_data(
                                add_result, flss, current_class)
                            if not first_parse_data:
                                first_parse_data = copy.deepcopy(
                                    flss)  # 保存第一条解析的数据
                            print('check_result+++++++++======:', check_result)
                            check_first += 1
                            if check_result:
                                check_flag = 1  # 匹配到数据
                                break
                            else:
                                check_flag = 0  # 没有匹配到
                        if not check_flag:
                            # 如果首页没有匹配到，则保存首页第一条数据到标准库，并记录其中一个字段
                            print('首页没有匹配到数据》》》》》》》》》')
                            try:
                                add_result.table_field = 'audit_date'  # 保存第一各异常字段名   各表不同
                                add_result.current_value = first_parse_data.audit_date  # 保存第一各异常字段值   各表不同
                                add_result.different_reason = '该页信息都不匹配，请通知数据管理员'
                                add_result.risk_level, add_result.standard_version = 1, 1
                                standard_value = single_oracle_orm.query(current_class).filter_by(  # 各表不同
                                    company_name=first_parse_data.company_name).first()
                                add_result.standard_value = standard_value.audit_date if standard_value else '-'
                                add_result.standard_version = 1
                                single_oracle_orm.add(add_result)
                                single_oracle_orm.commit()
                            except Exception as e:
                                print('check all datas error===={}'.format(e))
                        elif check_first > 1 and check_flag:
                            # 匹配到但不是第一条，更新页面第一条到标准库
                            unique_line = single_oracle_orm.query(
                                current_class).first()
                            single_oracle_orm.delete(unique_line)
                            single_oracle_orm.add(first_parse_data)
                            single_oracle_orm.commit()
                            print(
                                '首页已匹配到数据，但不是第一条,更新为当前页第一条》》》》》》》！{}'.format(key))

                else:
                    insert_result(self.search_name, table_name, result_dict)

    # 企业年报
    def html_parse_nianbao(self, year):
        logger.debug("Parse detail info 企业年报 {}".format(self.search_name))

        flss = TycQybjQynb()
        # 表头信息
        table = self.selector.xpath(
            '//div[@id="nav-main-reportCount"]/../div[@class="data-content"]/div/table')
        if table:
            thead_list = ['序号', '年报', '操作']
            result_dict = check_thead(table, thead_list)
            table_name = flss.__tablename__
            print('表头核对结果为.....：', result_dict)
            # print(table_name)
            if result_dict:

                # 获得企业年报大标签
                root_div = self.selector.xpath(
                    '//div[@id="nav-main-reportCount"]/../div[@class="data-content"]/div')

                if root_div:
                    # flss = TycQybjQynb()
                    key = self.search_name
                    root_div = root_div[0]
                    # 一行是一个tr
                    all_a = root_div.xpath(
                        '//a[contains(@href,"https://www.tianyancha.com/reportContent")]')

                    # for a in all_a:
                    if all_a:
                        a = all_a[0]

                        insert_value = ""
                        ss = a.xpath("./@href")[0]
                        flss.year = ss[-4:].strip()
                        flss.detail_url = ss.strip()
                        year_selector = year[flss.year]
                        try:
                            self.html_parse_year_jbxx(year_selector, flss.year)
                        except Exception as e:
                            logger.exception(e)
                        try:
                            self.html_parse_year_wzhwdxx(
                                year_selector, flss.year)
                        except Exception as e:
                            logger.exception(e)
                        try:
                            self.html_parse_year_gdczxx(
                                year_selector, flss.year)
                        except Exception as e:
                            logger.exception(e)
                        try:
                            self.html_parse_year_zczk(year_selector, flss.year)
                        except Exception as e:
                            logger.exception(e)
                        try:
                            self.html_parse_year_dwtz(year_selector, flss.year)
                        except Exception as e:
                            logger.exception(e)

                        flss.txt_id = self.txt_id
                        flss.company_name = key
                        flss.add_time = func.now()
                        flss.mark = 0
                        flss.agency_num = self.agency_num
                        flss.agency_name = self.agency_name
                        flss.batch = self.batch
                        value_list = [
                            flss.txt_id,
                            flss.company_name,
                            flss.detail_url,
                            flss.year,
                            flss.mark,
                            flss.agency_num,
                            flss.agency_name,
                            flss.batch]
                        print(value_list)

            else:
                insert_result(self.search_name, table_name, result_dict)

    # 解析：企业背景-->最终受益人
    def html_parse_zzsyr(self, index):

        logger.debug("Parse detail info 最终受益人 {}".format(self.search_name))

        if index == 1 and not isinstance(self.selector, int):
            # # 分页是否解析：传入当前公司名称和当前模块对应的数据表名
            # check_next_page(self.search_name, 'tyc_qybj_zzsyr')
            pass
        else:
            trs = self.selector.xpath(
                '//div[@id="_container_humanholding"]/table/tbody/tr')
        # //div[@class="out-investment-container"]/table/tbody/tr

        if trs:
            benefitPerson = TycQybjZzsyr()

            key = self.search_name
            for tr in trs:
                insert_value = ""
                tds = tr.xpath('./td')
                # 最终受益人名称
                benefitPerson.beneficiary_name = try_and_text(
                    "variable[1].xpath('/span/a/text()')[0]", tds)
                # 持股比例
                benefitPerson.shareholder_proportion = try_and_text(
                    "variable[2].xpath('./span/text()')[0]", tds)
                # 股权链
                benefitPerson.equity_chain = try_and_text(
                    "variable[3].xpath('./div')[0].xpath('string(.)')", tds)

                benefitPerson.txt_id = self.txt_id
                benefitPerson.company_name = key
                benefitPerson.mark = 0
                benefitPerson.add_time = func.now()
                benefitPerson.agency_num = self.agency_num
                benefitPerson.agency_name = self.agency_name
                benefitPerson.batch = self.batch
                # value_list = [
                #     benefitPerson.txt_id,
                #     benefitPerson.company_name,
                #     benefitPerson.mark,
                #     benefitPerson.agency_num,
                #     benefitPerson.agency_name,
                #     benefitPerson.batch,
                #     benefitPerson.beneficiaryName,
                #     benefitPerson.shareholderProportion,
                #     benefitPerson.equityChain]
                # value_list = ["'" + str(value) + "'" for value in value_list]
                # insert_value += '(' + ','.join(value_list) + ',sysdate' + ')'
                #
                # single_oracle.oracle_insert(
                #     benefitPerson.table_name,
                #     benefitPerson.column_name,
                #     insert_value)

    # 解析：企业背景-->实际控制权
    def html_parse_sjkzq(self, index):

        logger.debug("Parse detail info 实际控制权 {}".format(self.search_name))

        if index == 1 and not isinstance(self.selector, int):
            # 分页是否解析：传入当前公司名称和当前模块对应的数据表名
            check_next_page(self.search_name, 'tyc_qybj_sjkzq')
        else:
            trs = self.selector.xpath(
                '//div[@id="_container_companyholding"]//table/tbody/tr')
        if trs:
            holdingInfo = TycQybjSjkzq()

            key = self.search_name
            for tr in trs:
                insert_value = ""
                tds = tr.xpath('./td')
                # 控股企业名称
                holdingInfo.holding_name = try_and_text(
                    "variable[1].xpath('.//a/txext()')[0]", tds)
                # 投资比例 //*[@id="_container_companyholding"]/table/tbody/tr[1]/td[3]/span
                holdingInfo.invest_proportion = try_and_text(
                    "variable[2].xpath('.//text()')[0]", tds)
                # 投资链
                holdingInfo.equity_chain = try_and_text(
                    "variable[3].xpath('string(.)')", tds)

                holdingInfo.txt_id = self.txt_id
                holdingInfo.company_name = key
                holdingInfo.mark = 0
                holdingInfo.add_time = datetime.now()
                holdingInfo.agency_num = self.agency_num
                holdingInfo.agency_name = self.agency_name
                holdingInfo.batch = self.batch

                # value_list = [
                #     holdingInfo.txt_id,
                #     holdingInfo.company_name,
                #     holdingInfo.mark,
                #     holdingInfo.agency_num,
                #     holdingInfo.agency_name,
                #     holdingInfo.batch,
                #     holdingInfo.holding_name,
                #     holdingInfo.invest_proportion,
                #     holdingInfo.equity_chain]
                # value_list = ["'" + str(value) + "'" for value in value_list]
                # insert_value += '(' + ','.join(value_list) + ',sysdate' + ')'
                #
                # single_oracle.oracle_insert(
                #     holdingInfo.table_name,
                #     holdingInfo.column_name,
                #     insert_value)

    def parse_pages(self, key, index):
        # html_parse_xyzg _container_licensingXyzg  _container_purchaselandV2
        # _container_holder

        if key == '_container_licensing' or key == 'icensnav-main-leAllCount':
            try:
                self.html_parse_gsj(index)
            except BaseException:
                pass
        elif key == "_container_abnormal":
            try:
                self.html_parse_abnormal(index=index)
            except Exception as e:
                logger.exception(
                    "Detail info html_parse_abnormal() parse error! company_name：{}".format(e))
        elif key == "_container_holder":
            try:
                self.html_parse_shareholderInfo(index=index)
            except Exception as e:
                logger.exception(
                    "Detail info html_parse_shareholderInfo() parse error! company_name：{}".format(e))
        elif key == "_container_purchaselandV2":
            try:
                self.html_parse_buyInfo(index=index)
            except Exception as e:
                logger.exception(
                    "Detail info html_parse_buyInfo() parse error! company_name：{}".format(e))

        elif key == "_container_licensingXyzg":
            try:
                self.html_parse_xyzg(index=index)
            except Exception as e:
                logger.exception(
                    "Detail info html_parse_copyright() parse error! company_name：{}".format(e))
        elif key == '_container_announcementcourt':
            try:
                self.html_parse_ktgg(index)
            except BaseException:
                pass

        elif key == "_container_copyright" or key == 'nav-main-copyrightWorks':
            try:
                self.html_parse_copyright(index=index)
            except Exception as e:
                logger.exception(
                    "Detail info html_parse_copyright() parse error! company_name：{}".format(e))
                # 招聘
        elif key == "_container_baipin" or key == 'nav-main-recruitCount' or key == '_container_recruit':
            try:

                self.html_parse_recruitment(index=index)
            except Exception as e:
                logger.exception(
                    "Detail info html_parse_recruitment() parse error! company_name：{}".format(e))
                # 法律诉讼
        elif key == "_container_lawsuit" or key == 'nav-main-lawsuitCount':
            try:

                self.html_parse_lawsuit(index=index)
            except Exception as e:
                logger.exception(
                    "Detail info html_parse_lawsuit() parse error! company_name：{}".format(e))
                # 商标信息
        elif key == "nav-main-tmCount" or key == '_container_tmInfo':
            try:
                self.html_parse_trademark(index=index)
            except Exception as e:
                logger.exception(
                    "Detail info html_parse_trademark() parse error! company_name：{}".format(e))
                # 对外投资
        elif key == "_container_invest" or key == 'nav-main-inverstCount':
            try:
                self.html_parse_investInfo(index=index)
            except Exception as e:
                logger.exception(
                    "Detail info html_parse_investInfo() parse error! company_name：{}".format(e))
                # 记录变更
        elif key == "_container_changeinfo" or key == 'nav-main-changeCount':
            try:
                self.html_parse_alterRecord(index=index)
            except Exception as e:
                logger.exception(
                    "Detail info html_parse_alterRecord() parse error! company_name：{}".format(e))
                # 分支机构
        elif key == "_container_branch" or key == 'nav-main-branchCount':
            try:
                self.html_parse_branch(index=index)
            except Exception as e:
                logger.exception(e)

                # 资质证书
        elif key == "_container_certificate" or key == 'nav-main-certificateCount':
            try:
                self.html_parse_certificateInfo(index=index)
            except Exception as e:
                logger.exception(e)
                # 网站备案
        elif key == "_container_icp" or key == 'nav-main-icpCount':
            try:
                self.html_parse_website(index=index)
            except Exception as e:
                logger.exception(
                    "Detail info html_parse_website() parse error! company_name：{}".format(e))
                # 核心团队
        elif key == "_container_teamMember" or key == 'nav-main-companyTeammember':
            try:
                self.html_parse_coreTeam(index=index)
            except Exception as e:
                logger.exception(
                    "Detail info html_parse_coreTeam() parse error! company_name：{}".format(e))
                # 投资事件
        elif key == "_container_touzi" or key == 'nav-main-jigouTzanli':
            try:
                self.html_parse_investEvent(index=index)
            except Exception as e:
                logger.exception(
                    "Detail info html_parse_investEvent() parse error! company_name：{}".format(e))
                # 企业业务
        elif key == "_container_firmProduct" or key == 'nav-main-companyProduct':
            try:
                self.html_parse_entBusiness(index=index)
            except Exception as e:
                logger.exception(
                    "Detail info html_parse_entBusiness() parse error! company_name：{}".format(e))
                # 竞品信息
        elif key == "_container_jingpin" or key == 'nav-main-companyJingpin':
            try:
                self.html_parse_jpInfo(index=index)
            except Exception as e:
                logger.exception(
                    "Detail info html_parse_jpInfo() parse error! company_name：{}".format(e))
                # 法院公告
        elif key == "_container_court" or key == 'nav-main-courtCount':
            try:
                self.html_parse_announcement(index=index)
            except Exception as e:
                logger.exception(
                    "Detail info html_parse_announcement() parse error! company_name：{}".format(e))
                # 抽查检查
        elif key == "_container_check" or key == 'nav-main-checkCount':
            try:
                self.html_parse_check(index=index)
            except Exception as e:
                logger.exception(
                    "Detail info html_parse_check() parse error! company_name：{}".format(e))
                # 专利信息
        elif key == "_container_patent" or key == 'nav-main-patentCount':
            try:
                self.html_parse_patent(index=index)
            except Exception as e:
                logger.exception(
                    "Detail info html_parse_patent() parse error! company_name：{}".format(e))
                # 作品著作
        elif key == "_container_copyrightWorks" or key == 'nav-main-copyrightWorks':
            try:
                self.html_parse_copyzzq(index=index)
            except Exception as e:
                logger.exception(
                    "Detail info html_parse_copyzzq() parse error! company_name：{}".format(e))
                # 微信
        elif key == "_container_wechat" or key == 'nav-main-weChatCount':
            try:
                self.html_parse_entWechat(index=index)
            except Exception as e:
                logger.exception(
                    "Detail info html_parse_entWechat() parse error! company_name：{}".format(e))
                # 产品信息
        elif key == "_container_product" or key == 'nav-main-productinfo':
            try:
                self.html_parse_product(index=index)
            except Exception as e:
                logger.exception(
                    "Detail info html_parse_product() parse error! company_name：{}".format(e))
                # 被执行人
        elif key == "_container_zhixing" or key == 'nav-main-zhixing':
            try:
                self.html_parse_executed(index=index)
            except Exception as e:
                logger.exception(
                    "Detail info html_parse_executed() parse error! company_name：{}".format(e))
                # 招投标
        elif key == "_container_bid" or key == 'nav-main-bidCount':
            try:
                self.html_parse_bidding(index=index)
            except Exception as e:
                logger.exception(
                    "Detail info html_parse_bidding() parse error! company_name：{}".format(e))
        elif key == "nav-main-bondCount":
            try:
                self.html_parse_zhaiquan(index=index)
            except Exception as e:
                logger.exception(
                    "Detail info html_parse_zhaiquan() parse error! company_name：{}".format(e))
                # 欠税公告
        elif key == "_container_towntax" or key == 'nav-main-ownTaxCount':
            try:
                self.html_parse_taxesNotice(index=index)
            except Exception as e:
                logger.exception(
                    "Detail info html_parse_taxesNotice() parse error! company_name：{}".format(e))
                # 动产抵押
        elif key == "_container_mortgage" or key == 'nav-main-mortgageCount':
            try:
                self.html_parse_dongchandiya(index=index)
            except Exception as e:
                logger.exception(
                    "Detail info html_parse_dongchandiya() parse error! company_name：{}".format(e))
                # 股权出质
        elif key == "_container_equity" or key == 'nav-main-equityCount':
            try:
                self.html_parse_pledge(index=index)
            except Exception as e:
                logger.exception(e)
        # 行政处罚
        elif key == "_container_punish" or key == 'nav-main-punishment':
            try:
                self.html_parse_xingzhengchufa(index=index)
            except Exception as e:
                logger.exception(e)
                # 失信人
        elif key == "_container_dishonest" or key == 'nav-main-dishonest':
            try:
                self.html_parse_shixinren(index=index)
            except Exception as e:
                logger.exception(
                    "Detail info html_parse_shixinren() parse error! company_name：{}".format(e))
                # 税务评级
        elif key == "_container_taxcredit" or key == 'nav-main-taxCreditCount':
            try:
                self.html_parse_tax(index=index)
            except Exception as e:
                logger.exception(e)


def main(i):
    parameter = {'parse': 0}
    # count = 1
    mongo_where_parameter = {

    }
    # reload(sys)
    # sys.setdefaultencoding('utf-8')
    while True:
        # if count == 2:

        #     break
        # count += 1

        # for i in txt_ids:
        try:

            detail_info = {}
            #
            txt_id = single_redis.server.rpop('parses')
            # # txt_id='5c9076fefd797013a87d4162;重庆市久满汽车内饰件有限公司'
            # # logger.debug txt_id
            if not txt_id:
                single_redis.put_parse()
                txt_id = single_redis.server.rpop('parses')
            if not txt_id:
                time.sleep(60)
                continue

            if isinstance(txt_id, bytes):
                txt_id = txt_id.decode()
            id_name = txt_id.split(',')
            txt_id = id_name[0]

            search_name = id_name[1]

            mongo_where_parameter['_id'] = ObjectId(txt_id)
            # logger.debug(ObjectId(txt_id))
            mongo_table = "company_detail_info"
            detail_info = single_mongodb.mongodb_find_one(
                mongo_table, mongo_where_parameter)
            # print(detail_info)
        except Exception as e:
            logger.exception(e)
            continue

        if detail_info:
            tyc_Parse = TycDetailParse(
                single_mongodb, single_oracle, search_name)
            if 'dicts' in detail_info:
                tyc_Parse.dicts = detail_info['dicts']
            # txt_id = str(detail_info["_id"])
            try:
                agency_name = ''
                agency_num = ''
                batch = ''
                branch = ''
                if 'agency_num' in detail_info:
                    agency_num = detail_info['agency_num']
                if 'agency_name' in detail_info:
                    agency_name = detail_info['agency_name']
                if 'batch' in detail_info:
                    batch = detail_info['batch']
                if 'branch' in detail_info:
                    branch = detail_info['branch']
                # 判断该公司是否已经解析入库
                # param = {'ent_name': ent_name}
                # table = "tyc_qybj_jbxx"
                # check_sql = 'SELECT id from tyc_qybj_jbxx WHERE ent_name="%s" ' % ent_name
                # result = single_oracle.oracle_find_by_param(check_sql)
                error_list = []

                html = detail_info["text"]
                selector = etree.HTML(html)
                soup = BeautifulSoup(html, 'lxml')
                # logger.debug(soup.prettify())
                tyc_Parse.detail_info = detail_info
                tyc_Parse.txt_id = txt_id
                tyc_Parse.agency_num = agency_num
                tyc_Parse.agency_name = agency_name or 'NA'
                tyc_Parse.batch = batch
                tyc_Parse.soup = soup
                tyc_Parse.selector = selector
            except Exception as e:
                logger.debug("%s - %s 初始化网页内容出错！" % (search_name, txt_id))
                logger.exception("Exception Logged")
                logger.debug(e)
                continue

            # 基本信息
            try:
                tyc_Parse.html_parse_baseinfo()
                print('>>>>>>>>>>>>该模块检测完毕：基本信息')
            except Exception as e:
                print('>>>>>>>>>>>>该模块检测有误：基本信息', e)
                error_list.append("html_parse_baseinfo")
                logger.exception(
                    "Detail info html_parse_baseinfo() parse error! company_name：%s ID：%s",
                    search_name,
                    txt_id)

            # 主要信息
            try:
                tyc_Parse.html_parse_mainPerson()
                print('>>>>>>>>>>>>该模块检测完毕：主要信息')
            except Exception as e:
                print('>>>>>>>>>>>>该模块检测有误!!!!!：主要信息', e)
                error_list.append("html_parse_mainPerson")
                logger.exception(
                    "Detail info html_parse_mainPerson() parse error! company_name：%s ID：%s",
                    search_name,
                    txt_id)

            # 股东
            try:
                tyc_Parse.html_parse_shareholderInfo(0)
                print('>>>>>>>>>>>>该模块检测完毕：股东')
            except Exception as e:
                print('>>>>>>>>>>>>该模块检测有误!!!!!：股东', e)
                error_list.append("html_parse_shareholderInfo")
                logger.exception(
                    "Detail info html_parse_shareholderInfo() parse error! company_name：%s ID：%s",
                    search_name,
                    txt_id)

            # 法律诉讼
            try:
                tyc_Parse.html_parse_lawsuit(index=0)
                print('>>>>>>>>>>>>该模块检测完毕：法律诉讼')
            except Exception as e:
                print('>>>>>>>>>>>>该模块检测有误!!!!!：法律诉讼', e)
                logger.debug('Exception====={}'.format(e))
                error_list.append("html_parse_lawsuit")
                logger.exception(
                    "Detail info html_parse_lawsuit() parse error! company_name：{}, ID：{}".format(
                        search_name, txt_id))
            # 著作权
            try:
                tyc_Parse.html_parse_copyright(index=0)
                print('>>>>>>>>>>>>该模块检测完毕：著作权')
            except Exception as e:
                print('>>>>>>>>>>>>该模块检测有误!!!!!：著作权', e)
                error_list.append("html_parse_copyright")
                logger.exception(
                    "Detail info html_parse_copyright() parse error! company_name：%s ID：%s",
                    search_name,
                    txt_id)
            # 招聘
            try:
                job = ''
                if "job" in detail_info:
                    job = detail_info["job"]
                tyc_Parse.html_parse_recruitment(index=0)
                print('>>>>>>>>>>>>该模块检测完毕：招聘')
            except Exception as e:
                print('>>>>>>>>>>>>该模块检测有误!!!!!：招聘', e)
                error_list.append("html_parse_recruitment")
                logger.exception(
                    "Detail info html_parse_recruitment() parse error! company_name：%s ID：%s",
                    search_name,
                    txt_id)
            # 商标信息
            try:
                tyc_Parse.html_parse_trademark(index=0)
                print('>>>>>>>>>>>>该模块检测完毕：商标信息')
            except Exception as e:
                print('>>>>>>>>>>>>该模块检测有误!!!!!：商标信息', e)
                error_list.append("html_parse_trademark")
                logger.exception(
                    "Detail info html_parse_trademark() parse error! company_name：%s ID：%s",
                    search_name,
                    txt_id)
            # 对外投资
            try:
                tyc_Parse.html_parse_investInfo(index=0)
                print('>>>>>>>>>>>>该模块检测完毕：对外投资')
            except Exception as e:
                print('>>>>>>>>>>>>该模块检测有误!!!!!：对外投资', e)
                error_list.append("html_parse_investInfo")
                logger.exception(
                    "Detail info html_parse_investInfo() parse error! company_name：%s ID：%s",
                    search_name,
                    txt_id)
            # 记录变更
            try:
                tyc_Parse.html_parse_alterRecord(index=0)
                print('>>>>>>>>>>>>该模块检测完毕：记录变更')
            except Exception as e:
                print('>>>>>>>>>>>>该模块检测有误!!!!!：记录变更', e)
                error_list.append("html_parse_alterRecord")
                logger.exception(
                    "Detail info html_parse_alterRecord() parse error! company_name：%s ID：%s",
                    search_name,
                    txt_id)
            # 分支机构
            try:
                tyc_Parse.html_parse_branch(0)
                print('>>>>>>>>>>>>该模块检测完毕：分支机构')
            except Exception as e:
                print('>>>>>>>>>>>>该模块检测有误!!!!!：分支机构', e)
                error_list.append("html_parse_branch")
                logger.exception(
                    "Detail info html_parse_branch() parse error! company_name：%s ID：%s",
                    search_name,
                    txt_id)
                # 股权出质
            try:
                tyc_Parse.html_parse_pledge(0)
                print('>>>>>>>>>>>>该模块检测完毕：股权出质')
            except Exception as e:
                print('>>>>>>>>>>>>该模块检测有误!!!!!：股权出质', e)
                error_list.append("html_parse_pledge")
                logger.exception(
                    "Detail info html_parse_pledge() parse error! company_name：%s ID：%s",
                    search_name,
                    txt_id)
            # 资质证书
            try:
                tyc_Parse.html_parse_certificateInfo(index=0)
                print('>>>>>>>>>>>>该模块检测完毕：资质证书')
            except Exception as e:
                print('>>>>>>>>>>>>该模块检测有误!!!!!：资质证书', e)
                error_list.append("html_parse_certificateInfo")
                logger.exception(
                    "Detail info html_parse_certificateInfo() parse error! company_name：%s ID：%s",
                    search_name,
                    txt_id)
            # 网站备案
            try:
                tyc_Parse.html_parse_website(index=0)
                print('>>>>>>>>>>>>该模块检测完毕：网站备案')
            except Exception as e:
                print('>>>>>>>>>>>>该模块检测有误!!!!!：网站备案', e)
                error_list.append("html_parse_website")
                logger.exception(
                    "Detail info html_parse_website() parse error! company_name：%s ID：%s",
                    search_name,
                    txt_id)
            # 核心团队
            try:
                tyc_Parse.html_parse_coreTeam(index=0)
                print('>>>>>>>>>>>>该模块检测完毕：核心团队')
            except Exception as e:
                print('>>>>>>>>>>>>该模块检测有误!!!!!：核心团队', e)
                error_list.append("html_parse_coreTeam")
                logger.exception(
                    "Detail info html_parse_coreTeam() parse error! company_name：%s ID：%s",
                    search_name,
                    txt_id)
            # 投资事件
            try:
                tyc_Parse.html_parse_investEvent(index=0)
                print('>>>>>>>>>>>>该模块检测完毕：投资事件')
            except Exception as e:
                print('>>>>>>>>>>>>该模块检测有误!!!!!：投资事件', e)
                error_list.append("html_parse_investEvent")
                logger.exception(
                    "Detail info html_parse_investEvent() parse error! company_name：%s ID：%s",
                    search_name,
                    txt_id)
            # 企业业务
            try:
                tyc_Parse.html_parse_entBusiness(index=0)
                print('>>>>>>>>>>>>该模块检测完毕：企业业务')
            except Exception as e:
                print('>>>>>>>>>>>>该模块检测有误!!!!!：企业业务', e)
                error_list.append("html_parse_entBusiness")
                logger.exception(
                    "Detail info html_parse_entBusiness() parse error! company_name：%s ID：%s",
                    search_name,
                    txt_id)
            # 竞品信息
            try:
                tyc_Parse.html_parse_jpInfo(index=0)
                print('>>>>>>>>>>>>该模块检测完毕：竞品信息')
            except Exception as e:
                print('>>>>>>>>>>>>该模块检测有误!!!!!：竞品信息', e)
                error_list.append("html_parse_jpInfo")
                logger.exception(
                    "Detail info html_parse_jpInfo() parse error! company_name：%s ID：%s",
                    search_name,
                    txt_id)
            # 法院公告
            try:
                tyc_Parse.html_parse_announcement(index=0)
                print('>>>>>>>>>>>>该模块检测完毕：法院公告')
            except Exception as e:
                print('>>>>>>>>>>>>该模块检测有误!!!!!：法院公告', e)
                error_list.append("html_parse_announcement")
                logger.exception(
                    "Detail info html_parse_announcement() parse error! company_name：%s ID：%s",
                    search_name,
                    txt_id)
            # 抽查检查
            try:
                tyc_Parse.html_parse_check(index=0)
                print('>>>>>>>>>>>>该模块检测完毕：抽查检查')
            except Exception as e:
                print('>>>>>>>>>>>>该模块检测有误!!!!!：抽查检查', e)
                error_list.append("html_parse_check")
                logger.exception(
                    "Detail info html_parse_check() parse error! company_name：%s ID：%s",
                    search_name,
                    txt_id)
            # 专利信息
            try:
                tyc_Parse.html_parse_patent(index=0)
                print('>>>>>>>>>>>>该模块检测完毕：专利信息')
            except Exception as e:
                print('>>>>>>>>>>>>该模块检测有误!!!!!：专利信息', e)
                error_list.append("html_parse_patent")
                logger.exception(
                    "Detail info html_parse_patent() parse error! company_name：%s ID：%s",
                    search_name,
                    txt_id)
            # 作品著作
            try:
                tyc_Parse.html_parse_copyzzq(index=0)
                print('>>>>>>>>>>>>该模块检测完毕：作品著作')
            except Exception as e:
                print('>>>>>>>>>>>>该模块检测有误!!!!!：作品著作', e)
                error_list.append("html_parse_copyzzq")
                logger.exception(
                    "Detail info html_parse_copyzzq() parse error! company_name：%s ID：%s",
                    search_name,
                    txt_id)
            # 微信
            try:
                tyc_Parse.html_parse_entWechat(index=0)
                print('>>>>>>>>>>>>该模块检测完毕：微信')
            except Exception as e:
                print('>>>>>>>>>>>>该模块检测有误!!!!!：微信', e)
                error_list.append("html_parse_entWechat")
                logger.exception(
                    "Detail info html_parse_entWechat() parse error! company_name：%s ID：%s",
                    search_name,
                    txt_id)
            # 产品信息
            try:
                tyc_Parse.html_parse_product(index=0)
                print('>>>>>>>>>>>>该模块检测完毕：产品信息')
            except Exception as e:
                print('>>>>>>>>>>>>该模块检测有误!!!!!：产品信息', e)
                error_list.append("html_parse_product")
                logger.exception(
                    "Detail info html_parse_product() parse error! company_name：%s ID：%s",
                    search_name,
                    txt_id)
            # 被执行人
            try:
                tyc_Parse.html_parse_executed(index=0)
                print('>>>>>>>>>>>>该模块检测完毕：被执行人')
            except Exception as e:
                print('>>>>>>>>>>>>该模块检测有误!!!!!：被执行人', e)
                error_list.append("html_parse_executed")
                logger.exception(
                    "Detail info html_parse_executed() parse error! company_name：%s ID：%s",
                    search_name,
                    txt_id)
            # 招投标
            try:
                tyc_Parse.html_parse_bidding(index=0)
                print('>>>>>>>>>>>>该模块检测完毕：招投标')
            except Exception as e:
                print('>>>>>>>>>>>>该模块检测有误!!!!!：招投标', e)
                error_list.append("html_parse_bidding")
                logger.exception(
                    "Detail info html_parse_bidding() parse error! company_name：%s ID：%s",
                    search_name,
                    txt_id)
            # 债券信息
            try:
                tyc_Parse.html_parse_zhaiquan(index=0)
                print('>>>>>>>>>>>>该模块检测完毕：债券信息')
            except Exception as e:
                print('>>>>>>>>>>>>该模块检测有误!!!!!：债券信息', e)
                error_list.append("html_parse_zhaiquan")
                logger.exception(
                    "Detail info html_parse_zhaiquan() parse error! company_name：%s ID：%s",
                    search_name,
                    txt_id)
            # 欠税公告
            try:
                tyc_Parse.html_parse_taxesNotice(index=0)
                print('>>>>>>>>>>>>该模块检测完毕：欠税公告')
            except Exception as e:
                print('>>>>>>>>>>>>该模块检测有误!!!!!：欠税公告', e)
                error_list.append("html_parse_taxesNotice")
                logger.exception(
                    "Detail info html_parse_taxesNotice() parse error! company_name：%s ID：%s",
                    search_name,
                    txt_id)
            # 动产抵押
            try:
                tyc_Parse.html_parse_dongchandiya(index=0)
                print('>>>>>>>>>>>>该模块检测完毕：动产抵押')
            except Exception as e:
                print('>>>>>>>>>>>>该模块检测有误!!!!!：动产抵押', e)
                error_list.append("html_parse_dongchandiya")
                logger.exception(
                    "Detail info html_parse_dongchandiya() parse error! company_name：%s ID：%s",
                    search_name,
                    txt_id)
            # 股权出质
            try:
                tyc_Parse.html_parse_pledge(index=0)
                print('>>>>>>>>>>>>该模块检测完毕：股权出质')
            except Exception as e:
                print('>>>>>>>>>>>>该模块检测有误!!!!!：股权出质', e)
                error_list.append("html_parse_pledge")
                logger.exception(
                    "Detail info html_parse_pledge() parse error! company_name：%s ID：%s",
                    search_name,
                    txt_id)
            # 行政处罚
            try:
                tyc_Parse.html_parse_xingzhengchufa(index=0)
                print('>>>>>>>>>>>>该模块检测完毕：行政处罚')
            except Exception as e:
                print('>>>>>>>>>>>>该模块检测有误!!!!!：行政处罚', e)
                error_list.append("html_parse_xingzhengchufa")
                logger.exception(
                    "Detail info html_parse_xingzhengchufa() parse error! company_name：%s ID：%s",
                    search_name,
                    txt_id)
            # 失信人
            try:
                tyc_Parse.html_parse_shixinren(index=0)
                print('>>>>>>>>>>>>该模块检测完毕：失信人')
            except Exception as e:
                print('>>>>>>>>>>>>该模块检测有误!!!!!：失信人', e)
                error_list.append("html_parse_shixinren")
                logger.exception(
                    "Detail info html_parse_shixinren() parse error! company_name：%s ID：%s",
                    search_name,
                    txt_id)
            # 税务评级
            try:
                tyc_Parse.html_parse_tax(index=0)
                print('>>>>>>>>>>>>该模块检测完毕：税务评级')
            except Exception as e:
                print('>>>>>>>>>>>>该模块检测有误!!!!!：税务评级', e)
                error_list.append("html_parse_tax")
                logger.exception(
                    "Detail info html_parse_tax() parse error! company_name：%s ID：%s",
                    search_name,
                    txt_id)
            # 融资
            try:
                tyc_Parse.html_parse_financeHistory()
                print('>>>>>>>>>>>>该模块检测完毕：融资')
            except Exception as e:
                print('>>>>>>>>>>>>该模块检测有误!!!!!：融资', e)
                error_list.append("html_parse_financeHistory")
                logger.exception(
                    "Detail info html_parse_financeHistory() parse error! company_name：%s ID：%s",
                    search_name,
                    txt_id)
            # 经营异常
            try:
                tyc_Parse.html_parse_abnormal(0)
                print('>>>>>>>>>>>>该模块检测完毕：经营异常')
            except Exception as e:
                print('>>>>>>>>>>>>该模块检测有误!!!!!：经营异常', e)
                error_list.append("html_parse_abnormal")
                logger.exception(
                    "Detail info html_parse_abnormal() parse error! company_name：%s ID：%s",
                    search_name,
                    txt_id)
            # 严重违法
            try:
                tyc_Parse.html_parse_illegalSerious()
                print('>>>>>>>>>>>>该模块检测完毕：严重违法')
            except Exception as e:
                print('>>>>>>>>>>>>该模块检测有误!!!!!：严重违法', e)
                error_list.append("html_parse_illegalSerious")
                logger.exception(
                    "Detail info html_parse_illegalSerious() parse error! company_name：%s ID：%s",
                    search_name,
                    txt_id)

            # 购地信息
            try:
                tyc_Parse.html_parse_buyInfo(0)
                print('>>>>>>>>>>>>该模块检测完毕：购地信息')
            except Exception as e:
                print('>>>>>>>>>>>>该模块检测有误!!!!!：购地信息', e)
                error_list.append("html_parse_buyInfo")
                logger.exception(
                    "Detail info html_parse_buyInfo() parse error! company_name：%s ID：%s",
                    search_name,
                    txt_id)
            # 年报
            try:
                if "year" in detail_info:
                    year = detail_info["year"]
                    if year:
                        tyc_Parse.html_parse_nianbao(year)
                print('>>>>>>>>>>>>该模块检测完毕：年报')
            except Exception as e:
                print('>>>>>>>>>>>>该模块检测有误!!!!!：年报', e)
                error_list.append("html_parse_nianbao")
                logger.exception(
                    "Detail info html_parse_nianbao() parse error! company_name：%s ID：%s",
                    search_name,
                    txt_id)
            # 进出口
            try:
                tyc_Parse.html_parse_outputxy()
                print('>>>>>>>>>>>>该模块检测完毕：进出口')
            except Exception as e:
                print('>>>>>>>>>>>>该模块检测有误!!!!!：进出口', e)
                error_list.append("html_parse_outputxy")
                logger.exception(
                    "Detail info html_parse_outputxy() parse error! company_name：%s ID：%s",
                    search_name,
                    txt_id)

            # 最终受益人
            try:
                tyc_Parse.html_parse_zzsyr(index=0)
                print('>>>>>>>>>>>>该模块检测完毕：最终受益人')
            except Exception as e:
                print('>>>>>>>>>>>>该模块检测有误!!!!!：最终受益人', e)
                error_list.append("html_parse_zzsyr")
                logger.exception(
                    "Detail info html_parse_zzsyr() parse error! company_name：%s ID：%s",
                    search_name,
                    txt_id)

            # 实际控制权
            try:
                tyc_Parse.html_parse_sjkzq(index=0)
                print('>>>>>>>>>>>>该模块检测完毕：实际控制权')
            except Exception as e:
                print('>>>>>>>>>>>>该模块检测有误!!!!!：实际控制权', e)
                error_list.append("html_parse_sjkzq")
                logger.exception(
                    "Detail info html_parse_sjkzq() parse error! company_name：%s ID：%s",
                    search_name,
                    txt_id)

            # 开庭公告
            try:
                tyc_Parse.html_parse_ktgg(index=0)
                print('>>>>>>>>>>>>该模块检测完毕：开庭公告')
            except Exception as e:
                print('>>>>>>>>>>>>该模块检测有误!!!!!：开庭公告', e)
                error_list.append("html_parse_ktgg")
                logger.exception(
                    "Detail info html_parse_ktgg() parse error! company_name：%s ID：%s",
                    search_name,
                    txt_id)
            #
            # 司法协助
            try:
                tyc_Parse.html_parse_sfxz(index=0)
                print('>>>>>>>>>>>>该模块检测完毕：司法协助')
            except Exception as e:
                print('>>>>>>>>>>>>该模块检测有误!!!!!：司法协助', e)
                error_list.append("html_parse_sfxz")
                logger.exception(
                    "Detail info html_parse_sfxz() parse error! company_name：%s ID：%s",
                    search_name,
                    txt_id)
            #
            # 公示催告
            try:
                tyc_Parse.html_parse_gscg()
                print('>>>>>>>>>>>>该模块检测完毕：公示催告')
            except Exception as e:
                print('>>>>>>>>>>>>该模块检测有误!!!!!：公示催告', e)
                error_list.append("html_parse_gscg")
                logger.exception(
                    "Detail info html_parse_gscg() parse error! company_name：%s ID：%s",
                    search_name,
                    txt_id)

            # 司法拍卖
            try:
                tyc_Parse.html_parse_sfpm(index=0)
                print('>>>>>>>>>>>>该模块检测完毕：司法拍卖')
            except Exception as e:
                print('>>>>>>>>>>>>该模块检测有误!!!!!：司法拍卖', e)
                error_list.append("html_parse_sfpm")
                logger.exception(
                    "Detail info html_parse_sfpm() parse error! company_name：%s ID：%s",
                    search_name,
                    txt_id)

            # 清算信息
            try:
                tyc_Parse.html_parse_qsxx(index=0)
                print('>>>>>>>>>>>>该模块检测完毕：清算信息')
            except Exception as e:
                print('>>>>>>>>>>>>该模块检测有误!!!!!：清算信息', e)
                error_list.append("html_parse_qsxx")
                logger.exception(
                    "Detail info html_parse_qsxx() parse error! company_name：%s ID：%s",
                    search_name,
                    txt_id)

            # 行政许可【工商局】
            try:
                tyc_Parse.html_parse_gsj(index=0)
                print('>>>>>>>>>>>>该模块检测完毕：行政许可【工商局】')
            except Exception as e:
                print('>>>>>>>>>>>>该模块检测有误!!!!!：行政许可【工商局】', e)
                error_list.append("html_parse_gsj")
                logger.exception(
                    "Detail info html_parse_gsj() parse error! company_name：%s ID：%s",
                    search_name,
                    txt_id)

            # 行政许可【信用中国】
            try:
                tyc_Parse.html_parse_xyzg(index=0)
                print('>>>>>>>>>>>>该模块检测完毕：行政许可【信用中国】')
            except Exception as e:
                print('>>>>>>>>>>>>该模块检测有误!!!!!：行政许可【信用中国】', e)
                error_list.append("html_parse_xyzg")
                logger.exception(
                    "Detail info html_parse_xyzg() parse error! company_name：%s ID：%s",
                    search_name,
                    txt_id)

            # 电信许可
            try:
                tyc_Parse.html_parse_dxxk(index=0)
                print('>>>>>>>>>>>>该模块检测完毕：电信许可')
            except Exception as e:
                print('>>>>>>>>>>>>该模块检测有误!!!!!：电信许可', e)
                error_list.append("html_parse_dxxk")
                logger.exception(
                    "Detail info html_parse_dxxk() parse error! company_name：%s ID：%s",
                    search_name,
                    txt_id)

            # 分页解析开始
            logger.debug("分页解析开始 %s" % search_name)
            try:
                pages = detail_info["page"]
            except BaseException:
                pages = {}
            try:
                # page={'key':[[1,2,3],[],[]],'key1':[]}
                for key, value in pages.items():  # [[{},{}}],[1,2],[]]
                    logger.debug(key)
                    single_redis.server.hset('id', key, 1)
                    if isinstance(value, list):
                        for text in value:  # [1,2,3]
                            logger.debug(type(text))
                            if isinstance(text, str):
                                # if isinstance(text, unicode):
                                #     text = text.encode('utf-8')
                                selector = etree.HTML(text)
                                soup = BeautifulSoup(text, "lxml")
                                tyc_Parse.soup = soup
                                tyc_Parse.selector = selector
                                tyc_Parse.parse_pages(key=key, index=1)
                            elif isinstance(text, dict):
                                for i in text.values():
                                    # if isinstance(i, unicode):
                                    #     i = i.encode('utf-8')
                                    selector = etree.HTML(i)
                                    soup = BeautifulSoup(i, "lxml")
                                    tyc_Parse.soup = soup
                                    tyc_Parse.selector = selector
                                    tyc_Parse.parse_pages(key=key, index=1)

                    else:
                        tyc_Parse.soup = tyc_Parse.selector = value
                        tyc_Parse.parse_pages(key=key, index=1)

            except Exception as e:
                logger.exception(e)

            logger.debug("分页解析结束 %s" % search_name)

            try:
                single_oracle.oracle_update(
                    "update company_basic_info set parsed=1 where txt_id='{}'".format(
                        detail_info["_id"]))
                single_mongodb.mongodb_update(
                    "company_detail_info", {
                        '_id': ObjectId(
                            detail_info["_id"])}, {
                        'parse': 1, "error_list": str(error_list)})

                batch_detail = Batch_Detail()
                column_name = "(company_name,searched,error,add_time,agency_num,txt_id,batch_type)"
                agency_num = agency_num if agency_num else branch
                batch_type = '1'
                if agency_num:
                    batch_type = '0'
                insert_value_batch = "('" + search_name + "'," + '1' + "," + '0' + ",sysdate ,'" + str(
                    agency_num) + "','" + txt_id + "','" + batch_type + "')"

                # single_oracle.oracle_insert(batch_detail.table_name, column_name, insert_value_batch)
            except Exception as e:
                logger.exception(e)
                logger.debug("datebases update False!")
                logger.exception("Exception Logged")
                # single_mongodb = single_mongodb()
                # single_oracle = single_oracle()

            # 汇总记录翻页有问题的模块，入库check_result表
            global NEXT_PAGE_DICT
            check_company_next_page(NEXT_PAGE_DICT, search_name)

        else:
            continue
            sql = "SELECT company_number FROM batch_detail WHERE searched=0"
            sql_resut = single_oracle.oracle_find_by_param_all(sql)
            if sql_resut:
                # logger.debug "sleeping!!"
                time.sleep(60 * 60)
            else:
                try:
                    logger.debug("No detail to be parsed!")
                    bd = BatchList()
                    result_batch = single_oracle.find_batch()
                    batch = result_batch[0]
                    bd.batch = ''.join(batch)

                    bd.end_time = func.now()
                    value_list = [bd.batch, bd.end_time]
                    value_list = [
                        "'" + str(value) + "'" for value in value_list]
                    check_batch = single_oracle.oracle_find_one(
                        bd.table_name, {"batch": batch})
                    if check_batch:
                        insert_value = '(' + ','.join(value_list) + ')'

                        single_oracle.oracle_update(
                            bd.table_name, {
                                "end_time": datetime.now()}, {
                                "batch": batch})
                    else:
                        bd.add_time = result_batch[1]
                        insert_value = '(' + ','.join(value_list) + ')'

                        single_oracle.oracle_insert(
                            bd.table_name, bd.column_name, insert_value)
                except Exception as e:
                    logger.debug(e)
                    continue


# ['html_parse_pledge', 'html_parse_pledge'] ['html_parse_gscg'] ['html_parse_shixinren']
if __name__ == "__main__":
    # search_name = '佐源集团有限公司'
    #
    # global NEXT_PAGE_DICT
    # check_company_next_page(NEXT_PAGE_DICT, search_name)
    main(1)
