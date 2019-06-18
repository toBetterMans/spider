# !/usr/bin/env python
import logging.config
import re
import sys
# import HTMLParser
from datetime import datetime

from bs4 import BeautifulSoup
from bson import ObjectId
from cpca import *
from lxml import etree

from db import single_mongodb, single_oracle
from redis_cache import single_redis
from tyc_bean_1 import *

# reload(sys)
# sys.setdefaultencoding('utf-8')
logging.config.fileConfig("../log_file/parse.conf")

logger = logging.getLogger("loggerText")

CURRENT_VERSION_NULL = '此版本无此信息'

def try_and_text(func, variable):
    s = 'NA'
    if not func:
        return 'NA'
    try:
        s = eval(func)
    except Exception as e:
        logger.error(e)
    finally:
        return s

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

def replace_special_string(strings=''):
    return strings.replace(
        u'<em>',
        u'').replace(
        u'</em>',
        u'').replace(
        u'\ue004',
        u'').replace(
        u'\ufffd',
        u'').replace(
        u'\u2022',
        u'').replace(
        u'\xb3',
        u'').replace(
        u'\ue005',
        u'').replace(
        u'\xa9',
        '').replace(
        u'\u003C',
        u'').replace(
        u'\u003E',
        u'').replace(
        u'\ufffd',
        u'').replace(
        u'\ufffd',
        u'').replace(
        u'\xa9',
        u'').replace(
        u'\u002F',
        u'').replace(
        u'\u003E',
        u'').replace(
        u"'",
        u'"').replace(
        u'\u003c\u0065\u006d\u003e',
        u'').replace(
        u'\u003c\u002f\u0065\u006d\u003e',
        '').replace(
        u'\xa5',
        u'').replace(
        u'\xa0',
        u'').replace(r'\uff08', '(').replace(u'\u0029', ')').replace('（', '(').replace('）', ')')

