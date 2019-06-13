# -*- coding:utf-8 -*-
# !/usr/bin/env python
from db import *
from bs4 import BeautifulSoup
import logging
import logging.config
from tyc_bean import *
from datetime import datetime
from lxml import etree
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
logging.config.fileConfig("../log_file/detailParseLog.conf")

logger = logging.getLogger("loggerText")


class TycDetailParse(object):
    txtId = ""
    entName = ""
    agency_num = ""
    agency_name = ""
    batch = ""
    soup = None
    selector = None

    def __init__(self):
        self.mongodbClient = MongodbClient()
        self.mysqlClient = MysqlClient()

    # 解析：企业背景-->主要人员
    def html_parse_mainPerson(self):
        insert_value = ""
        mainPerson = TycQybjZyry()
        key = self.entName
        logger.info("Parse detail info 主要人员 %s", key)
        trs = self.selector.xpath('//div[@id="_container_staff"]//div[@class="clearfix"]/table//tbody/tr')
        if trs:
            trs=trs[0]
            for div in trs:
                position = div.xpath('./td[position()=2]/div/a/text()')

                mainPerson.position = position[0].replace('\n', '').replace(' ', '') if position else '-'
                name=div.xpath('./td[position()=1]/span[position()=1]/text()')
                mainPerson.name = name[0].replace('\n', '').replace(' ', '') if name else '-'
                mainPerson.txtId = self.txtId
                mainPerson.entName = key
                mainPerson.mark = str(0)
                mainPerson.addtime = str(datetime.now())
                mainPerson.agency_num = self.agency_num
                mainPerson.agency_name = self.agency_name
                mainPerson.batch = self.batch
                value_list = [mainPerson.txtId, mainPerson.entName, mainPerson.position, mainPerson.name,
                              mainPerson.mark, mainPerson.addtime, mainPerson.agency_num, mainPerson.agency_name,
                              mainPerson.batch]
                value_list = ['"' + value + '"' for value in value_list]
                insert_value += '(' + ','.join(value_list) + '),'
            insert_value = insert_value[0:-1]
            self.mysqlClient.mysql_insert(mainPerson.table_name, mainPerson.column_name, insert_value)

    # 解析：企业背景-->基本信息(工商信息)
    def html_parse_baseinfo(self, branch):
        insert_value = ""
        baseinfo = TycQybjJbxx()
        key = self.entName
        logger.info("Parse detail info 基本信息 %s", key)
        top= (self.selector.xpath('//div[@id="company_web_top"]'))

        table_lists = (self.selector.xpath('//div[contains(@id,"container_baseInfo")]//table'))
        text_list=table_lists[0].xpath('string()')
        text_list2 = table_lists[0].xpath('string(.)')
        if top:
            top=top[0]
            email = top.xpath('.//span[@class="email"]/text()')
            baseinfo.email =email[0] if email else '-'
            detail_basic=top.xpath('.//div[@class="box"]//div[@class="content"]//div[contains(@class,"detail")]')
            if detail_basic:
                detail_basic=detail_basic[0]
                # #print(detail_basic.xpath('string()'))
                telephone =detail_basic.xpath('./div[position()=1]/div[position()=1]/span[2]/text()')[0]
                baseinfo.telephone = telephone
                urls = detail_basic.xpath('./div[position()=2]//a[@class="company-link"][position()=1]/text()')
                baseinfo.url = '' or urls[0]  if urls else ''
            if table_lists:
                # string_list=table[0].xpath('/string()')

                if 1:

                    trs0=table_lists[0].xpath('./tbody//tr')
                    trs1=table_lists[1].xpath('./tbody//tr')
                    if trs0:
                        baseinfo.registerFund = trs0[0].xpath('./td[position()=2]/div[position()=2]/@title')[0] or ''
                        baseinfo.registerDate = '-'
                        baseinfo.companyStatus = trs0[2].xpath('./td/div[position()=2]/text()')[0]
                        baseinfo.registerNum = trs1[0].xpath('./td[position()=2]/text()')[0]
                        baseinfo.tissueNum = trs1[0].xpath('./td[position()=4]/text()')[0]
                        baseinfo.creditNum = trs1[1].xpath('./td[position()=2]/text()')[0]
                        baseinfo.companyType =trs1[1].xpath('./td[position()=4]/text()')[0]
                        baseinfo.taxpayerNum = trs1[2].xpath('./td[position()=2]/text()')[0]
                        baseinfo.industry = trs1[2].xpath('./td[position()=4]/text()')[0]
                        baseinfo.businessTerm = trs1[3].xpath('./td[position()=2]/span/text()')[0]
                        baseinfo.checkDate = '-'
                        baseinfo.registerOffice = trs1[5].xpath('./td[position()=4]/text()')[0]
                        baseinfo.englishName = trs1[6].xpath('./td[position()=4]/text()')[0]
                        baseinfo.registerSite = trs1[7].xpath('./td[position()=2]/text()')[0]
                        businessScope = trs1[8].xpath('./td[position()=2]/span[position()=1]/span[position()=1]/span[position()=2]/text()')
                        baseinfo.businessScope=businessScope[0] if businessScope else '-'
            baseinfo.txtId = self.txtId or ''
            baseinfo.entName = key
            baseinfo.mark = 0
            baseinfo.addtime = str(datetime.now())
            baseinfo.agency_num = self.agency_num
            baseinfo.agency_name = self.agency_name
            baseinfo.batch = self.batch

        value_list = [baseinfo.txtId, baseinfo.entName, baseinfo.registerNum, baseinfo.tissueNum, baseinfo.creditNum,
                      baseinfo.companyType, baseinfo.taxpayerNum, baseinfo.industry, baseinfo.businessTerm,
                      baseinfo.checkDate, baseinfo.registerOffice, baseinfo.englishName, baseinfo.registerSite,
                      baseinfo.registerFund, baseinfo.registerDate, baseinfo.companyStatus, baseinfo.businessScope,
                      baseinfo.telephone, baseinfo.email, baseinfo.url, baseinfo.mark, baseinfo.addtime,
                      baseinfo.agency_num, baseinfo.agency_name, baseinfo.batch, branch]
        #print(value_list)
        value_list = ['"' + str(value) + '"' for value in value_list]
        insert_value += '(' + ','.join(value_list) + '),'
        insert_value = insert_value[0:-1]
        #print insert_value
        self.mysqlClient.mysql_insert(baseinfo.table_name, baseinfo.column_name, insert_value)

    # 解析：企业背景-->股东信息
    def html_parse_shareholderInfo(self):
        insert_value = ""
        key = self.entName
        logger.info("Parse detail info 股东信息 %s", key)
        trs = (self.selector.xpath('//div[@id="_container_holder"]/table/tbody/tr'))
        shareholderInfo = TycQybjGdxx()
        if trs:

            for tr in trs:
                tds=tr.xpath('.//td')
                shareholderInfo.shareholder = tds[1].xpath('./div/div[position()=2]/a/text()')[0]
                shareholderInfo.fundRatio = tds[2].xpath('./div/div/span/text()')[0]
                shareholderInfo.fundSubcribe = tds[3].xpath('./div/span/text()')[0]
                shareholderInfo.txtId = self.txtId
                shareholderInfo.entName = key
                shareholderInfo.mark = str(0)
                shareholderInfo.addtime = str(datetime.now())
                shareholderInfo.agency_num = self.agency_num
                shareholderInfo.agency_name = self.agency_name
                shareholderInfo.batch = self.batch
                value_list = [shareholderInfo.txtId, shareholderInfo.entName, shareholderInfo.shareholder,
                              shareholderInfo.fundRatio, shareholderInfo.fundSubcribe, shareholderInfo.mark,
                              shareholderInfo.addtime, shareholderInfo.agency_num, shareholderInfo.agency_name,
                              shareholderInfo.batch]
                value_list = ['"' + value + '"' for value in value_list]
                insert_value += '(' + ','.join(value_list) + '),'
            insert_value = insert_value[0:-1]
            self.mysqlClient.mysql_insert(shareholderInfo.table_name, shareholderInfo.column_name, insert_value)

    # 解析：企业发展-->融资历史
    def html_parse_financeHistory(self):
        insert_value = ""
        key = self.entName
        logger.info("Parse detail info 融资历史 %s", key)
        trs = (self.selector.xpath('//div[@id="_container_rongzi"]//table/tbody/tr'))
        financeHistory = TycQyfzRzls()
        if trs:
            for tr in trs:
                tds = tr.xpath('./td')
                financeHistory.financeDate = tds[1].xpath('string(.)').replace('\n', '').replace(' ', '')
                financeHistory.financeRound = tds[2].xpath('string(.)').replace('\n', '').replace(' ', '')
                financeHistory.financeValue = tds[3].xpath('string(.)').replace('\n', '').replace(' ', '')
                financeHistory.financeMoney = tds[4].xpath('string(.)').replace('\n', '').replace(' ', '')
                financeHistory.financeRatio = tds[5].xpath('string(.)').replace('\n', '').replace(' ', '')
                financeHistory.financeInvestor =''
                touzi= tds[6].xpath('string(.)')
                financeInvestor = ""
                touzifangs=(tds[6].xpath('.//a/text()'))
                if touzifangs:
                    for touzi in touzifangs:
                        financeInvestor+=touzi.replace('\n', '').replace(' ', '')+';'
                financeHistory.financeInvestor=financeInvestor
                source=tds[7].xpath('string(.)').replace('\n', '').replace(' ', '')
                if len(source)>22:
                    financeHistory.financeSource = tds[7].xpath('./a/text()').replace('\n', '').replace(' ', '')
                else:
                    financeHistory.financeSource='-'
                financeHistory.txtId = self.txtId
                financeHistory.entName = key
                financeHistory.mark = str(0)
                financeHistory.addtime = str(datetime.now())
                financeHistory.agency_num = self.agency_num
                financeHistory.agency_name = self.agency_name
                financeHistory.batch = self.batch
                value_list = [financeHistory.txtId, financeHistory.entName, financeHistory.financeDate,
                              financeHistory.financeRound, financeHistory.financeValue, financeHistory.financeMoney,
                              financeHistory.financeRatio, financeHistory.financeInvestor, financeHistory.financeSource,
                              financeHistory.mark, financeHistory.addtime, financeHistory.agency_num,
                              financeHistory.agency_name, financeHistory.batch]
                value_list = ['"' + value + '"' for value in value_list]
                insert_value += '(' + ','.join(value_list) + '),'
            insert_value = insert_value[0:-1]
            self.mysqlClient.mysql_insert(financeHistory.table_name, financeHistory.column_name, insert_value)

    # 产品信息
    def html_parse_product(self, index):
        flss = TycJyzkCpxx()
        key = self.entName
        logger.info("Parse detail info 产品信息 %s", key)
        if index == 1:
            root_div = (self.selector.xpath('//table'))[0]
        else:
            # 获得产品信息大标签
            root_div = (self.selector.xpath('//div[@id="_container_product"]/table'))
        if root_div:
            # 一行是一个tr
            root_div=root_div[0]
            trs = root_div.xpath("./tbody/tr")
            insert_value = ""
            for tr in trs:
                tds = tr.xpath("./td")
                flss.product_name = tds[1].xpath('./table/tbody/tr/td[1]/span/text()')
                flss.product_referred = tds[2].xpath('./span/text()')
                flss.product_classification = tds[3].xpath('./span/text()')
                flss.field = tds[4].xpath('./span/text()')
                flss.detail_info = '详情'
                flss.txt_id = self.txtId
                flss.ent_name = key
                flss.add_time = str(datetime.now())
                flss.mark = str(0)
                flss.agency_num = self.agency_num
                flss.agency_name = self.agency_name
                flss.batch = self.batch
                value_list = [flss.product_name, flss.product_referred, flss.product_classification, flss.field,
                              flss.detail_info, flss.txt_id, flss.ent_name, flss.add_time, flss.mark, flss.agency_num,
                              flss.agency_name, flss.batch]
                value_list = ['"' + value + '"' for value in value_list]
                insert_value += '(' + ','.join(value_list) + '),'
            insert_value = insert_value[0:-1]
            self.mysqlClient.mysql_insert(flss.table_name, flss.column_name, insert_value)

    # 专利信息
    def html_parse_patent(self, index):
        flss = TycZscqZl()
        key = self.entName
        logger.info("Parse detail info 专利信息 %s", key)
        if index == 1:
            root_div = (self.selector.xpath("//table"))[0]
        else:
            # 获得专利信息大标签
            root_div = self.selector.xpath('//div[@id="_container_patent"][position()=1]/table')
        if root_div:
            # 一行是一个tr
            root_div=root_div[0]
            trs = root_div.xpath("./tbody/tr")
            insert_value = ""
            for tr in trs:
                tds = tr.xpath("./td")
                flss.apply_publish_date = tds[1].xpath('./span/text()')[0]
                flss.patent_name = tds[2].xpath('./span/text()')[0]
                flss.apply_number = tds[3].xpath('./span/text()')[0]
                flss.apply_publish_number =tds[4].xpath('./span/text()')[0]
                flss.detail_info = '详情..'
                flss.txt_id = self.txtId
                flss.ent_name = key
                flss.add_time = str(datetime.now())
                flss.mark = str(0)
                flss.agency_num = self.agency_num
                flss.agency_name = self.agency_name
                flss.batch = self.batch
                value_list = [flss.apply_publish_date, flss.patent_name, flss.apply_number, flss.apply_publish_number,
                              flss.detail_info, flss.txt_id, flss.ent_name, flss.add_time, flss.mark, flss.agency_num,
                              flss.agency_name, flss.batch]
                value_list = ['"' + str(value) + '"' for value in value_list]
                insert_value += '(' + ','.join(value_list) + '),'
            insert_value = insert_value[0:-1]
            #print(insert_value)
            self.mysqlClient.mysql_insert(flss.table_name, flss.column_name, insert_value)

    # 抽查检查
    def html_parse_check(self, index):
        flss = TycJyzkCcjc()
        key = self.entName
        logger.info("Parse detail info 抽查检查 %s", key)
        if index == 1:
            root_div = (self.selector.xpath('//table'))[0]
        else:
            # 获得抽查检查大标签
            root_div = (self.selector.xpath('//div[@id="_container_check"]/table'))
        if root_div:
            # 一行是一个tr
            root_div=root_div[0]
            trs = root_div.xpath("./tbody/tr")
            insert_value = ""
            for tr in trs:
                tds = tr.xpath("./td")
                flss.date = tds[1].xpath('./text()')
                flss.type = tds[2].xpath('./text()')
                flss.result = tds[3].xpath('./text()')
                flss.check_department = tds[4].xpath('./text()')
                flss.txt_id = self.txtId
                flss.ent_name = key
                flss.add_time = str(datetime.now())
                flss.mark = str(0)
                flss.agency_num = self.agency_num
                flss.agency_name = self.agency_name
                flss.batch = self.batch
                value_list = [flss.date, flss.type, flss.result, flss.check_department, flss.txt_id, flss.ent_name,
                              flss.add_time, flss.mark, flss.agency_num, flss.agency_name, flss.batch]
                value_list = ['"' + value + '"' for value in value_list]
                insert_value += '(' + ','.join(value_list) + '),'
            insert_value = insert_value[0:-1]
            self.mysqlClient.mysql_insert(flss.table_name, flss.column_name, insert_value)

    # 法院公告
    def html_parse_announcement(self, index):
        flss = TycSffxFygg()
        key = self.entName
        logger.info("Parse detail info 法院公告 %s", key)
        if index == 1:
            root_div = self.selector.xpath('//table')
        else:
            # 获得法院公告大标签
            root_div = self.selector.xpath('//div[@id="_container_court"]/table')

        if root_div:
            # 一行是一个tr
            root_div = root_div[0]
            trs = root_div.xpath("./tbody/tr")
            insert_value = ""
            for tr in trs:
                tds = tr.xpath("./td")
                flss.announcement_date = tds[1].xpath('./text()')[0]
                plaintiff = tds[2].xpath('.//a/text()')
                if plaintiff:
                    flss.plaintiff=plaintiff[0]
                else:
                    plaintiff=tds[2].xpath('./span/text()')
                    if plaintiff:
                        flss.plaintiff = plaintiff[0]
                    else:
                        flss.plaintiff =''
                        #TODO
                defendant = tds[3].xpath('/text()')
                flss.defendant=defendant[0] if defendant else '-'

                flss.announcement_type = tds[4].xpath('./span/text()')[0]
                flss.court = tds[5].xpath('./span/text()')[0]
                flss.detail_info = '操作..'
                flss.txt_id = self.txtId
                flss.ent_name = key
                flss.add_time = str(datetime.now())
                flss.mark = str(0)
                flss.agency_num = self.agency_num
                flss.agency_name = self.agency_name
                flss.batch = self.batch
                value_list = [flss.announcement_date, flss.plaintiff, flss.defendant, flss.announcement_type,
                              flss.court, flss.detail_info, flss.txt_id, flss.ent_name, flss.add_time, flss.mark,
                              flss.agency_num, flss.agency_name, flss.batch]
                value_list = ['"' + str(value) + '"' for value in value_list]
                insert_value += '(' + ','.join(value_list) + '),'
            insert_value = insert_value[0:-1]
            if insert_value:
                #print(insert_value)
                self.mysqlClient.mysql_insert(flss.table_name, flss.column_name, insert_value)

    # 解析：企业背景--竞品信息
    def html_parse_jpInfo(self, index):
        insert_value = ""
        key = self.entName
        logger.info("Parse detail info 竞品信息 %s", key)
        if index == 1:
            trs = self.selector.xpath('//table/tbody/tr')
        else:
            trs = self.selector.xpath('//div[@id="_container_jingpin"]//table/tbody/tr')
        jpInfo = TycQyfzJpxx()

        if trs:

            for tr in trs:
                tds = tr.xpath('./td')
                jpInfo.jpProduct = tds[1].xpath('./a[-1]/text()').replace('\n', '').replace(' ', '')
                jpInfo.jpArea = tds[2].xpath('string(.)').replace('\n', '').replace(' ', '')
                jpInfo.jpRound = tds[3].xpath('string(.)').replace('\n', '').replace(' ', '')
                jpInfo.jpIndustry = tds[4].xpath('string(.)').replace('\n', '').replace(' ', '')
                jpInfo.jpBusiness = tds[5].xpath('string(.)').replace('\n', '').replace(' ', '')
                jpInfo.jpDate = tds[6].xpath('string(.)').replace('\n', '').replace(' ', '')
                jpInfo.jpValue = tds[7].xpath('string(.)').replace('\n', '').replace(' ', '')
                jpInfo.txtId = self.txtId
                jpInfo.entName = key
                jpInfo.mark = str(0)
                jpInfo.addtime = str(datetime.now())
                jpInfo.agency_num = self.agency_num
                jpInfo.agency_name = self.agency_name
                jpInfo.batch = self.batch
                value_list = [jpInfo.txtId, jpInfo.entName, jpInfo.jpProduct, jpInfo.jpArea, jpInfo.jpRound,
                              jpInfo.jpIndustry, jpInfo.jpBusiness, jpInfo.jpDate, jpInfo.jpValue, jpInfo.mark,
                              jpInfo.addtime, jpInfo.agency_num, jpInfo.agency_name, jpInfo.batch]
                value_list = ['"' + value + '"' for value in value_list]
                insert_value += '(' + ','.join(value_list) + '),'
            insert_value = insert_value[0:-1]
            self.mysqlClient.mysql_insert(jpInfo.table_name, jpInfo.column_name, insert_value)
    # {"a":{"b":"c"}}
    # 解析：企业背景--企业业务
    def html_parse_entBusiness(self, index):
        insert_value = ""
        key = self.entName
        logger.info("Parse detail info 企业业务 %s", key)
        if index == 1:
            divs = selector.xpath('//div/a')
        else:
            divs = self.selector.xpath(
                '//div[@id="_container_firmProduct"]/div/a')
        entBusiness = TycQyfzQyyw()

        if divs:
            divs = divs[0]
            for div in divs:
                entBusiness.businessName = div.xpath('./div[position()=2]/div[position()=1]/text()')
                entBusiness.businessQuale = div.xpath('./div[position()=2]/div[position()=2]/text()')
                entBusiness.businessInfo = div.xpath('./div[position()=2]/div[position()=3]/text()')
                entBusiness.txtId = self.txtId
                entBusiness.entName = key
                entBusiness.mark = str(0)
                entBusiness.addtime = str(datetime.now())
                entBusiness.agency_num = self.agency_num
                entBusiness.agency_name = self.agency_name
                entBusiness.batch = self.batch
                value_list = [entBusiness.txtId, entBusiness.entName, entBusiness.businessName,
                              entBusiness.businessQuale, entBusiness.businessInfo, entBusiness.mark,
                              entBusiness.addtime, entBusiness.agency_num, entBusiness.agency_name, entBusiness.batch]
                value_list = ['"' + value + '"' for value in value_list]
                insert_value += '(' + ','.join(value_list) + '),'
            insert_value = insert_value[0:-1]
            self.mysqlClient.mysql_insert(entBusiness.table_name, entBusiness.column_name, insert_value)

    # 解析：企业背景--投资事件
    def html_parse_investEvent(self, index):
        insert_value = ""
        key = self.entName
        logger.info("Parse detail info 投资事件 %s", key)
        if index == 1:
            trs = self.selector.xpath('//table/tbody/tr')
        else:
            trs = self.selector.xpath('//div[@id="_container_touzi"]//table/tbody/tr')
        investEvent = TycQyfzTzsj()

        if trs:
            trs = trs[0]
            for tr in trs:
                tds = tr.xpath('./td')
                investEvent.touziDate = tds[1].xpath('string(.)').replace('\n', '').replace(' ', '')
                investEvent.touziRound = tds[2].xpath('string(.)').replace('\n', '').replace(' ', '')
                investEvent.touziMoney = tds[3].xpath('string(.)').replace('\n', '').replace(' ', '')
                investEvent.touziEnt = (tds[4].xpath('//a/text()'))[0].replace('\n', '').replace(' ', '')
                investEvent.touziProduct = (tds[5].xpath('//a/text()'))[0].replace('\n', '').replace(' ', '')
                investEvent.touziArea = tds[6].xpath('string(.)').replace('\n', '').replace(' ', '')
                investEvent.touziIndustry = tds[7].xpath('/a/text()').replace('\n', '').replace(' ', '')
                investEvent.touziBusiness = tds[8].xpath('string(.)').replace('\n', '').replace(' ', '')
                investEvent.txtId = self.txtId
                investEvent.entName = key
                investEvent.mark = str(0)
                investEvent.addtime = str(datetime.now())
                investEvent.agency_num = self.agency_num
                investEvent.agency_name = self.agency_name
                investEvent.batch = self.batch
                value_list = [investEvent.txtId, investEvent.entName, investEvent.touziDate, investEvent.touziRound,
                              investEvent.touziMoney, investEvent.touziEnt, investEvent.touziProduct,
                              investEvent.touziArea, investEvent.touziIndustry, investEvent.touziBusiness,
                              investEvent.mark, investEvent.addtime, investEvent.agency_num, investEvent.agency_name,
                              investEvent.batch]
                value_list = ['"' + value + '"' for value in value_list]
                insert_value += '(' + ','.join(value_list) + '),'
            insert_value = insert_value[0:-1]
            self.mysqlClient.mysql_insert(investEvent.table_name, investEvent.column_name, insert_value)

    # 解析：企业背景--核心团队
    def html_parse_coreTeam(self, index):
        insert_value = ""
        coreTeam = TycQyfzHxtd()
        key = self.entName
        logger.info("Parse detail info 核心团队 %s", key)
        if index == 1:
            divs = self.selector.xpath('//div[@class="card-team"]')
        else:
            divs = self.selector.xpath('//div[@id="_container_teamMember"]//div[@class="card-team"]')

        if divs:
            divs = divs[0]
            for div in divs:
                coreTeam.personName = div.xpath('.//div[@class="name"]/text()')[0].strip()
                position=div.xpath('./div[position()=2]/div/text()')
                ps= div.xpath('./div[position()=2]/p/text()')
                personInfo=''
                for p in ps:
                    personInfo += str(p)+'、'
                coreTeam.personInfo = personInfo
                coreTeam.txtId = self.txtId
                coreTeam.entName = key
                coreTeam.mark = str(0)
                coreTeam.addtime = str(datetime.now())
                coreTeam.agency_num = self.agency_num
                coreTeam.agency_name = self.agency_name
                coreTeam.batch = self.batch
                value_list = [coreTeam.txtId, coreTeam.entName, coreTeam.personName, coreTeam.personInfo, coreTeam.mark,
                              coreTeam.addtime, coreTeam.agency_num, coreTeam.agency_name, coreTeam.batch]
                value_list = ['"' + value + '"' for value in value_list]
                insert_value += '(' + ','.join(value_list) + '),'
            insert_value = insert_value[0:-1]
            self.mysqlClient.mysql_insert(coreTeam.table_name, coreTeam.column_name, insert_value)

    # 网站备案
    def html_parse_website(self, index):
        flss = TycZscqWzba()
        key = self.entName
        logger.info("Parse detail info 网站备案 %s", key)
        if index == 1:
            root_div = self.selector.xpath('//table')
        else:
            # 获得网站备案大标签
            root_div = self.selector.xpath('//div[@id="_container_icp"]/table')

        if root_div:
            root_div = root_div[0]
            # 一行是一个tr
            trs = root_div.xpath("./tbody/tr")
            insert_value = ""
            for tr in trs:
                tds = tr.xpath('./td')
                flss.audit_date = tds[1].xpath('./span/text()')[0]
                flss.web_name = tds[2].xpath('./span/text()')[0]
                flss.web_homepage = tds[3].xpath('.//a//text()')[0]
                domain_name = tds[4].xpath('./span/text()')
                flss.domain_name = domain_name[0] if domain_name   else '-'
                record_number=tds[5].xpath('./span/text()')
                flss.record_number = record_number[0] if record_number   else '-'
                flss.status = tds[6].xpath('./span/text()')[0]
                flss.department_type = tds[7].xpath('./span/text()')[0]

                flss.txt_id = self.txtId
                flss.ent_name = key
                flss.add_time = str(datetime.now())
                flss.mark = str(0)
                flss.agency_num = self.agency_num
                flss.agency_name = self.agency_name
                flss.batch = self.batch
                value_list = [flss.audit_date, flss.web_name, flss.web_homepage, flss.domain_name, flss.record_number,
                              flss.status, flss.department_type, flss.txt_id, flss.ent_name, flss.add_time, flss.mark,
                              flss.agency_num, flss.agency_name, flss.batch]
                value_list = ['"' + value + '"' for value in value_list]
                insert_value += '(' + ','.join(value_list) + '),'
            insert_value = insert_value[0:-1]
            self.mysqlClient.mysql_insert(flss.table_name, flss.column_name, insert_value)

    # 股权出质
    def html_parse_pledge(self, index):
        flss = TycJyfxGqcz()
        key = self.entName
        logger.info("Parse detail info 股权出质 %s", key)
        if index == 1:
            root_div = self.selector.xpath('//table[position()=1]')
        else:
            # 获得股权出质大标签
            root_div = self.selector.xpath('//div[@id="_container_equity"][position()=1]/table')
        if root_div:
            # 一行是一个tr
            trs = root_div.xpath("./tbody/tr")
            insert_value = ""
            for tr in trs:
                tds = tr.xpath("./td")
                flss.announcement_date = tds[1].xpath('./text()')[0]
                flss.registration_number = tds[2].xpath('./text()')[0]
                flss.pledgor = tds[3].xpath('./a/text()')[0]
                flss.pledgee = tds[4].xpath('./a/text()')[0]
                flss.status = tds[5].xpath('./text()')[0]
                flss.detail_info = '详情..'
                flss.txt_id = self.txtId
                flss.ent_name = key
                flss.add_time = str(datetime.now())
                flss.mark = str(0)
                flss.agency_num = self.agency_num
                flss.agency_name = self.agency_name
                flss.batch = self.batch
                value_list = [flss.announcement_date, flss.registration_number, flss.pledgor, flss.pledgee, flss.status,
                              flss.detail_info, flss.txt_id, flss.ent_name, flss.add_time, flss.mark, flss.agency_num,
                              flss.agency_name, flss.batch]
                value_list = ['"' + value + '"' for value in value_list]
                insert_value += '(' + ','.join(value_list) + '),'
            insert_value = insert_value[0:-1]
            self.mysqlClient.mysql_insert(flss.table_name, flss.column_name, insert_value)

    # 解析：企业背景-->变更记录
    def html_parse_alterRecord(self, index):
        insert_value = ""
        key = self.entName
        logger.info("Parse detail info 变更记录 %s", key)

        if index == 1:
            trs = self.selector.xpath('//table[position()=1]/tbody/tr')
        else:
            trs = self.selector.xpath('//div[@id="_container_changeinfo"]//table/tbody/tr')
        alterRecord = TycQybjBgjl()
        if trs:
            for tr in trs:
                alterRecord = TycQybjBgjl()
                tds = tr.xpath('./td')
                tds_len=len(tds)
                alterDate = tds[1].xpath('text()')
                alterRecord.alterDate = alterDate[0] if alterDate else '-'
                alterProject = tds[2].xpath('text()')
                alterRecord.alterProject = alterProject[0] if alterProject else '-'
                alterBefor = tds[3].xpath('./div/text()')
                alterRecord.alterBefor = alterBefor[0].replace('\n', '').replace(r'<em><font color="#EF5644">','').replace(r'</font></em>','').replace(r'<em><font style="color:#9E9E9E;text-decoration:line-through;text-decoration-color:#ff3b30;">','') if alterBefor else '-'
                alterAfter = tds[4].xpath('./div/text()')
                alterRecord.alterAfter = alterAfter[0].replace('\n', '').replace(r'<em><font color="#EF5644">','').replace(r'</font></em>','').replace(r'<em><font style="color:#9E9E9E;text-decoration:line-through;text-decoration-color:#ff3b30;">','') if alterAfter else '-'
                # <em><font color="#EF5644">长</font></em>
                alterRecord.txtId = self.txtId
                alterRecord.entName = key
                alterRecord.mark = str(0)
                alterRecord.addtime = str(datetime.now())
                alterRecord.agency_num = self.agency_num
                alterRecord.agency_name = self.agency_name
                alterRecord.batch = self.batch
                value_list = [alterRecord.txtId, alterRecord.entName, alterRecord.alterDate, alterRecord.alterProject,
                              alterRecord.alterBefor, alterRecord.alterAfter, alterRecord.mark, alterRecord.addtime,
                              alterRecord.agency_num, alterRecord.agency_name, alterRecord.batch]
                value_list = ['"' + value + '"' for value in value_list]
                insert_value += '(' + ','.join(value_list) + '),'
            insert_value = insert_value[0:-1]
            self.mysqlClient.mysql_insert(alterRecord.table_name, alterRecord.column_name, insert_value)

    # 分支机构
    def html_parse_branch(self, index):
        flss = TycQybjFzjg()
        key = self.entName
        logger.info("Parse detail info 分支机构 %s", key)
        if index == 1:
            root_div = self.selector.xpath(".//table[position()=1]")
        else:
            # 获得分支机构大标签
            root_div = self.selector.xpath('//div[@id="_container_branch"]/table')
        if root_div:
            # 一行是一个tr
            root_div=root_div[0]
            trs = root_div.xpath("tbody/tr")
            insert_value = ""
            for tr in trs:
                tds = tr.xpath("td")
                company_name=tds[1].xpath('//td/a/text()')
                flss.company_name = company_name[0] if company_name else self.entName

                flss.legal_representative = tds[2].xpath('./span/text()')[0]
                flss.registered_date= tds[3].xpath('./span/text()')[0]
                flss.status = tds[4].xpath('./span/text()')[0]
                flss.txt_id = self.txtId
                flss.ent_name = key
                flss.add_time = str(datetime.now())
                flss.mark = str(0)
                flss.agency_num = self.agency_num
                flss.agency_name = self.agency_name
                flss.batch = self.batch
                value_list = [flss.company_name, flss.legal_representative, flss.status, flss.registered_date,
                              flss.txt_id, flss.ent_name, flss.add_time, flss.mark, flss.agency_num, flss.agency_name,
                              flss.batch]
                value_list = ['"' + value + '"' for value in value_list]
                insert_value += '(' + ','.join(value_list) + '),'
            insert_value = insert_value[0:-1]
            self.mysqlClient.mysql_insert(flss.table_name, flss.column_name, insert_value)

    # 解析：企业背景-->对外投资
    def html_parse_investInfo(self, index):
        insert_value = ""
        key = self.entName
        logger.info("Parse detail info 对外投资 %s", key)

        if index == 1:

            trs = self.selector.xpath('//table/tbody/tr')
        else:
            trs = self.selector.xpath(
                '//div[@id="_container_invest"]/table/tbody/tr')
        # //div[@class="out-investment-container"]/table/tbody/tr
        investInfo = TycQybjDwtz()
        if trs:

            for tr in trs:
                tds = tr.xpath('./td')
                investInfo.investCompany = tds[1].xpath('//td[position()=2]/a/text()')[0]
                investInfo.investPerson = tds[2].xpath('./span/a/text()')[0]
                investInfo.investFund = tds[3].xpath('./span/text()')[0]
                # investInfo.investAmount = tds[4].xpath('string(.)').replace('\n', '').replace(' ', '')
                investInfo.investRatio = tds[4].xpath('./span/text()')[0]
                investInfo.investDate = tds[5].xpath('./span/text()')[0]
                investInfo.investStatus = tds[6].xpath('./span/text()')[0]
                investInfo.txtId = self.txtId
                investInfo.entName = key
                investInfo.mark = str(0)
                investInfo.addtime = str(datetime.now())
                investInfo.agency_num = self.agency_num
                investInfo.agency_name = self.agency_name
                investInfo.batch = self.batch
                value_list = [investInfo.txtId, investInfo.entName, investInfo.investCompany, investInfo.investPerson,
                              investInfo.investFund, investInfo.investAmount, investInfo.investRatio,
                              investInfo.investDate, investInfo.investStatus, investInfo.mark, investInfo.addtime,
                              investInfo.agency_num, investInfo.agency_name, investInfo.batch]
                value_list = ['"' + value + '"' for value in value_list]
                insert_value += '(' + ','.join(value_list) + '),'
            insert_value = insert_value[0:-1]
            self.mysqlClient.mysql_insert(investInfo.table_name, investInfo.column_name, insert_value)

    # 进出口信用
    def html_parse_outputxy(self):
        flss = TycJyzkJckxy()
        key = self.entName
        logger.info("Parse detail info 进出口信用 %s", key)
        # 获得大标签
        root_div = self.selector.xpath('//div[@id="_container_importAndExport"][0]')
        if root_div:
            # 一行是一个tr
            root_div=root_div[0]
            trs = root_div.xpath("./table/tbody/tr")
            insert_value = ""
            for tr in trs:
                tds = tr.xpath("/td")
                flss.register_customs = tds[0].xpath('./text()')[0]
                flss.customs_number = tds[1].xpath('./text()')[0]
                flss.manger_type = tds[2].xpath('./text()')[0]
                flss.detail_info = '详情..'
                flss.txtId = self.txtId
                flss.ent_name = key
                flss.add_time = str(datetime.now())
                flss.mark = str(0)
                flss.agency_num = self.agency_num
                flss.agency_name = self.agency_name
                flss.batch = self.batch
                value_list = [flss.register_customs, flss.customs_number, flss.manger_type, flss.detail_info,
                              flss.txtId, flss.ent_name, flss.mark, flss.add_time, flss.agency_num, flss.agency_name,
                              flss.batch]
                value_list = ['"' + value + '"' for value in value_list]
                insert_value += '(' + ','.join(value_list) + '),'
            insert_value = insert_value[0:-1]
            self.mysqlClient.mysql_insert(flss.table_name, flss.column_name, insert_value)

    # 作品著作权
    def html_parse_copyzzq(self, index):
        flss = TycZscqZpzzq()
        key = self.entName
        logger.info("Parse detail info 作品著作权 %s", key)

        # 获得作品著作权大标签
        if index == 1:
            root_div = self.selector.xpath(".//table[position()=1]")
        else:
            root_div = self.selector.xpath('//div[@id="_container_copyrightWorks"][position()=2]')

        if root_div:
            root_div=root_div[0]
            trs = root_div.xpath("./table/tbody/tr")
            insert_value = ""
            for tr in trs:
                # 作品名称	登记号	类别	 创作完成日期	登记日期	首次发布日期
                tds = tr.xpath("./td")
                flss.works_name = tds[1].xpath('./text()')[0]
                flss.register_name = tds[2].xpath('./text()')[0]
                flss.type = tds[3].xpath('./text()')[0]
                flss.creat_date = tds[4].xpath('./text()')[0]
                flss.register_date = tds[5].xpath('./text()')[0]
                flss.firstpublish_date = tds[6].xpath('./text()')[0]
                flss.txtId = self.txtId
                flss.ent_name = key
                flss.add_time = str(datetime.now())
                flss.mark = str(0)
                flss.agency_num = self.agency_num
                flss.agency_name = self.agency_name
                flss.batch = self.batch
                value_list = [flss.works_name, flss.register_name, flss.type, flss.creat_date, flss.register_date,
                              flss.firstpublish_date, flss.txtId, flss.ent_name, flss.add_time, flss.mark,
                              flss.agency_num, flss.agency_name, flss.batch]
                value_list = ['"' + value + '"' for value in value_list]
                insert_value += '(' + ','.join(value_list) + '),'
            insert_value = insert_value[0:-1]
            self.mysqlClient.mysql_insert(flss.table_name, flss.column_name, insert_value)

    # 微信公众号解析
    def html_parse_entWechat(self, index):
        insert_value = ""
        key = self.entName
        logger.info("Parse detail info 微信公众号 %s", key)
        if index:
            divs = self.selector.xpath('//div[@class="wechat"][position()=1]')
        else:
            divs = self.selector.xpath(
                '//div[@id="_container_wechat"][position()=1]/div[@class="wechat-list"]//div[@class="wechat"][position()=1]')
        entWeChat = TycJyzkWxgzh()
        if divs:
            for div in divs:
                entWeChat.mp_name = div.xpath('.//div[@class="content"][position()=1]/div[@class="title"]/text()')[0]
                entWeChat.mp_number = div.xpath('.//div[@class="content"][position()=1]/div[position()=2]/span[1]/text()')[0]
                entWeChat.mp_info = div.xpath('.//div[@class="content"][position()=1]/div[position()=3]/span[position()=2]/text()')[0]
                entWeChat.txtId = self.txtId
                entWeChat.ent_name = key
                entWeChat.mark = str(0)
                entWeChat.addtime = str(datetime.now())
                entWeChat.agency_num = self.agency_num
                entWeChat.agency_name = self.agency_name
                entWeChat.batch = self.batch
                value_list = [entWeChat.mp_name, entWeChat.mp_number, entWeChat.mp_info, entWeChat.txtId,
                              entWeChat.ent_name, entWeChat.mark, entWeChat.addtime, entWeChat.agency_num,
                              entWeChat.agency_name, entWeChat.batch]
                value_list = ['"' + value + '"' for value in value_list]
                insert_value += '(' + ','.join(value_list) + '),'
            insert_value = insert_value[0:-1]
            self.mysqlClient.mysql_insert(entWeChat.table_name, entWeChat.column_name, insert_value)

    # 商标信息
    def html_parse_trademark(self, index):
        flss = TycZscqSbxx()
        key = self.entName
        logger.info("Parse detail info 商标信息 %s", key)

        if index == 1:
            root_div = self.selector.xpath("//table")
        else:
            # 获得商标信息大标签
            root_div = self.selector.xpath('//div[@id= "_container_tmInfo"][position()=1]/table')
        if root_div:
            # 一行是一个tr
            root_div=root_div[0]
            trs = root_div.xpath("./tbody//tr[position()=1]")
            insert_value = ""
            for tr in trs:
                tds = tr.xpath("./td")
                if tds:
                    flss.apply_date = tds[1].xpath('./span/text()')[0]
                    flss.trademark = tds[2].xpath('./span/img/@src')[0]
                    flss.trademark_name = tds[3].xpath('./span/text()')[0]
                    flss.registration_number = tds[4].xpath('./span/text()')[0]
                    flss.type = tds[5].xpath('./span/text()')[0]
                    flss.status = tds[6].xpath('./span/text()')[0]
                    flss.txt_id = self.txtId
                    flss.ent_name = key
                    flss.add_time = str(datetime.now())
                    flss.mark = str(0)
                    flss.agency_num = self.agency_num
                    flss.agency_name = self.agency_name
                    flss.batch = self.batch
                    value_list = [flss.apply_date, flss.trademark, flss.trademark_name, flss.registration_number, flss.type,
                                  flss.status, flss.txt_id, flss.ent_name, flss.add_time, flss.mark, flss.agency_num,
                                  flss.agency_name, flss.batch]
                    value_list = ['"' + value + '"' for value in value_list]
                    insert_value += '(' + ','.join(value_list) + ')'
                insert_value = insert_value[0:-1]
                self.mysqlClient.mysql_insert(flss.table_name, flss.column_name, insert_value)


    # 软件著作权
    def html_parse_copyright(self, index):
        flss = TycZscqZzq()
        key = self.entName
        logger.info("Parse detail info 软件著作权 %s", key)
        if index == 1:
            root_div = self.selector.xpath("//table[position()=1]")
        else:
            root_div = self.selector.xpath('//div[@id="_container_copyright"][position()=1]/table')
        # 获得著作权大标签
        if root_div:
            # 一行是一个tr
            root_div=root_div[0]
            trs = root_div.xpath("./tbody/tr")
            insert_value = ""
            for tr in trs:
                tds = tr.xpath("./td")
                flss.approval_date = tds[1].xpath('./span/text()')[0]
                flss.software_name = tds[2].xpath('./span/text()')[0]
                flss.software_referred = tds[3].xpath('./span/text()')[0]
                flss.registration_number = tds[4].xpath('./span/text()')[0]
                flss.type_number = tds[5].xpath('./span/text()')[0]
                flss.version_number = tds[6].xpath('./span/text()')[0]
                flss.detail_info = '详情..'

                flss.txt_id = self.txtId
                flss.ent_name = key
                flss.add_time = str(datetime.now())
                flss.mark = str(0)
                flss.agency_num = self.agency_num
                flss.agency_name = self.agency_name
                flss.batch = self.batch
                value_list = [flss.approval_date, flss.software_name, flss.software_referred, flss.registration_number,
                              flss.type_number, flss.version_number, flss.detail_info, flss.txt_id, flss.ent_name,
                              flss.add_time, flss.mark, flss.agency_num, flss.agency_name, flss.batch]
                value_list = ['"' + value + '"' for value in value_list]
                insert_value += '(' + ','.join(value_list) + '),'
            insert_value = insert_value[0:-1]
            self.mysqlClient.mysql_insert(flss.table_name, flss.column_name, insert_value)

    # 解析：经营状况--资质证书
    def html_parse_certificateInfo(self, index):
        insert_value = ""
        key = self.entName
        logger.info("Parse detail info 资质证书 %s", key)
        if index == 1:
            trs = self.selector.xpath('//table[position()=1]/tbody/tr')
        else:
            trs = self.selector.xpath('//div[@id="_container_certificate"][position()=1]//table[position()=1]/tbody/tr')

        if trs:
            for tr in trs:
                certificateInfo = TycJyzkZzzs()
                tds = tr.xpath('./td')
                certificateInfo.certificateType = tds[1].xpath('./span/text()')[0]
                certificateInfo.certificateNum = tds[2].xpath('./span/text()')[0]
                certificateInfo.sendDate = tds[3].xpath('./span/text()')[0]
                certificateInfo.offDate = tds[4].xpath('./span/text()')[0]
                # certificateInfo.deviceNum = tds[4].xpath('string(.)').replace('\n', '').replace(' ', '')
                # certificateInfo.permitNum = tds[5].xpath('string(.)').replace('\n', '').replace(' ', '')
                certificateInfo.txtId = self.txtId
                certificateInfo.entName = key
                certificateInfo.mark = str(0)
                certificateInfo.addtime = str(datetime.now())
                certificateInfo.agency_num = self.agency_num
                certificateInfo.agency_name = self.agency_name
                certificateInfo.batch = self.batch
                value_list = [certificateInfo.txtId, certificateInfo.entName, certificateInfo.certificateNum,
                              certificateInfo.certificateType, certificateInfo.sendDate, certificateInfo.offDate,
                              certificateInfo.mark, certificateInfo.addtime, certificateInfo.agency_num,
                              certificateInfo.agency_name, certificateInfo.batch]
                value_list = ['"' + value + '"' for value in value_list]
                insert_value += '(' + ','.join(value_list) + '),'
            insert_value = insert_value[0:-1]
            self.mysqlClient.mysql_insert(certificateInfo.table_name, certificateInfo.column_name, insert_value)

    # 法律诉讼
    def html_parse_lawsuit(self, law, index):
        flss = TycSffxFlss()
        key = self.entName
        logger.info("Parse detail info 法律诉讼 %s", key)
        law_true = False
        if index == 1:
            root_div = self.selector.xpath("//table[position()=1]")
            law_true=True
        else:
            # 获得法律诉讼大标签
            root_div = self.selector.xpath('//div[@id="_container_lawsuit"][position()=1]/table')
        if root_div:
            # 一行是一个tr
            root_div=root_div[0]
            trs = root_div.xpath("./tbody/tr")

            law_count=0
            for tr in trs:
                insert_value = ""
                tds = tr.xpath("./td")
                if tds:
                    flss.judgment_date = tds[1].xpath('./span/text()')[0]
                    flss.judgment_document = tds[2].xpath('./a/text()')[0].decode('utf-8')

                    tds_href= tds[2].xpath('./a/href')
                    flss.document_url=tds_href[0] if tds_href else '-'
                    case_type=tds[3].xpath('./a/text()')
                    flss.case_type = case_type[0] if case_type else '-'
                    case_identity=tds[4].xpath('./text()')
                    flss.case_identity = case_identity[0] if case_identity else '-'
                    case_number = tds[5].xpath('./a/text()')
                    flss.case_number = case_number[0].decode('gbk') if case_number else '-'
                    flss.txt_id = self.txtId
                    flss.ent_name = key
                    flss.add_time = str(datetime.now())
                    flss.mark = str(0)
                    flss.agency_num = self.agency_num
                    flss.agency_name = self.agency_name
                    # 区别key
                    flss.batch = self.batch
                    text_info=''
                    if law_true:

                        text1=law.values()[law_count]
                        law_count+=1
                        soup2 = etree.HTML(text1 )
                        text_info=soup2.xpath('//div[@class="container-left"][position()=1]/text()')
                    flss.text_info = text_info[0].replace('"', '') if text_info else '-'
                    value_list = [flss.judgment_date, flss.judgment_document, flss.case_type, flss.case_identity,
                                  flss.case_number, flss.document_url, flss.txt_id, flss.ent_name, flss.add_time, flss.mark,
                                  flss.text_info, flss.agency_num, flss.agency_name, flss.batch]
                    value_list = ['"' + str(value) + '"' for value in value_list]
                    insert_value += '(' + ','.join(value_list) + ')'
                    self.mysqlClient.mysql_insert(flss.table_name, flss.column_name, insert_value)

    # 招聘
    def html_parse_recruitment(self, index):
        flss = TycJyzkZp()
        key = self.entName
        logger.info("Parse detail info 招聘 %s", key)

        # 判断分页
        if index == 1:
            # 获得招聘大标签
            root_div = self.selector.xpath('//table[position()=1]')
        else:
            root_div = self.selector.xpath('//div[@id="_container_recruit"][position()=1]/table')
        if root_div:
            # 一行是一个tr
            root_div=root_div[0]
            trs = root_div.xpath("./tbody/tr")
            insert_value = ""
            for tr in trs:
                tds = tr.xpath("td")
                flss.publish_date = tds[1].xpath('./text()')[0]
                flss.recruitment_job = tds[2].xpath('./text()')[0]
                flss.salary = tds[3].xpath('./text()')[0]
                flss.work_year = tds[4].xpath('./text()')[0]
                flss.recruitment_numbers = tds[5].xpath('./text()')[0]
                flss.work_city = tds[6].xpath('./text()')[0]
                flss.detail_info = '详情..'
                    # tds[7].text.replace("详情 》", "").replace('\\"', '"').strip().replace('"', '\\"')
                flss.txt_id = self.txtId
                flss.ent_name = key
                flss.add_time = str(datetime.now())
                flss.mark = str(0)
                flss.agency_num = self.agency_num
                flss.agency_name = self.agency_name
                flss.batch = self.batch
                value_list = [flss.publish_date, flss.recruitment_job, flss.salary, flss.work_year,
                              flss.recruitment_numbers, flss.work_city, flss.detail_info, flss.txt_id, flss.ent_name,
                              flss.add_time, flss.mark, flss.agency_num, flss.agency_name, flss.batch]
                value_list = ['"' + value + '"' for value in value_list]
                insert_value += '(' + ','.join(value_list) + '),'
            insert_value = insert_value[0:-1]
            self.mysqlClient.mysql_insert(flss.table_name, flss.column_name, insert_value)

    # 被执行人
    def html_parse_executed(self, index):
        flss = TycSffxBzxr()
        key = self.entName
        logger.info("Parse detail info 被执行人 %s", key)
        if index == 1:
            root_div = self.selector.xpath("//table[position()=1]")
        else:
            # 获得被执行人大标签
            root_div = self.selector.xpath('//div[@id="_container_zhixing"][position()=1]/table')
        if root_div:
            root_div=root_div[0]
            # 一行是一个tr
            trs = root_div.xpath("./tbody/tr")
            insert_value = ""
            for tr in trs:
                tds = tr.xpath("./td")
                flss.record_date = tds[1].xpath('./text()')[0]
                flss.Execute_underlying = tds[2].xpath('./text()')[0]
                flss.case_number = tds[3].xpath('./text()')[0]
                flss.court = tds[4].xpath('./text()')[0]
                flss.txt_id = self.txtId
                flss.ent_name = key
                flss.add_time = str(datetime.now())
                flss.mark = str(0)
                flss.agency_num = self.agency_num
                flss.agency_name = self.agency_name
                flss.batch = self.batch
                value_list = [flss.record_date, flss.Execute_underlying, flss.case_number, flss.court, flss.txt_id,
                              flss.ent_name, flss.add_time, flss.mark, flss.agency_num, flss.agency_name, flss.batch]
                value_list = ['"' + str(value) + '"' for value in value_list]
                insert_value += '(' + ','.join(value_list) + '),'
            insert_value = insert_value[0:-1]
            if insert_value:
                self.mysqlClient.mysql_insert(flss.table_name, flss.column_name, insert_value)

    # 招投标
    def html_parse_bidding(self, index):
        flss = TycJyzkZtb()
        key = self.entName
        logger.info("Parse detail info 招投标 %s", key)
        if index == 1:
            root_div = self.selector.xpath('//table[0]')
        else:
            # 获得招投标大标签
            root_div = self.selector.xpath('//div[@id="_container_bid"][position()=1]/table')
        if root_div:
            # 一行是一个tr
            root_div=root_div[0]
            trs = root_div.xpath("./tbody/tr")
            insert_value = ""
            for tr in trs:
                tds = tr.xpath("./td")
                flss.publish_date = tds[1].xpath('./text()')[0]
                flss.title = tds[2].xpath('./a/text()')[0]
                flss.title_url= tds[2].xpath('./a/@href')[0]
                flss.procurement =tds[3].xpath('./text()')[0]
                flss.txt_id = self.txtId
                flss.ent_name = key
                flss.add_time = str(datetime.now())
                flss.mark = str(0)
                flss.agency_num = self.agency_num
                flss.agency_name = self.agency_name
                flss.batch = self.batch
                value_list = [flss.publish_date, flss.title, flss.title_url, flss.procurement, flss.txt_id,
                              flss.ent_name, flss.add_time, flss.mark, flss.agency_num, flss.agency_name, flss.batch]
                value_list = ['"' + value + '"' for value in value_list]
                insert_value += '(' + ','.join(value_list) + '),'
            insert_value = insert_value[0:-1]
            self.mysqlClient.mysql_insert(flss.table_name, flss.column_name, insert_value)

    # 债券信息
    def html_parse_zhaiquan(self, index):
        flss = TycJyzkZqxx()
        key = self.entName
        logger.info("Parse detail info 债券信息 %s", key)
        if index == 1:
            root_div = self.selector.xpath("//table[position()=1]")
        else:
            # 获得债券信息大标签
            root_div = self.selector.xpath('//div[@id="_container_bond"][position()=1]/table')
        if root_div:
            # 一行是一个tr
            root_div=root_div[0]
            trs = root_div.xpath("./tbody/tr")
            insert_value = ""
            for tr in trs:
                tds = tr.xpath("/td")
                flss.publish_date = tds[1].xpath('./text()')[0]
                flss.bond_name = tds[2].xpath('./text()')[0]
                flss.bond_code = tds[3].xpath('./text()')[0]
                flss.bond_type = tds[4].xpath('./text()')[0]
                flss.latest_rating = tds[5].xpath('./text()')[0]
                flss.detail_info ='详情..'
                    # tds[6].text.replace("详情 》", "").strip().replace('"', '\\"')
                flss.txt_id = self.txtId
                flss.ent_name = key
                flss.add_time = str(datetime.now())
                flss.mark = str(0)
                flss.agency_num = self.agency_num
                flss.agency_name = self.agency_name
                flss.batch = self.batch
                value_list = [flss.publish_date, flss.bond_name, flss.bond_code, flss.bond_type, flss.latest_rating,
                              flss.detail_info, flss.txt_id, flss.ent_name, flss.add_time, flss.mark, flss.agency_num,
                              flss.agency_name, flss.batch]
                value_list = ['"' + str(value) + '"' for value in value_list]
                insert_value += '(' + ','.join(value_list) + '),'
            insert_value = insert_value[0:-1]
            self.mysqlClient.mysql_insert(flss.table_name, flss.column_name, insert_value)

    # 解析：经营风险--欠税公告
    def html_parse_taxesNotice(self, index):
        insert_value = ""
        key = self.entName
        logger.info("Parse detail info 欠税公告 %s", key)
        if index == 1:
            trs = self.selector.xpath('//table[@class="table  companyInfo-table"][position()=1]//tbody[position()=1]/tr')
        else:
            trs = self.selector.xpath('//div[@id="_container_towntax"][position()=1]//table[position()=1]/tbody/tr')
        if trs:
            for tr in trs:
                taxesNotice = TycJyfxQsgg()
                tds = tr.xpath('./td')
                taxesNotice.taxesDate = tds[1].xpath('text()')[0]
                taxesNotice.taxesNum = tds[2].xpath('text()')[0]
                taxesNotice.taxesType = tds[3].xpath('text()')[0]
                taxesNotice.taxesMoney = tds[4].xpath('text()')[0]
                taxesNotice.taxesBalance = tds[5].xpath('text()')[0]
                taxesNotice.taxesOffice = tds[6].xpath('text()')[0]
                taxesNotice.txtId = self.txtId
                taxesNotice.entName = key
                taxesNotice.mark = str(0)
                taxesNotice.addtime = str(datetime.now())
                taxesNotice.agency_num = self.agency_num
                taxesNotice.agency_name = self.agency_name
                taxesNotice.batch = self.batch

                value_list = [taxesNotice.txtId, taxesNotice.entName, taxesNotice.taxesDate, taxesNotice.taxesNum,
                              taxesNotice.taxesType, taxesNotice.taxesMoney, taxesNotice.taxesBalance,
                              taxesNotice.taxesOffice, taxesNotice.mark, taxesNotice.addtime, taxesNotice.agency_num,
                              taxesNotice.agency_name, taxesNotice.batch]
                value_list = ['"' + str(value) + '"' for value in value_list]
                insert_value += '(' + ','.join(value_list) + '),'
            insert_value = insert_value[0:-1]
            self.mysqlClient.mysql_insert(taxesNotice.table_name, taxesNotice.column_name, insert_value)

    # 股权出质
    def html_parse_pledge(self, index):
        flss = TycJyfxGqcz()
        key = self.entName
        logger.info("Parse detail info 股权出质 %s", key)
        if index == 1:
            root_div = self.selector.xpath("//table[position()=1]")
        else:
            # 获得股权出质大标签
            root_div = self.selector.xpath('//div[@id="_container_equity"][position()=1]/table')
        if root_div:
            # 一行是一个tr
            root_div=root_div[0]
            trs = root_div.xpath("./tbody/tr")
            insert_value = ""
            for tr in trs:
                tds = tr.xpath("./td")
                # #print(tds.xpath('text()'))
                flss.announcement_date = tds[1].xpath('./text()')[0]
                flss.registration_number = tds[2].xpath('./text()')[0]
                pledgor = tds[3].xpath('./text()')
                flss.pledgor = pledgor[0] if pledgor else '-'
                pledgee = tds[4].xpath('./text()')
                flss.pledgee = pledgee[0] if pledgee else '-'
                status = tds[5].xpath('./text()')
                flss.status = status[0] if status else '-'

                flss.detail_info = '详情..'
                    # tds[6].text.replace("详情 》", "").strip().replace('"', '\\"')
                flss.txt_id = self.txtId
                flss.ent_name = key
                flss.add_time = str(datetime.now())
                flss.mark = str(0)
                flss.agency_num = self.agency_num
                flss.agency_name = self.agency_name
                flss.batch = self.batch
                value_list = [flss.announcement_date, flss.registration_number, flss.pledgor, flss.pledgee, flss.status,
                              flss.detail_info, flss.txt_id, flss.ent_name, flss.add_time, flss.mark, flss.agency_num,
                              flss.agency_name, flss.batch]
                value_list = ['"' + str(value) + '"' for value in value_list]
                insert_value += '(' + ','.join(value_list) + '),'
            insert_value = insert_value[0:-1]
            self.mysqlClient.mysql_insert(flss.table_name, flss.column_name, insert_value)

    # 动产抵押
    # TODO 没找到相应公司
    def html_parse_dongchandiya(self, index):
        flss = tycJyfxDcdy()
        key = self.entName
        logger.info("Parse detail info 动产抵押 %s", key)
        if index == 1:
            root_div = self.soup.find("div")
        else:
            # 获得动产抵押大标签
            root_div = self.soup.find("div", attrs={"tyc-event-ch": "CompangyDetail.dongchandiya"})
        if root_div:
            # 一行是一个tr
            # root_div=root_div[0]
            trs = root_div.find("table").find("tbody").find_all("tr")
            insert_value = ""
            for tr in trs:
                tds = tr.find_all("td")
                flss.registration_date = tds[1].text.strip()
                flss.registration_number = tds[2].text.strip()
                flss.guarantee_amount = tds[4].text.strip()
                flss.guarantee_type = tds[3].text.strip()
                flss.registration_department = tds[5].text.strip()
                flss.status = tds[6].text.strip()
                flss.detail_info = '详情..'
                    # tds[7].text.replace("详情 》", "").strip().replace('"', '\\"')

                flss.txt_id = self.txtId
                flss.ent_name = key
                flss.add_time = str(datetime.now())
                flss.mark = str(0)
                flss.agency_num = self.agency_num
                flss.agency_name = self.agency_name
                flss.batch = self.batch
                value_list = [flss.registration_date, flss.registration_number, flss.guarantee_type,flss.guarantee_amount,
                              flss.registration_department, flss.status, flss.detail_info, flss.txt_id, flss.ent_name,
                              flss.add_time, flss.mark, flss.agency_num, flss.agency_name, flss.batch]
                value_list = ['"' + value + '"' for value in value_list]
                insert_value += '(' + ','.join(value_list) + '),'
            insert_value = insert_value[0:-1]
            self.mysqlClient.mysql_insert(flss.table_name, flss.column_name, insert_value)

    # 行政处罚
    def html_parse_xingzhengchufa(self, index):
        flss = TycJyfxXzcf()
        key = self.entName
        logger.info("Parse detail info 行政处罚 %s", key)
        if index == 1:
            root_div = self.selector.xpath("//table[position()=1]")
        else:
            # 获得行政处罚大标签
            root_div = self.selector.xpath('//div[@id="_container_punish"][position()=1]/table')
        if root_div:
            # 一行是一个tr
            root_div=root_div[0]
            trs = root_div.xpath("./tbody/tr")
            insert_value = ""
            for tr in trs:
                tds = tr.xpath("./td")
                try:
                    flss.decision_date = tds[1].xpath('./text()')[0]
                    flss.decision_number = tds[2].xpath('./text()')[0]
                    flss.type = tds[3].xpath('./text()')[0]
                    flss.decision_department = tds[4].xpath('./text()')[0]
                    flss.detail_info = '详情..'
                        # tds[5].text.replace("详情 》", "").strip().replace('"', '\\"')
                except:
                    flss.decision_date = ""
                    flss.decision_number = ""
                    flss.type = ""
                    flss.decision_department = ""
                    flss.punishment_name = tds[1].xpath('text()')[0]
                    flss.punishment_area = tds[2].xpath('text()')[0]
                    flss.detail_info = '详情..'
                        # tds[3].text.replace("详情 》", "").strip().replace('"', '\\"')
                flss.txt_id = self.txtId
                flss.ent_name = key
                flss.add_time = str(datetime.now())
                flss.mark = str(0)
                flss.agency_num = self.agency_num
                flss.agency_name = self.agency_name
                flss.batch = self.batch
                value_list = [flss.decision_date, flss.decision_number, flss.type, flss.decision_department,
                              flss.detail_info, flss.punishment_name, flss.punishment_area, flss.txt_id, flss.ent_name,
                              flss.add_time, flss.mark, flss.agency_num, flss.agency_name, flss.batch]
                value_list = ['"' + value + '"' for value in value_list]
                insert_value += '(' + ','.join(value_list) + '),'
            insert_value = insert_value[0:-1]
            self.mysqlClient.mysql_insert(flss.table_name, flss.column_name, insert_value)

    # 失信人
    def html_parse_shixinren(self, index):
        flss = TycSffxSxr()
        key = self.entName
        logger.info("Parse detail info 失信人 %s", key)
        if index == 1:
            root_div = self.selector.xpath("//table[position()=1]")
        else:
            # 获得失信人大标签
            root_div = self.selector.xpath('//div[@id="_container_dishonest"][position()=1]/table')
        if root_div:
            # 一行是一个tr
            root_div=root_div[0]
            trs = root_div.xpath("./tbody/tr")
            insert_value = ""
            for tr in trs:
                tds = tr.xpath("//td")
                case_date = tds[1].xpath('./text()')
                case_number = tds[2].xpath('./text()')
                execution_court = tds[3].xpath('./text()')
                performance_state = tds[4].xpath('./text()')
                execute_number = tds[5].xpath('./text()')


                flss.case_date = case_date[0] if case_date else '-'
                flss.case_number = case_number[0] if case_number else '-'
                flss.execution_court =execution_court[0] if execution_court else '-'
                flss.performance_state = performance_state[0] if performance_state else '-'
                flss.execute_number = execute_number[0] if execute_number else '-'
                flss.detail_info = '详情..'
                    # tds[6].text.replace("详情 》", "").strip().replace('"', '\\"')
                flss.txt_id = self.txtId
                flss.ent_name = key
                flss.add_time = str(datetime.now())
                flss.mark = str(0)
                flss.agency_num = self.agency_num
                flss.agency_name = self.agency_name
                flss.batch = self.batch
                value_list = [flss.case_date, flss.case_number, flss.execution_court, flss.performance_state,
                              flss.execute_number, flss.detail_info, flss.txt_id, flss.ent_name, flss.add_time,
                              flss.mark, flss.agency_num, flss.agency_name, flss.batch]
                value_list = ['"' + str(value) + '"' for value in value_list]
                insert_value += '(' + ','.join(value_list) + '),'
            insert_value = insert_value[0:-1]
            #print(insert_value)
            self.mysqlClient.mysql_insert(flss.table_name, flss.column_name, insert_value)

    # 税务评级
    def html_parse_tax(self, index):
        flss = TycJyzkSwpj()
        key = self.entName
        logger.info("Parse detail info 税务评级 %s", key)
        if index == 1:
            root_div = self.selector.xpath("//table[position()=1]")
        else:
            # 获得税务评级大标签
            root_div = self.selector.xpath('//div[@id="_container_taxcredit"][position()=1]/table')
        if root_div:
            root_div=root_div[0]
            # 一行是一个tr
            trs = root_div.xpath("./tbody/tr")
            insert_value = ""
            for tr in trs:
                tds = tr.xpath("td")
                flss.year = tds[1].xpath('./text()')[0]
                flss.tax_rating = tds[2].xpath('./text()')[0]
                flss.tax_type = tds[3].xpath('./text()')[0]
                flss.tax_identification_number = tds[4].xpath('./text()')[0]
                flss.evaluate_department = tds[5].xpath('./text()')[0]
                flss.txt_id = self.txtId
                flss.ent_name = key
                flss.add_time = str(datetime.now())
                flss.mark = str(0)
                flss.agency_num = self.agency_num
                flss.agency_name = self.agency_name
                flss.batch = self.batch
                value_list = [flss.year, flss.tax_rating, flss.tax_type, flss.tax_identification_number,
                              flss.evaluate_department, flss.txt_id, flss.ent_name, flss.add_time, flss.mark,
                              flss.agency_num, flss.agency_name, flss.batch]
                value_list = ['"' + value + '"' for value in value_list]
                insert_value += '(' + ','.join(value_list) + '),'
            insert_value = insert_value[0:-1]
            self.mysqlClient.mysql_insert(flss.table_name, flss.column_name, insert_value)

    # 经营异常
    def html_parse_abnormal(self):
        flss = TycJyfxJyyc()
        key = self.entName
        logger.info("Parse detail info 经营异常 %s", key)

        # 获得经营异常大标签
        root_div = self.selector.xpath('//div[@id= "_container_abnormal"][position()=1]/table')
        if root_div:
            # 一行是一个tr
            root_div=root_div[0]
            trs = root_div.xpath("./tbody/tr")
            insert_value = ""
            for tr in trs:
                tds = tr.xpath(".//td")
                insert_date=tds[1].xpath('/text()')
                flss.insert_date = insert_date[0] if insert_date else '-'
                insert_cause = tds[2].xpath('/text()')
                flss.insert_cause = insert_cause[0] if insert_cause else '-'
                insert_department = tds[3].xpath('/text()')
                flss.insert_department =insert_department[0] if  insert_department else '-'

                flss.txt_id = self.txtId
                flss.ent_name = key
                flss.add_time = str(datetime.now())
                flss.mark = str(0)
                flss.agency_num = self.agency_num
                flss.agency_name = self.agency_name
                flss.batch = self.batch
                value_list = [flss.insert_date, flss.insert_cause, flss.insert_department, flss.txt_id, flss.ent_name,
                              flss.add_time, flss.mark, flss.agency_num, flss.agency_name, flss.batch]
                value_list = ['"' + value + '"' for value in value_list]
                insert_value += '(' + ','.join(value_list) + '),'
            insert_value = insert_value[0:-1]
            self.mysqlClient.mysql_insert(flss.table_name, flss.column_name, insert_value)

    # 解析：经营风险--严重违法
    # TODO 没找到相应公司
    def html_parse_illegalSerious(self):
        insert_value = ""
        key = self.entName
        logger.info("Parse detail info 严重违法 %s", key)

        trs = self.selector.xpath('//div[@id="_container_illegal"][position()=1]//table[position()=1]/tbody/tr')
        if trs:
            for tr in trs:
                illegalSerious = TycJyfxYzwf()
                tds = tr.xpath('./td')
                illegalSerious.illegalDate = tds[1].xpath('text()')[0].replace('\n', '').replace(' ', '') or ''
                illegalSerious.illegalReason = tds[2].xpath('text()')[0].replace('\n', '').replace(' ', '') or ''
                illegalSerious.office = tds[3].xpath('text()')[0].replace('\n', '').replace(' ', '') or ''
                illegalSerious.txtId = self.txtId
                illegalSerious.entName = key
                illegalSerious.mark = str(0)
                illegalSerious.addtime = str(datetime.now())
                illegalSerious.agency_num = self.agency_num
                illegalSerious.agency_name = self.agency_name
                illegalSerious.batch = self.batch
                value_list = [illegalSerious.txtId, illegalSerious.entName, illegalSerious.illegalDate,
                              illegalSerious.illegalReason, illegalSerious.office, illegalSerious.mark,
                              illegalSerious.addtime, illegalSerious.agency_num, illegalSerious.agency_name,
                              illegalSerious.batch]
                value_list = ['"' + value + '"' for value in value_list]
                insert_value += '(' + ','.join(value_list) + '),'
            insert_value = insert_value[0:-1]
            self.mysqlClient.mysql_insert(illegalSerious.table_name, illegalSerious.column_name, insert_value)

    # 解析：经营状况--购地信息
    # TODO 没找到相应公司
    def html_parse_buyInfo(self):
        insert_value = ""
        key = self.entName
        logger.info("Parse detail info 购地信息 %s", key)

        trs = self.selector.xpath('//div[@id="_container_purchaseland"][position()=1]//table[position()=1]/tbody/tr')
        if trs:
            for tr in trs:
                buyInfo = TycJyzkGdxx()
                tds = tr.xpath('./td')
                buyInfo.gdSignDate = tds[1].xpath('text()')[0].replace('\n', '').replace(' ', '') or ''
                buyInfo.gdNum = tds[2].xpath('text()')[0].replace('\n', '').replace(' ', '') or ''
                buyInfo.gdActDate = tds[3].xpath('text()')[0].replace('\n', '').replace(' ', '') or ''
                buyInfo.gdArea = tds[4].xpath('text()')[0].replace('\n', '').replace(' ', '') or ''
                buyInfo.gdRegion = tds[5].xpath('text()')[0].replace('\n', '').replace(' ', '') or ''
                buyInfo.gdOperate = tds[6].xpath('text()')[0].replace('\n', '').replace(' ', '') or ''
                buyInfo.txtId = self.txtId
                buyInfo.entName = key
                buyInfo.mark = str(0)
                buyInfo.addtime = str(datetime.now())
                buyInfo.agency_num = self.agency_num
                buyInfo.agency_name = self.agency_name
                buyInfo.batch = self.batch
                value_list = [buyInfo.txtId, buyInfo.entName, buyInfo.gdSignDate, buyInfo.gdNum, buyInfo.gdActDate,
                              buyInfo.gdArea, buyInfo.gdRegion, buyInfo.gdOperate, buyInfo.mark, buyInfo.addtime,
                              buyInfo.agency_num, buyInfo.agency_name, buyInfo.batch]
                value_list = ['"' + value + '"' for value in value_list]
                insert_value += '(' + ','.join(value_list) + '),'
            insert_value = insert_value[0:-1]
            self.mysqlClient.mysql_insert(buyInfo.table_name, buyInfo.column_name, insert_value)

    # 企业年报
    def html_parse_nianbao(self, year):
        flss = TycQybjQynb()
        key = self.entName
        logger.info("Parse detail info 企业年报 %s", key)

        # 获得企业年报大标签
        root_div = self.selector.xpath('//div[@id="nav-main-reportCount"]/../div[@class="data-content"]/div[@class="report-item-list"]/div')
        if root_div:
            root_div=root_div[0]
            # 一行是一个tr
            all_a = root_div.xpath('//a[contains(@href,"https://www.tianyancha.com/reportContent")]')
            insert_value = ""
            for a in all_a:
                ss=a.xpath("./@href")[0]
                flss.year=ss[-4:].strip()
                flss.detail_url = ss.strip()
                year_selector = year[flss.year]
                try:
                    self.html_parse_year_jbxx(year_selector, flss.year)
                except Exception as e:
                    logger.exception("Detail info html_parse_year_jbxx() parse error! company_name：%s ID：%s", ent_name,
                                     txt_id)
                # try:
                #     self.html_parse_year_wzhwdxx(soup2, flss.year)
                # except Exception as e:
                #     logger.exception("Detail info html_parse_year_wzhwdxx() parse error! company_name：%s ID：%s",
                #                      ent_name, txt_id)
                try:
                    self.html_parse_year_gdczxx(year_selector, flss.year)
                except Exception as e:
                    logger.exception("Detail info html_parse_year_gdczxx() parse error! company_name：%s ID：%s",
                                     ent_name, txt_id)
                try:
                    self.html_parse_year_zczk(year_selector, flss.year)
                except Exception as e:
                    logger.exception("Detail info html_parse_year_zczk() parse error! company_name：%s ID：%s", ent_name,
                                     txt_id)
                try:
                    self.html_parse_year_dwtz(year_selector, flss.year)
                except Exception as e:
                    logger.exception("Detail info html_parse_year_dwtz() parse error! company_name：%s ID：%s", ent_name,
                                     txt_id)

                flss.txt_id = self.txtId
                flss.ent_name = key
                flss.add_time = str(datetime.now())
                flss.mark = str(0)
                flss.agency_num = self.agency_num
                flss.agency_name = self.agency_name
                flss.batch = batch
                value_list = [flss.year, flss.detail_url, flss.txt_id, flss.ent_name, flss.add_time, flss.mark,
                              flss.agency_num, flss.agency_name, flss.batch]
                value_list = ['"' + str(value) + '"' for value in value_list]
                insert_value += '(' + ','.join(value_list) + '),'
            insert_value = insert_value[0:-1]
            self.mysqlClient.mysql_insert(flss.table_name, flss.column_name, insert_value)

    # 年报基本信息
    def html_parse_year_jbxx(self, year_selector, year):

        flss = TycYearJbxx()
        key = self.entName
        logger.info("Parse detail info 年报基本解析 %s", key)
        # 获得大标签
        if year_selector:
            year_selector=etree.HTML(year_selector)
        root_div = year_selector.xpath('//div[@class="block-data"]')
        insert_value = ""
        if root_div:
            root_div=root_div[0]
            # 一行是一个tr
            trs = root_div.xpath(".//table[position()=1]//tr")
            flss.credit_num = trs[0].xpath("./td[1]/text()")[0]
            flss.company_name = trs[0].xpath("./td[3]/text()")[0]
            flss.company_tel = trs[1].xpath("./td[1]/text()")[0]
            flss.postal_code = trs[1].xpath("./td[3]/text()")[0]
            flss.manger_state = trs[2].xpath("./td[1]/text()")[0]
            flss.people_count = trs[2].xpath("./td[3]/text()")[0]
            flss.email = trs[3].xpath("./td[1]/text()")[0]
            flss.website = trs[3].xpath("./td[3]/text()")[0]
            flss.company_address = trs[4].xpath("./td[1]/text()")[0]
            flss.buy_equity = trs[4].xpath("./td[3]/text()")[0]
            flss.year = year
            flss.txt_id = self.txtId
            flss.ent_name = key
            flss.add_time = str(datetime.now())
            flss.mark = str(0)
            flss.agency_num = self.agency_num
            flss.agency_name = self.agency_name
            flss.batch = self.batch
            value_list = [flss.credit_num, flss.company_name, flss.company_tel, flss.postal_code, flss.manger_state,
                          flss.people_count, flss.email, flss.website, flss.company_address, flss.buy_equity, flss.year,
                          flss.txt_id, flss.ent_name, flss.add_time, flss.mark, flss.agency_num, flss.agency_name,
                          flss.batch]
            value_list = ['"' + str(value) + '"' for value in value_list]
            insert_value += '(' + ','.join(value_list) + ')'

            #print('year html_parse_year_jbxx................',insert_value)
            self.mysqlClient.mysql_insert(flss.table_name, flss.column_name, insert_value)

    # 解析年报网站信息
    def html_parse_year_wzhwdxx(self, soup_year, year):

        website = TycYearWzhwdxx()
        key = self.entName
        logger.info("Parse detail info 企业年报 %s", key)
        root_div = soup_year.find("div", attrs={"class": "report_website"})
        if root_div:
            # 一行是一个tr
            root_div=root_div[0]
            trs = root_div.find("table").find("tbody").find_all("tr")
            insert_value = ""
            for tr in trs:
                tds = tr.find_all("td")
                website.website_type = tds[0].find_all("div")[0].text or ''
                website.web_name = tds[1].find_all("div")[0].text or ''
                website.web_url = tds[2].find_all("div")[0].text or ''
                website.year = year
                website.txt_id = self.txtId
                website.ent_name = key
                website.add_time = str(datetime.now())
                website.mark = str(0)
                website.agency_num = self.agency_num
                website.agency_name = self.agency_name
                website.batch = self.batch
                value_list = [website.website_type, website.web_name, website.web_url, website.year, website.txt_id,
                              website.ent_name, website.add_time, website.mark, website.agency_num, website.agency_name,
                              website.batch]

                value_list = ['"' + value + '"' for value in value_list]
                insert_value += '(' + ','.join(value_list) + '),'
            insert_value = insert_value[0:-1]
            #print('year html_parse_year_wzhwdxx................', insert_value)
            self.mysqlClient.mysql_insert(website.table_name, website.column_name, insert_value)

    # 股东及出资信息
    def html_parse_year_gdczxx(self, year_selector, year):
        gdcz = TycYearGdczxx()
        key = self.entName
        logger.info("Parse detail info 股份出资信息 %s", key)
        # 获得分支机构大标签
        if year_selector:
            year_selector=etree.HTML(year_selector)
        root_div = year_selector.xpath('//div[@class="block-data"]')
        if root_div:
            root_div = root_div[1]
            # 一行是一个tr
            trs = root_div.xpath("//table[position()=1]/tbody/tr")
            insert_value = ""
            for tr in trs:
                tds = tr.xpath("/td")
                gdcz.shareholder = tds[0].xpath('./a/text()')[0]
                gdcz.subscirbe_contribution = tds[1].xpath('./text()')[0]
                gdcz.contribution_time = tds[2].xpath('./text()')[0]
                gdcz.contribution_style = tds[3].xpath('./text()')[0]
                gdcz.actual_contribution = tds[4].xpath('./a/text()')[0]
                gdcz.actual_time = tds[5].xpath('./a/text()')[0]
                gdcz.actual_style = tds[6].xpath('./a/text()')[0]
                gdcz.year = year
                gdcz.txt_id = self.txtId
                gdcz.ent_name = key
                gdcz.add_time = str(datetime.now())
                gdcz.mark = str(0)
                gdcz.agency_num = self.agency_num
                gdcz.agency_name = self.agency_name
                gdcz.batch = self.batch
                value_list = [gdcz.shareholder, gdcz.subscirbe_contribution, gdcz.contribution_time,
                              gdcz.contribution_style, gdcz.actual_contribution, gdcz.actual_time, gdcz.actual_style,
                              year, gdcz.txt_id, gdcz.ent_name, gdcz.add_time, gdcz.mark, gdcz.agency_num,
                              gdcz.agency_name, gdcz.batch]
                value_list = ['"' + value + '"' for value in value_list]
                insert_value += '(' + ','.join(value_list) + '),'
            insert_value = insert_value[0:-1]
            #print('year html_parse_year_gdczxx................', insert_value)
            self.mysqlClient.mysql_insert(gdcz.table_name, gdcz.column_name, insert_value)

    # 年报基本信息
    def html_parse_year_zczk(self, year_selector, year):

        flss = TycYearZczk()
        key = self.entName
        logger.info("Parse detail info 资产状况 %s", key)
        # 获得大标签
        if year_selector:
            year_selector=etree.HTML(year_selector)
        root_div = year_selector.xpath('//div[@class="block-data"]')
        insert_value = ""
        if root_div:
            root_div = root_div[2]
            # 一行是一个tr
            trs = root_div.xpath("//table[position()=1]/tr")
            flss.total_assets = trs[0].xpath("./td[position()=2]/text()")[0]
            flss.total_income = trs[0].xpath("td[position()=4]/text()")[0]
            flss.total_sales = trs[1].xpath("td[position()=2]/text()")[0]
            flss.total_profit = trs[1].xpath("td[position()=4]/text()")[0]
            flss.operation_income = trs[2].xpath("td[position()=2]/text()")[0]
            flss.net_profit = trs[2].xpath("td[position()=4]/text()")[0]
            flss.total_tax = trs[3].xpath("td[position()=2]/text()")[0]
            flss.total_debt = trs[3].xpath("td[position()=5]/text()")[0]

            flss.year = year
            flss.txt_id = self.txtId
            flss.ent_name = key
            flss.add_time = str(datetime.now())
            flss.mark = str(0)
            flss.agency_num = self.agency_num
            flss.agency_name = self.agency_name
            flss.batch = self.batch
            value_list = [flss.total_assets, flss.total_income, flss.total_sales, flss.total_profit,
                          flss.operation_income, flss.net_profit, flss.total_tax, flss.total_debt, flss.year,
                          flss.txt_id, flss.ent_name, flss.add_time, flss.mark, flss.agency_num, flss.agency_name,
                          flss.batch]
            value_list = ['"' + value + '"' for value in value_list]
            insert_value += '(' + ','.join(value_list) + '),'
            insert_value = insert_value[0:-1]
            self.mysqlClient.mysql_insert(flss.table_name, flss.column_name, insert_value)

    # 对外投资
    def html_parse_year_dwtz(self, year_selector, year):
        dwtz = TycYearDwtz()
        key = self.entName
        logger.info("Parse detail info 股份出资信息 %s", key)
        # 获得分支机构大标签
        if year_selector:
            year_selector=etree.HTML(year_selector)
        root_div = year_selector.xpath('//div[@class="block-data"]')
        if root_div:
            root_div = root_div[3]
            # 一行是一个tr
            trs = root_div.xpath("//table[position()=1]/tbody/tr")
            insert_value = ""
            for tr in trs:
                tds = tr.xpath("./td")
                dwtz.credit_num = tds[0].xpath('/td/text()')[0]
                dwtz.outbound_company = tds[1].xpath('/td/text()')[0]

                dwtz.year = year
                dwtz.txt_id = self.txtId
                dwtz.ent_name = key
                dwtz.add_time = str(datetime.now())
                dwtz.mark = str(0)
                dwtz.agency_num = self.agency_num
                dwtz.agency_name = self.agency_name
                dwtz.batch = self.batch
                value_list = [dwtz.credit_num, dwtz.outbound_company, year, dwtz.txt_id, dwtz.ent_name, dwtz.add_time,
                              dwtz.mark, dwtz.agency_num, dwtz.agency_name, dwtz.batch]
                value_list = ['"' + value + '"' for value in value_list]
                insert_value += '(' + ','.join(value_list) + '),'
            insert_value = insert_value[0:-1]
            self.mysqlClient.mysql_insert(dwtz.table_name, dwtz.column_name, insert_value)


