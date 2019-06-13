#!/usr/bin/env python
# -*- coding:utf-8 -*-
 # MongoDB连接信息
# MONGODB_HOST = "10.0.5.10"
# MONGODB_PORT = 27017
# MONGODB_PASSWORD = None
# MONGODB_DATABASE = "tyc"

#
# # MySql连接的IP地址、密码、端口号
# MYSQL_HOST = "10.0.5.10"
# MYSQL_PASSWORD = "Bd2016zyfd"
# MYSQL_PORT = 3306
# MYSQL_USER = "zyfd"
# MYSQL_DATABASE = "tyc"

#  MongoDB连接信息
MONGODB_HOST = "127.0.0.1"
MONGODB_PORT = 27017
MONGODB_PASSWORD = None
MONGODB_DATABASE = "tyc"

# MySql连接的IP地址、密码、端口号
MYSQL_HOST = "127.0.0.1"
MYSQL_PORT = 3306
MYSQL_DATABASE = "tyc"
MYSQL_USER = "root"
MYSQL_PASSWORD = "root"

REDIS_HOST = '10.0.32.85'
# REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
REDIS_DB=''
REDIS_CASHE=60

# Oralce连接的IP地址、密码、端口号 ('tyc/Tyc%2018@10.0.3.213:1521/CASPRD')
# ORALCE_HOST = "10.0.3.213"
# ORALCE_PORT = 1521
# SERVICE="CASPRD"
# ORALCE_DATABASE = "tyc"
# ORALCE_USER = "tyc"
# ORALCE_PASSWORD = "Tyc%2018"
# ORACLE_API = 'cx_oracle'
ORALCE_PORT = 1521
ORALCE_HOST = "127.0.0.1:1521"
SERVICE = "orcl"
ORALCE_DATABASE = "tyc"
ORALCE_USER = "c##niu"
ORALCE_PASSWORD = "niu_123"


# IP代理
proxyUser = "H09EIQ188A9U99AD"
proxyPass = "6546F4FA2BC7D868"


