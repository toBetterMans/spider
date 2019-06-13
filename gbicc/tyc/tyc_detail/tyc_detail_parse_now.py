# -*- coding:utf-8 -*-
# !/usr/bin/env python
from db import *
from bs4 import BeautifulSoup
import logging
import logging.config
from tyc_bean import *
from datetime import datetime
from lxml import etree

logging.config.fileConfig("../log_file/detailParseLog.conf")

logger = logging.getLogger("loggerText")


class TycDetailParse(object):
    txtId = ""
    entName = ""
    agency_num = ""
    agency_name = ""
    batch = ""
    soup = ""
    selector = ""

    def __init__(self):
        self.mongodbClient = MongodbClient()
        self.mysqlClient = MysqlClient()

    # 解析：企业背景-->主要人员
    def html_parse_mainPerson(self):
        insert_value = ""
        mainPerson = TycQybjZyry()
        key = self.entName
        logger.info("Parse detail info 主要人员 %s", key)
        divs = self.selector.xpath('//div[@id="_container_staff"]//div[@class="clearfix"]/div')
        if divs:
            for div in divs:
                mainPerson.position = div.xpath('./div/div')[0].xpath('string(.)').replace('\n', '').replace(' ', '')
                mainPerson.name = div.xpath('./div/a')[0].xpath('string(.)').replace('\n', '').replace(' ', '')
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

    # 解析：企业背景-->基本信息
    def html_parse_baseinfo(self, branch):
        insert_value = ""
        baseinfo = TycQybjJbxx()
        key = self.entName
        logger.info("Parse detail info 基本信息 %s", key)
        lists = self.soup.select(
            "html body div div#web-content div div.top_container_new.b-c-gray div.container.company_container div.row.position-rel div div.col-9.company-main.pl0.pr10.company_new_2017 div.b-c-white.new-border-bottom.new-border-left.new-border-right.position-rel div.pl30.pr30.pt25 div div#_container_baseInfo div div.base0910 table.table.companyInfo-table.f14 tbody tr td")
        trs = self.soup.find_all("div", attrs={"class": "baseinfo-module-content-value"})
        if trs:
            email = self.soup.find("span", attrs={"class": "in-block vertical-top sec-c3"})
            baseinfo.email = email.text
            telephone = self.soup.find("div", attrs={"class": "in-block vertical-top overflow-width mr20"})
            baseinfo.telephone = telephone.text.replace("[", ",").replace("\"", "").replace("]更多", "")
            urls = self.soup.find_all("div", attrs={"class": "in-block vertical-top overflow-width mr20"})
            url = urls[1].text
            baseinfo.url = url
            baseinfo.registerFund = trs[0].text or ''
            baseinfo.registerDate = trs[1].text  or ''
            baseinfo.companyStatus = trs[2].text or ''
            if lists:
                baseinfo.registerNum = lists[1].text or ''
                baseinfo.tissueNum = lists[3].text or ''
                baseinfo.creditNum = lists[6].text or ''
                baseinfo.companyType = lists[8].text or ''
                baseinfo.taxpayerNum = lists[10].text or ''
                baseinfo.industry = lists[12].text or ''
                baseinfo.businessTerm = lists[14].text or ''
                baseinfo.checkDate = lists[16].text or ''
                baseinfo.registerOffice = lists[18].text or ''
                baseinfo.englishName = lists[20].text or ''
                baseinfo.registerSite = lists[22].text or ''
                baseinfo.businessScope = lists[24].text or ''
            baseinfo.txtId = self.txtId or ''
            baseinfo.entName = key
            baseinfo.mark = str(0)
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

        value_list = ['"' + value + '"' for value in value_list]
        insert_value += '(' + ','.join(value_list) + '),'
        insert_value = insert_value[0:-1]
        self.mysqlClient.mysql_insert(baseinfo.table_name, baseinfo.column_name, insert_value)

    # 解析：企业背景-->股东信息
    def html_parse_shareholderInfo(self):
        insert_value = ""
        key = self.entName
        logger.info("Parse detail info 股东信息 %s", key)
        trs = self.selector.xpath('//div[@id="_container_holder"]/div/table/tbody/tr')
        shareholderInfo = TycQybjGdxx()
        if trs:
            for tr in trs:
                tds = tr.xpath("./td")
                ll = tds[0].xpath('./a')
                if ll:
                    shareholderInfo.shareholder = ll[1].xpath('string(.)').replace('\n', '').replace(' ', '')
                shareholderInfo.fundRatio = tds[2].xpath('string(.)').replace('\n', '').replace(' ', '')
                shareholderInfo.fundSubcribe = tds[3].xpath('string(.)').replace('\n', '').replace(' ', '')
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
        trs = self.selector.xpath('//div[@id="_container_rongzi"]//table/tbody/tr')
        financeHistory = TycQyfzRzls()
        if trs:
            for tr in trs:
                tds = tr.xpath('./td')
                financeHistory.financeDate = tds[1].xpath('string(.)').replace('\n', '').replace(' ', '')
                financeHistory.financeRound = tds[2].xpath('string(.)').replace('\n', '').replace(' ', '')
                financeHistory.financeValue = tds[3].xpath('string(.)').replace('\n', '').replace(' ', '')
                financeHistory.financeMoney = tds[4].xpath('string(.)').replace('\n', '').replace(' ', '')
                financeHistory.financeRatio = tds[5].xpath('string(.)').replace('\n', '').replace(' ', '')
                financeHistory.financeInvestor = tds[6].xpath('string(.)').replace('\n', '').replace(' ', '')
                financeHistory.financeSource = tds[7].xpath('string(.)').replace('\n', '').replace(' ', '')
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
            root_div = self.soup.find("div")
        else:
            # 获得产品信息大标签
            root_div = self.soup.find("div", attrs={"tyc-event-ch": "CompangyDetail.chanpin"})
        if root_div:
            # 一行是一个tr
            trs = root_div.find("table").find("tbody").find_all("tr")
            insert_value = ""
            for tr in trs:
                tds = tr.find_all("td")
                flss.product_name = tds[1].text.strip()
                flss.product_referred = tds[2].text.strip()
                flss.product_classification = tds[3].text.strip()
                flss.field = tds[4].text.strip()
                flss.detail_info = tds[5].text.replace("详情 》", "").strip().replace('"', '\\"')
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
            root_div = self.soup.find("div")
        else:
            # 获得专利信息大标签
            root_div = self.soup.find("div", attrs={"tyc-event-ch": "CompangyDetail.zhuzuoquan"})
        if root_div:
            # 一行是一个tr
            trs = root_div.find("table").find("tbody").find_all("tr")
            insert_value = ""
            for tr in trs:
                tds = tr.find_all("td")
                flss.apply_publish_date = tds[1].text.strip()
                flss.patent_name = tds[2].text.strip()
                flss.apply_number = tds[3].text.strip()
                flss.apply_publish_number = tds[4].text.strip()
                flss.detail_info = tds[5].text.replace("详情 》", "").strip().replace('"', '\\"')
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
                value_list = ['"' + value + '"' for value in value_list]
                insert_value += '(' + ','.join(value_list) + '),'
            insert_value = insert_value[0:-1]
            self.mysqlClient.mysql_insert(flss.table_name, flss.column_name, insert_value)

    # 抽查检查
    def html_parse_check(self, index):
        flss = TycJyzkCcjc()
        key = self.entName
        logger.info("Parse detail info 抽查检查 %s", key)
        if index == 1:
            root_div = self.soup.find("div")
        else:
            # 获得抽查检查大标签
            root_div = self.soup.find("div", attrs={"id": "_container_check"})
        if root_div:
            # 一行是一个tr
            trs = root_div.find("table").find("tbody").find_all("tr")
            insert_value = ""
            for tr in trs:
                tds = tr.find_all("td")
                flss.date = tds[1].text.strip()
                flss.type = tds[2].text.strip()
                flss.result = tds[3].text.strip()
                flss.check_department = tds[4].text.strip()
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
            root_div = self.soup.find("div")
        else:
            # 获得法院公告大标签
            root_div = self.soup.find("div", attrs={"tyc-event-ch": "CompangyDetail.fayuangonggao"})
        if root_div:
            # 一行是一个tr
            trs = root_div.find("table").find("tbody").find_all("tr")
            insert_value = ""
            for tr in trs:
                tds = tr.find_all("td")
                flss.announcement_date = tds[1].text.strip()
                flss.plaintiff = tds[2].text.strip()
                flss.defendant = tds[3].text.strip()
                flss.announcement_type = tds[4].text.strip()
                flss.court = tds[5].text.strip()
                flss.detail_info = tds[6].text.replace("详情 》", "").strip().replace('"', '\\"')
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
                value_list = ['"' + value + '"' for value in value_list]
                insert_value += '(' + ','.join(value_list) + '),'
            insert_value = insert_value[0:-1]
            if insert_value:
                self.mysqlClient.mysql_insert(flss.table_name, flss.column_name, insert_value)

    # 解析：企业背景--竞品信息
    def html_parse_jpInfo(self, index):
        insert_value = ""
        key = self.entName
        logger.info("Parse detail info 竞品信息 %s", key)
        if index == 1:
            trs = self.selector.xpath('//table[@class="table  companyInfo-table"]//tbody/tr')
        else:
            trs = self.selector.xpath('//div[@id="_container_jingpin"]//table/tbody/tr')
        jpInfo = TycQyfzJpxx()
        if trs:
            for tr in trs:
                tds = tr.xpath('./td')
                jpInfo.jpProduct = tds[1].xpath('string(.)').replace('\n', '').replace(' ', '')
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

    # 解析：企业背景--企业业务
    def html_parse_entBusiness(self, index):
        insert_value = ""
        key = self.entName
        logger.info("Parse detail info 企业业务 %s", key)
        if index == 1:
            divs = self.selector.xpath('//div[@class="firmproduct"]/div[@class="product-item"]')
        else:
            divs = self.selector.xpath(
                '//div[@id="_container_firmProduct"]//div[@class="firmproduct"]/div[@class="product-item"]')
        entBusiness = TycQyfzQyyw()
        if divs:
            for div in divs:
                entBusiness.businessName = div.xpath('.//span[@class="title"]')[0].xpath('string(.)').replace('\n',
                                                                                                              '').replace(
                    ' ', '')
                entBusiness.businessQuale = div.xpath('.//div[@class="hangye"]')[0].xpath('string(.)').replace('\n',
                                                                                                               '').replace(
                    ' ', '')
                entBusiness.businessInfo = str(div.xpath('.//div[@class="yeweu overflow-width"]')[0].text).strip()
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
            trs = self.selector.xpath('//table[@class="table  companyInfo-table"]//tbody/tr')
        else:
            trs = self.selector.xpath('//div[@id="_container_touzi"]//table/tbody/tr')
        investEvent = TycQyfzTzsj()
        if trs:
            for tr in trs:
                tds = tr.xpath('./td')
                investEvent.touziDate = tds[1].xpath('string(.)').replace('\n', '').replace(' ', '')
                investEvent.touziRound = tds[2].xpath('string(.)').replace('\n', '').replace(' ', '')
                investEvent.touziMoney = tds[3].xpath('string(.)').replace('\n', '').replace(' ', '')
                investEvent.touziEnt = tds[4].xpath('string(.)').replace('\n', '').replace(' ', '')
                investEvent.touziProduct = tds[5].xpath('string(.)').replace('\n', '').replace(' ', '')
                investEvent.touziArea = tds[6].xpath('string(.)').replace('\n', '').replace(' ', '')
                investEvent.touziIndustry = tds[7].xpath('string(.)').replace('\n', '').replace(' ', '')
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
            divs = self.selector.xpath('//div[@class="team-item"]')
        else:
            divs = self.selector.xpath('//div[@id="_container_teamMember"]//div[@class="team-item"]')
        if divs:
            for div in divs:
                coreTeam.personName = div.xpath('.//div[@class="team-name"]/text()')[0].strip()
                coreTeam.personInfo = div.xpath('.//span[@class="text-dark-color"]/text()')[0].strip().replace('\n',
                                                                                                               '').replace(
                    '\r', '').replace(' ', '')
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
            root_div = self.soup.find("div")
        else:
            # 获得网站备案大标签
            root_div = self.soup.find("div", attrs={"id": "_container_icp"})
        if root_div:
            # 一行是一个tr
            trs = root_div.find("table").find("tbody").find_all("tr")
            insert_value = ""
            for tr in trs:
                tds = tr.find_all("td")
                flss.audit_date = tds[1].text.strip()
                flss.web_name = tds[2].text.strip()
                flss.web_homepage = tds[3].text.strip()
                flss.domain_name = tds[4].text.strip()
                flss.record_number = tds[5].text.strip()
                flss.status = tds[6].text.strip()
                flss.department_type = tds[7].text.strip()

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
            root_div = self.soup.find("div")
        else:
            # 获得股权出质大标签
            root_div = self.soup.find("div", attrs={"tyc-event-ch": "CompangyDetail.guquanchuzhi"})
        if root_div:
            # 一行是一个tr
            trs = root_div.find("table").find("tbody").find_all("tr")
            insert_value = ""
            for tr in trs:
                tds = tr.find_all("td")
                flss.announcement_date = tds[1].text.strip()
                flss.registration_number = tds[2].text.strip()
                flss.pledgor = tds[3].text.strip()
                flss.pledgee = tds[4].text.strip()
                flss.status = tds[5].text.strip()
                flss.detail_info = tds[6].text.replace("详情 》", "").strip().replace('"', '\\"')
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
            trs = self.selector.xpath('//table[@class="table  companyInfo-table"]//tbody/tr')
        else:
            trs = self.selector.xpath('//div[@id="_container_changeinfo"]//table/tbody/tr')

        alterRecord = TycQybjBgjl()
        if trs:
            for tr in trs:
                alterRecord = TycQybjBgjl()
                tds = tr.xpath('./td')
                tds_len=len(tds)
                logger.info(tds_len)
                if 1 < tds_len:
                    alterRecord.alterDate = tds[1].xpath('string(.)').replace('\n', '').replace(' ', '')
                    if isinstance(alterRecord.alterDate, UnicodeType):
                        alterRecord.alterDate = alterRecord.alterDate.encode("utf8")
                    else:
                        alterRecord.alterDate = alterRecord.alterDate.decode("gb2312").encode("utf8")

                if 2 < tds_len:
                    alterRecord.alterProject = tds[2].xpath('string(.)').replace('\n', '').replace(' ', '')
                    if isinstance(alterRecord.alterProject, UnicodeType):
                        alterRecord.alterProject = alterRecord.alterProject.encode("utf8")
                    else:
                        alterRecord.alterProject = alterRecord.alterProject.decode("gb2312").encode("utf8")
                if 3 < tds_len:
                    alterRecord.alterBefor = tds[3].xpath('string(.)').replace('\n', '').replace('\r', '').replace(' ',
                                                                                                                   '')
                    if isinstance(alterRecord.alterBefor, UnicodeType):
                        alterRecord.alterBefor = alterRecord.alterBefor.encode("utf8")
                    else:
                        alterRecord.alterBefor = alterRecord.alterBefor.decode("gb2312").encode("utf8")
                if 4 <tds_len:
                    alterRecord.alterAfter = tds[4].xpath('string(.)').replace('\n', '').replace('\r', '').replace(' ', '')
                    if isinstance(alterRecord.alterAfter, UnicodeType):
                        alterRecord.alterAfter = alterRecord.alterAfter.encode("utf8")
                    else:
                        alterRecord.alterAfter = alterRecord.alterAfter.decode("gb2312").encode("utf8")
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
            root_div = self.soup.find("div")
        else:
            # 获得分支机构大标签
            root_div = self.soup.find("div", attrs={"id": "_container_branch"})
        if root_div:
            # 一行是一个tr
            trs = root_div.find("table").find("tbody").find_all("tr")
            insert_value = ""
            for tr in trs:
                tds = tr.find_all("td")
                flss.company_name = tds[1].text.strip()

                flss.legal_representative = tds[2].text.strip()
                flss.status = tds[3].text.strip()
                flss.registered_date = tds[4].text.strip()

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

            trs = self.selector.xpath('//table[@class="table companyInfo-table"]//tbody/tr')
        else:
            trs = self.selector.xpath(
                '//div[@id="_container_invest"]//div[@class="out-investment-container"]/table/tbody/tr')
        # //div[@class="out-investment-container"]/table/tbody/tr
        investInfo = TycQybjDwtz()
        if trs:
            for tr in trs:
                tds = tr.xpath('./td')
                investInfo.investCompany = tds[1].xpath('string(.)').replace('\n', '').replace(' ', '')
                try:
                    investInfo.investPerson = tds[2].xpath('.//a')[0].xpath('string(.)').replace('\n', '').replace(' ',
                                                                                                                   '')
                except:
                    pass
                investInfo.investFund = tds[3].xpath('string(.)').replace('\n', '').replace(' ', '')
                # investInfo.investAmount = tds[4].xpath('string(.)').replace('\n', '').replace(' ', '')
                investInfo.investRatio = tds[4].xpath('string(.)').replace('\n', '').replace(' ', '')
                investInfo.investDate = tds[5].xpath('string(.)').replace('\n', '').replace(' ', '')
                investInfo.investStatus = tds[6].xpath('string(.)').replace('\n', '').replace(' ', '')
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
        root_div = self.soup.find("div", attrs={"tyc-event-ch": "CompangyDetail.zizhi"})
        if root_div:
            # 一行是一个tr
            trs = root_div.find("table").find("tbody").find_all("tr")
            insert_value = ""
            for tr in trs:
                tds = tr.find_all("td")
                flss.register_customs = tds[1].text.strip()
                flss.customs_number = tds[2].text.strip()
                flss.manger_type = tds[3].text.strip()
                flss.detail_info = tds[4].text.replace("详情 》", "").strip().replace('"', '\\"')
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
            root_div = self.soup.find("div")
        else:
            root_div = self.soup.find("div", attrs={"id": "_container_copyrightWorks"})

        if root_div:
            trs = root_div.find("table").find("tbody").find_all("tr")
            insert_value = ""
            for tr in trs:
                # 作品名称	登记号	类别	 创作完成日期	登记日期	首次发布日期
                tds = tr.find_all("td")
                flss.works_name = tds[1].text.strip()
                flss.register_name = tds[2].text.strip()
                flss.type = tds[3].text.strip()
                flss.creat_date = tds[4].text.strip()
                flss.register_date = tds[5].text.strip()
                flss.firstpublish_date = tds[6].text.strip()
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
            divs = self.selector.xpath('//div[@class="wechat clearfix"]/div[@class="mb10 in-block float-left"]')
        else:
            divs = self.selector.xpath(
                '//div[@id="_container_wechat"]//div[@class="wechat clearfix"]/div[@class="mb10 in-block float-left"]')
        entWeChat = TycJyzkWxgzh()
        if divs:
            for div in divs:
                entWeChat.mp_name = div.xpath('.//div[@class="mb5"]')[0].xpath('string(.)').replace('\n', '').replace(
                    ' ', '')
                entWeChat.mp_number = div.xpath('.//span[@class="in-block vertical-top sec-c2"]')[0].xpath(
                    'string(.)').replace('\n', '').replace(' ', '')
                entWeChat.mp_info = str(
                    div.xpath('.//span[@class="overflow-width in-block vertical-top sec-c2"]')[0].text).strip()
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
            root_div = self.soup.find("div")
        else:
            # 获得商标信息大标签
            root_div = self.soup.find("div", attrs={"tyc-event-ch": "CompangyDetail.shangbiao"})

        if root_div:
            # 一行是一个tr
            trs = root_div.find("table").find("tbody").find_all("tr")
            insert_value = ""
            for tr in trs:
                tds = tr.find_all("td")
                if tds:
                    flss.apply_date = tds[1].text.strip()
                    if isinstance( flss.apply_date,UnicodeType):
                        flss.apply_date=flss.apply_date.encode("utf8")
                    flss.trademark = tds[2].text.strip()
                    if isinstance( flss.trademark,UnicodeType):
                        flss.trademark=flss.trademark.encode("utf8")
                    flss.trademark_name = tds[3].text.strip()
                    if isinstance( flss.trademark_name,UnicodeType):
                        flss.trademark_name=flss.trademark_name.encode("utf8")
                    flss.registration_number = tds[4].text.strip()
                    if isinstance( flss.registration_number,UnicodeType):
                        flss.registration_number=flss.registration_number.encode("utf8")
                    flss.type = tds[5].text.strip()
                    if isinstance( flss.type,UnicodeType):
                        flss.type=flss.type.encode("utf8")
                    flss.status = tds[6].text.strip()

                    if isinstance( flss.status,UnicodeType):
                        flss.status=flss.status.encode("utf8")
                    else:
                        flss.status = flss.status.decode("gb2312").encode("utf8")
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
                    insert_value += ' (' + ','.join(value_list) + ')'
                    self.mysqlClient.mysql_insert(flss.table_name, flss.column_name, insert_value)

    # 软件著作权
    def html_parse_copyright(self, index):
        flss = TycZscqZzq()
        key = self.entName
        logger.info("Parse detail info 软件著作权 %s", key)
        if index == 1:
            root_div = self.soup.find("div")

        else:
            root_div = self.soup.find("div", attrs={"id": "_container_copyright"})

        # 获得著作权大标签
        if root_div:
            # 一行是一个tr
            trs = root_div.find("table").find("tbody").find_all("tr")
            insert_value = ""
            for tr in trs:
                tds = tr.find_all("td")
                flss.approval_date = tds[1].text.strip()
                flss.software_name = tds[2].text.strip()
                flss.software_referred = tds[3].text.strip()
                flss.registration_number = tds[4].text.strip()
                flss.type_number = tds[5].text.strip()
                flss.version_number = tds[6].text.strip()
                flss.detail_info = tds[7].text.replace("详情 》", "").strip().replace('"', '\\"')

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
            trs = self.selector.xpath('//table[@class="table companyInfo-table"]//tbody/tr')
        else:
            trs = self.selector.xpath('//div[@id="_container_certificate"]//table/tbody/tr')

        if trs:
            for tr in trs:
                certificateInfo = TycJyzkZzzs()
                tds = tr.xpath('./td')
                certificateInfo.certificateNum = tds[2].xpath('string(.)').replace('\n', '').replace(' ', '')
                certificateInfo.certificateType = tds[1].xpath('string(.)').replace('\n', '').replace(' ', '')
                certificateInfo.sendDate = tds[3].xpath('string(.)').replace('\n', '').replace(' ', '')
                certificateInfo.offDate = tds[4].xpath('string(.)').replace('\n', '').replace(' ', '')
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
        if index == 1:
            root_div = self.soup.find("div")
        else:
            # 获得法律诉讼大标签
            root_div = self.soup.find("div", attrs={"tyc-event-ch": "CompangyDetail.lawsuit"})
        if root_div:
            # 一行是一个tr
            trs = root_div.find("table").find("tbody").find_all("tr")
            insert_value = ""
            for tr in trs:
                tds = tr.find_all("td")
                if tds:
                    flss.judgment_date = tds[1].text.strip()
                    flss.judgment_document = tds[2].text.strip().replace('\n', '').replace('\r', '').replace(' ', '')
                    tds_href= tds[1].find("a")
                    if (tds_href )and ("href" in tds_href):
                        flss.document_url=tds_href["href"]
                    flss.case_type = tds[3].text.strip()
                    flss.case_identity = tds[4].text.strip()
                    flss.case_number = tds[5].text.strip()
                    flss.txt_id = self.txtId
                    flss.ent_name = key
                    flss.add_time = str(datetime.now())
                    flss.mark = str(0)
                    flss.agency_num = self.agency_num
                    flss.agency_name = self.agency_name
                    # 区别key
                    flss.batch = self.batch
                    key1 = str(flss.judgment_document + flss.case_number).replace(".", "-")
                if isinstance(key1, UnicodeType):
                    text1 = law[key1]
                else:
                    text1 = law[key1.decode("utf-8")]
                soup2 = BeautifulSoup(text1, "lxml")
                flss.text_info = soup2.find("div",
                                            attrs={"class", "lawsuitcontent pt20 pb50 lawsuitcontentnew"}).text.replace(
                    '"', '')
                value_list = [flss.judgment_date, flss.judgment_document, flss.case_type, flss.case_identity,
                              flss.case_number, flss.document_url, flss.txt_id, flss.ent_name, flss.add_time, flss.mark,
                              flss.text_info, flss.agency_num, flss.agency_name, flss.batch]
                value_list = ['"' + value + '"' for value in value_list]
                insert_value += '(' + ','.join(value_list) + '),'
            insert_value = insert_value[0:-1]
            self.mysqlClient.mysql_insert(flss.table_name, flss.column_name, insert_value)

    # 招聘
    def html_parse_recruitment(self, index):
        flss = TycJyzkZp()
        key = self.entName
        logger.info("Parse detail info 招聘 %s", key)

        # 判断分页
        if index == 1:
            # 获得招聘大标签
            root_div = self.soup.find("div")
        else:

            root_div = self.soup.find("div", attrs={"tyc-event-ch": "CompangyDetail.zhaopin"})

        if root_div:
            # 一行是一个tr
            trs = root_div.find("table").find("tbody").find_all("tr")
            insert_value = ""
            for tr in trs:
                tds = tr.find_all("td")
                flss.publish_date = tds[1].text.strip()
                flss.recruitment_job = tds[2].text.strip()
                flss.salary = tds[3].text.strip()
                flss.work_year = tds[4].text.strip().replace('"', "")
                flss.recruitment_numbers = tds[5].text.strip()
                flss.work_city = tds[6].text.strip()
                flss.detail_info = tds[7].text.replace("详情 》", "").replace('\\"', '"').strip().replace('"', '\\"')
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
            root_div = self.soup.find("div")
        else:
            # 获得被执行人大标签
            root_div = self.soup.find("div", id="_container_zhixing")
        if root_div:
            # 一行是一个tr
            trs = root_div.find("table").find("tbody").find_all("tr")
            insert_value = ""
            for tr in trs:
                tds = tr.find_all("td")
                flss.record_date = tds[1].text.strip()
                flss.Execute_underlying = tds[2].text.strip()
                flss.case_number = tds[3].text.strip()
                flss.court = tds[4].text.strip()
                flss.txt_id = self.txtId
                flss.ent_name = key
                flss.add_time = str(datetime.now())
                flss.mark = str(0)
                flss.agency_num = self.agency_num
                flss.agency_name = self.agency_name
                flss.batch = self.batch
                value_list = [flss.record_date, flss.Execute_underlying, flss.case_number, flss.court, flss.txt_id,
                              flss.ent_name, flss.add_time, flss.mark, flss.agency_num, flss.agency_name, flss.batch]
                value_list = ['"' + value + '"' for value in value_list]
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
            root_div = self.soup.find("div")
        else:
            # 获得招投标大标签
            root_div = self.soup.find("div", attrs={"tyc-event-ch": "CompangyDetail.zhaotoubiao"})
        if root_div:
            # 一行是一个tr
            trs = root_div.find("table").find("tbody").find_all("tr")
            insert_value = ""
            for tr in trs:
                tds = tr.find_all("td")
                flss.publish_date = tds[1].text.strip()
                flss.title = tds[2].text.strip()
                flss.title_url = tds[3].find("a")["href"]
                flss.procurement = tds[4].text.strip()
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
            root_div = self.soup.find("div")
        else:
            # 获得债券信息大标签
            root_div = self.soup.find("div", attrs={"tyc-event-ch": "CompangyDetail.zhaiquan"})
        if root_div:
            # 一行是一个tr
            trs = root_div.find("table").find("tbody").find_all("tr")
            insert_value = ""
            for tr in trs:
                tds = tr.find_all("td")
                flss.publish_date = tds[1].text.strip()
                flss.bond_name = tds[2].text.strip()
                flss.bond_code = tds[3].text.strip()
                flss.bond_type = tds[4].text.strip()
                flss.latest_rating = tds[5].text.strip()
                flss.detail_info = tds[6].text.replace("详情 》", "").strip().replace('"', '\\"')
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
                value_list = ['"' + value + '"' for value in value_list]
                insert_value += '(' + ','.join(value_list) + '),'
            insert_value = insert_value[0:-1]
            self.mysqlClient.mysql_insert(flss.table_name, flss.column_name, insert_value)

    # 解析：经营风险--欠税公告
    def html_parse_taxesNotice(self, index):
        insert_value = ""
        key = self.entName
        logger.info("Parse detail info 欠税公告 %s", key)
        if index == 1:
            trs = self.selector.xpath('//table[@class="table  companyInfo-table"]//tbody/tr')
        else:
            trs = self.selector.xpath('//div[@id="_container_towntax"]//table/tbody/tr')
        if trs:
            for tr in trs:
                taxesNotice = TycJyfxQsgg()
                tds = tr.xpath('./td')
                taxesNotice.taxesDate = tds[1].xpath('string(.)').replace('\n', '').replace(' ', '')
                taxesNotice.taxesNum = tds[2].xpath('string(.)').replace('\n', '').replace(' ', '')
                taxesNotice.taxesType = tds[3].xpath('string(.)').replace('\n', '').replace(' ', '')
                taxesNotice.taxesMoney = tds[4].xpath('string(.)').replace('\n', '').replace(' ', '')
                taxesNotice.taxesBalance = tds[5].xpath('string(.)').replace('\n', '').replace(' ', '')
                taxesNotice.taxesOffice = tds[6].xpath('string(.)').replace('\n', '').replace(' ', '')
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
                value_list = ['"' + value + '"' for value in value_list]
                insert_value += '(' + ','.join(value_list) + '),'
            insert_value = insert_value[0:-1]
            self.mysqlClient.mysql_insert(taxesNotice.table_name, taxesNotice.column_name, insert_value)

    # 股权出质
    def html_parse_pledge(self, index):
        flss = TycJyfxGqcz()
        key = self.entName
        logger.info("Parse detail info 股权出质 %s", key)
        if index == 1:
            root_div = self.soup.find("div")
        else:
            # 获得股权出质大标签
            root_div = self.soup.find("div", attrs={"tyc-event-ch": "CompangyDetail.guquanchuzhi"})
        if root_div:
            # 一行是一个tr
            trs = root_div.find("table").find("tbody").find_all("tr")
            insert_value = ""
            for tr in trs:
                tds = tr.find_all("td")
                flss.announcement_date = tds[1].text.strip()
                flss.registration_number = tds[2].text.strip()
                flss.pledgor = tds[3].text.strip()
                flss.pledgee = tds[4].text.strip()
                flss.status = tds[5].text.strip()

                flss.detail_info = tds[6].text.replace("详情 》", "").strip().replace('"', '\\"')
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

    # 动产抵押
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
                flss.detail_info = tds[7].text.replace("详情 》", "").strip().replace('"', '\\"')

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
            root_div = self.soup.find("div")
        else:
            # 获得行政处罚大标签
            root_div = self.soup.find("div", attrs={"tyc-event-ch": "CompangyDetail.xingzhengchufa"})
        if root_div:
            # 一行是一个tr
            trs = root_div.find("table").find("tbody").find_all("tr")
            insert_value = ""
            for tr in trs:
                tds = tr.find_all("td")
                try:
                    flss.decision_date = tds[1].text.strip()
                    flss.decision_number = tds[2].text.strip()
                    flss.type = tds[3].text.strip().replace('"', "")
                    flss.decision_department = tds[4].text.strip()
                    flss.detail_info = tds[5].text.replace("详情 》", "").strip().replace('"', '\\"')
                except:
                    flss.decision_date = ""
                    flss.decision_number = ""
                    flss.type = ""
                    flss.decision_department = ""

                    flss.punishment_name = tds[1].text.strip()
                    flss.punishment_area = tds[2].text.strip()
                    flss.detail_info = tds[3].text.replace("详情 》", "").strip().replace('"', '\\"')

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
            root_div = self.soup.find("div")
        else:
            # 获得失信人大标签
            root_div = self.soup.find("div", attrs={"tyc-event-ch": "CompangyDetail.shixinren"})
        if root_div:
            # 一行是一个tr
            trs = root_div.find("table").find("tbody").find_all("tr")
            insert_value = ""
            for tr in trs:
                tds = tr.find_all("td")
                flss.case_date = tds[1].text.strip()
                flss.case_number = tds[2].text.strip()
                flss.execution_court = tds[3].text.strip()
                flss.performance_state = tds[4].text.strip()
                flss.execute_number = tds[5].text.strip()
                flss.detail_info = tds[6].text.replace("详情 》", "").strip().replace('"', '\\"')

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
                value_list = ['"' + value + '"' for value in value_list]
                insert_value += '(' + ','.join(value_list) + '),'
            insert_value = insert_value[0:-1]
            self.mysqlClient.mysql_insert(flss.table_name, flss.column_name, insert_value)

    # 税务评级
    def html_parse_tax(self, index):
        flss = TycJyzkSwpj()
        key = self.entName
        logger.info("Parse detail info 税务评级 %s", key)
        if index == 1:
            root_div = self.soup.find("div")
        else:
            # 获得税务评级大标签
            root_div = self.soup.find("div", attrs={"id": "_container_taxcredit"})
        if root_div:
            # 一行是一个tr
            trs = root_div.find("table").find("tbody").find_all("tr")
            insert_value = ""
            for tr in trs:
                tds = tr.find_all("td")
                flss.year = tds[1].text.strip()
                flss.tax_rating = tds[2].text.strip()
                flss.tax_type = tds[3].text.strip()
                flss.tax_identification_number = tds[4].text.strip()
                flss.evaluate_department = tds[5].text.strip()
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
        root_div = self.soup.find("div", attrs={"id": "_container_abnormal"})
        if root_div:
            # 一行是一个tr
            trs = root_div.find("table").find("tbody").find_all("tr")
            insert_value = ""
            for tr in trs:
                tds = tr.find_all("td")
                flss.insert_date = tds[1].text.strip()
                flss.insert_cause = tds[2].text.strip()
                flss.insert_department = tds[3].text.strip()

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
    def html_parse_illegalSerious(self):
        insert_value = ""
        key = self.entName
        logger.info("Parse detail info 严重违法 %s", key)

        trs = self.selector.xpath('//div[@id="_container_illegal"]//table/tbody/tr')
        if trs:
            for tr in trs:
                illegalSerious = TycJyfxYzwf()
                tds = tr.xpath('./td')
                illegalSerious.illegalDate = tds[1].xpath('string(.)').replace('\n', '').replace(' ', '') or ''
                illegalSerious.illegalReason = tds[2].xpath('string(.)').replace('\n', '').replace(' ', '') or ''
                illegalSerious.office = tds[3].xpath('string(.)').replace('\n', '').replace(' ', '') or ''
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
    def html_parse_buyInfo(self):
        insert_value = ""
        key = self.entName
        logger.info("Parse detail info 购地信息 %s", key)

        trs = self.selector.xpath('//div[@id="_container_purchaseland"]//table/tbody/tr')
        if trs:
            for tr in trs:
                buyInfo = TycJyzkGdxx()
                tds = tr.xpath('./td')
                buyInfo.gdSignDate = tds[1].xpath('string(.)').replace('\n', '').replace(' ', '') or ''
                buyInfo.gdNum = tds[2].xpath('string(.)').replace('\n', '').replace(' ', '') or ''
                buyInfo.gdActDate = tds[3].xpath('string(.)').replace('\n', '').replace(' ', '') or ''
                buyInfo.gdArea = tds[4].xpath('string(.)').replace('\n', '').replace(' ', '') or ''
                buyInfo.gdRegion = tds[5].xpath('string(.)').replace('\n', '').replace(' ', '') or ''
                buyInfo.gdOperate = tds[6].xpath('string(.)').replace('\n', '').replace(' ', '') or ''
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
        root_div = self.soup.find("div", attrs={"tyc-event-ch": "CompangyDetail.nianbao"})
        if root_div:
            # 一行是一个tr
            all_a = root_div.find_all("a")
            insert_value = ""
            for a in all_a:
                if "href" in a:
                    ss=a["href"]
                    flss.year=ss[-4:].strip()
                    flss.detail_url = a["href"].strip()
                else:
                    continue
                soup2 = BeautifulSoup(year[flss.year], "lxml")
                try:
                    self.html_parse_year_jbxx(soup2, flss.year)
                except Exception as e:
                    logger.exception("Detail info html_parse_year_jbxx() parse error! company_name：%s ID：%s", ent_name,
                                     txt_id)
                try:
                    self.html_parse_year_wzhwdxx(soup2, flss.year)
                except Exception as e:
                    logger.exception("Detail info html_parse_year_wzhwdxx() parse error! company_name：%s ID：%s",
                                     ent_name, txt_id)
                try:
                    self.html_parse_year_gdczxx(soup2, flss.year)
                except Exception as e:
                    logger.exception("Detail info html_parse_year_gdczxx() parse error! company_name：%s ID：%s",
                                     ent_name, txt_id)
                try:
                    self.html_parse_year_zczk(soup2, flss.year)
                except Exception as e:
                    logger.exception("Detail info html_parse_year_zczk() parse error! company_name：%s ID：%s", ent_name,
                                     txt_id)
                try:
                    self.html_parse_year_dwtz(soup2, flss.year)
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
                value_list = ['"' + value + '"' for value in value_list]
                insert_value += '(' + ','.join(value_list) + ')'
            # insert_value = insert_value[0:-1]
                self.mysqlClient.mysql_insert(flss.table_name, flss.column_name, insert_value)

    # 年报基本信息
    def html_parse_year_jbxx(self, soup_year, year):

        flss = TycYearJbxx()
        key = self.entName
        logger.info("Parse detail info 年报基本解析 %s", key)
        # 获得大标签
        root_div = soup_year.find("div", attrs={"class": "report_baseInfo"})
        insert_value = ""
        if root_div:
            # 一行是一个tr
            trs = root_div.find("table").find_all("tr")
            flss.credit_num = trs[0].find_all("td")[1].text or ''
            flss.company_name = trs[0].find_all("td")[3].text or ''
            flss.company_tel = trs[1].find_all("td")[1].text or ''
            flss.postal_code = trs[1].find_all("td")[3].text or ''
            flss.manger_state = trs[2].find_all("td")[1].text or ''
            flss.people_count = trs[2].find_all("td")[3].text or ''
            flss.email = trs[3].find_all("td")[1].text or ''
            flss.website = trs[3].find_all("td")[3].text or ''
            flss.company_address = trs[4].find_all("td")[1].text or ''
            flss.buy_equity = trs[4].find_all("td")[3].text or ''
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
            value_list = ['"' + value + '"' for value in value_list]
            insert_value += '(' + ','.join(value_list) + '),'
            insert_value = insert_value[0:-1]
            self.mysqlClient.mysql_insert(flss.table_name, flss.column_name, insert_value)

    # 解析年报网站信息
    def html_parse_year_wzhwdxx(self, soup_year, year):

        website = TycYearWzhwdxx()
        key = self.entName
        logger.info("Parse detail info 企业年报 %s", key)
        root_div = soup_year.find("div", attrs={"class": "report_website"})
        if root_div:
            # 一行是一个tr
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
            self.mysqlClient.mysql_insert(website.table_name, website.column_name, insert_value)

    # 股东及出资信息
    def html_parse_year_gdczxx(self, soup_year, year):
        gdcz = TycYearGdczxx()
        key = self.entName
        logger.info("Parse detail info 股份出资信息 %s", key)
        # 获得分支机构大标签
        root_div = soup_year.find("div", attrs={"class": "report_holder"})
        if root_div:
            # 一行是一个tr
            trs = root_div.find("table").find("tbody").find_all("tr")
            insert_value = ""
            for tr in trs:
                tds = tr.find_all("td")
                gdcz.shareholder = tds[0].text.strip() or ''
                gdcz.subscirbe_contribution = tds[1].text.strip() or ''
                gdcz.contribution_time = tds[2].text.strip() or ''
                gdcz.contribution_style = tds[3].text.strip() or ''
                gdcz.actual_contribution = tds[4].text.strip() or ''
                gdcz.actual_time = tds[5].text.strip() or ''
                gdcz.actual_style = tds[6].text.strip() or ''
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
            self.mysqlClient.mysql_insert(gdcz.table_name, gdcz.column_name, insert_value)

    # 年报基本信息
    def html_parse_year_zczk(self, soup_year, year):

        flss = TycYearZczk()
        key = self.entName
        logger.info("Parse detail info 资产状况 %s", key)
        # 获得大标签
        root_div = soup_year.find("div", attrs={"class": "report_property"})
        insert_value = ""
        if root_div:
            # 一行是一个tr
            trs = root_div.find("table").find_all("tr")
            flss.total_assets = trs[0].find_all("td")[1].text or ''
            flss.total_income = trs[0].find_all("td")[3].text or ''
            flss.total_sales = trs[1].find_all("td")[1].text or ''
            flss.total_profit = trs[1].find_all("td")[3].text or ''
            flss.operation_income = trs[2].find_all("td")[1].text or ''
            flss.net_profit = trs[2].find_all("td")[3].text or ''
            flss.total_tax = trs[3].find_all("td")[1].text or ''
            flss.total_debt = trs[3].find_all("td")[3].text or ''

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
    def html_parse_year_dwtz(self, soup_year, year):
        dwtz = TycYearDwtz()
        key = self.entName
        logger.info("Parse detail info 股份出资信息 %s", key)
        # 获得分支机构大标签
        root_div = soup_year.find("div", attrs={"class": "report_outbound"})
        if root_div:
            # 一行是一个tr
            trs = root_div.find("table").find("tbody").find_all("tr")
            insert_value = ""
            for tr in trs:
                tds = tr.find_all("td")
                dwtz.credit_num = tds[0].text.strip()
                dwtz.outbound_company = tds[1].text.strip()

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
    import sys

    reload(sys)
    sys.setdefaultencoding('utf-8')
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
            detail_info = mongodbClient.mongodb_find_one("company_detail_info", parameter)
        except:
            logger.exception("Exception Logged")
            continue

        if detail_info:
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
                result = mysqlClient.mysql_find_one(table, param)
                error_list = []
                html = detail_info["text"]
                soup = BeautifulSoup(html, 'lxml')
                selector = etree.HTML(html)
                tyc_Parse.txtId = txt_id
                tyc_Parse.entName = ent_name
                tyc_Parse.agency_num = agency_num
                tyc_Parse.agency_name = agency_name
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
            try:
                logger.info("No detail to be parsed!")
                bd = BatchList()
                batch = mysqlClient.find_batch()
                bd.batch = ''.join(batch)

                bd.end_time = str(datetime.now())

                value_list = [bd.batch, bd.end_time]
                value_list = ['"' + value + '"' for value in value_list]
                insert_value = '(' + ','.join(value_list) + '),'
                insert_value = insert_value[0:-1]
                mysqlClient.mysql_insert(bd.table_name, bd.column_name, insert_value)
            except:
                logger.info("batch is error")
            break
