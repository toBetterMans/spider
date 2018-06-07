# -*- coding:utf-8 -*-

# MongoDB连接信息
# MONGODB_HOST = "10.10.130.85"
# MONGODB_PORT = 27017
# MONGODB_PASSWORD = None
# MONGODB_DATABASE = "tyc"


# MySql连接的IP地址、密码、端口号
# MYSQL_HOST = "10.10.130.85"
# MYSQL_PASSWORD = "Bd2016zyfd"
# MYSQL_PORT = 3306
# MYSQL_USER = "zyfd"
# MYSQL_DATABASE = "tyc"

# #  MongoDB连接信息
MONGODB_HOST = "127.0.0.1"
MONGODB_PORT = 27017
MONGODB_PASSWORD = None
MONGODB_DATABASE = "tyc"

#
# # MySql连接的IP地址、密码、端口号
MYSQL_HOST = "127.0.0.1"
MYSQL_PASSWORD = "root"
MYSQL_PORT = 3306
MYSQL_USER = "root"
MYSQL_DATABASE = "tyc"

# 分页字典
tyc_page = {
    # 对外投资
    "nav-main-inverstCount": ["https://www.tianyancha.com/pagination/invest.xhtml?ps=20", "id", 20],
    # 变更记录
    "nav-main-changeCount": ["https://www.tianyancha.com/pagination/changeinfo.xhtml?ps=5", "id", 5],
    # 分支机构
    "nav-main-branchCount": ["https://www.tianyancha.com/pagination/branch.xhtml?ps=10", "id", 10],
    # 核心团队
    "nav-main-companyTeammember": ["https://www.tianyancha.com/pagination/teamMember.xhtml?ps=5", "name", 5],
    # 企业业务
    "nav-main-companyProduct": ["https://www.tianyancha.com/pagination/firmProduct.xhtml?ps=15", "name", 15],
    # 投资事件
    "nav-main-jigouTzanli": ["https://www.tianyancha.com/pagination/touzi.xhtml?ps=10", "name", 10],
    # 竞品信息
    "nav-main-companyJingpin": ["https://www.tianyancha.com/pagination/jingpin.xhtml?ps=10", "name", 10],
    # 法律诉讼
    "nav-main-lawsuitCount": ["https://www.tianyancha.com/pagination/lawsuit.xhtml?ps=5", "name", 5],
    # 法院公告
    "nav-main-courtCount": ["https://www.tianyancha.com/pagination/court.xhtml?ps=5", "name", 5],
    # 失信人
    "nav-main-dishonest": ["https://www.tianyancha.com/pagination/dishonest.xhtml?ps=5", "name", 5],
    # 被执行人
    "nav-main-zhixing": ["https://www.tianyancha.com/pagination/zhixing.xhtml?ps=5", "id", 5],
    # 开庭公告
    "nav-main-announcementCount": ["https://www.tianyancha.com/pagination/announcementcourt.xhtml?ps=5", "id", 5],
    # 行政处罚
    "nav-main-punishment": ["https://www.tianyancha.com/pagination/punish.xhtml?ps=5", "name", 5],
    # 股权出质
    "nav-main-equityCount": ["https://www.tianyancha.com/pagination/equity.xhtml?ps=5", "name", 5],
    # 动产抵押
    "nav-main-mortgageCount": ["https://www.tianyancha.com/pagination/mortgage.xhtml?ps=5", "name", 5],
    # 欠税公告
    "nav-main-ownTaxCount": ["https://www.tianyancha.com/pagination/towntax.xhtml?ps=5", "id", 5],
    # 招投标
    "nav-main-bidCount": ["https://www.tianyancha.com/pagination/bid.xhtml?ps=10", "id", 10],
    # 债券信息
    "nav-main-bondCount": ["https://www.tianyancha.com/pagination/bond.xhtml?ps=5", "name", 5],
    # 招聘
    "nav-main-recruitCount": ["https://www.tianyancha.com/pagination/recruit.xhtml?ps=10", "name", 10],
    # 税务评级
    "nav-main-taxCreditCount": ["https://www.tianyancha.com/pagination/taxcredit.xhtml?ps=5", "id", 5],
    # 抽查检查
    "nav-main-checkCount": ["https://www.tianyancha.com/pagination/check.xhtml?ps=5", "name", 5],
    # 产品信息
    "nav-main-productinfo": ["https://www.tianyancha.com/pagination/product.xhtml?ps=5", "id", 5],
    # 资质证书
    "nav-main-certificateCount": ["https://www.tianyancha.com/pagination/certificate.xhtml?ps=5", "id", 5],
    # 微信公众号
    "nav-main-weChatCount": ["https://www.tianyancha.com/pagination/wechat.xhtml?ps=10", "id", 10],
    # 商标信息
    "nav-main-tmCount": ["https://www.tianyancha.com/pagination/tmInfo.xhtml?ps=5", "id", 5],
    # 专利信息
    "nav-main-patentCount": ["https://www.tianyancha.com/pagination/patent.xhtml?ps=5", "id", 5],
    # 软件著作权
    "nav-main-cpoyRCount": ["https://www.tianyancha.com/pagination/copyright.xhtml?ps=5", "id", 5],
    # 作品著作权
    "nav-main-copyrightWorks": ["https://www.tianyancha.com/pagination/copyrightWorks.xhtml?ps=5", "id", 5],
    # 网站备案
    "nav-main-icpCount": ["https://www.tianyancha.com/pagination/icp.xhtml?ps=5", "id", 5],
}