USER_AGENTS = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
]

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
    "_container_dishonest": ["https://www.tianyancha.com/pagination/dishonest.xhtml?ps=5", "name", 5],
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

    # 对外投资 ++
    # https://www.tianyancha.com/pagination/invest.xhtml?ps=20&pn=2&id=22822&_=1531706165342
    "nav-main-inverstCount": ["https://www.tianyancha.com/pagination/invest.xhtml?ps=20", "id", 20],
    # 变更记录 ++  https://www.tianyancha.com/pagination/changeinfo.xhtml?ps=10&pn=2&id=2312445367&_=1531811351481
    "nav-main-changeCount": ["https://www.tianyancha.com/pagination/changeinfo.xhtml?ps=10", "id", 5],
    # 分支机构 ++
    "nav-main-branchCount": ["https://www.tianyancha.com/pagination/branch.xhtml?ps=10", "id", 10],
    # 核心团队 ++
    "nav-main-companyTeammember": ["https://www.tianyancha.com/pagination/teamMember.xhtml?ps=5", "name", 5],
    # 企业业务 ++
    "nav-main-companyProduct": ["https://www.tianyancha.com/pagination/firmProduct.xhtml?ps=15", "name", 15],
    # 投资事件 ++
    "nav-main-jigouTzanli": ["https://www.tianyancha.com/pagination/touzi.xhtml?ps=10", "name", 10],
    # 竞品信息 ++
    "nav-main-companyJingpin": ["https://www.tianyancha.com/pagination/jingpin.xhtml?ps=10", "name", 10],
    # 法律诉讼 ++
    "nav-main-lawsuitCount": ["https://www.tianyancha.com/pagination/lawsuit.xhtml?ps=5", "name", 5],
    # 法院公告 ++
    "nav-main-courtCount": ["https://www.tianyancha.com/pagination/court.xhtml?ps=5", "name", 5],
    # 失信人 ++
    "nav-main-dishonest": ["https://www.tianyancha.com/pagination/dishonest.xhtml?ps=5", "name", 5],
    # 被执行人 ++
    "nav-main-zhixing": ["https://www.tianyancha.com/pagination/zhixing.xhtml?ps=5", "id", 5],


    # 严重违法
    # _container_illegal

    #司法拍卖
    # _container_judicialSale   象山茂源小额贷款有限公司 爬取详情
    #清算信息
    # container_clearingCount 新疆瑞新企业清算事务有限公司
    #知识产权出质
    
    # 购地信息
    '_container_purchaselandV2': ['https://www.tianyancha.com/pagination/purchaselandV2.xhtml?ps=5', 'name', 5],
    
    # 公示催告
    # _container_publicnoticeItem script
    "_container_publicnoticeItem": ["https://www.tianyancha.com/pagination/publicnoticeItem.xhtml?ps=5", "id", 5],

    #电信许可
    # _container_permission  script

    # 开庭公告
    "nav-main-announcementCount": ["https://www.tianyancha.com/pagination/announcementcourt.xhtml?ps=5", "id", 5],
    # 行政处罚 ++
    "nav-main-punishment": ["https://www.tianyancha.com/pagination/punish.xhtml?ps=5", "name", 5],
    # 股权出质 ++
    "nav-main-equityCount": ["https://www.tianyancha.com/pagination/equity.xhtml?ps=5", "name", 5],
    # 动产抵押 ++
    "nav-main-mortgageCount": ["https://www.tianyancha.com/pagination/mortgage.xhtml?ps=5", "name", 5],
    # 欠税公告 ++
    "nav-main-ownTaxCount": ["https://www.tianyancha.com/pagination/towntax.xhtml?ps=5", "id", 5],
    # 招投标 ++
    "nav-main-bidCount": ["https://www.tianyancha.com/pagination/bid.xhtml?ps=10", "id", 10],

    #行政许可
    # "nav-main-licenseAllCount":["https://www.tianyancha.com/pagination/bid.xhtml?ps=10", "id", 10],



    # 债券信息 ++
    "nav-main-bondCount": ["https://www.tianyancha.com/pagination/bond.xhtml?ps=5", "name", 5],
    # 招聘    ++
    "nav-main-recruitCount": ["https://www.tianyancha.com/pagination/recruit.xhtml?ps=10", "name", 10],
    # 税务评级 ++
    "nav-main-taxCreditCount": ["https://www.tianyancha.com/pagination/taxcredit.xhtml?ps=5", "id", 5],
    # 抽查检查 ++
    "nav-main-checkCount": ["https://www.tianyancha.com/pagination/check.xhtml?ps=5", "name", 5],
    # 产品信息 ++
    "nav-main-productinfo": ["https://www.tianyancha.com/pagination/product.xhtml?ps=5", "id", 5],
    # 资质证书 ++
    "nav-main-certificateCount": ["https://www.tianyancha.com/pagination/certificate.xhtml?ps=5", "id", 5],
    # 微信公众号 ++
    "nav-main-weChatCount": ["https://www.tianyancha.com/pagination/wechat.xhtml?ps=10", "id", 10],
    # 商标信息 ++
    "nav-main-tmCount": ["https://www.tianyancha.com/pagination/tmInfo.xhtml?ps=5", "id", 5],
    # 专利信息 ++
    "nav-main-patentCount": ["https://www.tianyancha.com/pagination/patent.xhtml?ps=5", "id", 5],
    # 软件著作权 ++
    "nav-main-cpoyRCount": ["https://www.tianyancha.com/pagination/copyright.xhtml?ps=5", "id", 5],
    # 作品著作权 ++
    "nav-main-copyrightWorks": ["https://www.tianyancha.com/pagination/copyrightWorks.xhtml?ps=5", "id", 5],
    # 网站备案 ++
    "nav-main-icpCount": ["https://www.tianyancha.com/pagination/icp.xhtml?ps=5", "id", 5],
}

detail_href = {
    '_container_lawsuit': r'https://www.tianyancha.com/lawsuit/*',
    'year': r'https://www.tianyancha.com/reportContent/*',
    '_container_judicialSale': r'https://sf.taobao.com/court_detail/*',
    '_container_court': r'https://www.tianyancha.com/court/*',
    
    '_container_recruit': r'https://job.tianyancha.com/*',
    
    '_container_product': r'https://www.tianyancha.com/product/*',
    '_container_patent': r'https://www.tianyancha.com/patent/*'
}

detail_onclick = {
    '_container_certificate': {'onclick': r'certificatePopup',
                               'url': 'https://www.tianyancha.com/company/certificateDetail.json?id={id}&_={tim}'},
    '_container_judicialAid': {'onclick': r'openJudicialAidDetail',
                               'url': 'https://www.tianyancha.com/company/judicialAidDetail.json?id={id}&_={tim}'},
    '_container_tmInfo': {'onclick': r'openTmDetail',
                          'url': 'https://www.tianyancha.com/company/tmDetail.json?regNo={regNo}&tmClass ={clas}-&_={tim}'}
}