if __name__ == "__main__":

    mongodbClient = MongodbClient()
    mysqlClient = MysqlClient()
    parameter = {'parse': 0}
    tyc_Parse = TycDetailParse()
    # count = 1
    while True:

        # if count == 2:
        #     break
        # count += 1
        try:
            detail_info={}
            detail_info = mongodbClient.mongodb_find_one("company_detail_info", parameter)
        except:
            logger.exception("Exception Logged")
            continue

        if detail_info and ("page" in detail_info or "year" in detail_info  or "law" in detail_info):
            ent_name = ''
            name=''
            if "ent_name" in detail_info:
                name = detail_info['ent_name']
            else:
                continue
            if type(name) == UnicodeType:
                ent_name = name.encode("utf-8")
            else:
                ent_name = name
            txt_id = str(detail_info["_id"])
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
                param = {'ent_name': ent_name}
                table = "tyc_qybj_jbxx"
                check_sql='SELECT id from tyc_qybj_jbxx WHERE ent_name="%s" '%ent_name
                result = mysqlClient.mysql_find_by_param(check_sql)
                error_list = []




                html = detail_info["text"]
                selector = etree.HTML(html)
                soup = BeautifulSoup(html, 'lxml')




                tyc_Parse.txtId = txt_id
                try:
                    tyc_Parse.entName = ent_name.decode('utf-8')
                except:
                    tyc_Parse.entName = ent_name
                tyc_Parse.agency_num = agency_num
                tyc_Parse.agency_name = agency_name or ''
                tyc_Parse.batch = batch
                tyc_Parse.soup = soup
                tyc_Parse.selector = selector
            except Exception as e:
                logger.info("%s - %s 初始化网页内容出错！" % (ent_name, txt_id))
                logger.exception("Exception Logged")
                mongodbClient = MongodbClient()
                mysqlClient = MysqlClient()
                continue
            # 基本信息
            try:
                tyc_Parse.html_parse_baseinfo(branch)
            except Exception as e:
                error_list.append("html_parse_baseinfo")
                logger.exception("Detail info html_parse_baseinfo() parse error! company_name：%s ID：%s", ent_name,
                                 txt_id)

            # 主要信息
            try:
                tyc_Parse.html_parse_mainPerson()
            except Exception as e:
                error_list.append("html_parse_mainPerson")
                logger.exception("Detail info html_parse_mainPerson() parse error! company_name：%s ID：%s", ent_name,
                                 txt_id)

            # 股东
            try:
                tyc_Parse.html_parse_shareholderInfo()
            except Exception as e:
                error_list.append("html_parse_shareholderInfo")
                logger.exception("Detail info html_parse_shareholderInfo() parse error! company_name：%s ID：%s",
                                 ent_name, txt_id)

            # 法律诉讼
            try:
                if "law" in detail_info:
                    law = detail_info["law"]
                    tyc_Parse.html_parse_lawsuit(law, index=0)
            except Exception as e:
                error_list.append("html_parse_lawsuit")
                logger.exception("Detail info html_parse_lawsuit() parse error! company_name：%s ID：%s", ent_name,
                                 txt_id)
            # 著作权
            try:
                tyc_Parse.html_parse_copyright(index=0)
            except Exception as e:
                error_list.append("html_parse_copyright")
                logger.exception("Detail info html_parse_copyright() parse error! company_name：%s ID：%s", ent_name,
                                 txt_id)
            # 招聘
            try:
                tyc_Parse.html_parse_recruitment(index=0)
            except Exception as e:
                error_list.append("html_parse_recruitment")
                logger.exception("Detail info html_parse_recruitment() parse error! company_name：%s ID：%s", ent_name,
                                 txt_id)
            # 商标信息
            try:
                tyc_Parse.html_parse_trademark(index=0)
            except Exception as e:
                error_list.append("html_parse_trademark")
                logger.exception("Detail info html_parse_trademark() parse error! company_name：%s ID：%s", ent_name,
                                 txt_id)
            # 对外投资
            try:
                tyc_Parse.html_parse_investInfo(index=0)
            except Exception as e:
                error_list.append("html_parse_investInfo")
                logger.exception("Detail info html_parse_investInfo() parse error! company_name：%s ID：%s", ent_name,
                                 txt_id)
            # 记录变更
            try:
                tyc_Parse.html_parse_alterRecord(index=0)
            except Exception as e:
                error_list.append("html_parse_alterRecord")
                logger.exception("Detail info html_parse_alterRecord() parse error! company_name：%s ID：%s", ent_name,
                                 txt_id)
            # 分支机构
            try:
                tyc_Parse.html_parse_branch(0)
            except Exception as e:
                error_list.append("html_parse_branch")
                logger.exception("Detail info html_parse_branch() parse error! company_name：%s ID：%s", ent_name, txt_id)
            try:
                tyc_Parse.html_parse_pledge(0)
            except Exception as e:
                error_list.append("html_parse_pledge")
                logger.exception("Detail info html_parse_pledge() parse error! company_name：%s ID：%s", ent_name, txt_id)
            # 资质证书
            try:
                tyc_Parse.html_parse_certificateInfo(index=0)
            except Exception as e:
                error_list.append("html_parse_certificateInfo")
                logger.exception("Detail info html_parse_certificateInfo() parse error! company_name：%s ID：%s",
                                 ent_name, txt_id)
            # 网站备案
            try:
                tyc_Parse.html_parse_website(index=0)
            except Exception as e:
                error_list.append("html_parse_website")
                logger.exception("Detail info html_parse_website() parse error! company_name：%s ID：%s", ent_name,
                                 txt_id)
            # 核心团队
            try:
                tyc_Parse.html_parse_coreTeam(index=0)
            except Exception as e:
                error_list.append("html_parse_coreTeam")
                logger.exception("Detail info html_parse_coreTeam() parse error! company_name：%s ID：%s", ent_name,
                                 txt_id)
            # 投资事件
            try:
                tyc_Parse.html_parse_investEvent(index=0)
            except Exception as e:
                error_list.append("html_parse_investEvent")
                logger.exception("Detail info html_parse_investEvent() parse error! company_name：%s ID：%s", ent_name,
                                 txt_id)
            # 企业业务
            try:
                tyc_Parse.html_parse_entBusiness(index=0)
            except Exception as e:
                error_list.append("html_parse_entBusiness")
                logger.exception("Detail info html_parse_entBusiness() parse error! company_name：%s ID：%s", ent_name,
                                 txt_id)
            # 竞品信息
            try:
                tyc_Parse.html_parse_jpInfo(index=0)
            except Exception as e:
                error_list.append("html_parse_jpInfo")
                logger.exception("Detail info html_parse_jpInfo() parse error! company_name：%s ID：%s", ent_name, txt_id)
            # 法院公告
            try:
                tyc_Parse.html_parse_announcement(index=0)
            except Exception as e:
                error_list.append("html_parse_announcement")
                logger.exception("Detail info html_parse_announcement() parse error! company_name：%s ID：%s", ent_name,
                                 txt_id)
            # 抽查检查
            try:
                tyc_Parse.html_parse_check(index=0)
            except Exception as e:
                error_list.append("html_parse_check")
                logger.exception("Detail info html_parse_check() parse error! company_name：%s ID：%s", ent_name, txt_id)
            # 专利信息
            try:
                tyc_Parse.html_parse_patent(index=0)
            except Exception as e:
                error_list.append("html_parse_patent")
                logger.exception("Detail info html_parse_patent() parse error! company_name：%s ID：%s", ent_name, txt_id)
            # 作品著作
            try:
                tyc_Parse.html_parse_copyzzq(index=0)
            except Exception as e:
                error_list.append("html_parse_copyzzq")
                logger.exception("Detail info html_parse_copyzzq() parse error! company_name：%s ID：%s", ent_name,
                                 txt_id)
            # 微信
            try:
                tyc_Parse.html_parse_entWechat(index=0)
            except Exception as e:
                error_list.append("html_parse_entWechat")
                logger.exception("Detail info html_parse_entWechat() parse error! company_name：%s ID：%s", ent_name,
                                 txt_id)
            # 产品信息
            try:
                tyc_Parse.html_parse_product(index=0)
            except Exception as e:
                error_list.append("html_parse_product")
                logger.exception("Detail info html_parse_product() parse error! company_name：%s ID：%s", ent_name,
                                 txt_id)
            # 被执行人
            try:
                tyc_Parse.html_parse_executed(index=0)
            except Exception as e:
                error_list.append("html_parse_executed")
                logger.exception("Detail info html_parse_executed() parse error! company_name：%s ID：%s", ent_name,
                                 txt_id)
            # 招投标
            try:
                tyc_Parse.html_parse_bidding(index=0)
            except Exception as e:
                error_list.append("html_parse_bidding")
                logger.exception("Detail info html_parse_bidding() parse error! company_name：%s ID：%s", ent_name,
                                 txt_id)
            # 债券信息
            try:
                tyc_Parse.html_parse_zhaiquan(index=0)
            except Exception as e:
                error_list.append("html_parse_zhaiquan")
                logger.exception("Detail info html_parse_zhaiquan() parse error! company_name：%s ID：%s", ent_name,
                                 txt_id)
            # 欠税公告
            try:
                tyc_Parse.html_parse_taxesNotice(index=0)
            except Exception as e:
                error_list.append("html_parse_taxesNotice")
                logger.exception("Detail info html_parse_taxesNotice() parse error! company_name：%s ID：%s", ent_name,
                                 txt_id)
            # 动产抵押
            try:
                tyc_Parse.html_parse_dongchandiya(index=0)
            except Exception as e:
                error_list.append("html_parse_dongchandiya")
                logger.exception("Detail info html_parse_dongchandiya() parse error! company_name：%s ID：%s", ent_name,
                                 txt_id)
            # 股权出质
            try:
                tyc_Parse.html_parse_pledge(index=0)
            except Exception as e:
                error_list.append("html_parse_pledge")
                logger.exception("Detail info html_parse_pledge() parse error! company_name：%s ID：%s", ent_name, txt_id)
            # 行政处罚
            try:
                tyc_Parse.html_parse_xingzhengchufa(index=0)
            except Exception as e:
                error_list.append("html_parse_xingzhengchufa")
                logger.exception("Detail info html_parse_xingzhengchufa() parse error! company_name：%s ID：%s", ent_name,
                                 txt_id)
            # 失信人
            try:
                tyc_Parse.html_parse_shixinren(index=0)
            except Exception as e:
                error_list.append("html_parse_shixinren")
                logger.exception("Detail info html_parse_shixinren() parse error! company_name：%s ID：%s", ent_name,
                                 txt_id)
            # 税务评级
            try:
                tyc_Parse.html_parse_tax(index=0)
            except Exception as e:
                error_list.append("html_parse_tax")
                logger.exception("Detail info html_parse_tax() parse error! company_name：%s ID：%s", ent_name, txt_id)
            # 融资
            try:
                tyc_Parse.html_parse_financeHistory()
            except Exception as e:
                error_list.append("html_parse_financeHistory")
                logger.exception("Detail info html_parse_financeHistory() parse error! company_name：%s ID：%s", ent_name,
                                 txt_id)
            # 经营异常
            try:
                tyc_Parse.html_parse_abnormal()
            except Exception as e:
                error_list.append("html_parse_abnormal")
                logger.exception("Detail info html_parse_abnormal() parse error! company_name：%s ID：%s", ent_name,
                                 txt_id)
            # 严重违法
            try:
                tyc_Parse.html_parse_illegalSerious()
            except Exception as e:
                error_list.append("html_parse_illegalSerious")
                logger.exception("Detail info html_parse_illegalSerious() parse error! company_name：%s ID：%s", ent_name,
                                 txt_id)

            # 购地信息
            try:
                tyc_Parse.html_parse_buyInfo()
            except Exception as e:
                error_list.append("html_parse_buyInfo")
                logger.exception("Detail info html_parse_buyInfo() parse error! company_name：%s ID：%s", ent_name,
                                 txt_id)
            # 年报
            try:
                if "year" in detail_info:
                    year = detail_info["year"]
                    if year:
                        tyc_Parse.html_parse_nianbao(year)
            except Exception as e:
                error_list.append("html_parse_nianbao")
                logger.exception("Detail info html_parse_nianbao() parse error! company_name：%s ID：%s", ent_name,
                                 txt_id)
            # 进出口
            try:
                tyc_Parse.html_parse_outputxy()
            except Exception as e:
                error_list.append("html_parse_outputxy")
                logger.exception("Detail info html_parse_outputxy() parse error! company_name：%s ID：%s", ent_name,
                                 txt_id)

            # 分页解析开始
            logger.info("分页解析开始 %s" % ent_name)
            try:
                pages = detail_info["page"]
            except:
                pages = {}

            for key, value in pages.items():

                for text in value:
                    try:
                        selector = etree.HTML(text)
                        soup = BeautifulSoup(text, "lxml")
                        tyc_Parse.soup = soup
                        tyc_Parse.selector=selector
                    except Exception as e:
                        logger.exception("Detail info selector soup parse(text) is none error! company_name：%s ID：%s",
                                         ent_name, txt_id)
                    # 法律诉讼
                    # 软件著作权
                    if key == "nav-main-cpoyRCount":
                        try:
                            tyc_Parse.html_parse_copyright(index=1)
                        except Exception as e:
                            logger.exception("Detail info html_parse_copyright() parse error! company_name：%s ID：%s",
                                             ent_name, txt_id)
                    # 招聘
                    elif key == "nav-main-recruitCount":
                        try:
                            tyc_Parse.html_parse_recruitment(index=1)
                        except Exception as e:
                            logger.exception("Detail info html_parse_recruitment() parse error! company_name：%s ID：%s",
                                             ent_name, txt_id)
                    # 法律诉讼
                    elif key == "nav-main-lawsuitCount":
                        try:
                            tyc_Parse.html_parse_lawsuit(law, index=1)
                        except Exception as e:
                            logger.exception("Detail info html_parse_lawsuit() parse error! company_name：%s ID：%s",
                                             ent_name, txt_id)
                    # 商标信息
                    elif key == "nav-main-tmCount":
                        try:
                            tyc_Parse.html_parse_trademark(index=1)
                        except Exception as e:
                            logger.exception("Detail info html_parse_trademark() parse error! company_name：%s ID：%s",
                                             ent_name, txt_id)
                    # 对外投资
                    elif key == "nav-main-inverstCount":
                        try:
                            tyc_Parse.html_parse_investInfo(index=1)
                        except Exception as e:
                            logger.exception("Detail info html_parse_investInfo() parse error! company_name：%s ID：%s",
                                             ent_name, txt_id)
                    # 记录变更
                    elif key == "nav-main-changeCount":
                        try:
                            tyc_Parse.html_parse_alterRecord(index=1)
                        except Exception as e:
                            logger.exception("Detail info html_parse_alterRecord() parse error! company_name：%s ID：%s",
                                             ent_name, txt_id)
                    # 分支机构
                    elif key == "nav-main-branchCount":
                        try:
                            tyc_Parse.html_parse_branch(index=1)
                        except Exception as e:
                            logger.exception("Detail info html_parse_branch() parse error! company_name：%s ID：%s",
                                             ent_name, txt_id)
                    # 股权出资
                    elif key == "nav-main-equityCount":
                        try:
                            tyc_Parse.html_parse_pledge(index=1)
                        except Exception as e:
                            logger.exception("Detail info html_parse_pledge() parse error! company_name：%s ID：%s",
                                             ent_name, txt_id)
                    # 资质证书
                    elif key == "nav-main-certificateCount":
                        try:
                            tyc_Parse.html_parse_certificateInfo(index=1)
                        except Exception as e:
                            logger.exception(
                                "Detail info html_parse_certificateInfo() parse error! company_name：%s ID：%s", ent_name,
                                txt_id)
                    # 网站备案
                    elif key == "nav-main-icpCount":
                        try:
                            tyc_Parse.html_parse_website(index=1)
                        except Exception as e:
                            logger.exception("Detail info html_parse_website() parse error! company_name：%s ID：%s",
                                             ent_name, txt_id)
                    # 核心团队
                    elif key == "nav-main-companyTeammember":
                        try:
                            tyc_Parse.html_parse_coreTeam(index=1)
                        except Exception as e:
                            logger.exception("Detail info html_parse_coreTeam() parse error! company_name：%s ID：%s",
                                             ent_name, txt_id)
                    # 投资事件
                    elif key == "nav-main-jigouTzanli":
                        try:
                            tyc_Parse.html_parse_investEvent(index=1)
                        except Exception as e:
                            logger.exception("Detail info html_parse_investEvent() parse error! company_name：%s ID：%s",
                                             ent_name, txt_id)
                    # 企业业务
                    elif key == "nav-main-companyProduct":
                        try:
                            tyc_Parse.html_parse_entBusiness(index=1)
                        except Exception as e:
                            logger.exception("Detail info html_parse_entBusiness() parse error! company_name：%s ID：%s",
                                             ent_name, txt_id)
                    # 竞品信息
                    elif key == "nav-main-companyJingpin":
                        try:
                            tyc_Parse.html_parse_jpInfo(index=1)
                        except Exception as e:
                            logger.exception("Detail info html_parse_jpInfo() parse error! company_name：%s ID：%s",
                                             ent_name, txt_id)
                    # 法院公告
                    elif key == "nav-main-courtCount":
                        try:
                            tyc_Parse.html_parse_announcement(index=1)
                        except Exception as e:
                            logger.exception("Detail info html_parse_announcement() parse error! company_name：%s ID：%s",
                                             ent_name, txt_id)
                    # 抽查检查
                    elif key == "nav-main-checkCount":
                        try:
                            tyc_Parse.html_parse_check(index=1)
                        except Exception as e:
                            logger.exception("Detail info html_parse_check() parse error! company_name：%s ID：%s",
                                             ent_name, txt_id)
                    # 专利信息
                    elif key == "nav-main-patentCount":
                        try:
                            tyc_Parse.html_parse_patent(index=1)
                        except Exception as e:
                            logger.exception("Detail info html_parse_patent() parse error! company_name：%s ID：%s",
                                             ent_name, txt_id)
                    # 作品著作
                    elif key == "nav-main-copyrightWorks":
                        try:
                            tyc_Parse.html_parse_copyzzq(index=1)
                        except Exception as e:
                            logger.exception("Detail info html_parse_copyzzq() parse error! company_name：%s ID：%s",
                                             ent_name, txt_id)
                    # 微信
                    elif key == "nav-main-weChatCount":
                        try:
                            tyc_Parse.html_parse_entWechat(index=1)
                        except Exception as e:
                            logger.exception("Detail info html_parse_entWechat() parse error! company_name：%s ID：%s",
                                             ent_name, txt_id)
                    # 产品信息
                    elif key == "nav-main-productinfo":
                        try:
                            tyc_Parse.html_parse_product(index=1)
                        except Exception as e:
                            logger.exception("Detail info html_parse_product() parse error! company_name：%s ID：%s",
                                             ent_name, txt_id)
                    # 被执行人
                    elif key == "nav-main-zhixing":
                        try:
                            tyc_Parse.html_parse_executed(index=1)
                        except Exception as e:
                            logger.exception("Detail info html_parse_executed() parse error! company_name：%s ID：%s",
                                             ent_name, txt_id)
                    # 招投标
                    elif key == "nav-main-bidCount":
                        try:
                            tyc_Parse.html_parse_bidding(index=1)
                        except Exception as e:
                            logger.exception("Detail info html_parse_bidding() parse error! company_name：%s ID：%s",
                                             ent_name, txt_id)
                    # 债券信息
                    elif key == "nav-main-bondCount":
                        try:
                            tyc_Parse.html_parse_zhaiquan(index=1)
                        except Exception as e:
                            logger.exception("Detail info html_parse_zhaiquan() parse error! company_name：%s ID：%s",
                                             ent_name, txt_id)
                    # 欠税公告
                    elif key == "nav-main-ownTaxCount":
                        try:
                            tyc_Parse.html_parse_taxesNotice(index=1)
                        except Exception as e:
                            logger.exception("Detail info html_parse_taxesNotice() parse error! company_name：%s ID：%s",
                                             ent_name, txt_id)
                    # 动产抵押
                    elif key == "nav-main-mortgageCount":
                        try:
                            tyc_Parse.html_parse_dongchandiya(index=1)
                        except Exception as e:
                            logger.exception("Detail info html_parse_dongchandiya() parse error! company_name：%s ID：%s",
                                             ent_name, txt_id)
                    # 股权出质
                    elif key == "nav-main-equityCount":
                        try:
                            tyc_Parse.html_parse_pledge(index=1)
                        except Exception as e:
                            logger.exception("Detail info html_parse_pledge() parse error! company_name：%s ID：%s",
                                             ent_name, txt_id)
                    # 行政处罚
                    elif key == "nav-main-punishment":
                        try:
                            tyc_Parse.html_parse_xingzhengchufa(index=1)
                        except Exception as e:
                            logger.exception(
                                "Detail info html_parse_xingzhengchufa() parse error! company_name：%s ID：%s", ent_name,
                                txt_id)
                    # 失信人
                    elif key == "nav-main-dishonest":
                        try:
                            tyc_Parse.html_parse_shixinren(index=1)
                        except Exception as e:
                            logger.exception("Detail info html_parse_shixinren() parse error! company_name：%s ID：%s",
                                             ent_name, txt_id)
                    # 税务评级
                    elif key == "nav-main-taxCreditCount":
                        try:
                            tyc_Parse.html_parse_tax(index=1)
                        except Exception as e:
                            logger.exception("Detail info html_parse_tax() parse error! company_name：%s ID：%s",
                                             ent_name, txt_id)

            logger.info("分页解析结束 %s" % ent_name)

            try:
                mysqlClient.mysql_update("company_basic_info", {'parsed': 1}, {'ent_name': ent_name})
                mongodbClient.mongodb_update("company_detail_info", {'_id': detail_info["_id"]},
                                             {'parse': 1, "error_list": str(error_list)})

                company_name = ent_name.decode('utf-8')
            except:
                logger.info("datebases update False!")
                logger.exception("Exception Logged")
                mongodbClient = MongodbClient()
                mysqlClient = MysqlClient()
        else:
            sql = "SELECT company_number FROM batch_detail WHERE searched=0"
            sql_resut = mysqlClient.mysql_find_by_param(sql)
            if sql_resut:
                #print "sleeping!!"
                time.sleep(60 * 60)
            else:
                try:
                    logger.info("No detail to be parsed!")
                    bd = BatchList()
                    result_batch = mysqlClient.find_batch()
                    batch=result_batch[0]
                    bd.batch = ''.join(batch)

                    bd.end_time = str(datetime.now())
                    value_list = [bd.batch, bd.end_time]
                    value_list = ['"' + value + '"' for value in value_list]
                    check_batch=mysqlClient.mysql_find_one(bd.table_name, {"batch":batch})
                    if check_batch:
                        insert_value = '(' + ','.join(value_list) + '),'
                        insert_value = insert_value[0:-1]
                        mysqlClient.mysql_update(bd.table_name, {"end_time":datetime.now()}, {"batch":batch})
                    else:
                        bd.add_time = result_batch[1]
                        insert_value = '(' + ','.join(value_list) + '),'
                        insert_value = insert_value[0:-1]
                        mysqlClient.mysql_insert(bd.table_name,bd.column_name,insert_value)
                except:
                    logger.info("batch is error")
                break
