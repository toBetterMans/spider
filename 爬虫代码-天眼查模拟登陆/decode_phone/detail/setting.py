#!/usr/bin/env python
# -*- coding:utf-8 -*-
 # MongoDB连接信息
MONGODB_HOST = "10.0.5.10"
MONGODB_PORT = 27017
MONGODB_PASSWORD = None
MONGODB_DATABASE = "tyc"
#
#
# # MySql连接的IP地址、密码、端口号
MYSQL_HOST = "10.0.5.10"
MYSQL_PASSWORD = "Bd2016zyfd"
MYSQL_PORT = 3306
MYSQL_USER = "zyfd"
MYSQL_DATABASE = "tyc"

#  MongoDB连接信息
#MONGODB_HOST = "127.0.0.1"
#MONGODB_PORT = 27017
#MONGODB_PASSWORD = None
#MONGODB_DATABASE = "tyc"


# MySql连接的IP地址、密码、端口号
#MYSQL_HOST = "127.0.0.1"
#MYSQL_PORT = 3306
#MYSQL_DATABASE = "tyc"
#MYSQL_USER = "root"
#MYSQL_PASSWORD = "root"
# REDIS_HOST = '10.0.32.85'
REDIS_PORT = 6379
REDIS_DB=''
REDIS_CASHE=60
REDIS_HOST = '127.0.0.1'
#REDIS_PORT = 6379
#REDIS_DB=''
#REDIS_CASHE=60

# 分页字典
tyc_page = {
    # 对外投资 ++
    # https://www.tianyancha.com/pagination/invest.xhtml?ps=20&pn=2&id=22822&_=1531706165342
    "_container_invest": ["https://www.tianyancha.com/pagination/invest.xhtml?ps=20", "id", 20],
    # 变更记录 ++  https://www.tianyancha.com/pagination/changeinfo.xhtml?ps=10&pn=2&id=2312445367&_=1531811351481
    "_container_changeinfo": ["https://www.tianyancha.com/pagination/changeinfo.xhtml?ps=10", "id", 5],
    # 分支机构 ++
    "_container_branch": ["https://www.tianyancha.com/pagination/branch.xhtml?ps=10", "id", 10],
    # 核心团队 ++
    "_container_teamMember": ["https://www.tianyancha.com/pagination/teamMember.xhtml?ps=5", "name", 5],
    # 企业业务 ++
    "_container_firmProduct": ["https://www.tianyancha.com/pagination/firmProduct.xhtml?ps=15", "name", 15],
    # 投资事件 ++
    "_container_touzi": ["https://www.tianyancha.com/pagination/touzi.xhtml?ps=10", "name", 10],
    # 竞品信息 ++
    "_container_jingpin": ["https://www.tianyancha.com/pagination/jingpin.xhtml?ps=10", "name", 10],
    # 法律诉讼 ++
    "_container_lawsuit": ["https://www.tianyancha.com/pagination/lawsuit.xhtml?ps=5", "name", 5],
    # 法院公告 ++
    "_container_court": ["https://www.tianyancha.com/pagination/court.xhtml?ps=5", "name", 5],
    # 失信人 ++
    "nav-main-dishonest": ["https://www.tianyancha.com/pagination/dishonest.xhtml?ps=5", "name", 5],
    # 被执行人 ++
    "_container_zhixing": ["https://www.tianyancha.com/pagination/zhixing.xhtml?ps=5", "id", 5],
    #开庭公告
    # "_container_announcementcourt": ["https://www.tianyancha.com/pagination/zhixing.xhtml?ps=5", "id", 5],
    #司法协助
    # "nav-main-judicialaAidCount":["https://www.tianyancha.com/pagination/zhixing.xhtml?ps=5", "id", 5],
    #司法拍卖
    #清算信息
    #知识产权出质


    # 开庭公告
    "_container_announcementcourt": ["https://www.tianyancha.com/pagination/announcementcourt.xhtml?ps=5", "id", 5],
    # 行政处罚 ++
    "_container_punish": ["https://www.tianyancha.com/pagination/punish.xhtml?ps=5", "name", 5],
    "_container_punishCreditchina": ["https://www.tianyancha.com/pagination/punish.xhtml?ps=5", "name", 5],
    # 股权出质 ++
    "_container_equity": ["https://www.tianyancha.com/pagination/equity.xhtml?ps=5", "name", 5],
    # 动产抵押 ++
    "nav-main-mortgageCount": ["https://www.tianyancha.com/pagination/mortgage.xhtml?ps=5", "name", 5],
    # 欠税公告 ++
    "nav-main-ownTaxCount": ["https://www.tianyancha.com/pagination/towntax.xhtml?ps=5", "id", 5],
    # 招投标 ++
    "nav-main-bidCount": ["https://www.tianyancha.com/pagination/bid.xhtml?ps=10", "id", 10],

    #行政许可
    "_container_licensing":["https://www.tianyancha.com/pagination/bid.xhtml?ps=10", "id", 10],
    #
    # 股东信息
    "_container_holder":["https://www.tianyancha.com/pagination/holder.xhtml?ps=30", "id", 30],
    # 债券信息 ++
    "nav-main-bondCount": ["https://www.tianyancha.com/pagination/bond.xhtml?ps=5", "name", 5],
    # 招聘    ++
    "_container_recruit": ["https://www.tianyancha.com/pagination/recruit.xhtml?ps=10", "name", 10],
    # 税务评级 ++
    "_container_taxcredit": ["https://www.tianyancha.com/pagination/taxcredit.xhtml?ps=5", "id", 5],
    # 抽查检查 ++
    "_container_check": ["https://www.tianyancha.com/pagination/check.xhtml?ps=5", "name", 5],
    # 产品信息 ++
    "_container_product": ["https://www.tianyancha.com/pagination/product.xhtml?ps=5", "id", 5],
    # 资质证书 ++
    "_container_certificate": ["https://www.tianyancha.com/pagination/certificate.xhtml?ps=5", "id", 5],
    # 微信公众号 ++
    "_container_wechat": ["https://www.tianyancha.com/pagination/wechat.xhtml?ps=10", "id", 10],
    # 商标信息 ++
    "nav-main-tmCount": ["https://www.tianyancha.com/pagination/tmInfo.xhtml?ps=5", "id", 5],
    # 专利信息 ++
    "_container_patent": ["https://www.tianyancha.com/pagination/patent.xhtml?ps=5", "id", 5],
    # 软件著作权 ++
    "_container_copyright": ["https://www.tianyancha.com/pagination/copyright.xhtml?ps=5", "id", 5],
    # 作品著作权 ++
    "_container_copyrightWorks": ["https://www.tianyancha.com/pagination/copyrightWorks.xhtml?ps=5", "id", 5],
    # 网站备案 ++
    "_container_icp": ["https://www.tianyancha.com/pagination/icp.xhtml?ps=5", "id", 5],
}