class TycDetailParse(object):
    txtId = ''
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
                email = top.xpath('.//span[@class="email"]/text()')[0]
            except:
                email = 'NA'
            baseinfo.email = email
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
                        registerFund = trs1[0].xpath('./td/div/@title')[0] or 'NA'
                
                    except:
                        registerFund = trs1[0].xpath('./td//text()')[0]
                    baseinfo.registerFund = registerFund
                
                    baseinfo.companyStatus = trs1[1].xpath(
                        './td[2]//text()')[0]
                    baseinfo.registerNum = trs1[1].xpath('./td[4]//text()')[0]
                    baseinfo.tissueNum = trs1[2].xpath(
                        './td[position()=4]/text()')[0]
                    baseinfo.creditNum = trs1[2].xpath(
                        './td[position()=2]/text()')[0]
                    baseinfo.companyType = trs1[3].xpath('./td[4]')[0].xpath('string(.)')
                    baseinfo.taxpayerNum = trs1[3].xpath('./td[2]')[0].xpath('string(.)')
                    baseinfo.industry = trs1[4].xpath('./td[4]')[0].xpath('string(.)')
                    businessTerm = trs1[4].xpath('./td[2]')[0].xpath('string(.)')
                    if businessTerm == '-' or businessTerm == '未公开':
                        business_term_begin = business_term_end = '-'
                    else:
                        business_term_begin = businessTerm.split('至')[0]
                        business_term_end = businessTerm.split('至')[1]
                        if business_term_end == '无固定期限':
                            business_term_end = '2999-12-31'
                
                    registerDate = try_and_text("variable[0].xpath('./td[4]')[0].xpath('string(.)')", trs1)
                    # 新增 纳税人资质
                    taxQualificate = try_and_text("variable[5].xpath('./td[2]')[0].xpath('string(.)')", trs1)
                    baseinfo.taxQualificate = taxQualificate[0] if taxQualificate else 'NA'
                
                    checkDate = try_and_text("variable[5].xpath('./td[4]')[0].xpath('string(.)')", trs1)
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
                    baseinfo.businessTerm = businessTerm
                    baseinfo.registerDate = registerDate
                    baseinfo.checkDate = checkDate
                
                    baseinfo.englishName = try_and_text("variable[8].xpath('./td[4]')[0].xpath('string(.)')", trs1)
                    # 此处改为曾用名
                    baseinfo.used_name = try_and_text("variable[8].xpath('./td[2]')[0].xpath('string(.)')", trs1)
                    baseinfo.registerSite = try_and_text("variable[9].xpath('./td[2]')[0].xpath('string(.)')",
                                                         trs1).replace(
                        '附近公司', '')
                    address_1 = address_2 = address_3 = 'NA'
                
                    df = transform([baseinfo.registerSite], cut=False)
                    for addr in df.index:
                        print(addr)
                        address_1 = df.loc[addr].values[0]
                        address_2 = df.loc[addr].values[1]
                        address_3 = df.loc[addr].values[2]
                
                    businessScope = replace_special_string(try_and_text("variable[10].xpath('./td[2]')[0].xpath('string(.)')", trs1))
                    baseinfo.businessScope = businessScope.replace(
                        "'", '') if businessScope else 'NA'
                
                    # 人员规模
                    baseinfo.persionSize = try_and_text("variable[6].xpath('./td[4]')[0].xpath('string(.)')", trs1)
                    # 实缴资本：
                    baseinfo.paidCapital = try_and_text("variable[6].xpath('./td[2]')[0].xpath('string(.)')", trs1)
                    # 参保人数：
                    baseinfo.insuredPersion = try_and_text("variable[7].xpath('./td[2]')[0].xpath('string(.)')", trs1)
                    baseinfo.registerOffice = try_and_text("variable[7].xpath('./td[4]')[0].xpath('string(.)')", trs1)
                    baseinfo.txtId = self.txtId or 'NA'
                    baseinfo.entName = key
                    baseinfo.mark = 0
                    baseinfo.addtime = 'sysdate'
                    baseinfo.agency_num = self.agency_num
                    baseinfo.agency_name = self.agency_name
                    baseinfo.batch = self.batch
                    baseinfo.industry_4 = 'NA'
                
                    value_list = [
                        baseinfo.insuredPersion,
                        baseinfo.taxQualificate,
                        baseinfo.persionSize,
                        baseinfo.paidCapital,
                        baseinfo.txtId,
                        baseinfo.entName,
                        baseinfo.registerNum,
                        baseinfo.tissueNum,
                        baseinfo.creditNum,
                        baseinfo.companyType,
                        baseinfo.taxpayerNum,
                        baseinfo.industry,
                        baseinfo.businessTerm,
                        baseinfo.checkDate,
                        baseinfo.registerOffice,
                        baseinfo.registerSite,
                        baseinfo.registerFund,
                        baseinfo.registerDate,
                        baseinfo.companyStatus,
                        baseinfo.businessScope,
                        baseinfo.telephone,
                        baseinfo.email,
                        baseinfo.url,
                        baseinfo.used_name,
                        baseinfo.englishName,
                        baseinfo.mark,
                        baseinfo.agency_num,
                        baseinfo.agency_name,
                        baseinfo.batch,
                        baseinfo.industry_4,
                        baseinfo.branch,
                        address_1,
                        address_2,
                        address_3,
                        business_term_begin,
                        business_term_end
                    ]
                
                    # logger.debug('基本信息获取到数据====', value_list)
                    value_list = ["'" + str(value) + "'" for value in value_list]
                    insert_value = '(' + ','.join(value_list) + ',sysdate' + ')'
                
                    # logger.debug insert_value
                    single_oracle.oracle_insert(
                        baseinfo.table_name, baseinfo.column_name, insert_value)
    
    # 解析：企业背景-->主要人员
    def html_parse_mainPerson(self):
    
        logger.debug("Parse detail info 主要人员 {}".format(self.search_name))
        trs = self.selector.xpath(
            '//div[@id="_container_staff"]/div/table/tbody/tr')
        if trs:
    
            mainPerson = TycQybjZyry()
            key = self.search_name
            # trs = trs[0]
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
                    mainPerson.name = name[0].replace(
                        '\n', '').replace(
                        "'", '') if name else 'NA'
                except:
                    mainPerson.name = 'ERROR'
                mainPerson.txtId = self.txtId
                mainPerson.entName = key
                mainPerson.mark = 0
                mainPerson.addtime = 'sysdate'
                mainPerson.agency_num = self.agency_num
                mainPerson.agency_name = self.agency_name
                mainPerson.batch = self.batch

                value_list = [
                    mainPerson.txtId,
                    mainPerson.entName,
                    mainPerson.position,
                    mainPerson.name,
                    mainPerson.mark,
                    mainPerson.agency_num,
                    mainPerson.agency_name,
                    mainPerson.batch]
                value_list = ["'" + str(value) + "'" for value in value_list]

                insert_value += '(' + ','.join(value_list) + ',sysdate' + ')'

                logger.debug(insert_value)

                single_oracle.oracle_insert(
                    mainPerson.table_name,
                    mainPerson.column_name,
                    insert_value)

    # 解析：企业背景-->股东信息
    def html_parse_shareholderInfo(self, index):
        logger.debug("Parse detail info 股东信息 {}".format(self.search_name))
        if index == 1 and not isinstance(self.selector, int):
            root_div = (self.selector.xpath('//table/tbody/tr'))
        else:
    
            trs = (self.selector.xpath(
                '//div[@id="_container_holder"]/table/tbody/tr'))

        if trs:
            shareholderInfo = TycQybjGdxx()

            key = self.search_name
            for tr in trs:
                insert_value = ""
                tds = tr.xpath('./td')
                shareholderInfo.shareholder = try_and_text("variable[1].xpath('.//a/text()')[0]", tds)
                shareholderInfo.fundRatio = try_and_text("variable[2].xpath('.//text()')[0]", tds)
                shareholderInfo.fundSubcribe = try_and_text("variable[3].xpath('.//text()')[0]", tds)
                shareholderInfo.txtId = self.txtId
                shareholderInfo.company_name = key
                shareholderInfo.mark = 0
                shareholderInfo.addtime = 'sysdate'
                shareholderInfo.agency_num = self.agency_num
                shareholderInfo.agency_name = self.agency_name
                shareholderInfo.batch = self.batch

                # 增加 出资时间
                fundTime = try_and_text("variable[4].xpath('.//text()')", tds)
                shareholderInfo.fundTime = fundTime[0] if fundTime else 'NA'

                value_list = [
                    shareholderInfo.fundTime,
                    shareholderInfo.txtId,
                    shareholderInfo.company_name,
                    shareholderInfo.shareholder,
                    shareholderInfo.fundRatio,
                    shareholderInfo.fundSubcribe,
                    shareholderInfo.mark,
                    shareholderInfo.agency_num,
                    shareholderInfo.agency_name,
                    shareholderInfo.batch]

                value_list = ["'" + str(value) + "'" for value in value_list]
                insert_value += '(' + ','.join(value_list) + ',sysdate' + ')'

                single_oracle.oracle_insert(
                    shareholderInfo.table_name,
                    shareholderInfo.column_name,
                    insert_value)

    # 解析：企业背景-->对外投资
    def html_parse_investInfo(self, index):
        logger.debug("Parse detail info 对外投资 {}".format(self.search_name))
    
        if index == 1 and not isinstance(self.selector, int):
        
            trs = self.selector.xpath('//table/tbody/tr')
        else:
            trs = self.selector.xpath(
                '//div[@id="_container_invest"]/table/tbody/tr')
        # //div[@class="out-investment-container"]/table/tbody/tr
    
        if trs:
            investInfo = TycQybjDwtz()
        
            key = self.search_name
            for tr in trs:
                insert_value = ""
                tds = tr.xpath('./td')
                try:
                    investInfo.investCompany = try_and_text("variable[1].xpath('.//text()')[-1]", tds)
                except:
                    investInfo.investCompany = 'ERROR'
                try:
                    investInfo.investPerson = try_and_text("variable[2].xpath('.//a')[0].xpath('./text()')[0]", tds)
                except:
                    investInfo.investPerson = 'ERROR'
                investInfo.investFund = try_and_text("variable[3].xpath('.//text()')[0]", tds)
                # investInfo.investAmount = tds[4].xpath('string(.)')
                investInfo.investAmount = CURRENT_VERSION_NULL
                investInfo.investRatio = try_and_text("variable[4].xpath('.//text()')[0]", tds)
                investInfo.investDate = try_and_text("variable[5].xpath('.//text()')[0]", tds)
                investInfo.investStatus = try_and_text("variable[6].xpath('.//text()')[0]", tds)
                investInfo.txtId = self.txtId
                investInfo.company_name = key
                investInfo.mark = 0
                investInfo.addtime = 'sysdate'
                investInfo.agency_num = self.agency_num
                investInfo.agency_name = self.agency_name
                investInfo.batch = self.batch
                value_list = [
                    investInfo.txtId,
                    investInfo.company_name,
                    investInfo.investCompany,
                    investInfo.investPerson,
                    investInfo.investFund,
                    investInfo.investAmount,
                    investInfo.investRatio,
                    investInfo.investDate,
                    investInfo.investStatus,
                    investInfo.mark,
                    investInfo.agency_num,
                    investInfo.agency_name,
                    investInfo.batch]
                column_name = "(txt_id,company_name,invest_company,invest_person,invest_fund,invest_amount,invest_ratio,invest_date,invest_status,mark,agency_num,agency_name,batch,add_time)"
                value_list = ["'" + str(value) + "'" for value in value_list]
                insert_value += '(' + ','.join(value_list) + ',sysdate' + ')'
            
                single_oracle.oracle_insert(
                    investInfo.table_name,
                    investInfo.column_name,
                    insert_value)

    # 解析：企业背景-->变更记录
    def html_parse_alterRecord(self, index):
        logger.debug("Parse detail info 变更记录 {}".format(self.search_name))
    
        if index == 1 and not isinstance(self.selector, int):
            trs = self.selector.xpath('//table[position()=1]/tbody/tr')
        else:
            trs = self.selector.xpath(
                '//div[@id="_container_changeinfo"]//table/tbody/tr')
    
        if trs:
            logger.debug('环境编码：{}'.format(sys.getdefaultencoding()))
            key = self.search_name
            for tr in trs:
                insert_value = ""
                alterRecord = TycQybjBgjl()
                tds = tr.xpath('./td')
                tds_len = len(tds)
                alterDate = try_and_text("variable[1].xpath('./text()')", tds)
                alterRecord.alterDate = alterDate[0] if alterDate else 'NA'
                alterProject = try_and_text("variable[2].xpath('./text()')", tds)
                alterRecord.alterProject = alterProject[0] if alterProject else 'NA'
                alterBefor = try_and_text("variable[3].xpath('./div')[0].xpath('string(.)')", tds)
            
                try:
                    alterBefor = replace_special_string(alterBefor)
                except:
                    alterBefor = replace_special_string(alterBefor)
                alterRecord.alterBefor = alterBefor
                alterAfter = try_and_text("variable[4].xpath('./div')[0].xpath('string(.)')", tds)
                # alterAfter = replace_special_string(alterAfter)
            
                alterAfter = replace_special_string(alterAfter)
            
                alterRecord.alterAfter = alterAfter
                # <em><font color="#EF5644">长</font></em>
                alterRecord.txtId = self.txtId
                alterRecord.company_name = key
                # alterRecord.company_name = key
                alterRecord.mark = 0
                alterRecord.addtime = 'sysdate'
                alterRecord.agency_num = self.agency_num
                alterRecord.agency_name = self.agency_name
                alterRecord.batch = self.batch
                value_list = [
                    alterRecord.txtId,
                    alterRecord.company_name,
                    alterRecord.alterDate,
                    alterRecord.alterProject,
                    alterRecord.alterBefor,
                    alterRecord.alterAfter,
                    alterRecord.mark,
                    alterRecord.agency_num,
                    alterRecord.agency_name,
                    alterRecord.batch]
                #
                column_name = "(txt_id,company_name,alter_date,alter_project,alter_befor,alter_after,mark,agency_num,agency_name,batch,add_time)"
            
                # value_list = ["'" + str(value) + "'" for value in value_list]
                # insert_value += '(' + ','.join(value_list) + ',sysdate' + ')'
                # #
                single_oracle.oracle_insert_sql_param(
                    create_insert_sql(
                        alterRecord.table_name, alterRecord.column_name, len(
                            alterRecord.column_name.split(','))), value_list)
                # single_oracle.oracle_insert(alterRecord.table_name, alterRecord.column_name, insert_value)

    # 年报 企业基本信息 第一个table
    def html_parse_year_jbxx(self, year_selector, year):
        logger.debug("Parse detail info 年报基本解析 {}".format(self.search_name))
        # 获得大标签
        if year_selector:
            year_selector = year_selector.replace(u'企业基本信息', 'year_basic_info')
            year_selector = etree.HTML(year_selector)
        trs = year_selector.xpath('// div[text()="year_basic_info"]/parent::*/div/table/tr')
        insert_value = ""
        if trs:
            flss = TycYearJbxx()
            key = self.search_name
            # root_div = root_div[0]
            # 一行是一个tr
        
            flss.credit_num = try_and_text('variable[0].xpath("./td[2]/text()")[0]', trs)
            flss.ent_name = try_and_text('variable[0].xpath("./td[4]/text()")[0]', trs)
            flss.company_tel = try_and_text('variable[1].xpath("./td[2]/text()")[0]', trs)
            flss.postal_code = try_and_text('variable[1].xpath("./td[4]/text()")[0]', trs)
            flss.manager_state = try_and_text('variable[2].xpath("./td[2]/text()")[0]', trs)
            flss.people_count = try_and_text('variable[2].xpath("./td[4]/text()")[0]', trs)
            flss.email = try_and_text('variable[3].xpath("./td[2]/text()")[0]', trs)
            flss.website = try_and_text('variable[3].xpath("./td[4]/text()")[0]', trs)
            flss.company_address = try_and_text('variable[4].xpath("./td[2]/text()")[0]', trs)
            flss.buy_equity = try_and_text('variable[4].xpath("./td[4]/text()")[0]', trs)
            flss.year = year
            flss.txt_id = self.txtId
            flss.company_name = key
            flss.add_time = 'sysdate'
            flss.mark = 0
            flss.agency_num = self.agency_num
            flss.agency_name = self.agency_name
            flss.batch = self.batch
            value_list = [
                flss.credit_num,
                flss.company_name,
                flss.company_tel,
                flss.postal_code,
                flss.manager_state,
                flss.people_count,
                flss.email,
                flss.website,
                flss.company_address,
                flss.buy_equity,
                flss.year,
                flss.txt_id,
                flss.ent_name,
                flss.mark,
                flss.agency_num,
                flss.agency_name,
                flss.batch]
        
            value_list = ["'" + str(value) + "'" for value in value_list]
            insert_value += '(' + ','.join(value_list) + ',sysdate' + ')'
        
            # logger.debug('year html_parse_year_jbxx................',insert_value)
            single_oracle.oracle_insert(
                flss.table_name, flss.column_name, insert_value)

    # 解析年报网站信息
    def html_parse_year_wzhwdxx(self, year_selector, year):
        logger.debug("Parse detail info 企业年报网站信息 {}".format(self.search_name))
        year_selector = year_selector.replace(u'网站或网店信息', 'year_wangzhan')
        if year_selector:
            year_selector = etree.HTML(year_selector)
            # trs = year_selector.xpath('//div[contains(text(),"year_wangzhan")//table/tbody/tr')
            trs = year_selector.xpath(
                '//div[text()="year_wangzhan"]/parent::*//table/tbody/tr')
            # root_div = soup_year.find("div", attrs={"class": "report_website"})
            if trs:
                # 一行是一个tr
                website = TycYearWzhwdxx()
                key = self.search_name
                # root_div = root_div[0]
                # trs = root_div.find("table").find("tbody").find_all("tr")
            
                for tr in trs:
                    insert_value = ""
                    tds = tr.xpath("./td")
                    website.website_type = try_and_text('variable[0].xpath(".//text()")[0]', tds)
                    website.web_name = try_and_text('variable[1].xpath(".//text()")[0]', tds)
                    web_url = try_and_text('variable[2].xpath(".//text()")', tds)
                    logger.debug(
                        'web_url={} {}'.format(
                            web_url, type(web_url)))
                    if web_url:
                        web_url = web_url[0] or 'NA'
                    website.web_url = web_url or 'NA'
                    website.year = year
                    website.txt_id = self.txtId
                    website.company_name = key
                    website.add_time = 'sysdate'
                    website.mark = 0
                    website.agency_num = self.agency_num
                    website.agency_name = self.agency_name
                    website.batch = self.batch
                    value_list = [
                        website.website_type,
                        website.web_name,
                        website.web_url,
                        website.year,
                        website.txt_id,
                        website.company_name,
                        website.mark,
                        website.agency_num,
                        website.agency_name,
                        website.batch]
                
                    #
                    # column_name = "(website_type,web_name,web_url,year,txt_id,company_name,mark,agency_num,agency_name,batch,add_time)"
                
                    value_list = [
                        "'" + str(value) + "'" for value in value_list]
                    insert_value += '(' + ','.join(value_list) + \
                                    ',sysdate' + ')'
                
                    # logger.debug('year html_parse_year_wzhwdxx................', insert_value)
                    single_oracle.oracle_insert(
                        website.table_name, website.column_name, insert_value)

    # 年报 股东及出资信息
    def html_parse_year_gdczxx(self, year_selector, year):
        logger.debug("Parse detail info 股份出资信息 {}".format(self.search_name))
        # 获得分支机构大标签
        year_selector = year_selector.replace(u'股东及出资信息', 'year_gudongchuzi')
        if year_selector:
            year_selector = etree.HTML(year_selector)
        trs = year_selector.xpath(
            '//div[text()="year_gudongchuzi"]/parent::*//table/tbody/tr')
        if trs:
            gdcz = TycYearGdczxx()
            key = self.search_name
            # root_div = root_div[1]
            # 一行是一个tr
        
            for tr in trs:
                insert_value = ""
                tds = tr.xpath("./td")
            
                gdcz.shareholder = try_and_text("variable[0].xpath('.//text()')[0]", tds)
                gdcz.subscirbe_contribution = try_and_text("variable[1].xpath('./text()')[0]", tds)
            
                gdcz.contribution_time = try_and_text("variable[2].xpath('./text()')[0]", tds)
                gdcz.contribution_style = try_and_text("variable[3].xpath('./text()')[0]", tds)
                actual_contribution = try_and_text("variable[4].xpath('./text()')", tds)
                gdcz.actual_contribution = 'NA'
                if actual_contribution:
                    gdcz.actual_contribution = actual_contribution[0]
                gdcz.actual_time = try_and_text("variable[5].xpath('./text()')[0]", tds)
                gdcz.actual_style = try_and_text("variable[6].xpath('./text()')[0]", tds)
                gdcz.year = year
                gdcz.txt_id = self.txtId
                gdcz.company_name = key
                gdcz.add_time = 'sysdate'
                gdcz.mark = 0
                gdcz.agency_num = self.agency_num
                gdcz.agency_name = self.agency_name
                gdcz.batch = self.batch
                value_list = [
                    gdcz.txt_id,
                    gdcz.company_name,
                    gdcz.year,
                    gdcz.shareholder,
                    gdcz.subscirbe_contribution,
                    gdcz.contribution_time,
                    gdcz.contribution_style,
                    gdcz.actual_contribution,
                    gdcz.actual_time,
                    gdcz.actual_style,
                    gdcz.mark,
                    gdcz.agency_num,
                    gdcz.agency_name,
                    gdcz.batch]
                value_list = ["'" + str(value) + "'" for value in value_list]
                insert_value += '(' + ','.join(value_list) + ',sysdate' + ')'
            
                # logger.debug('year html_parse_year_gdczxx................', insert_value)
                single_oracle.oracle_insert(
                    gdcz.table_name, gdcz.column_name, insert_value)

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
        
            flss.total_assets = try_and_text("variable[0].xpath('./td[position()=2]/text()')[0]", trs)
            flss.total_income = try_and_text("variable[0].xpath('td[position()=4]/text()')[0]", trs)
            flss.total_sales = try_and_text("variable[1].xpath('td[position()=2]/text()')[0]", trs)
            flss.total_profit = try_and_text("variable[1].xpath('td[position()=4]/text()')[0]", trs)
            flss.operation_income = try_and_text("variable[2].xpath('td[position()=2]/text()')[0]", trs)
            flss.net_profit = try_and_text("variable[2].xpath('td[position()=4]/text()')[0]", trs)
            flss.total_tax = try_and_text("variable[3].xpath('td[position()=2]/text()')[0]", trs)
            flss.total_debt = try_and_text("variable[3].xpath('td[position()=4]/text()')[0]", trs)
        
            flss.year = year
            flss.txt_id = self.txtId
            flss.company_name = key
            flss.add_time = 'sysdate'
            flss.mark = 0
            flss.agency_num = self.agency_num
            flss.agency_name = self.agency_name
            flss.batch = self.batch
            value_list = [
                flss.batch,
                flss.agency_name,
                flss.agency_num,
                flss.mark,
                flss.total_debt,
                flss.net_profit,
                flss.total_profit,
                flss.total_income,
                flss.total_tax,
                flss.operation_income,
                flss.total_sales,
                flss.total_assets,
                flss.year,
                flss.company_name,
                flss.txt_id]
            #
            column_name = "(batch,agency_name,agency_num,mark,total_debt,net_profit,total_profit,total_income,total_tax,operation_income,total_sales,total_assets,year,company_name,txt_id,add_time)"
        
            value_list = ["'" + str(value) + "'" for value in value_list]
            insert_value += '(' + ','.join(value_list) + ',sysdate' + ')'
        
            single_oracle.oracle_insert(
                flss.table_name, flss.column_name, insert_value)

    # 年报 对外投资
    def html_parse_year_dwtz(self, year_selector, year):
        logger.debug("Parse detail info 对外投资 {}".format(self.search_name))
        year_selector = year_selector.replace(
            u'对外投资信息', 'year_outbound_company')
        if year_selector:
            year_selector = etree.HTML(year_selector)
            # trs = year_selector.xpath('//div[contains(text(),"year_outbound_company")')
            trs = year_selector.xpath(
                '//div[text()="year_outbound_company"]/parent::*//table/tbody/tr')
        
            if trs:
                # trs = trs[0].xpath('.//table/tbody/tr')
                dwtz = TycYearDwtz()
                key = self.search_name
                # root_div = root_div[3]
                # 一行是一个tr
                # trs = root_div.xpath("")
            
                for tr in trs:
                    insert_value = ""
                    tds = tr.xpath("./td")
                    dwtz.credit_num = try_and_text("variable[0].xpath('string(.)')", tds)
                    dwtz.outbound_company = try_and_text("variable[1].xpath('string(.)')", tds)
                
                    dwtz.year = year
                    dwtz.txt_id = self.txtId
                    dwtz.company_name = key
                    dwtz.add_time = 'sysdate'
                    dwtz.mark = 0
                    dwtz.agency_num = self.agency_num
                    dwtz.agency_name = self.agency_name
                    dwtz.batch = self.batch
                    value_list = [
                        dwtz.txt_id,
                        dwtz.mark,
                        dwtz.outbound_company,
                        dwtz.company_name,
                        dwtz.year,
                        dwtz.credit_num,
                        dwtz.agency_num,
                        dwtz.agency_name,
                        dwtz.batch]
                
                    #
                    value_list = [
                        "'" + str(value) + "'" for value in value_list]
                    insert_value += '(' + ','.join(value_list) + \
                                    ',sysdate' + ')'
                
                    single_oracle.oracle_insert(
                        dwtz.table_name, dwtz.column_name, insert_value)

    # 分支机构
    def html_parse_branch(self, index):
        flss = TycQybjFzjg()
        key = self.search_name
        logger.debug("Parse detail info 分支机构 {}".format(self.search_name))
        if index == 1 and not isinstance(self.selector, int):
            root_div = self.selector.xpath(".//table[position()=1]")
        else:
            # 获得分支机构大标签
            root_div = self.selector.xpath(
                '//div[@id="_container_branch"]/table')
        if root_div:
            # 一行是一个tr
            root_div = root_div[0]
            trs = root_div.xpath("./tbody/tr")
        
            for tr in trs:
                insert_value = ""
                tds = tr.xpath("./td")
                ent_name = try_and_text("variable[1].xpath('.//td/a/text()')", tds)
                flss.ent_name = ent_name[0] if ent_name else self.search_name
            
                flss.registered_date = try_and_text("variable[3].xpath('.//text()')[0]", tds)
                flss.status = 'NA'
            
                flss.status = try_and_text("variable[4].xpath('.//text()')[0]", tds)
            
                legal_representative = try_and_text("variable[2].xpath('./div/div[2]/a/text()')", tds)
                logger.debug(
                    '负责人={} type={}'.format(
                        legal_representative,
                        type(legal_representative)))
                if legal_representative:
                    flss.legal_representative = legal_representative[0]
                else:
                    flss.legal_representative = 'NA'
                flss.txt_id = self.txtId
                flss.company_name = key
                flss.add_time = 'sysdate'
                flss.mark = 0
                flss.agency_num = self.agency_num
                flss.agency_name = self.agency_name
                flss.batch = self.batch
                value_list = [
                    flss.txt_id,
                    flss.company_name,
                    flss.ent_name,
                    flss.legal_representative,
                    flss.status,
                    flss.registered_date,
                    flss.mark,
                    flss.agency_num,
                    flss.agency_name,
                    flss.batch]
            
                value_list = ["'" + str(value) + "'" for value in value_list]
                insert_value += '(' + ','.join(value_list) + ',sysdate' + ')'
            
                #
                column_name = "(txt_id,company_name,ent_name,legal_representative,status,register_date,mark,agency_num,agency_name,batch,add_time)"
            
                single_oracle.oracle_insert(
                    flss.table_name, flss.column_name, insert_value)

    # 司法风险
    # 解析：司法风险-->开庭公告
    def html_parse_ktgg(self, index):
        logger.debug("Parse detail info 开庭公告 {}".format(self.search_name))
    
        if index == 1 and not isinstance(self.selector, int):
        
            trs = self.selector.xpath('//table/tbody/tr')
        else:
            trs = self.selector.xpath(
                '//div[@id="_container_announcementcourt"]/table/tbody/tr')
    
        if trs:
            ktggInfo = TycSffxKtgg()
        
            key = self.search_name
            for tr in trs:
                insert_value = ""
                tds = tr.xpath('./td')
                # 开庭日期
                ktggInfo.trialDate = try_and_text("variable[1].xpath('./text()')[0]", tds)
                # 案号
                ktggInfo.reference_num = try_and_text("variable[2].xpath('.//text()')[0]", tds)
                # 案由
                ktggInfo.causeAction = try_and_text("variable[3].xpath('.//text()')[0]", tds)
                # 原告/上诉人
                plaintiff = try_and_text("variable[4].xpath('string(.)')", tds)
                ktggInfo.plaintiff = plaintiff if plaintiff else 'NA'
                # 被告/被上诉人
                ktggInfo.defendant = 'NA'
                try:
                    ktggInfo.defendant = '、'.join(
                        tds[5].xpath('./div//text()'))
                except Exception as e:
                    logger.debug(e)
                # 详情 \u003C\u002Fa\u003E
            
                detail = try_and_text("variable[6].xpath('./script/text()')[0]", tds)
                ktggInfo.detail = replace_special_string(detail)
            
                ktggInfo.txtId = self.txtId
                ktggInfo.company_name = key
                ktggInfo.mark = 0
                ktggInfo.add_time = datetime.now()
                ktggInfo.agency_num = self.agency_num
                ktggInfo.agency_name = self.agency_name
                ktggInfo.batch = self.batch
            
                value_list = [
                    ktggInfo.detail,
                    ktggInfo.defendant,
                    ktggInfo.plaintiff,
                    ktggInfo.reference_num,
                    ktggInfo.causeAction,
                    ktggInfo.trialDate,
                    ktggInfo.batch,
                    ktggInfo.agency_name,
                    ktggInfo.agency_num,
                    ktggInfo.mark,
                    ktggInfo.company_name,
                    ktggInfo.txtId]
                insert_sql = create_insert_sql(
                    ktggInfo.table_name, ktggInfo.column_name, len(
                        ktggInfo.column_name.split(',')))
                single_oracle.oracle_insert_sql_param(insert_sql, value_list)

    # 法律诉讼
    def html_parse_lawsuit(self, index):
        logger.debug("Parse detail info 法律诉讼 {}".format(self.search_name))
        if index == 1:
            root_div = self.selector.xpath('//table/tbody/tr')
        else:
            root_div = self.selector.xpath(
                '//div[@id="_container_lawsuit"]/table/tbody/tr')
        if root_div:
            flss = TycSffxFlss()
            key = self.search_name
            # 一行是一个tr
            # root_div = root_div[0]
            # trs = root_div.xpath(".")
        
            law_count = 0
            for tr in root_div:
                insert_value = ""
                tds = tr.xpath("./td")
                if tds:
                    flss.judgment_date = try_and_text("variable[1].xpath('./span/text()')[0]", tds)
                    # flss.judgment_document = try_and_text("variable[2].xpath('./a/text()')[0]", tds)
                
                    tds_href = try_and_text("variable[2].xpath('./a/@href')[0]", tds)
                    flss.judgment_name = try_and_text("variable[2].xpath('./a//text()')[0]", tds)
                    name = try_and_text("variable[2].xpath('./a/text()')[0]", tds)
                    flss.document_url = tds_href if tds_href else 'NA'
                    case_type = try_and_text("variable[3].xpath('./span/text()')", tds)
                    flss.case_type = case_type[0] if case_type else 'NA'
                    # case_identity = try_and_text("variable[4].xpath('.//text()')", tds)
                    # flss.case_identity = ','.join(
                    #     case_identity) if case_identity else 'NA'
                    s1 = s2 = ''
                    plaintiff = try_and_text("variable[4].xpath('./div[position()=1]//text()')", tds)
                    defendant = try_and_text("variable[4].xpath('./div[position()=2]//text()')", tds)
                    if len(plaintiff) != 0:
                        for i in plaintiff:
                            s1 += i
                    if len(defendant) != 0:
                        for j in defendant:
                            s2 += j
                    flss.case_identity = s1 + ';' + s2

                    case_number = try_and_text("variable[5].xpath('./span/text()')", tds)
                    flss.case_number = case_number[0] if case_number else 'NA'
                    flss.txt_id = self.txtId
                
                    flss.company_name = key
                    flss.add_time = 'sysdate'
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
                
                    flss.judgment_document = replace_special_string(text_info)
                    value_list = [
                        flss.txt_id,
                        flss.company_name,
                        flss.judgment_date,
                        flss.judgment_name,
                        flss.judgment_document,
                        flss.case_type,
                        flss.case_identity,
                        flss.case_number,
                        flss.document_url,
                        flss.mark,
                        flss.detail_status,
                        flss.agency_num,
                        flss.agency_name,
                        flss.batch
                    ]
                    insert_sql = create_insert_sql(
                        flss.table_name, flss.column_name, len(
                            flss.column_name.split(',')))
                    single_oracle.oracle_insert_sql_param(
                        insert_sql, value_list)

    # 法院公告
    def html_parse_announcement(self, index):
        logger.debug("Parse detail info 法院公告 {}".format(self.search_name))
        if index == 1 and not isinstance(self.selector, int):
            root_div = self.selector.xpath('//table')
        else:
            # 获得法院公告大标签
            root_div = self.selector.xpath(
                '//div[@id="_container_court"]/table')
    
        if root_div:
            flss = TycSffxFygg()
            key = self.search_name
            # 一行是一个tr
            root_div = root_div[0]
            trs = root_div.xpath("./tbody/tr")
        
            for tr in trs:
                insert_value = ""
                tds = tr.xpath("./td")
                flss.announcement_date = try_and_text("variable[1].xpath('./text()')[0]", tds)
                plaintiff = try_and_text("variable[2].xpath('string(.)')", tds)
                if plaintiff:
                    flss.plaintiff = plaintiff
                defendant = try_and_text("variable[3].xpath('string(.)')", tds)
                flss.defendant = defendant if defendant else 'NA'
            
                flss.announcement_type = try_and_text("variable[4].xpath('string(.)')", tds)
                flss.court = try_and_text("variable[5].xpath('string(.)')", tds)
                text_info = try_and_text("variable[6].xpath('./script/text()')[0]", tds)
                text_info = replace_special_string(text_info)
                flss.detail_info = text_info
                flss.txt_id = self.txtId
                flss.company_name = key
                flss.add_time = 'sysdate'
                flss.mark = 0
                flss.agency_num = self.agency_num
                flss.agency_name = self.agency_name
                flss.batch = self.batch
                value_list = [
                    flss.txt_id,
                    flss.company_name,
                    flss.announcement_date,
                    flss.plaintiff,
                    flss.defendant,
                    flss.announcement_type,
                    flss.court,
                    flss.detail_info,
                    flss.mark,
                    flss.agency_num,
                    flss.agency_name,
                    flss.batch]
                insert_sql = create_insert_sql(
                    flss.table_name, flss.column_name, len(
                        flss.column_name.split(',')))
                single_oracle.oracle_insert_sql_param(insert_sql, value_list)

    # 失信人
    def html_parse_shixinren(self, index):
        logger.debug("Parse detail info 失信人{}".format(self.search_name))
        if index == 1 and not isinstance(self.selector, int):
            root_div = self.selector.xpath("//table[position()=1]")
        else:
            # 获得失信人大标签
            root_div = self.selector.xpath(
                '//div[@id="_container_dishonest"][position()=1]/table')
        if root_div:
            flss = TycSffxSxr()
            key = self.search_name
            # 一行是一个tr
        
            root_div = root_div[0]
            trs = root_div.xpath("./tbody/tr")
        
            for tr in trs:
                insert_value = ""
                tds = tr.xpath("./td")
                case_date = try_and_text("variable[1].xpath('.//text()')", tds)
                case_number = try_and_text("variable[2].xpath('.//text()')", tds)
                execution_court = try_and_text("variable[3].xpath('.//text()')", tds)
                performance_state = try_and_text("variable[4].xpath('.//text()')", tds)
                execute_number = try_and_text("variable[5].xpath('.//text()')", tds)
            
                flss.case_date = case_date[0] if case_date else 'NA'
                flss.case_number = case_number[0] if case_number else 'NA'
                flss.execution_court = execution_court[0] if execution_court else 'NA'
                flss.performance_state = performance_state[0] if performance_state else 'NA'
                flss.execute_number = execute_number[0] if execute_number else 'NA'
                href = try_and_text("variable[6].xpath('./span/@onclick')[0]", tds)
                res = re.search(r'"(.*?)"', href).groups(1)
                href = res[0]
                text_info = 'NA'
                try:
                    text_info = self.detail_info["_container_dishonest"][href]
                    text_info = replace_special_string(text_info)
                except BaseException:
                    pass
                flss.detail_info = text_info
            
                flss.txt_id = self.txtId
                flss.company_name = key
                flss.add_time = 'sysdate'
                flss.mark = 0
                flss.agency_num = self.agency_num
                flss.agency_name = self.agency_name
                flss.batch = self.batch
                value_list = [
                    flss.txt_id,
                    flss.company_name,
                    flss.case_date,
                    flss.case_number,
                    flss.execution_court,
                    flss.performance_state,
                    flss.execute_number,
                    flss.detail_info,
                    flss.mark,
                    flss.agency_num,
                    flss.agency_name,
                    flss.batch]
            
                insert_sql = create_insert_sql(
                    flss.table_name, flss.column_name, len(
                        flss.column_name.split(',')))
                single_oracle.oracle_insert_sql_param(insert_sql, value_list)
                # value_list = ["'" + str(value) + "'" for value in value_list]
                # insert_value += '(' + ','.join(value_list) + ',sysdate' + ')'
                #
                # # logger.debug(insert_value)
                # single_oracle.oracle_insert(flss.table_name, flss.column_name, insert_value)

    # 被执行人
    def html_parse_executed(self, index):
        logger.debug("Parse detail info 被执行人{}".format(self.search_name))
        if index == 1 and not isinstance(self.selector, int):
            root_div = self.selector.xpath("//table[position()=1]")
        else:
            # 获得被执行人大标签
            root_div = self.selector.xpath(
                '//div[@id="_container_zhixing"][position()=1]/table')
        if root_div:
            flss = TycSffxBzxr()
            key = self.search_name
            root_div = root_div[0]
            # 一行是一个tr
            trs = root_div.xpath("./tbody/tr")
        
            for tr in trs:
                insert_value = ""
                tds = tr.xpath("./td")
                flss.record_date = try_and_text("variable[1].xpath('./text()')[0]", tds)
                flss.execute_underlying = try_and_text("variable[2].xpath('./text()')[0]", tds)
                flss.case_number = try_and_text("variable[3].xpath('./text()')[0]", tds)
                flss.court = try_and_text("variable[4].xpath('./text()')[0]", tds)
                href = try_and_text("variable[5].xpath('./span/@onclick')[0]", tds)
                res = re.search(r'"(.*?)"', href).groups(1)
                href = res[0]
                text_info = 'NA'
                try:
                    text_info = self.detail_info["_container_zhixing"][href]
                    text_info = replace_special_string(text_info)
                except BaseException:
                    pass
                flss.detail = text_info
            
                flss.txt_id = self.txtId
                flss.company_name = key
                flss.add_time = 'sysdate'
                flss.mark = 0
                flss.agency_num = self.agency_num
                flss.agency_name = self.agency_name
                flss.batch = self.batch
                value_list = [
                    flss.agency_num,
                    flss.agency_name,
                    flss.batch,
                    flss.txt_id,
                    flss.company_name,
                    flss.record_date,
                    flss.execute_underlying,
                    flss.case_number,
                    flss.court,
                    flss.mark,
                    flss.detail]
            
                insert_sql = create_insert_sql(
                    flss.table_name, flss.column_name, len(
                        flss.column_name.split(',')))
                single_oracle.oracle_insert_sql_param(insert_sql, value_list)

    # 解析：司法风险-->司法协助
    def html_parse_sfxz(self, index):
        logger.debug("Parse detail info 司法协助 {}".format(self.search_name))
        if index == 1 and not isinstance(self.selector, int):
        
            trs = self.selector.xpath('//table/tbody/tr')
        else:
            trs = self.selector.xpath(
                '//div[@id="_container_judicialAid"]/table/tbody/tr')
        if trs:
            sfxzInfo = TycSffxSfxz()
        
            key = self.search_name
        
            for tr in trs:
                insert_value = ""
                tds = tr.xpath('./td')
                # 被执行人
                sfxzInfo.enforcementPerson = try_and_text("variable[1].xpath('./text()')[0]", tds)
                # 股权数额
                sfxzInfo.equityAmount = try_and_text("variable[2].xpath('./text()')[0]", tds)
                # 执行法院
                sfxzInfo.executiveCourt = try_and_text("variable[3].xpath('./text()')[0]", tds)
                # 执行通知文号
                sfxzInfo.approvalNum = try_and_text("variable[4].xpath('./text()')[0]", tds)
                # 类型|状态
                sfxzInfo.status = try_and_text("variable[5].xpath('./text()')[0]", tds)
                href = try_and_text("variable[6].xpath('./span/@onclick')[0]", tds)
                res = re.search(r'"(.*?)"', href).groups(1)
                href = res[0]
                text_info = 'NA'
                try:
                    text_info = self.detail_info["_container_judicialAid"][href]
                    text_info = replace_special_string(text_info)
                except BaseException:
                    pass
                sfxzInfo.detail = text_info
                sfxzInfo.txtId = self.txtId
                sfxzInfo.company_name = key
                sfxzInfo.mark = 0
                sfxzInfo.add_time = datetime.now()
                sfxzInfo.agency_num = self.agency_num
                sfxzInfo.agency_name = self.agency_name
                sfxzInfo.batch = self.batch
            
                value_list = [
                    sfxzInfo.txtId,
                    sfxzInfo.company_name,
                    sfxzInfo.mark,
                    sfxzInfo.agency_num,
                    sfxzInfo.agency_name,
                    sfxzInfo.batch,
                    sfxzInfo.enforcementPerson,
                    sfxzInfo.equityAmount,
                    sfxzInfo.executiveCourt,
                    sfxzInfo.approvalNum,
                    sfxzInfo.status,
                    sfxzInfo.detail]
            
                insert_sql = create_insert_sql(
                    sfxzInfo.table_name, sfxzInfo.column_name, len(
                        sfxzInfo.column_name.split(',')))
                single_oracle.oracle_insert_sql_param(insert_sql, value_list)

    # 经营风险
    # 经营异常
    def html_parse_abnormal(self, index):
        logger.debug("Parse detail info 经营异常 {}".format(self.search_name))
        if index == 1 and not isinstance(self.selector, int):
            root_div = self.selector.xpath("//table/tbody/tr")
        else:
            # 获得经营异常大标签
            root_div = self.selector.xpath(
                '//div[@id= "_container_abnormal"]/table/tbody/tr')
        if root_div:
            flss = TycJyfxJyyc()
            key = self.search_name
            # 一行是一个tr
            # root_div = root_div[0]
            # trs = root_div.xpath(".")
        
            for tr in root_div:
                insert_value = ""
                tds = tr.xpath("./td")
                # 加入
                insert_date = try_and_text("variable[1].xpath('.//text()')[0]", tds)
                flss.insert_date = insert_date
                insert_cause = try_and_text("variable[2].xpath('.//text()')[0]", tds)
                logger.debug(
                    '列入原因={} type={}'.format(
                        insert_cause,
                        type(insert_cause)))
                flss.insert_cause = insert_cause
                insert_department = 'NA'
                insert_department = try_and_text("variable[3].xpath('.//text()')[0]", tds)
                flss.insert_department = insert_department
            
                flss.out_date = CURRENT_VERSION_NULL
                flss.out_cause = CURRENT_VERSION_NULL
                flss.out_department = CURRENT_VERSION_NULL
                # 新增 移除日期
                try:
                    out_date = try_and_text("variable[4].xpath('.//text()')[0]", tds)
                    flss.out_date = out_date if out_date else 'NA'
                    # 新增  移除原因
                    out_cause = try_and_text("variable[5].xpath('.//text()')[0]", tds)
                    flss.out_cause = out_cause if out_cause else 'NA'
                    # 新增 移除机关
                    out_department = try_and_text("variable[6].xpath('.//text()')[0]", tds)
                    flss.out_department = out_department if out_department else 'NA'
                except BaseException:
                    pass
            
                flss.txt_id = self.txtId
                flss.company_name = key
                flss.add_time = 'sysdate'
                flss.mark = 0
                flss.agency_num = self.agency_num
                flss.agency_name = self.agency_name
                flss.batch = self.batch
            
                value_list = [
                    flss.txt_id,
                    flss.company_name,
                    flss.insert_date,
                    flss.insert_cause,
                    flss.insert_department,
                    flss.mark,
                    flss.agency_num,
                    flss.agency_name,
                    flss.batch,
                    flss.out_date,
                    flss.out_cause,
                    flss.out_department]
                value_list = ["'" + str(value) + "'" for value in value_list]
                insert_value += '(' + ','.join(value_list) + ',sysdate' + ')'
            
                single_oracle.oracle_insert(
                    flss.table_name, flss.column_name, insert_value)

    # 行政处罚
    def html_parse_xingzhengchufa(self, index):
        logger.debug("Parse detail info 行政处罚{}".format(self.search_name))
        if index == 1 and not isinstance(self.selector, int):
            root_div = self.selector.xpath("//table[position()=1]")
        else:
            # 获得行政处罚大标签
            root_div = self.selector.xpath(
                '//div[@id="_container_punish"][position()=1]/table')
        if root_div:
            flss = TycJyfxXzcf()
            key = self.search_name
            # 一行是一个tr
            root_div = root_div[0]
            trs = root_div.xpath("./tbody/tr")
        
            for tr in trs:
                insert_value = ""
                tds = tr.xpath("./td")
                try:
                    flss.punishment_name = CURRENT_VERSION_NULL
                    flss.punishment_area = CURRENT_VERSION_NULL
                    flss.decision_date = try_and_text("variable[1].xpath('./text()')[0]", tds)
                    flss.decision_number = try_and_text("variable[2].xpath('./text()')[0]", tds)
                    flss.punishment_contents = try_and_text("variable[3].xpath('./text()')[0]", tds)
                    # flss.type = try_and_text("variable[4].xpath('./text()')[0]",tds)
                    flss.type = CURRENT_VERSION_NULL
                    flss.decision_department = try_and_text("variable[4].xpath('./text()')[0]",
                                                            tds)
                    flss.detail_info = try_and_text("variable[5].xpath('./script/text()')[0]", tds)
                    # tds[5].text.replace("详情 》", "").strip().replace("'", '\\"')
                except BaseException:
                    flss.decision_date = ""
                    flss.decision_number = ""
                    flss.type = ""
                    flss.decision_department = ""
                    flss.punishment_name = try_and_text("variable[1].xpath('text()')[0]", tds)
                    flss.punishment_area = try_and_text("variable[2].xpath('text()')[0]", tds)
                    flss.detail_info = try_and_text("variable[3].xpath('./script/text()')[0]", tds)
                    # tds[3].text.replace("详情 》", "").strip().replace("'", '\\"')
                flss.txt_id = self.txtId
                try:
                    flss.company_name = key
                except:
                    flss.company_name = key
            
                flss.add_time = 'sysdate'
                flss.mark = 0
                flss.agency_num = self.agency_num
                flss.agency_name = self.agency_name
                flss.batch = self.batch
                value_list = [
                    flss.txt_id,
                    flss.company_name,
                    flss.decision_date,
                    flss.decision_number,
                    flss.punishment_contents,
                    flss.type,
                    flss.decision_department,
                    flss.detail_info,
                    flss.punishment_name,
                    flss.punishment_area,
                    flss.mark,
                    flss.agency_num,
                    flss.agency_name,
                    flss.batch]
            
                insert_sql = create_insert_sql(
                    flss.table_name, flss.column_name, len(
                        flss.column_name.split(',')))
                single_oracle.oracle_insert_sql_param(insert_sql, value_list)
                # value_list = ["'" + str(value) + "'" for value in value_list]
                # insert_value += '(' + ','.join(value_list) + ',sysdate' + ')'
                #
                # single_oracle.oracle_insert(flss.table_name, flss.column_name, insert_value)

    # 解析：经营风险--严重违法
    def html_parse_illegalSerious(self):
        logger.debug("Parse detail info 严重违法 {}".format(self.search_name))
    
        trs = self.selector.xpath(
            '//div[@id="_container_illegal"]/table/tbody/tr')
        if trs:
        
            key = self.search_name
            for tr in trs:
                insert_value = ""
                illegalSerious = TycJyfxYzwf()
                tds = tr.xpath('./td')
                illegalSerious.illegalDate = try_and_text(
                    "variable[1].xpath('text()')[0]", tds)
                illegalSerious.illegalReason = try_and_text(
                    "variable[2].xpath('text()')[0] ", tds)
                illegalSerious.office = try_and_text(
                    "variable[3].xpath('text()')[0]", tds)
                # 新增移出
                illegalSerious.out_date = 'NA'
                illegalSerious.out_reason = 'NA'
                illegalSerious.out_department = 'NA'
                # 移出日期
                try:
                    out_date = try_and_text("variable[4].xpath('./text()')", tds)
                    illegalSerious.out_date = out_date[0] if out_date else 'NA'
                    # 移出原因
                    out_reason = try_and_text("variable[5].xpath('./text()')[0]", tds)
                    illegalSerious.out_reason = out_reason[0] if out_reason else 'NA'
                    # 移出决定机关
                    out_department = try_and_text("variable[6].xpath('./text()')[0]", tds)
                    illegalSerious.out_department = out_department[0] if out_department else 'NA'
                except BaseException:
                    pass
            
                illegalSerious.txtId = self.txtId
                illegalSerious.company_name = key
                illegalSerious.mark = 0
                illegalSerious.addtime = 'sysdate'
                illegalSerious.agency_num = self.agency_num
                illegalSerious.agency_name = self.agency_name
                illegalSerious.batch = self.batch
                value_list = [
                    illegalSerious.out_date,
                    illegalSerious.out_reason,
                    illegalSerious.out_department,
                    illegalSerious.txtId,
                    illegalSerious.company_name,
                    illegalSerious.illegalDate,
                    illegalSerious.illegalReason,
                    illegalSerious.office,
                    illegalSerious.mark,
                    illegalSerious.agency_num,
                    illegalSerious.agency_name,
                    illegalSerious.batch]
                value_list = ["'" + str(value) + "'" for value in value_list]
                insert_value += '(' + ','.join(value_list) + ',sysdate' + ')'
            
                single_oracle.oracle_insert(
                    illegalSerious.table_name,
                    illegalSerious.column_name,
                    insert_value)

    # 股权出质
    def html_parse_pledge(self, index):
        # 无变化
        logger.debug("Parse detail info 股权出质{}".format(self.search_name))
        if index == 1 and not isinstance(self.selector, int):
            root_div = self.selector.xpath("//table/tbody/tr")
        elif index == 0:
            # 获得股权出质大标签  nav-main-equityCount
            root_div = self.selector.xpath(
                '//div[@id="_container_equity"]/table/tbody/tr')
        if root_div:
            logger.debug(
                'cccc有股权出质。。。。。。。。。。。。。。。。。{}'.format(
                    self.search_name))
            flss = TycJyfxGqcz()
            key = self.search_name
            # 一行是一个tr
            # root_div = root_div[0]
            # trs = root_div.xpath(".")
        
            for tr in root_div:
                insert_value = ""
                tds = tr.xpath("./td")
                # #logger.debug(tds.xpath('text()'))
                flss.announcement_date = try_and_text("variable[1].xpath('.//text()')[0]", tds)
                flss.registration_number = try_and_text("variable[2].xpath('.//text()')[0]", tds)
            
                flss.pledgor = try_and_text("variable[3].xpath('.//text()')[0]", tds)
                flss.pledgee = try_and_text("variable[4].xpath('.//text()')[0]", tds)
                flss.status = try_and_text("variable[5].xpath('.//text()')[0]", tds)
                flss.pledged_amount = try_and_text("variable[6].xpath('.//text()')[0]", tds)
                text_info = try_and_text("variable[7].xpath('./script/text()')[0]", tds)
                text_info = replace_special_string(text_info)
                flss.detail_info = text_info
                # tds[6].text.replace("详情 》", "").strip().replace("'", '\\"')
                flss.txt_id = self.txtId
                flss.company_name = key
                flss.add_time = 'sysdate'
                flss.mark = 0
                flss.agency_num = self.agency_num
                flss.agency_name = self.agency_name
                flss.batch = self.batch
                value_list = [
                    flss.announcement_date,
                    flss.registration_number,
                    flss.pledgor,
                    flss.pledgee,
                    flss.status,
                    flss.pledged_amount,
                    flss.detail_info,
                    flss.txt_id,
                    flss.company_name,
                    flss.mark,
                    flss.agency_num,
                    flss.agency_name,
                    flss.batch]
            
                # value_list = ["'" + str(value) + "'" for value in value_list]
                # insert_value += '(' + ','.join(value_list) + ',sysdate' + ')'
            
                # single_oracle.oracle_insert(flss.table_name, flss.column_name, insert_value)
                insert_sql = create_insert_sql(
                    flss.table_name, flss.column_name, len(
                        flss.column_name.split(',')))
                single_oracle.oracle_insert_sql_param(insert_sql, value_list)

    # 动产抵押
    def html_parse_dongchandiya(self, index):
        logger.debug("Parse detail info 动产抵押{}".format(self.search_name))
        if index == 1 and not isinstance(self.selector, int):
            root_div = self.soup.find("//table/tbody/tr")
        else:
            # 获得动产抵押大标签
            root_div = self.selector.xpath(
                "//div[@id='_container_mortgage']/table/tbody/tr")
        if root_div:
            logger.debug(
                'cccc有动产抵押。。。。。。。。。。。。。。。。。{}'.format(
                    self.search_name))
        
            key = self.search_name
            # 一行是一个tr
        
            for tr in root_div:
                flss = tycJyfxDcdy()
                insert_value = ""
                tds = tr.xpath('./td')
                flss.registration_date = try_and_text("variable[1].xpath('./text()')[0]", tds)
                flss.registration_number = try_and_text("variable[2].xpath('./text()')[0]", tds)
                flss.guarantee_amount = try_and_text("variable[4].xpath('./text()')[0]", tds)
                flss.guarantee_type = try_and_text("variable[3].xpath('./text()')[0]", tds)
                flss.registration_department = try_and_text("variable[5].xpath('./text()')[0]", tds)
                flss.status = try_and_text("variable[6].xpath('./text()')[0]", tds)
            
                detail_info = try_and_text("variable[7].xpath('.//script/text()')[0]", tds)
                # tds[7].text.replace("详情 》", "").strip().replace("'", '\\"')
                flss.detail_info = replace_special_string(detail_info)
                flss.txt_id = self.txtId
                flss.company_name = key
                flss.add_time = 'sysdate'
                flss.mark = 0
                flss.agency_num = self.agency_num
                flss.agency_name = self.agency_name
                flss.batch = self.batch
                value_list = [
                    flss.registration_date,
                    flss.registration_number,
                    flss.guarantee_type,
                    flss.guarantee_amount,
                    flss.registration_department,
                    flss.status,
                    flss.detail_info,
                    flss.txt_id,
                    flss.company_name,
                    flss.mark,
                    flss.agency_num,
                    flss.agency_name,
                    flss.batch]
            
                print('tycJyfxDcdy==============', value_list)
                insert_sql = create_insert_sql(
                    flss.table_name, flss.column_name, len(
                        flss.column_name.split(',')))
                single_oracle.oracle_insert_sql_param(insert_sql, value_list)

    # 解析：经营风险--欠税公告
    def html_parse_taxesNotice(self, index):
        logger.debug("Parse detail info 欠税公告{}".format(self.search_name))
        if index == 1 and not isinstance(self.selector, int):
            trs = self.selector.xpath(
                '//table/tbody/tr')
        else:
            trs = self.selector.xpath(
                '//div[@id="_container_towntax"][position()=1]//table[position()=1]/tbody/tr')
        if trs:
        
            key = self.search_name
            taxesNotice = TycJyfxQsgg()
            for tr in trs:
                insert_value = ""
                tds = tr.xpath('./td')
                taxesNotice.taxesDate = try_and_text("variable[1].xpath('text()')[0]", tds)
                taxesNotice.taxesNum = try_and_text("variable[2].xpath('text()')[0]", tds)
                taxesNotice.taxesType = try_and_text("variable[3].xpath('text()')[0]", tds)
                taxesNotice.taxesMoney = try_and_text("variable[4].xpath('text()')[0]", tds)
                taxesNotice.taxesBalance = try_and_text("variable[5].xpath('text()')[0]", tds)
                taxesNotice.taxesOffice = try_and_text("variable[6].xpath('text()')[0]", tds)
                # 新增 详情
                taxesNotice.detail = try_and_text("variable[7].xpath('./script/text()')[0]", tds)
            
                taxesNotice.txtId = self.txtId
                taxesNotice.company_name = key
                taxesNotice.mark = 0
                taxesNotice.addtime = 'sysdate'
                taxesNotice.agency_num = self.agency_num
                taxesNotice.agency_name = self.agency_name
                taxesNotice.batch = self.batch
            
                value_list = [
                    taxesNotice.detail,
                    taxesNotice.batch,
                    taxesNotice.agency_name,
                    taxesNotice.agency_num,
                    taxesNotice.mark,
                    taxesNotice.taxesOffice,
                    taxesNotice.taxesBalance,
                    taxesNotice.taxesMoney,
                    taxesNotice.taxesType,
                    taxesNotice.taxesNum,
                    taxesNotice.taxesDate,
                    taxesNotice.company_name,
                    taxesNotice.txtId]
            
                value_list = ["'" + str(value) + "'" for value in value_list]
                insert_value += '(' + ','.join(value_list) + ',sysdate' + ')'
            
                single_oracle.oracle_insert(
                    taxesNotice.table_name,
                    taxesNotice.column_name,
                    insert_value)

    # 解析：经营风险-->司法拍卖
    def html_parse_sfpm(self, index):
        logger.debug("Parse detail info 司法拍卖 {}".format(self.search_name))
        if index == 1 and not isinstance(self.selector, int):
        
            trs = self.selector.xpath('//table/tbody/tr')
        else:
            trs = self.selector.xpath(
                '//div[@id="_container_judicialSale"]/table/tbody/tr')
        if trs:
            sfpaInfo = TycJyfxSfpm()
        
            key = self.search_name
        
            for tr in trs:
                insert_value = ""
                tds = tr.xpath('./td')
                # 拍卖公告
                sfpaInfo.auctionNotice = try_and_text("variable[1].xpath('./a/text()')[0]", tds)
                # 公告日期
                sfpaInfo.auctionDate = try_and_text("variable[2].xpath('./text()')[0]", tds)
                # 执行法院
                sfpaInfo.executeCourt = try_and_text("variable[3].xpath('./text()')[0]", tds)
                # 拍卖标的
                sfpaInfo.auctionTarget = try_and_text("variable[4].xpath('string(.)')", tds)
                text_info = 'NA'
                href = try_and_text("variable[1].xpath('./a/@href')[0]", tds)
                # 新增 详情 brand  TODO:详情
                try:
                    text_info = self.detail_info["_container_judicialSale"][href.split('/')[-1].replace('.', '_')]
                except BaseException:
                    pass
                sfpaInfo.auction_detail = replace_special_string(text_info)
            
                # sfpaInfo.auction_detail = '详情'
            
                sfpaInfo.txtId = self.txtId
                sfpaInfo.company_name = key
                sfpaInfo.mark = 0
                sfpaInfo.add_time = datetime.now()
                sfpaInfo.agency_num = self.agency_num
                sfpaInfo.agency_name = self.agency_name
                sfpaInfo.batch = self.batch
                value_list = [
                    sfpaInfo.auction_detail,
                    sfpaInfo.txtId,
                    sfpaInfo.company_name,
                    sfpaInfo.auctionNotice,
                    sfpaInfo.auctionDate,
                    sfpaInfo.executeCourt,
                    sfpaInfo.auctionTarget,
                    sfpaInfo.mark,
                    sfpaInfo.agency_num,
                    sfpaInfo.agency_name,
                    sfpaInfo.batch]
                # value_list = ["'" + str(value) + "'" for value in value_list]
                # insert_value += '(' + ','.join(value_list) + ',sysdate' + ')'
            
                insert_sql = create_insert_sql(
                    sfpaInfo.table_name, sfpaInfo.column_name, len(
                        sfpaInfo.column_name.split(',')))
                single_oracle.oracle_insert_sql_param(insert_sql, value_list)

    # 解析：经营风险-->清算信息
    def html_parse_qsxx(self, index):
        logger.debug("Parse detail info 清算信息 {}".format(self.search_name))
    
        if index == 1 and not isinstance(self.selector, int):
        
            trs = self.selector.xpath('//table/tbody/tr')
        else:
            trs = self.selector.xpath(
                '//div[@id="_container_clearingCount"]/table/tbody/tr')
        if trs:
            qsxxInfo = TycJyfxQsxx()
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
        
            qsxxInfo.txtId = self.txtId
            qsxxInfo.company_name = key
            qsxxInfo.mark = 0
            qsxxInfo.add_time = datetime.now()
            qsxxInfo.agency_num = self.agency_num
            qsxxInfo.agency_name = self.agency_name
            qsxxInfo.batch = self.batch
        
            value_list = [
                qsxxInfo.member,
                qsxxInfo.principal,
                qsxxInfo.batch,
                qsxxInfo.agency_name,
                qsxxInfo.agency_num,
                qsxxInfo.mark,
                qsxxInfo.company_name,
                qsxxInfo.txtId]
            value_list = ["'" + str(value) + "'" for value in value_list]
            insert_value += '(' + ','.join(value_list) + ',sysdate' + ')'
        
            single_oracle.oracle_insert(
                qsxxInfo.table_name,
                qsxxInfo.column_name,
                insert_value)

    # 解析：经营风险-->公示催告
    def html_parse_gscg(self):
        logger.debug("Parse detail info 公示催告 {}".format(self.search_name))
    
        trs = self.selector.xpath(
            '//div[@id="_container_publicnoticeItem"]/table/tbody/tr')
    
        if trs:
            gscgInfo = TycJyfxGscg()
        
            key = self.search_name
        
            for tr in trs:
                insert_value = ""
                tds = tr.xpath('./td')
                # 票据号
                gscgInfo.billNumber = try_and_text("variable[1].xpath('.//text()')[0]", tds)
                # 票据类型
                gscgInfo.billType = try_and_text("variable[2].xpath('.//text()')[0]", tds)
                # 票面金额
                gscgInfo.denomination = try_and_text("variable[3].xpath('.//text()')[0]", tds)
                # 发布机构
                gscgInfo.publishAuthority = try_and_text("variable[4].xpath('.//text()')[0]", tds)
                # 公告日期
                gscgInfo.announcementDate = try_and_text("variable[5].xpath('.//text()')[0]", tds)
                # 详情
                text_info = try_and_text("variable[6].xpath('.//text()')[0]", tds)
                text_info = replace_special_string(text_info)
                gscgInfo.detail = text_info
            
                gscgInfo.txtId = self.txtId
                gscgInfo.company_name = key
                gscgInfo.mark = 0
                gscgInfo.add_time = datetime.now()
                gscgInfo.agency_num = self.agency_num
                gscgInfo.agency_name = self.agency_name
                gscgInfo.batch = self.batch
            
                value_list = [
                    gscgInfo.txtId,
                    gscgInfo.company_name,
                    gscgInfo.billNumber,
                    gscgInfo.billType,
                    gscgInfo.denomination,
                    gscgInfo.publishAuthority,
                    gscgInfo.announcementDate,
                    gscgInfo.detail,
                    gscgInfo.mark,
                    gscgInfo.agency_num,
                    gscgInfo.agency_name,
                    gscgInfo.batch]
                print('公示催告TycJyfxGscg========', value_list)
                insert_sql = create_insert_sql(
                    gscgInfo.table_name, gscgInfo.column_name, len(
                        gscgInfo.column_name.split(',')))
                single_oracle.oracle_insert_sql_param(insert_sql, value_list)
    
    # 解析：企业发展-->融资历史
    def html_parse_financeHistory(self):
        # TODO
        logger.debug("Parse detail info 融资历史 {}".format(self.search_name))
        trs = (self.selector.xpath(
            '//div[@id="_container_rongzi"]/table/tbody/tr'))

        if trs:
            financeHistory = TycQyfzRzls()

            key = self.search_name
            for tr in trs:
                insert_value = ""
                tds = tr.xpath('./td')
                financeHistory.financeDate = try_and_text("variable[1].xpath('string(.)')", tds)
                financeHistory.event_date = try_and_text("variable[2].xpath('string(.)')", tds)
                financeHistory.financeRound = try_and_text("variable[4].xpath('string(.)')", tds)
                financeHistory.financeValue = try_and_text("variable[5].xpath('string(.)')", tds)
                financeHistory.financeMoney = try_and_text("variable[3].xpath('string(.)')", tds)
                financeHistory.financeRatio = try_and_text("variable[6].xpath('string(.)')", tds)
                financeHistory.financeInvestor = try_and_text("','.join(variable[7].xpath('.//text()'))", tds)
                source = try_and_text("variable[8].xpath('.//text()')[0]", tds)
                financeHistory.financeSource = source
                financeHistory.txtId = self.txtId
                financeHistory.company_name = key
                financeHistory.mark = 0
                financeHistory.addtime = 'sysdate'
                financeHistory.agency_num = self.agency_num
                financeHistory.agency_name = self.agency_name
                financeHistory.batch = self.batch
                value_list = [
                    financeHistory.batch,
                    financeHistory.agency_name,
                    financeHistory.agency_num,
                    financeHistory.mark,
                    financeHistory.financeSource,
                    financeHistory.financeInvestor,
                    financeHistory.financeRatio,
                    financeHistory.financeMoney,
                    financeHistory.financeValue,
                    financeHistory.financeRound,
                    financeHistory.financeDate,
                    financeHistory.event_date,
                    financeHistory.company_name,
                    financeHistory.txtId]

                value_list = ["'" + str(value) + "'" for value in value_list]
                insert_value += '(' + ','.join(value_list) + ',sysdate' + ')'

                single_oracle.oracle_insert(
                    financeHistory.table_name,
                    financeHistory.column_name,
                    insert_value)

    # 解析：企业背景--核心团队
    def html_parse_coreTeam(self, index):
        logger.debug("Parse detail info 核心团队 {}".format(self.search_name))
        if index == 1 and not isinstance(self.selector, int):
            trs = self.selector.xpath('//table/tbody/tr')
        else:
            trs = self.selector.xpath(
                '//div[@id="_container_teamMember"]/div/table/tbody/tr')
    
        if trs:
        
            coreTeam = TycQyfzHxtd()
            key = self.search_name
            # divs = divs[0]
            # trs=divs[0].xpath()
            for tr in trs:
                insert_value = ""
                tds = tr.xpath('./td')
                if tds[1].xpath('.//a/text()'):
                    personName = tds[1].xpath('.//a/text()')[0]
                else:
                    personName = tds[1].xpath('.//span/text()')[1]
                coreTeam.personName = personName
            
                coreTeam.position = try_and_text("variable[2].xpath('.//text()')[0]", tds)
                personInfo = replace_special_string(try_and_text("variable[3].xpath('./div/div/text()')[0]", tds))
            
                coreTeam.personInfo = ''.join(personInfo)
                coreTeam.txtId = self.txtId
                coreTeam.company_name = key
                coreTeam.mark = 0
                coreTeam.addtime = 'sysdate'
                coreTeam.agency_num = self.agency_num
                coreTeam.agency_name = self.agency_name
                coreTeam.batch = self.batch
                value_list = [
                    coreTeam.txtId,
                    coreTeam.company_name,
                    coreTeam.personName,
                    coreTeam.position,
                    coreTeam.personInfo,
                    coreTeam.mark,
                    coreTeam.agency_num,
                    coreTeam.agency_name,
                    coreTeam.batch]
                value_list = ["'" + str(value) + "'" for value in value_list]
                insert_value += '(' + ','.join(value_list) + ',sysdate' + ')'
                single_oracle.oracle_insert(
                    coreTeam.table_name, coreTeam.column_name, insert_value)

    # 解析：企业背景--企业业务
    def html_parse_entBusiness(self, index):
        logger.debug("Parse detail info 企业业务 {}".format(self.search_name))
        if index == 1 and not isinstance(self.selector, int):
            trs = self.selector.xpath('//table/tbody/tr')
        else:
            trs = self.selector.xpath(
                '//div[@id="_container_firmProduct"]/table/tbody/tr')
    
        if trs:
            entBusiness = TycQyfzQyyw()
        
            key = self.search_name
            # divs = divs[0]
            for tr in trs:
                tds = tr.xpath('./td')
                insert_value = ""
                entBusiness.businessName = try_and_text("variable[1].xpath('.//td//text()')[-1]", tds)
                entBusiness.businessQuale = try_and_text("variable[2].xpath('.//text()')[-1]", tds)
                entBusiness.businessInfo = try_and_text("variable[3].xpath('./div/div//text()')[0]", tds)
                entBusiness.txtId = self.txtId
                entBusiness.company_name = key
                entBusiness.mark = 0
                entBusiness.addtime = 'sysdate'
                entBusiness.agency_num = self.agency_num
                entBusiness.agency_name = self.agency_name
                entBusiness.batch = self.batch
                value_list = [
                    entBusiness.batch,
                    entBusiness.agency_name,
                    entBusiness.agency_num,
                    entBusiness.mark,
                    entBusiness.businessInfo,
                    entBusiness.businessQuale,
                    entBusiness.businessName,
                    entBusiness.company_name,
                    entBusiness.txtId]
                #
                value_list = ["'" + str(value) + "'" for value in value_list]
            
                insert_value += '(' + ','.join(value_list) + ',sysdate' + ')'
            
                single_oracle.oracle_insert(
                    entBusiness.table_name,
                    entBusiness.column_name,
                    insert_value)

    # 解析：企业背景--投资事件
    def html_parse_investEvent(self, index):
        logger.debug("Parse detail info 投资事件 {}".format(self.search_name))
        if index == 1 and not isinstance(self.selector, int):
            trs = self.selector.xpath('//table/tbody/tr')
        else:
            trs = self.selector.xpath(
                '//div[@id="_container_touzi"]/table/tbody/tr')
    
        if trs:
            investEvent = TycQyfzTzsj()
        
            key = self.search_name
        
            for tr in trs:
                insert_value = ""
                tds = tr.xpath('./td')
                investEvent.touziDate = try_and_text("variable[1].xpath('string(.)')", tds)
                investEvent.touziRound = try_and_text("variable[2].xpath('string(.)')", tds)
                investEvent.touziMoney = try_and_text("variable[3].xpath('string(.)')", tds)
                investEvent.touziEnt = try_and_text("variable[4].xpath('string(.)')", tds)
                investEvent.touziProduct = try_and_text("(variable[5].xpath('.//a/text()'))[0]", tds)
                investEvent.touziArea = try_and_text("variable[6].xpath('string(.)')", tds)
                investEvent.touziIndustry = try_and_text("variable[7].xpath('string(.)')", tds)
                #investEvent.touziBusiness = try_and_text("variable[8].xpath('string(.)')", tds)
                touziEnt = try_and_text("variable[4].xpath('.//text()')", tds)
                touziEnt = [s for s in touziEnt if len(s.strip()) >= 4]
                investEvent.touziEnt = str(touziEnt)[1:-1].replace("'", '')

                investEvent.txtId = self.txtId
                investEvent.company_name = key
                investEvent.mark = 0
                investEvent.addtime = 'sysdate'
                investEvent.agency_num = self.agency_num
                investEvent.agency_name = self.agency_name
                investEvent.batch = self.batch
                value_list = [
                    investEvent.txtId,
                    investEvent.company_name,
                    investEvent.touziDate,
                    investEvent.touziRound,
                    investEvent.touziMoney,
                    investEvent.touziEnt,
                    investEvent.touziProduct,
                    investEvent.touziArea,
                    investEvent.touziIndustry,
                    investEvent.touziBusiness,
                    investEvent.mark,
                    investEvent.agency_num,
                    investEvent.agency_name,
                    investEvent.batch]
                #
                column_name = "(txt_id,company_name,touzi_date,touzi_round,touzi_money,touzi_ent,touzi_product,touzi_area,touzi_industry,touzi_business,mark,agency_num,agency_name,batch,add_time)"
            
                value_list = ["'" + str(value) + "'" for value in value_list]
                insert_value += '(' + ','.join(value_list) + ',sysdate' + ')'
            
                single_oracle.oracle_insert(
                    investEvent.table_name,
                    investEvent.column_name,
                    insert_value)

    # 解析：企业背景--竞品信息   docker cp /etc/localtime: 2 /etc/localtime
    def html_parse_jpInfo(self, index):
        # TODO 解析有问题
        logger.debug("Parse detail info 竞品信息 {}".format(self.search_name))
        if index == 1 and not isinstance(self.selector, int):
            trs = self.selector.xpath('//table[@class="table"]/tbody/tr')
        else:
            trs = self.selector.xpath(
                '//div[@id="_container_jingpin"]/div/table/tbody/tr')
    
        if trs:
            jpInfo = TycQyfzJpxx()
            key = self.search_name
            for tr in trs:
                insert_value = ""
                tds = tr.xpath('./td')
                #jpInfo.jpProduct = try_and_text("variable[1].xpath('.//a/text()')[0]", tds)
                jpInfo.jpProduct = try_and_text("variable[1].xpath('.//img/alt')[0]", tds)
                jpInfo.jpArea = try_and_text("variable[2].xpath('.//text()')[0]", tds)
                jpInfo.jpRound = try_and_text("variable[3].xpath('.//text()')[0]", tds)
                jpInfo.jpIndustry = try_and_text("variable[4].xpath('.//text()')[0]", tds)
                jpInfo.jpBusiness = try_and_text("variable[5].xpath('.//text()')[0]", tds)
                jpInfo.jpDate = try_and_text("variable[6].xpath('.//text()')[0]", tds)
                jpInfo.jpValue = try_and_text("variable[7].xpath('.//text()')[0]", tds)
                jpInfo.txtId = self.txtId
                jpInfo.company_name = key
                jpInfo.mark = 0
                jpInfo.addtime = 'sysdate'
                jpInfo.agency_num = self.agency_num
                jpInfo.agency_name = self.agency_name
                jpInfo.batch = self.batch
                value_list = [
                    jpInfo.txtId,
                    jpInfo.company_name,
                    jpInfo.jpProduct,
                    jpInfo.jpArea,
                    jpInfo.jpRound,
                    jpInfo.jpIndustry,
                    jpInfo.jpBusiness,
                    jpInfo.jpDate,
                    jpInfo.jpValue,
                    jpInfo.mark,
                    jpInfo.agency_num,
                    jpInfo.agency_name,
                    jpInfo.batch]
            
                value_list = ["'" + str(value) + "'" for value in value_list]
                insert_value += '(' + ','.join(value_list) + ',sysdate'')'
            
                single_oracle.oracle_insert(
                    jpInfo.table_name, jpInfo.column_name, insert_value)

    # 招聘
    def html_parse_recruitment(self, index):
        logger.debug("Parse detail info 招聘 {}".format(self.search_name))
    
        # 判断分页
        if index == 1 and not isinstance(self.selector, int):
            # 获得招聘大标签
            root_div = self.selector.xpath('//table[position()=1]/tbody/tr')
        else:
            root_div = self.selector.xpath(
                '//div[@id="_container_recruit"][position()=1]//table')
            if not root_div:
                root_div = self.selector.xpath(
                    '//div[@id="_container_baipin"]/table/tbody/tr')
    
        if root_div:
            # 一行是一个
            flss = TycJyzkZp()
            key = self.search_name
            # root_div = root_div[0]
            for tr in root_div:  # bodys
                tds = tr.xpath('./td')
                tr_hrefs = try_and_text('variable[7].xpath(".//a/@href")[0]', tds)
                insert_value = ""
                flss.publish_date = try_and_text("variable[1].xpath('.//text()')[0]", tds)
                flss.recruitment_job = try_and_text("variable[2].xpath('.//text()')[0]", tds)
                flss.salary = try_and_text("variable[3].xpath('.//text()')[0]", tds)
                education = try_and_text("variable[4].xpath('.//text()')[0]", tds)
                work_year = try_and_text("variable[5].xpath('.//text()')[0]", tds)
                flss.work_city = try_and_text("variable[6].xpath('.//text()')[0]", tds)
            
                flss.work_year = work_year
                flss.recruitment_numbers = '此版本无此信息'
                flss.education = education
                href = tr_hrefs
            
                # 新增 详情 brand
                text_info = 'NA'
                try:
                    text_info_key = href.split(r'/')[-1].replace('.', '_')
                    text_info = self.detail_info["_container_baipin"][text_info_key]
                except BaseException:
                    text_info = '解析出错'
                flss.detail_info = replace_special_string(text_info)
                flss.txt_id = self.txtId
                flss.company_name = key
                flss.add_time = 'sysdate'
                flss.mark = 0
                flss.agency_num = self.agency_num
                flss.agency_name = self.agency_name
                flss.batch = self.batch
                value_list = [
                    flss.work_city,
                    flss.detail_info,
                    flss.education,
                    flss.mark,
                    flss.agency_num,
                    flss.agency_name,
                    flss.batch,
                    flss.txt_id,
                    flss.company_name,
                    flss.publish_date,
                    flss.recruitment_job,
                    flss.salary,
                    flss.work_year,
                    flss.recruitment_numbers]
                single_oracle.oracle_insert_sql_param(
                    create_insert_sql(
                        flss.table_name, flss.column_name, len(
                            flss.column_name.split(','))), value_list)
                # value_list = ["'" + str(value) + "'" for value in value_list]
                # insert_value += '(' + ','.join(value_list) + ',sysdate' + ')'
                #
                # single_oracle.oracle_insert(flss.table_name, flss.column_name, insert_value)

    # 解析：经营状况-->行政许可【工商局】
    def html_parse_gsj(self, index):
        logger.debug("Parse detail info 工商局 {}".format(self.search_name))
    
        if index == 1 and not isinstance(self.selector, int):
            trs = self.selector.xpath('//table/tbody/tr')

            # gsjInfo = TycJyzkGsj()
            # key = self.search_name
            # for tr in trs:
            #     insert_value = ""
            #     tds = tr.xpath('./td')
            #     # 许可书文编号
            #     gsjInfo.licenseDocNum = try_and_text("variable[1].xpath('./text()')[0]", tds)
            #     # 许可文件名称
            #     gsjInfo.licenseDocName = try_and_text("variable[2].xpath('./text()')[0]", tds)
            #     # 有效期自
            #     gsjInfo.validityBegin = try_and_text("variable[3].xpath('./text()')[0]", tds)
            #     # 有效期至
            #     gsjInfo.validityEnd = try_and_text("variable[4].xpath('./text()')[0]", tds)
            #     # 许可机关
            #     gsjInfo.licenseAuthority = try_and_text("variable[5].xpath('./text()')[0]", tds)
            #     # 许可内容
            #     gsjInfo.licenseContent = try_and_text("variable[6].xpath('./text()')[0]", tds)
    
        else:
            trs = self.selector.xpath(
                '//div[@id="_container_licensing"]/table/tbody/tr')
            if trs:
                gsjInfo = TycJyzkGsj()
                key = self.search_name
            
                for tr in trs:
                    insert_value = ""
                    tds = tr.xpath('./td')
                    # 许可书文编号
                    gsjInfo.licenseDocNum = try_and_text("variable[1].xpath('./text()')[0]", tds)
                    # 许可文件名称
                    gsjInfo.licenseDocName = try_and_text("variable[2].xpath('./text()')[0]", tds)
                    # 有效期自
                    gsjInfo.validityBegin = try_and_text("variable[3].xpath('./text()')[0]", tds)
                    # 有效期至
                    gsjInfo.validityEnd = try_and_text("variable[4].xpath('./text()')[0]", tds)
                    # 许可机关
                    gsjInfo.licenseAuthority = try_and_text("variable[5].xpath('./text()')[0]", tds)
                    # 许可内容
                    gsjInfo.licenseContent = try_and_text("variable[6].xpath('./text()')[0]", tds)
            
                    gsjInfo.txtId = self.txtId
                    gsjInfo.company_name = key
                    gsjInfo.mark = 0
                    gsjInfo.add_time = datetime.now()
                    gsjInfo.agency_num = self.agency_num
                    gsjInfo.agency_name = self.agency_name
                    gsjInfo.batch = self.batch

                    value_list = [
                        gsjInfo.batch,
                        gsjInfo.agency_name,
                        gsjInfo.agency_num,
                        gsjInfo.mark,
                        gsjInfo.licenseContent,
                        gsjInfo.licenseAuthority,
                        gsjInfo.validityEnd,
                        gsjInfo.validityBegin,
                        gsjInfo.licenseDocName,
                        gsjInfo.licenseDocNum,
                        gsjInfo.company_name,
                        gsjInfo.txtId]

                    #
                    column_name = "(batch,agency_name,agency_num,mark,license_content,license_authority,validity_end,validity_begin,license_document_name,license_documet_num,company_name,txt_id,add_time)"

                    value_list = ["'" + str(value) + "'" for value in value_list]
                    insert_value += '(' + ','.join(value_list) + ',sysdate' + ')'

                    single_oracle.oracle_insert(
                        gsjInfo.table_name, gsjInfo.column_name, insert_value)

    # 解析：经营状况-->行政许可【信用中国】
    def html_parse_xyzg(self, index):
        logger.debug("Parse detail info 信用中国 {}".format(self.search_name))
    
        if index == 1 and not isinstance(self.selector, int):
        
            trs = self.selector.xpath('//table/tbody/tr')
        else:
            trs = self.selector.xpath(
                '//div[@id="_container_licensingXyzg"]//table/tbody/tr')
        if trs:
            dxxkInfo = TycJyzkXyzg()
        
            key = self.search_name
        
            for tr in trs:
                insert_value = ""
                tds = tr.xpath('./td')
                # 行政许可文书号
                dxxkInfo.licenseDocNum = try_and_text("variable[1].xpath('.//text()')[0]", tds)
                # 许可决定机关
                dxxkInfo.licenseAuthority = try_and_text("variable[2].xpath('.//text()')[0]", tds)
                # 许可决定日期
                dxxkInfo.licenseDate = try_and_text("variable[3].xpath( './/text()')[0]", tds)
                # 详情
                text_info = try_and_text("variable[4].xpath('.//script/text()')[0]", tds)
                text_info = replace_special_string(text_info)
                dxxkInfo.detail = text_info
            
                dxxkInfo.txtId = self.txtId
                dxxkInfo.company_name = key
                dxxkInfo.mark = 0
                dxxkInfo.add_time = datetime.now()
                dxxkInfo.agency_num = self.agency_num
                dxxkInfo.agency_name = self.agency_name
                dxxkInfo.batch = self.batch
            
                value_list = [
                    dxxkInfo.txtId,
                    dxxkInfo.company_name,
                    dxxkInfo.licenseDocNum,
                    dxxkInfo.licenseAuthority,
                    dxxkInfo.licenseDate,
                    dxxkInfo.detail,
                    dxxkInfo.mark,
                    dxxkInfo.agency_num,
                    dxxkInfo.agency_name,
                    dxxkInfo.batch]
                #
                # column_name = "(txt_id,company_name,license_documet_num,license_authority,license_date,detail,mark,agency_num,agency_name,batch,add_time)"
            
                insert_sql = create_insert_sql(
                    dxxkInfo.table_name, dxxkInfo.column_name, len(
                        dxxkInfo.column_name.split(',')))
                single_oracle.oracle_insert_sql_param(insert_sql, value_list)
                # value_list = ["'" + str(value) + "'" for value in value_list]
                # insert_value += '(' + ','.join(value_list) + ',sysdate' + ')'
                #
                # single_oracle.oracle_insert(dxxkInfo.table_name, dxxkInfo.column_name, insert_value)

    # 税务评级
    def html_parse_tax(self, index):
        logger.debug("Parse detail info 税务评级{}".format(self.search_name))
        if index == 1 and not isinstance(self.selector, int):
            root_div = self.selector.xpath("//table[position()=1]")
        else:
            # 获得税务评级大标签
            root_div = self.selector.xpath(
                '//div[@id="_container_taxcredit"][position()=1]/table')
        if root_div:
            flss = TycJyzkSwpj()
            key = self.search_name
            root_div = root_div[0]
            # 一行是一个tr
            trs = root_div.xpath("./tbody/tr")
        
            for tr in trs:
                insert_value = ""
                tds = tr.xpath("td")
                flss.year = try_and_text("variable[1].xpath('./text()')[0]", tds)
                flss.tax_rating = try_and_text("variable[2].xpath('./text()')[0]", tds)
                flss.tax_type = try_and_text("variable[3].xpath('./text()')[0]", tds)
                flss.tax_identification_number = try_and_text("variable[4].xpath('./text()')[0]", tds)
                flss.evaluate_department = try_and_text("variable[5].xpath('./text()')[0]", tds)
                flss.txt_id = self.txtId
                flss.ent_name = key
                flss.add_time = 'sysdate'
                flss.mark = 0
                flss.agency_num = self.agency_num
                flss.agency_name = self.agency_name
                flss.batch = self.batch
                value_list = [
                    flss.txt_id,
                    flss.ent_name,
                    flss.year,
                    flss.tax_rating,
                    flss.tax_type,
                    flss.tax_identification_number,
                    flss.evaluate_department,
                    flss.mark,
                    flss.agency_num,
                    flss.agency_name,
                    flss.batch]
            
                value_list = ["'" + str(value) + "'" for value in value_list]
                insert_value += '(' + ','.join(value_list) + ',sysdate' + ')'
            
                single_oracle.oracle_insert(
                    flss.table_name, flss.column_name, insert_value)

    # 抽查检查
    def html_parse_check(self, index):
        logger.debug("Parse detail info 抽查检查 {}".format(self.search_name))
        if index == 1 and not isinstance(self.selector, int):
            root_div = (self.selector.xpath('//table/tbody/tr'))
        else:
            # 获得抽查检查大标签
            root_div = (self.selector.xpath(
                '//div[@id="_container_check"]//table/tbody/tr'))
        if root_div:
            flss = TycJyzkCcjc()
            key = self.search_name
            # 一行是一个tr
            # root_div = root_div[0]
            # trs = root_div.xpath(".")
            #
            for tr in root_div:
                insert_value = ""
                tds = tr.xpath("./td")
                flss.check_date = try_and_text("variable[1].xpath('.//text()')[0]", tds)
                flss.type = try_and_text("variable[2].xpath('.//text()')[0]", tds)
                flss.result = try_and_text("variable[3].xpath('.//text()')[0]", tds)
                flss.check_department = try_and_text("variable[4].xpath('.//text()')[0]", tds)
                flss.txt_id = self.txtId
                flss.company_name = key
                flss.add_time = 'sysdate'
                flss.mark = 0
                flss.agency_num = self.agency_num
                flss.agency_name = self.agency_name
                flss.batch = self.batch
                value_list = [
                    flss.check_date,
                    flss.type,
                    flss.result,
                    flss.check_department,
                    flss.txt_id,
                    flss.company_name,
                    flss.mark,
                    flss.agency_num,
                    flss.agency_name,
                    flss.batch]
                # column_name = "(check_date, type, result, check_department, txt_id, company_name, mark ,agency_num,agency_name,batch,add_time)"
            
                value_list = ["'" + str(value) + "'" for value in value_list]
                insert_value += '(' + ','.join(value_list) + ',sysdate' + ')'
            
                single_oracle.oracle_insert(flss.table_name, flss.column_name, insert_value)

    # 解析：经营状况--资质证书
    def html_parse_certificateInfo(self, index):
        key = self.search_name
        logger.debug("Parse detail info 资质证书 {}".format(self.search_name))
        if index == 1 and not isinstance(self.selector, int):
            trs = self.selector.xpath('//table[position()=1]/tbody/tr')
        else:
            trs = self.selector.xpath(
                '//div[@id="_container_certificate"][position()=1]//table[position()=1]/tbody/tr')
    
        if trs:
            certificateInfo = TycJyzkZzzs()
            for tr in trs:
                insert_value = ""
                tds = tr.xpath('./td')
                certificateInfo.certificateType = try_and_text("variable[1].xpath('./span/text()')[0]", tds)
                certificateInfo.certificateNum = try_and_text("variable[2].xpath('./span/text()')[0]", tds)
                certificateInfo.sendDate = try_and_text("variable[3].xpath('./span/text()')[0]", tds)
                certificateInfo.offDate = try_and_text("variable[4].xpath('./span/text()')[0]", tds)
                # certificateInfo.deviceNum = tds[4].xpath('string(.)')
                # certificateInfo.permitNum = tds[5].xpath('string(.)')
                # 新增 证书详情
                href = try_and_text("variable[1].xpath('./span/@onclick')[0]", tds)
                res = re.search(r"certificatePopup\('(.*?)'\)", href).groups(1)
                href = res[0]
                text_info = 'NA'
                try:
                    text_info = self.detail_info["_container_certificate"][href]
                except BaseException:
                    pass
                certificateInfo.detail = replace_special_string(text_info)
                certificateInfo.txtId = self.txtId
                certificateInfo.company_name = key
                certificateInfo.mark = 0
                certificateInfo.addtime = 'sysdate'
                certificateInfo.agency_num = self.agency_num
                certificateInfo.agency_name = self.agency_name
                certificateInfo.batch = self.batch
                value_list = [
                    certificateInfo.detail,
                    certificateInfo.txtId,
                    certificateInfo.company_name,
                    certificateInfo.certificateNum,
                    certificateInfo.certificateType,
                    certificateInfo.sendDate,
                    certificateInfo.offDate,
                    certificateInfo.mark,
                    certificateInfo.agency_num,
                    certificateInfo.agency_name,
                    certificateInfo.batch]
            
                #
                # column_name = "(detail,txt_id,company_name,certificate_num,certificate_type,send_date,off_date,mark,agency_num,agency_name,batch,add_time)"
            
                # value_list = ["'" + str(value) + "'" for value in value_list]
                # insert_value += '(' + ','.join(value_list) + ',sysdate' + ')'
                #
                # single_oracle.oracle_insert(
                #     certificateInfo.table_name,
                #     certificateInfo.column_name,
                #     insert_value)
                insert_sql = create_insert_sql(
                    certificateInfo.table_name, certificateInfo.column_name, len(
                        certificateInfo.column_name.split(',')))
                single_oracle.oracle_insert_sql_param(
                    insert_sql, value_list)

    # 招投标
    def html_parse_bidding(self, index):
        logger.debug("Parse detail info 招投标{}".format(self.search_name))
        if index == 1 and not isinstance(self.selector, int):
            root_div = self.selector.xpath('//table')
        else:
            # 获得招投标大标签
            root_div = self.selector.xpath(
                '//div[@id="_container_bid"][position()=1]/table')
        if root_div:
            flss = TycJyzkZtb()
            key = self.search_name
            # 一行是一个tr
            root_div = root_div[0]
            trs = root_div.xpath("./tbody/tr")
        
            for tr in trs:
                insert_value = ""
                tds = tr.xpath("./td")
                flss.publish_date = try_and_text("variable[1].xpath('./text()')[0]", tds)
                flss.title = try_and_text("variable[2].xpath('./a/text()')[0]", tds)
                flss.title_url = try_and_text("variable[2].xpath('./a/@href')[0]", tds)
                flss.procurement = try_and_text("variable[3].xpath('./text()')[0]", tds)
                flss.txt_id = self.txtId
                flss.company_name = key
                flss.add_time = 'sysdate'
                flss.mark = 0
                flss.agency_num = self.agency_num
                flss.agency_name = self.agency_name
                flss.batch = self.batch
                value_list = [
                    flss.txt_id,
                    flss.company_name,
                    flss.publish_date,
                    flss.title,
                    flss.title_url,
                    flss.procurement,
                    flss.mark,
                    flss.agency_num,
                    flss.agency_name,
                    flss.batch]
            
                value_list = ["'" + str(value) + "'" for value in value_list]
                insert_value += '(' + ','.join(value_list) + ',sysdate' + ')'
            
                single_oracle.oracle_insert(
                    flss.table_name, flss.column_name, insert_value)
    
    # 产品信息
    def html_parse_product(self, index):
        logger.debug("Parse detail info 产品信息 {}".format(self.search_name))
        if index == 1 and not isinstance(self.selector, int):
            root_div = (self.selector.xpath('//table/tbody/tr'))
        else:
            # 获得产品信息大标签
            root_div = self.selector.xpath(
                '//div[@id="_container_product"]/table/tbody/tr')
        if root_div:
            flss = TycJyzkCpxx()
            key = self.search_name
            # 一行是一个tr
            # root_div = root_div[0]
            # trs = root_div.xpath("./tbody/tr")

            for tr in root_div:
                insert_value = ""
                tds = tr.xpath("./td")
                flss.product_name = try_and_text("variable[1].xpath('.//span/text()')[0]", tds)
                flss.product_referred = try_and_text("variable[2].xpath('.//text()')[0]", tds)
                flss.product_classification = try_and_text("variable[3].xpath('.//text()')[0]", tds)
                flss.field = try_and_text("variable[4].xpath('.//text()')[0]", tds)
                href = try_and_text("variable[5].xpath('./a/@href')[0]", tds)
                text_info = 'NA'
                try:
                    text_info = self.detail_info["_container_product"][href.split(
                        r'/')[-1]]
                    text_info = replace_special_string(text_info)
                except BaseException:
                    pass
                flss.detail_info = text_info
                flss.txt_id = self.txtId
                flss.company_name = key
                flss.add_time = 'sysdate'
                flss.mark = 0
                flss.agency_num = self.agency_num
                flss.agency_name = self.agency_name
                flss.batch = self.batch
                value_list = [
                    flss.txt_id,
                    flss.company_name,
                    flss.product_name,
                    flss.product_referred,
                    flss.product_classification,
                    flss.field,
                    flss.detail_info,
                    flss.mark,
                    flss.agency_num,
                    flss.agency_name,
                    flss.batch]
                # column_name = "(txt_id,company_name,product_name,product_referred,product_classification,field,detail_info,mark,agency_num,agency_name,batch,add_time)"
                single_oracle.oracle_insert_sql_param(
                    create_insert_sql(
                        flss.table_name, flss.column_name, len(
                            flss.column_name.split(','))), value_list)
                # insert_value += '(' + ','.join(value_list) + ',sysdate' + ')'
                #
                # single_oracle.oracle_insert(flss.table_name, flss.column_name, insert_value)

    # 微信公众号解析
    def html_parse_entWechat(self, index):
        logger.debug("Parse detail info 微信公众号 {}".format(self.search_name))
        if index:
            trs = self.selector.xpath('//table[@class="table"]/tbody/tr')
        else:
            trs = self.selector.xpath('//div[@id="_container_wechat"]/table/tbody/tr')
    
        if trs:
            entWeChat = TycJyzkWxgzh()
        
            key = self.search_name
            for tr in trs:
                insert_value = ""
                #entWeChat.mp_name = try_and_text("variable.xpath('./td')[1].xpath('.//span/text()')[1]", tr)
                entWeChat.mp_name = try_and_text("variable.xpath('./td')[1].xpath('.//td')[1].xpath('./span/text()')[0]", tr)

                entWeChat.mp_number = try_and_text("variable.xpath('./td')[2].xpath('./span/text()')[0]", tr)
                entWeChat.mp_info = try_and_text("variable.xpath('./td')[4].xpath('./div/div/text()')[0]", tr)
                #entWeChat.detail = try_and_text("variable.xpath('./td')[5].xpath('./script/text()')[0]", tr)  # 新增
                detail = try_and_text("variable.xpath('./td')[5].xpath('./script/text()')[0]", tr)   # 新增
                entWeChat.detail = replace_special_string(detail)

                entWeChat.txtId = self.txtId
                entWeChat.company_name = key
                entWeChat.mark = 0
                entWeChat.addtime = 'sysdate'
                entWeChat.agency_num = self.agency_num
                entWeChat.agency_name = self.agency_name
                entWeChat.batch = self.batch
                value_list = [
                    entWeChat.txtId,
                    entWeChat.company_name,
                    entWeChat.mp_name,
                    entWeChat.mp_number,
                    entWeChat.mp_info,
                    entWeChat.mark,
                    entWeChat.detail,
                    entWeChat.agency_num,
                    entWeChat.agency_name,
                    entWeChat.batch]
            
                # value_list = ["'" + str(value) + "'" for value in value_list]
                # insert_value += '(' + ','.join(value_list) + ',sysdate' + ')'
                #
                # single_oracle.oracle_insert(
                #     entWeChat.table_name, entWeChat.column_name, insert_value)
                column_name = "(txt_id,company_name,mp_name,mp_number,mp_info,mark,detail,agency_num,agency_name,batch,add_time)"
            
                insert_sql = create_insert_sql(entWeChat.table_name, entWeChat.column_name, len(
                    entWeChat.column_name.split(','))
                                               )
                single_oracle.oracle_insert_sql_param(insert_sql, value_list)
            
                # 进出口信用

    def html_parse_outputxy(self):
        logger.debug("Parse detail info 进出口信用 {}".format(self.search_name))
        # 获得大标签
        root_div = self.selector.xpath(
            '//div[@id="_container_importAndExport"]//table/tbody/tr')
        if root_div:
            flss = TycJyzkJckxy()
            key = self.search_name
            # 一行是一个tr
    
            for tr in root_div:
                insert_value = ""
                tds = tr.xpath("./td")
                flss.register_customs = try_and_text("variable[1].xpath('./text()')[0]", tds)
                flss.industry_category = try_and_text("variable[2].xpath('./text()')[0]", tds)
                flss.manager_type = try_and_text("variable[3].xpath('./text()')[0]", tds)
                flss.register_date = try_and_text("variable[4].xpath('./text()')[0]", tds)
                flss.detail_info = 'NA'
                detail_info = try_and_text("variable[5].xpath('.//script/text()')[0]", tds)
                flss.detail_info = replace_special_string(detail_info)
                flss.txtId = self.txtId
                flss.company_name = key
                flss.add_time = 'sysdate'
                flss.mark = 0
                flss.agency_num = self.agency_num
                flss.agency_name = self.agency_name
                flss.batch = self.batch
                flss.customs_number = CURRENT_VERSION_NULL
                value_list = [
                    flss.txtId,
                    flss.company_name,
                    flss.register_customs,
                    flss.customs_number,
                    flss.industry_category,
                    flss.manager_type,
                    flss.register_date,
                    flss.detail_info,
                    flss.mark,
                    flss.agency_num,
                    flss.agency_name,
                    flss.batch]

                # column_name = "(txt_id,company_name,register_customs,customs_number,industry_category,manager_type,register_date,detail_info,mark,agency_num,agency_name,batch,add_time)"

                single_oracle.oracle_insert_sql_param(
                    create_insert_sql(
                        flss.table_name, flss.column_name, len(
                            flss.column_name.split(','))), value_list)
                # value_list = ["'" + str(value) + "'" for value in value_list]
                # insert_value += '(' + ','.join(value_list) + ',sysdate' + ')'
                #
                # single_oracle.oracle_insert(flss.table_name, flss.column_name, insert_value)

    # 债券信息
    def html_parse_zhaiquan(self, index):
        logger.debug("Parse detail info 债券信息{}".format(self.search_name))
        if index == 1 and not isinstance(self.selector, int):
            root_div = self.selector.xpath("//table[position()=1]")
        else:
            # 获得债券信息大标签
            root_div = self.selector.xpath('//div[@id="_container_bond"]/table')
        
        if root_div:
    
            flss = TycJyzkZqxx()
            logger.debug(
                'cccc有债券信息。。。。。。。。。。。。。。。。。{}'.format(
                    self.search_name))
            key = self.search_name
            # 一行是一个tr
            root_div = root_div[0]
            trs = root_div.xpath("./tbody/tr")
    
            for tr in trs:
                insert_value = ""
                tds = tr.xpath("./td")
                flss.publish_date = try_and_text("variable[1].xpath('.//text()')[0]", tds)
                flss.bond_name = try_and_text("variable[2].xpath('.//text()')[0]", tds)
                flss.bond_code = try_and_text("variable[3].xpath('.//text()')[0]", tds)
                flss.bond_type = try_and_text("variable[4].xpath('.//text()')[0]", tds)
                flss.latest_rating = try_and_text("variable[5].xpath('.//text()')[0]", tds)
                text_info = try_and_text("variable[6].xpath('.//script/text()')[0]", tds)
                text_info = replace_special_string(text_info)
                flss.detail_info = text_info
                # tds[6].text.replace("详情 》", "").strip().replace("'", '\\"')
                flss.txt_id = self.txtId
                flss.company_name = key
                # flss.add_time = 'sysdate'
                flss.mark = 0
                flss.agency_num = self.agency_num
                flss.agency_name = self.agency_name
                flss.batch = self.batch
                value_list = [
                    flss.batch,
                    flss.agency_name,
                    flss.agency_num,
                    flss.mark,
                    flss.detail_info,
                    flss.latest_rating,
                    flss.bond_type,
                    flss.bond_code,
                    flss.bond_name,
                    flss.publish_date,
                    flss.company_name,
                    flss.txt_id]

                insert_sql = create_insert_sql(
                    flss.table_name, flss.column_name, len(
                        flss.column_name.split(',')))
                single_oracle.oracle_insert_sql_param(insert_sql, value_list)

                # value_list = ["'" + str(value) + "'" for value in value_list]
                # insert_value += '(' + ','.join(value_list) + ',sysdate' + ')'
                #
                # single_oracle.oracle_insert(flss.table_name, flss.column_name, insert_value)

    # 解析：经营状况--购地信息
    def html_parse_buyInfo(self, index):
        logger.debug("Parse detail info 购地信息 {}".format(self.search_name))
        if index == 1 and not isinstance(self.selector, int):
            trs = self.selector.xpath("//table[position()=1]/tbody/tr")
        else:
            trs = self.selector.xpath('//div[@id="_container_purchaselandV2"]/table/tbody/tr')
    
        if trs:
            key = self.search_name
            for tr in trs:
                insert_value = ""
                buyInfo = TycJyzkGdxx()
                tds = tr.xpath('./td')
            
                # 签订日期
                buyInfo.gdSignDate = try_and_text("variable[6].xpath('./text()')[0]", tds)
                # 土地坐落
                where = try_and_text("variable[1].xpath('./span/text()')[0]", tds)
                # 购地详情
                gd_info = try_and_text("variable[1].xpath('./script/text()')[0]", tds)
                gd_info = gd_info.replace('\u002F','/')
                # 土地用途
                todo = try_and_text("variable[2].xpath('./text()')[0]", tds)
                # 总面积（公顷）
                gd_area = try_and_text("variable[3].xpath('./text()')[0]", tds)
                # 行政区
                gd_region = try_and_text("variable[4].xpath('./text()')[0]", tds)
                # 供应方式
                type = try_and_text("variable[5].xpath('./text()')[0]", tds)
                buyInfo.gdNum = CURRENT_VERSION_NULL
                buyInfo.gdActDate = CURRENT_VERSION_NULL
                buyInfo.gdArea = str(gd_area) + '公顷'
                buyInfo.gdRegion = gd_region
                buyInfo.gdOperate = CURRENT_VERSION_NULL
            
                # 新增 土地坐落
                buyInfo.located = where
                # 购地详情
                buyInfo.gd_info = gd_info
                # 新增 土地用途
                buyInfo.land_use = todo
                # 新增  供应方式
                buyInfo.supply_method = type
                buyInfo.txtId = self.txtId
                buyInfo.company_name = key
                buyInfo.mark = 0
                buyInfo.addtime = 'sysdate'
                buyInfo.agency_num = self.agency_num
                buyInfo.agency_name = self.agency_name
                buyInfo.batch = self.batch
                value_list = [
                    buyInfo.txtId,
                    buyInfo.company_name,
                    buyInfo.gdSignDate,
                    buyInfo.gdNum,  # 此版本无此信息
                    buyInfo.gdActDate,  # 此版本无此信息
                    buyInfo.gdArea,
                    buyInfo.gdRegion,
                    buyInfo.gdOperate,  # 此版本无此信息
                    buyInfo.located,
                    buyInfo.land_use,
                    buyInfo.supply_method,
                    buyInfo.mark,
                    buyInfo.agency_num,
                    buyInfo.agency_name,
                    buyInfo.batch,
                    buyInfo.gd_info]

                # column_name = "(txt_id,company_name,gd_sign_date,gd_area,located,land_use,supply_method,mark,agency_num,agency_name,batch,add_time)"
                # "(txt_id,company_name,gd_sign_date,gd_area,gd_region,located,land_use,supply_method,mark,agency_num,agency_name,batch,add_time)"
                
                value_list = ["'" + str(value) + "'" for value in value_list]
                insert_value += '(' + ','.join(value_list) + ',sysdate' + ')'
            
                single_oracle.oracle_insert(
                    buyInfo.table_name, buyInfo.column_name, insert_value)

    # 解析：经营状况-->电信许可
    def html_parse_dxxk(self, index):
        logger.debug("Parse detail info 电信许可 {}".format(self.search_name))
    
        if index == 1 and not isinstance(self.selector, int):
        
            trs = self.selector.xpath('//table/tbody/tr')
        else:
            trs = self.selector.xpath(
                '//div[@id="_container_permission"]/table/tbody/tr')
        if trs:
            dxxkInfo = TycJyzkDxxk()
        
            key = self.search_name
        
            for tr in trs:
                insert_value = ""
                tds = tr.xpath('./td')
                # 许可证号
                dxxkInfo.licenseKey = try_and_text("variable[1].xpath('./text()')[0]", tds)
                # 业务范围
                dxxkInfo.businessSphere = try_and_text("variable[2].xpath('./text()')[0]", tds)
                # 是否有效
                dxxkInfo.available = try_and_text("variable[3].xpath('./text()')[0]", tds)
                # 详情
                text_info = try_and_text("variable[4].xpath('./script/text()')[0]", tds)
                text_info = replace_special_string(text_info)
                dxxkInfo.detailInfo = text_info
            
                dxxkInfo.txtId = self.txtId
                dxxkInfo.company_name = key
                dxxkInfo.mark = 0
                dxxkInfo.add_time = datetime.now()
                dxxkInfo.agency_num = self.agency_num
                dxxkInfo.agency_name = self.agency_name
                dxxkInfo.batch = self.batch
            
                value_list = [
                    dxxkInfo.txtId,
                    dxxkInfo.company_name,
                    dxxkInfo.mark,
                    dxxkInfo.licenseKey,
                    dxxkInfo.businessSphere,
                    dxxkInfo.available,
                    dxxkInfo.detailInfo,
                    dxxkInfo.agency_num,
                    dxxkInfo.agency_name,
                    dxxkInfo.batch]
                #
                column_name = "(txt_id,company_name,mark,license_key,business_sphere,available,detail_info,agency_num,agency_name,batch,add_time)"
            
                insert_sql = create_insert_sql(
                    dxxkInfo.table_name, dxxkInfo.column_name, len(
                        dxxkInfo.column_name.split(',')))
                single_oracle.oracle_insert_sql_param(insert_sql, value_list)
                # value_list = ["'" + str(value) + "'" for value in value_list]
                # insert_value += '(' + ','.join(value_list) + ',sysdate' + ')'
                #
                # single_oracle.oracle_insert(dxxkInfo.table_name, dxxkInfo.column_name, insert_value)

    # 商标信息
    def html_parse_trademark(self, index):
        logger.debug("Parse detail info 商标信息 {}".format(self.search_name))
        
        if index == 1 and not isinstance(self.selector, int):
            root_div = self.selector.xpath("//table")
        else:
            # 获得商标信息大标签
            root_div = self.selector.xpath(
                '//div[@id= "_container_tmInfo"][position()=1]/div/table')
        if root_div:
            flss = TycZscqSbxx()
            key = self.search_name
            # 一行是一个tr
    
            root_div = root_div[0]
            trs = root_div.xpath("./tbody/tr")
    
            for tr in trs:
                insert_value = ""
                tds = tr.xpath("./td")
                if tds:
                    flss.apply_date = try_and_text("variable[1].xpath('.//text()')[0]", tds)
                    flss.trademark = try_and_text("variable[2].xpath('.//img/@data-src')[0]", tds)
                    flss.trademark_name = try_and_text("variable[3].xpath('.//text()')[0]", tds)
                    flss.registration_number = try_and_text("variable[4].xpath('.//text()')[0]", tds)
                    flss.type = try_and_text("variable[5].xpath('.//text()')[0]", tds)
                    flss.status = try_and_text("variable[6].xpath('.//text()')[0]", tds)
                    href = try_and_text("variable[7].xpath('./a/@href')[0]", tds)
                    # 新增 详情 brand
                    text_info = "NA"
                    try:
                        text_info = self.detail_info["_container_tmInfo"][href.split(
                            r'/')[-1]]
                        text_info = replace_special_string(text_info)
                    except BaseException:
                        pass
    
                    flss.detail = text_info
    
                    flss.txt_id = self.txtId
                    flss.company_name = key
                    flss.add_time = 'sysdate'
                    flss.mark = 0
                    flss.agency_num = self.agency_num
                    flss.agency_name = self.agency_name
                    flss.batch = self.batch
                    value_list = [
                        flss.detail,
                        flss.txt_id,
                        flss.company_name,
                        flss.apply_date,
                        flss.trademark,
                        flss.trademark_name,
                        flss.registration_number,
                        flss.type,
                        flss.status,
                        flss.mark,
                        flss.agency_num,
                        flss.agency_name,
                        flss.batch]
    
                    #
                    # column_name = "(detail,txt_id,company_name,apply_date,trademark,trademark_name,registration_number,type,status,mark,agency_num,agency_name,batch,add_time)"
                    single_oracle.oracle_insert_sql_param(
                        create_insert_sql(
                            flss.table_name, flss.column_name, len(
                                flss.column_name.split(','))), value_list)
                    # value_list = ["'" + str(value) + "'" for value in value_list]
                    # insert_value += '(' + ','.join(value_list) + ',sysdate' + ')'
                    #
                    # single_oracle.oracle_insert(flss.table_name, flss.column_name, insert_value)

    # 专利信息
    def html_parse_patent(self, index):
        logger.debug("Parse detail info 专利信息 {}".format(self.search_name))
        if index == 1 and not isinstance(self.selector, int):
            root_div = (self.selector.xpath("//table"))
        else:
            # 获得专利信息大标签
            root_div = self.selector.xpath(
                '//div[@id="_container_patent"][position()=1]/table')
        if root_div:
            flss = TycZscqZl()
            key = self.search_name
            # 一行是一个tr
            root_div = root_div[0]
            trs = root_div.xpath("./tbody/tr")
            
            for tr in trs:
                insert_value = ""
                tds = tr.xpath("./td")
                flss.apply_publish_date = try_and_text("variable[1].xpath('./span/text()')[0]", tds)
                flss.patent_name = try_and_text("variable[2].xpath('./span/text()')[0]", tds)
                flss.apply_number = try_and_text("variable[3].xpath('./span/text()')[0]", tds)
                flss.apply_publish_number = try_and_text("variable[4].xpath('./span/text()')[0]", tds)

                # 新增 专利类型
                patent_type = try_and_text("variable[5].xpath('./span/text()')", tds)
                flss.patent_type = patent_type[0] if patent_type else 'NA'

                href = try_and_text("variable[6].xpath('./a/@href')[0]", tds)
                # 新增 详情 brand
                text_info = 'NA'
                try:
                    text_info = self.detail_info["_container_patent"][href.split(
                        r'/')[-1]]
                except BaseException:
                    pass
                flss.detail_info = replace_special_string(text_info)
                flss.txt_id = self.txtId
                flss.company_name = key
                flss.add_time = 'sysdate'
                flss.mark = 0
                flss.agency_num = self.agency_num
                flss.agency_name = self.agency_name
                flss.batch = self.batch
                value_list = [
                    flss.apply_publish_date,
                    flss.patent_name,
                    flss.apply_number,
                    flss.apply_publish_number,
                    flss.detail_info,
                    flss.txt_id,
                    flss.company_name,
                    flss.mark,
                    flss.agency_num,
                    flss.agency_name,
                    flss.batch,
                    flss.patent_type]

                # value_list = ["'" + str(value) + "'" for value in value_list]
                # insert_value += '(' + ','.join(value_list) + ',sysdate' + ')'
                # #
                # logger.debug(insert_value)
                # single_oracle.oracle_insert(
                #     flss.table_name, flss.column_name, insert_value)

                insert_sql = create_insert_sql(
                    flss.table_name, flss.column_name, len(
                        flss.column_name.split(',')))
                single_oracle.oracle_insert_sql_param(insert_sql, value_list)
        
            # column_name = "(apply_publish_date,patent_name,apply_number,apply_publish_number,detail_info,txt_id,company_name,mark,agency_num,agency_name,batch,patent_type,add_time)"

    # 软件著作权
    def html_parse_copyright(self, index):
        logger.debug("Parse detail info 软件著作权 {}".format(self.search_name))
        if index == 1 and not isinstance(self.selector, int):
            root_div = self.selector.xpath("//table[position()=1]")
        else:
            root_div = self.selector.xpath(
                '//div[@id="_container_copyright"][position()=1]/table')
        # 获得著作权大标签
        if root_div:
            flss = TycZscqZzq()
            key = self.search_name
            # 一行是一个tr
            root_div = root_div[0]
            trs = root_div.xpath("./tbody/tr")
        
            for tr in trs:
                insert_value = ""
                tds = tr.xpath("./td")
                flss.approval_date = try_and_text("variable[1].xpath('./span/text()')[0]", tds)
                flss.software_name = try_and_text("variable[2].xpath('./span/text()')[0]", tds)
                flss.software_referred = try_and_text("variable[3].xpath('./span/text()')[0]", tds)
                flss.registration_number = try_and_text("variable[4].xpath('./span/text()')[0]", tds)
                flss.type_number = try_and_text("variable[5].xpath('./span/text()')[0]", tds)
                flss.version_number = try_and_text("variable[6].xpath('./span/text()')[0]", tds)
                text_info = try_and_text("variable[7].xpath('./script/text()')[0]", tds)
                text_info = replace_special_string(text_info)
                flss.detail_info = text_info
            
                flss.txt_id = self.txtId
                flss.company_name = key
                flss.add_time = 'sysdate'
                flss.mark = 0
                flss.agency_num = self.agency_num
                flss.agency_name = self.agency_name
                flss.batch = self.batch
                value_list = [
                    flss.batch,
                    flss.agency_num,
                    flss.mark,
                    flss.detail_info,
                    flss.version_number,
                    flss.type_number,
                    flss.software_referred,
                    flss.software_name,
                    flss.company_name,
                    flss.txt_id,
                    flss.approval_date,
                    flss.agency_name,
                    flss.registration_number]
                #
                # column_name = "(batch,agency_num,mark,detail_info,version_number,type_number,software_referred,software_name,company_name,txt_id,approval_date,agency_name,registration_number,add_time)"
            
                insert_sql = create_insert_sql(
                    flss.table_name, flss.column_name, len(
                        flss.column_name.split(',')))
                single_oracle.oracle_insert_sql_param(insert_sql, value_list)
                # single_oracle.oracle_insert(flss.table_name, flss.column_name, insert_value)

    # 作品著作权
    def html_parse_copyzzq(self, index):
        logger.debug("Parse detail info 作品著作权 {}".format(self.search_name))
    
        # 获得作品著作权大标签
        if index == 1 and not isinstance(self.selector, int):
            root_div = self.selector.xpath("//table/tbody/tr")
        else:
            root_div = self.selector.xpath(
                '//div[@id="_container_copyrightWorks"]/table/tbody/tr')
    
        if root_div:
            flss = TycZscqZpzzq()
            key = self.search_name
            # root_div = root_div[0]
            # trs = root_div.xpath(".")
            #
            for tr in root_div:
                insert_value = ""
                # 作品名称	登记号	类别	 创作完成日期	登记日期	首次发布日期
                tds = tr.xpath("./td")
                flss.works_name = try_and_text("variable[1].xpath('.//text()')[0]", tds)
                flss.register_name = try_and_text("variable[2].xpath('.//text()')[0]", tds)
                flss.type = try_and_text("variable[3].xpath('.//text()')[0]", tds)
                flss.create_date = try_and_text("variable[4].xpath('.//text()')[0]", tds)
                flss.register_date = try_and_text("variable[5].xpath('.//text()')[0]", tds)
                flss.firstpublish_date = try_and_text("variable[6].xpath('.//text()')[0]", tds)
                flss.txtId = self.txtId
                flss.company_name = key
                flss.add_time = 'sysdate'
                flss.mark = 0
                flss.agency_num = self.agency_num
                flss.agency_name = self.agency_name
                flss.batch = self.batch
                value_list = [
                    flss.works_name,
                    flss.mark,
                    flss.txtId,
                    flss.company_name,
                    flss.register_name,
                    flss.type,
                    flss.create_date,
                    flss.register_date,
                    flss.firstpublish_date,
                    flss.agency_num,
                    flss.agency_name,
                    flss.batch]
                #
                column_name = "(works_name,mark,txt_id,company_name,register_name,type,create_date,register_date,firstpublish_date,agency_num,agency_name,batch,add_time)"
                
                value_list = ["'" + str(value) + "'" for value in value_list]
                insert_value += '(' + ','.join(value_list) + ',sysdate' + ')'
                
                single_oracle.oracle_insert(
                    flss.table_name, flss.column_name, insert_value)
    
    # 网站备案
    def html_parse_website(self, index):
        logger.debug("Parse detail info 网站备案 {}".format(self.search_name))
        if index == 1 and not isinstance(self.selector, int):
            root_div = self.selector.xpath('//table')
        else:
            # 获得网站备案大标签
            root_div = self.selector.xpath('//div[@id="_container_icp"]/table')

        if root_div:
            flss = TycZscqWzba()
            key = self.search_name
            root_div = root_div[0]
            # 一行是一个tr
            trs = root_div.xpath("./tbody/tr")

            for tr in trs:
                insert_value = ""
                tds = tr.xpath('./td')
                flss.audit_date = try_and_text("variable[1].xpath('./span/text()')[0]", tds)
                flss.web_name = try_and_text("variable[2].xpath('./span/text()')[0]", tds)
                flss.web_homepage = try_and_text("variable[3].xpath('.//a//text()')[0]", tds)
                domain_name = try_and_text("variable[4].xpath('./text()')[0]", tds)
                flss.domain_name = domain_name if domain_name else 'NA'
                record_number = try_and_text("variable[5].xpath('./span/text()')[0]", tds)
                flss.record_number = record_number if record_number else 'NA'

                flss.status = CURRENT_VERSION_NULL
                flss.department_type = CURRENT_VERSION_NULL
                flss.txt_id = self.txtId
                flss.company_name = key
                flss.add_time = 'sysdate'
                flss.mark = 0
                flss.agency_num = self.agency_num
                flss.agency_name = self.agency_name
                flss.batch = self.batch
                value_list = [
                    flss.txt_id,
                    flss.domain_name,
                    flss.agency_num,
                    flss.company_name,
                    flss.audit_date,
                    flss.web_name,
                    flss.web_homepage,
                    flss.record_number,
                    flss.status,
                    flss.department_type,
                    flss.mark,
                    flss.agency_name,
                    flss.batch]

                value_list = ["'" + str(value) + "'" for value in value_list]
                insert_value += '(' + ','.join(value_list) + ',sysdate' + ')'

                single_oracle.oracle_insert(
                    flss.table_name, flss.column_name, insert_value)

    # 企业年报
    def html_parse_nianbao(self, year):
        logger.debug("Parse detail info 企业年报 {}".format(self.search_name))

        # 获得企业年报大标签
        root_div = self.selector.xpath(
            '//div[@id="nav-main-reportCount"]/../div[@class="data-content"]/div')
        if root_div:
            flss = TycQybjQynb()
            key = self.search_name
            root_div = root_div[0]
            # 一行是一个tr
            all_a = root_div.xpath(
                '//a[contains(@href,"https://www.tianyancha.com/reportContent")]')

            for a in all_a:
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
                    self.html_parse_year_wzhwdxx(year_selector, flss.year)
                except Exception as e:
                    logger.exception(e)
                try:
                    self.html_parse_year_gdczxx(year_selector, flss.year)
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

                flss.txt_id = self.txtId
                flss.company_name = key
                flss.add_time = 'sysdate'
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

                value_list = [
                    "'" +
                    str(value) +
                    "'" for value in value_list if value != 'sysdate']
                insert_value += '(' + ','.join(value_list) + ',sysdate' + ')'

                single_oracle.oracle_insert(
                    flss.table_name, flss.column_name, insert_value)

    # 解析：企业背景-->最终受益人
    def html_parse_zzsyr(self, index):
        # TODO 这是个异步抓取页面， https://www.tianyancha.com/company/holder_holding_analysis.xhtml?id=22822&_=1557886017705  GET
        logger.debug("Parse detail info 最终受益人 {}".format(self.search_name))

        if index == 1 and not isinstance(self.selector, int):
    
            trs = self.selector.xpath('//table/tbody/tr')
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
                benefitPerson.beneficiaryName = try_and_text("variable[1].xpath('/span/a/text()')[0]", tds)
                # 持股比例
                benefitPerson.shareholderProportion = try_and_text("variable[2].xpath('./span/text()')[0]", tds)
                # 股权链
                benefitPerson.equityChain = try_and_text("variable[3].xpath('./div')[0].xpath('string(.)')", tds)

                benefitPerson.txtId = self.txtId
                benefitPerson.company_name = key
                benefitPerson.mark = 0
                benefitPerson.add_time = 'sysdate'
                benefitPerson.agency_num = self.agency_num
                benefitPerson.agency_name = self.agency_name
                benefitPerson.batch = self.batch
                value_list = [
                    benefitPerson.txtId,
                    benefitPerson.company_name,
                    benefitPerson.mark,
                    benefitPerson.agency_num,
                    benefitPerson.agency_name,
                    benefitPerson.batch,
                    benefitPerson.beneficiaryName,
                    benefitPerson.shareholderProportion,
                    benefitPerson.equityChain]
                value_list = ["'" + str(value) + "'" for value in value_list]
                insert_value += '(' + ','.join(value_list) + ',sysdate' + ')'

                single_oracle.oracle_insert(
                    benefitPerson.table_name,
                    benefitPerson.column_name,
                    insert_value)

    # 解析：企业背景-->实际控制权
    def html_parse_sjkzq(self, index):
        # TODO 这是个异步抓取页面，https://www.tianyancha.com/company/holder_holding_analysis.xhtml?id=22822&_=1557886017705
        logger.debug("Parse detail info 实际控制权 {}".format(self.search_name))

        if index == 1 and not isinstance(self.selector, int):
    
            trs = self.selector.xpath('//table/tbody/tr')
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
                holdingInfo.holdingName = try_and_text("variable[1].xpath('.//a/txext()')[0]", tds)
                # 投资比例 //*[@id="_container_companyholding"]/table/tbody/tr[1]/td[3]/span
                holdingInfo.investProportion = try_and_text("variable[2].xpath('.//text()')[0]", tds)
                # 投资链
                holdingInfo.equityChain = try_and_text("variable[3].xpath('string(.)')", tds)

                holdingInfo.txtId = self.txtId
                holdingInfo.company_name = key
                holdingInfo.mark = 0
                holdingInfo.add_time = datetime.now()
                holdingInfo.agency_num = self.agency_num
                holdingInfo.agency_name = self.agency_name
                holdingInfo.batch = self.batch

                value_list = [
                    holdingInfo.txtId,
                    holdingInfo.company_name,
                    holdingInfo.mark,
                    holdingInfo.agency_num,
                    holdingInfo.agency_name,
                    holdingInfo.batch,
                    holdingInfo.holdingName,
                    holdingInfo.investProportion,
                    holdingInfo.equityChain]
                value_list = ["'" + str(value) + "'" for value in value_list]
                insert_value += '(' + ','.join(value_list) + ',sysdate' + ')'

                single_oracle.oracle_insert(
                    holdingInfo.table_name,
                    holdingInfo.column_name,
                    insert_value)

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
                tyc_Parse.txtId = txt_id
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
            except Exception as e:
                error_list.append("html_parse_baseinfo")
                logger.exception(
                    "Detail info html_parse_baseinfo() parse error! company_name：%s ID：%s",
                    search_name,
                    txt_id)

            # 主要信息
            try:
                tyc_Parse.html_parse_mainPerson()
            except Exception as e:
                error_list.append("html_parse_mainPerson")
                logger.exception(
                    "Detail info html_parse_mainPerson() parse error! company_name：%s ID：%s",
                    search_name,
                    txt_id)

            # 股东
            try:
                tyc_Parse.html_parse_shareholderInfo(0)
            except Exception as e:
                error_list.append("html_parse_shareholderInfo")
                logger.exception(
                    "Detail info html_parse_shareholderInfo() parse error! company_name：%s ID：%s",
                    search_name,
                    txt_id)

            # 法律诉讼
            try:
                tyc_Parse.html_parse_lawsuit(index=0)
            except Exception as e:
                logger.debug('Exception====={}'.format(e))
                error_list.append("html_parse_lawsuit")
                logger.exception(
                    "Detail info html_parse_lawsuit() parse error! company_name：{}, ID：{}".format(
                        search_name, txt_id))
            # 著作权
            try:
                tyc_Parse.html_parse_copyright(index=0)
            except Exception as e:
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
            except Exception as e:
                error_list.append("html_parse_recruitment")
                logger.exception(
                    "Detail info html_parse_recruitment() parse error! company_name：%s ID：%s",
                    search_name,
                    txt_id)
            # 商标信息
            try:
                tyc_Parse.html_parse_trademark(index=0)
            except Exception as e:
                error_list.append("html_parse_trademark")
                logger.exception(
                    "Detail info html_parse_trademark() parse error! company_name：%s ID：%s",
                    search_name,
                    txt_id)
            # 对外投资
            try:
                tyc_Parse.html_parse_investInfo(index=0)
            except Exception as e:
                error_list.append("html_parse_investInfo")
                logger.exception(
                    "Detail info html_parse_investInfo() parse error! company_name：%s ID：%s",
                    search_name,
                    txt_id)
            # 记录变更
            try:
                tyc_Parse.html_parse_alterRecord(index=0)
            except Exception as e:
                error_list.append("html_parse_alterRecord")
                logger.exception(
                    "Detail info html_parse_alterRecord() parse error! company_name：%s ID：%s",
                    search_name,
                    txt_id)
            # 分支机构
            try:
                tyc_Parse.html_parse_branch(0)
            except Exception as e:
                error_list.append("html_parse_branch")
                logger.exception(
                    "Detail info html_parse_branch() parse error! company_name：%s ID：%s",
                    search_name,
                    txt_id)
            try:
                tyc_Parse.html_parse_pledge(0)
            except Exception as e:
                error_list.append("html_parse_pledge")
                logger.exception(
                    "Detail info html_parse_pledge() parse error! company_name：%s ID：%s",
                    search_name,
                    txt_id)
            # 资质证书
            try:
                tyc_Parse.html_parse_certificateInfo(index=0)
            except Exception as e:
                error_list.append("html_parse_certificateInfo")
                logger.exception(
                    "Detail info html_parse_certificateInfo() parse error! company_name：%s ID：%s",
                    search_name,
                    txt_id)
            # 网站备案
            try:
                tyc_Parse.html_parse_website(index=0)
            except Exception as e:
                error_list.append("html_parse_website")
                logger.exception(
                    "Detail info html_parse_website() parse error! company_name：%s ID：%s",
                    search_name,
                    txt_id)
            # 核心团队
            try:
                tyc_Parse.html_parse_coreTeam(index=0)
            except Exception as e:
                error_list.append("html_parse_coreTeam")
                logger.exception(
                    "Detail info html_parse_coreTeam() parse error! company_name：%s ID：%s",
                    search_name,
                    txt_id)
            # 投资事件
            try:
                tyc_Parse.html_parse_investEvent(index=0)
            except Exception as e:
                error_list.append("html_parse_investEvent")
                logger.exception(
                    "Detail info html_parse_investEvent() parse error! company_name：%s ID：%s",
                    search_name,
                    txt_id)
            # 企业业务
            try:
                tyc_Parse.html_parse_entBusiness(index=0)
            except Exception as e:
                error_list.append("html_parse_entBusiness")
                logger.exception(
                    "Detail info html_parse_entBusiness() parse error! company_name：%s ID：%s",
                    search_name,
                    txt_id)
            # 竞品信息
            try:
                tyc_Parse.html_parse_jpInfo(index=0)
            except Exception as e:
                error_list.append("html_parse_jpInfo")
                logger.exception(
                    "Detail info html_parse_jpInfo() parse error! company_name：%s ID：%s",
                    search_name,
                    txt_id)
            # 法院公告
            try:
                tyc_Parse.html_parse_announcement(index=0)
            except Exception as e:
                error_list.append("html_parse_announcement")
                logger.exception(
                    "Detail info html_parse_announcement() parse error! company_name：%s ID：%s",
                    search_name,
                    txt_id)
            # 抽查检查
            try:
                tyc_Parse.html_parse_check(index=0)
            except Exception as e:
                error_list.append("html_parse_check")
                logger.exception(
                    "Detail info html_parse_check() parse error! company_name：%s ID：%s",
                    search_name,
                    txt_id)
            # 专利信息
            try:
                tyc_Parse.html_parse_patent(index=0)
            except Exception as e:
                error_list.append("html_parse_patent")
                logger.exception(
                    "Detail info html_parse_patent() parse error! company_name：%s ID：%s",
                    search_name,
                    txt_id)
            # 作品著作
            try:
                tyc_Parse.html_parse_copyzzq(index=0)
            except Exception as e:
                error_list.append("html_parse_copyzzq")
                logger.exception(
                    "Detail info html_parse_copyzzq() parse error! company_name：%s ID：%s",
                    search_name,
                    txt_id)
            # 微信
            try:
                tyc_Parse.html_parse_entWechat(index=0)
            except Exception as e:
                error_list.append("html_parse_entWechat")
                logger.exception(
                    "Detail info html_parse_entWechat() parse error! company_name：%s ID：%s",
                    search_name,
                    txt_id)
            # 产品信息
            try:
                tyc_Parse.html_parse_product(index=0)
            except Exception as e:
                error_list.append("html_parse_product")
                logger.exception(
                    "Detail info html_parse_product() parse error! company_name：%s ID：%s",
                    search_name,
                    txt_id)
            # 被执行人
            try:
                tyc_Parse.html_parse_executed(index=0)
            except Exception as e:
                error_list.append("html_parse_executed")
                logger.exception(
                    "Detail info html_parse_executed() parse error! company_name：%s ID：%s",
                    search_name,
                    txt_id)
            # 招投标
            try:
                tyc_Parse.html_parse_bidding(index=0)
            except Exception as e:
                error_list.append("html_parse_bidding")
                logger.exception(
                    "Detail info html_parse_bidding() parse error! company_name：%s ID：%s",
                    search_name,
                    txt_id)
            # 债券信息
            try:
                tyc_Parse.html_parse_zhaiquan(index=0)
            except Exception as e:
                error_list.append("html_parse_zhaiquan")
                logger.exception(
                    "Detail info html_parse_zhaiquan() parse error! company_name：%s ID：%s",
                    search_name,
                    txt_id)
            # 欠税公告
            try:
                tyc_Parse.html_parse_taxesNotice(index=0)
            except Exception as e:
                error_list.append("html_parse_taxesNotice")
                logger.exception(
                    "Detail info html_parse_taxesNotice() parse error! company_name：%s ID：%s",
                    search_name,
                    txt_id)
            # 动产抵押
            try:
                tyc_Parse.html_parse_dongchandiya(index=0)
            except Exception as e:
                error_list.append("html_parse_dongchandiya")
                logger.exception(
                    "Detail info html_parse_dongchandiya() parse error! company_name：%s ID：%s",
                    search_name,
                    txt_id)
            # 股权出质
            try:
                tyc_Parse.html_parse_pledge(index=0)
            except Exception as e:
                error_list.append("html_parse_pledge")
                logger.exception(
                    "Detail info html_parse_pledge() parse error! company_name：%s ID：%s",
                    search_name,
                    txt_id)
            # 行政处罚
            try:
                tyc_Parse.html_parse_xingzhengchufa(index=0)
            except Exception as e:
                error_list.append("html_parse_xingzhengchufa")
                logger.exception(
                    "Detail info html_parse_xingzhengchufa() parse error! company_name：%s ID：%s",
                    search_name,
                    txt_id)
            # 失信人
            try:
                tyc_Parse.html_parse_shixinren(index=0)
            except Exception as e:
                error_list.append("html_parse_shixinren")
                logger.exception(
                    "Detail info html_parse_shixinren() parse error! company_name：%s ID：%s",
                    search_name,
                    txt_id)
            # 税务评级
            try:
                tyc_Parse.html_parse_tax(index=0)
            except Exception as e:
                error_list.append("html_parse_tax")
                logger.exception(
                    "Detail info html_parse_tax() parse error! company_name：%s ID：%s",
                    search_name,
                    txt_id)
            # 融资
            try:
                tyc_Parse.html_parse_financeHistory()
            except Exception as e:
                error_list.append("html_parse_financeHistory")
                logger.exception(
                    "Detail info html_parse_financeHistory() parse error! company_name：%s ID：%s",
                    search_name,
                    txt_id)
            # 经营异常
            try:
                tyc_Parse.html_parse_abnormal(0)
            except Exception as e:
                error_list.append("html_parse_abnormal")
                logger.exception(
                    "Detail info html_parse_abnormal() parse error! company_name：%s ID：%s",
                    search_name,
                    txt_id)
            # 严重违法
            try:
                tyc_Parse.html_parse_illegalSerious()
            except Exception as e:
                error_list.append("html_parse_illegalSerious")
                logger.exception(
                    "Detail info html_parse_illegalSerious() parse error! company_name：%s ID：%s",
                    search_name,
                    txt_id)

            # 购地信息
            try:
                tyc_Parse.html_parse_buyInfo(0)
            except Exception as e:
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
            except Exception as e:
                error_list.append("html_parse_nianbao")
                logger.exception(
                    "Detail info html_parse_nianbao() parse error! company_name：%s ID：%s",
                    search_name,
                    txt_id)
            # 进出口
            try:
                tyc_Parse.html_parse_outputxy()
            except Exception as e:
                error_list.append("html_parse_outputxy")
                logger.exception(
                    "Detail info html_parse_outputxy() parse error! company_name：%s ID：%s",
                    search_name,
                    txt_id)

            # 最终受益人
            try:
                tyc_Parse.html_parse_zzsyr(index=0)
            except Exception as e:
                error_list.append("html_parse_zzsyr")
                logger.exception(
                    "Detail info html_parse_zzsyr() parse error! company_name：%s ID：%s",
                    search_name,
                    txt_id)

            # 实际控制权
            try:
                tyc_Parse.html_parse_sjkzq(index=0)
            except Exception as e:
                error_list.append("html_parse_sjkzq")
                logger.exception(
                    "Detail info html_parse_sjkzq() parse error! company_name：%s ID：%s",
                    search_name,
                    txt_id)

            # 开庭公告
            try:
                tyc_Parse.html_parse_ktgg(index=0)
            except Exception as e:
                error_list.append("html_parse_ktgg")
                logger.exception(
                    "Detail info html_parse_ktgg() parse error! company_name：%s ID：%s",
                    search_name,
                    txt_id)

            # 司法协助
            try:
                tyc_Parse.html_parse_sfxz(index=0)
            except Exception as e:
                error_list.append("html_parse_sfxz")
                logger.exception(
                    "Detail info html_parse_sfxz() parse error! company_name：%s ID：%s",
                    search_name,
                    txt_id)

            # 公示催告
            try:
                tyc_Parse.html_parse_gscg()
            except Exception as e:
                error_list.append("html_parse_gscg")
                logger.exception(
                    "Detail info html_parse_gscg() parse error! company_name：%s ID：%s",
                    search_name,
                    txt_id)

            # 司法拍卖
            try:
                tyc_Parse.html_parse_sfpm(index=0)
            except Exception as e:
                error_list.append("html_parse_sfpm")
                logger.exception(
                    "Detail info html_parse_sfpm() parse error! company_name：%s ID：%s",
                    search_name,
                    txt_id)

            # 清算信息
            try:
                tyc_Parse.html_parse_qsxx(index=0)
            except Exception as e:
                error_list.append("html_parse_qsxx")
                logger.exception(
                    "Detail info html_parse_qsxx() parse error! company_name：%s ID：%s",
                    search_name,
                    txt_id)

            # 行政许可【工商局】
            try:
                tyc_Parse.html_parse_gsj(index=0)
            except Exception as e:
                error_list.append("html_parse_gsj")
                logger.exception(
                    "Detail info html_parse_gsj() parse error! company_name：%s ID：%s",
                    search_name,
                    txt_id)

            # 行政许可【信用中国】
            try:
                tyc_Parse.html_parse_xyzg(index=0)
            except Exception as e:
                error_list.append("html_parse_xyzg")
                logger.exception(
                    "Detail info html_parse_xyzg() parse error! company_name：%s ID：%s",
                    search_name,
                    txt_id)

            # 电信许可
            try:
                tyc_Parse.html_parse_dxxk(index=0)
            except Exception as e:
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
                # continue
                # 法律诉讼
                # 软件著作权

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

                    bd.end_time = 'sysdate'
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
    main(1)
