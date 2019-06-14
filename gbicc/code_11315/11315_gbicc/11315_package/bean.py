# -*- coding:utf-8 -*-


class CompanyIndex(object):
    # 公司索引号
    number = ""
    # url
    url = ""
    # 公司名称
    company_name = ""
    # 所属行业
    company_industry = ""
    # 所在区域
    company_area = ""
    # 公司地址
    company_address = ""
    # 添加时间
    add_time = ""
    # 标记号
    mark = ""

    table_name = "11315_company"
    column_name = "(number, url, company_name, company_industry, company_area, company_address, add_time, mark)"
