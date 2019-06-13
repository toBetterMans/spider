#!/usr/bin/env python
# -*- coding:utf-8 -*-
# MongoDB连接信息
MONGODB_HOST = "10.10.82.12"
# MONGODB_HOST = "127.0.0.1"
MONGODB_PORT = 27017
MONGODB_USER = 'zyfd'
# MONGODB_PASSWORD = 'zyfd'
MONGODB_PASSWORD = 'ZYFD@2019_db'
MONGODB_DATABASE = "tyc"
#
#
# REDIS_HOST = "127.0.0.1"
# REDIS_HOST = '10.0.32.85'
REDIS_HOST = '10.10.82.12'
REDIS_PORT = 6379
REDIS_DB = ''
REDIS_CASHE = 60
REDIS_PASSWORD = 'ZYFD@2019_redis'


# Oralce连接的IP地址、密码、端口号 ('tyc/Tyc%2018@10.0.3.213:1521/CASPRD')
ORALCE_HOST = "10.10.82.12:1521"
SERVICE = "tycprd"
ORALCE_DATABASE = "tyc"
ORALCE_USER = "tyc"
ORALCE_PASSWORD = "tyc"

# 本地
# ORALCE_HOST = "127.0.0.1:1521"
# SERVICE = "orcl"
# ORALCE_DATABASE = "tyc"
# ORALCE_USER = "c##niu"
# ORALCE_PASSWORD = "niu_123"

# 本地 测试
# ORALCE_HOST = "127.0.0.1:1521"
# SERVICE = "orcl"
# ORALCE_DATABASE = "tyc"
# ORALCE_USER = "c##test"
# ORALCE_PASSWORD = "test_123"

# 生产
# ORALCE_HOST = "10.0.3.213:1521"
# ORALCE_PORT = 1521
# SERVICE = "CASPRD"
# ORALCE_DATABASE = "tyc"
# ORALCE_USER = "tyc"
# ORALCE_PASSWORD = "Tyc%2018"

# 测试 70 4169
# ORALCE_HOST = "10.10.82.70:1521"
# ORALCE_PORT = 1521
# SERVICE = "edwdev2"
# ORALCE_DATABASE = "tyc4169"
# ORALCE_USER = "tyc4169"
# ORALCE_PASSWORD = "tyc4169"

# 测试 70
# ORALCE_HOST = "10.10.82.70:1521"
# ORALCE_PORT = 1521
# ORALCE_DATABASE = "tyc"
# ORALCE_USER = "tyc"
# ORALCE_PASSWORD = "tyc"
# SERVICE = "edwdev2"

# 测试 70 中间库
# ORALCE_HOST = "10.10.82.70:1521"
# ORALCE_PORT = 1521
# ORALCE_DATABASE = "tyc"
# ORALCE_USER = "tyc_trans"
# ORALCE_PASSWORD = "tyc_trans"
# SERVICE = "edwdev2"

# 代理设置
# proxy_user = "H09EIQ188A9U99AD"
# proxy_pass = "6546F4FA2BC7D868"
proxy_user = "H09EIQ188A9U99AD"
proxy_pass = "6546F4FA2BC7D868"

USER_AGENTS = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
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
    "_container_teamMember": ["https://www.tianyancha.com/pagination/teamMember.xhtml?ps=10", "name", 10],
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
    # 开庭公告
    # "_container_announcementcourt": ["https://www.tianyancha.com/pagination/zhixing.xhtml?ps=5", "id", 5],
    # 司法协助  https://www.tianyancha.com/pagination/judicialAid.xhtml?ps=5&pn=2&id=13983271&_=1558405997182
    "nav-main-judicialaAidCount": ["https://www.tianyancha.com/pagination/judicialAid.xhtml?ps=5", "id", 5],
    "_container_judicialAid": ["https://www.tianyancha.com/pagination/judicialAid.xhtml?ps=5", "id", 5],
    # 司法拍卖
    # 清算信息
    # 知识产权出质
    
    # 开庭公告
    "_container_announcementcourt": ["https://www.tianyancha.com/pagination/announcementcourt.xhtml?ps=5", "id", 5],
    # 行政处罚 ++
    "_container_punish": ["https://www.tianyancha.com/pagination/punish.xhtml?ps=5", "name", 5],
    "_container_punishCreditchina": ["https://www.tianyancha.com/pagination/punish.xhtml?ps=5", "name", 5],
    # 股权出质 ++
    "_container_equity": ["https://www.tianyancha.com/pagination/equity.xhtml?ps=5", "name", 5],
    # 动产抵押 ++
    "_container_mortgage": ["https://www.tianyancha.com/pagination/mortgage.xhtml?ps=5", "name", 5],
    # 欠税公告 ++
    "_container_towntax": ["https://www.tianyancha.com/pagination/towntax.xhtml?ps=5", "id", 5],
    # 招投标 ++
    "_container_bid": ["https://www.tianyancha.com/pagination/bid.xhtml?ps=10", "id", 10],
    
    # 行政许可
    "_container_licensing": ["https://www.tianyancha.com/pagination/licensing.xhtml?ps=5", "id", 10],
    #
    # 股东信息
    "_container_holder": ["https://www.tianyancha.com/pagination/holder.xhtml?ps=30", "id", 30],
    # # 债券信息 ++
    # "nav-main-bondCount": ["https://www.tianyancha.com/pagination/bond.xhtml?ps=5", "name", 5],
    # 招聘    ++ _container_recruit  https://www.tianyancha.com/pagination/baipin.xhtml?ps=4&pn=2&id=220769465&_=1553220512110
    "_container_baipin": ["https://www.tianyancha.com/pagination/baipin.xhtml?ps=4", "id", 10],
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
    
    # 专利信息 ++
    "_container_patent": ["https://www.tianyancha.com/pagination/patent.xhtml?ps=5", "id", 5],
    # 软件著作权 ++
    "_container_copyright": ["https://www.tianyancha.com/pagination/copyright.xhtml?ps=5", "id", 5],
    # 作品著作权 ++
    "_container_copyrightWorks": ["https://www.tianyancha.com/pagination/copyrightWorks.xhtml?ps=5", "id", 5],
    # 网站备案 ++
    "_container_icp": ["https://www.tianyancha.com/pagination/icp.xhtml?ps=5", "id", 5],
    # 信用中国
    "_container_licensingXyzg": ["https://www.tianyancha.com/pagination/licensingXyzg.xhtml?ps=5", "id", 5],
    
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
    # "nav-main-dishonest": ["https://www.tianyancha.com/pagination/dishonest.xhtml?ps=5", "name", 5],
    # 被执行人 ++
    "nav-main-zhixing": ["https://www.tianyancha.com/pagination/zhixing.xhtml?ps=5", "id", 5],
    
    # 严重违法
    # _container_illegal
    
    # 司法拍卖
    # _container_judicialSale   象山茂源小额贷款有限公司 爬取详情
    # 清算信息
    # container_clearingCount 新疆瑞新企业清算事务有限公司
    # 知识产权出质
    
    # 购地信息
    '_container_purchaselandV2': ['https://www.tianyancha.com/pagination/purchaselandV2.xhtml?ps=5', 'name', 5],
    
    # 公示催告
    # _container_publicnoticeItem script
    "_container_publicnoticeItem": ["https://www.tianyancha.com/pagination/publicnoticeItem.xhtml?ps=5", "id", 5],
    
    # 电信许可
    # _container_permission  script
    
    # 开庭公告
    "_container_announcement": ["https://www.tianyancha.com/pagination/announcementcourt.xhtml?ps=5", "id", 5],
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
    
    # 行政许可
    # "icensnav-main-leAllCount":["https://www.tianyancha.com/pagination/bid.xhtml?ps=10", "id", 10],
    
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
    "nav-main-tmCount": [r"https://www.tianyancha.com/pagination/tmInfo.xhtml?ps=10", "id", 10],
    # https://www.tianyancha.com/pagination/tmInfo.xhtml?ps=10&pn=2&id=490952627&_=1553322677550
    '_container_tmInfo': [r'https://www.tianyancha.com/pagination/tmInfo.xhtml?ps=10', 'id', 10],
    # 专利信息 ++
    "nav-main-patentCount": ["https://www.tianyancha.com/pagination/patent.xhtml?ps=5", "id", 5],
    # 软件著作权 ++
    "nav-main-cpoyRCount": ["https://www.tianyancha.com/pagination/copyright.xhtml?ps=5", "id", 5],
    # 作品著作权 ++
    "nav-main-copyrightWorks": ["https://www.tianyancha.com/pagination/copyrightWorks.xhtml?ps=5", "id", 5],
    # 网站备案 ++
    "nav-main-icpCount": ["https://www.tianyancha.com/pagination/icp.xhtml?ps=5", "id", 5],
    #     融资历史  https://www.tianyancha.com/pagination/rongzi.xhtml?ps=10&pn=2&name=%E8%BD%AF%E9%80%9A%E5%8A%A8%E5%8A%9B%E4%BF%A1%E6%81%AF%E6%8A%80%E6%9C%AF%EF%BC%88%E9%9B%86%E5%9B%A2%EF%BC%89%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8&_=1558610721761
    '_container_rongzi': ['https://www.tianyancha.com/pagination/rongzi.xhtml?ps=10', 'name', 10]
}

detail_href = {
    '_container_lawsuit': r'https://www.tianyancha.com/lawsuit/*',
    'year': r'https://www.tianyancha.com/reportContent/*',
    # https://sf.taobao.com/notice_detail/1662350.htm
    '_container_judicialSale': r'https://sf.taobao.com/notice_detail/*',
    # '_container_court': r'https://www.tianyancha.com/court/*',
    # href="https://zhaopin.baidu.com/szzw?zp_fr=tianyancha&id=http%3A%2F%2Fkg.baidu.com%2Fod%2F4002%2F2004461%2Fe74ba750da6274c2b87b72c52597b815"
    '_container_baipin': r'https://zhaopin.baidu.com/szzw*',
    
    '_container_product': r'https://www.tianyancha.com/product/*',
    '_container_patent': r'https://www.tianyancha.com/patent/*',
    '_container_tmInfo': r'https://www.tianyancha.com/tm/*',
    'nav-main-tmCount': r'https://www.tianyancha.com/tm/*',
    # 企业关系  https://dis.tianyancha.com/dis/getInfoById/24416401.json?
    '_graph_container': 'https://dis.tianyancha.com/dis/getInfoById/24416401.json?',
    #     历史沿革
    'nav-main-graphTimeInfo': 'https://dis.tianyancha.com/dis/timeline.json?id=24416401'
}

detail_onclick = {
    '_container_certificate': {'onclick': r'certificatePopup',
                               'url': 'https://www.tianyancha.com/company/certificateDetail.json?id={id}&_={tim}'},
    '_container_judicialAid': {'onclick': r'openJudicialAidDetail',
                               'url': 'https://www.tianyancha.com/company/judicialAidDetail.json?id={id}&_={tim}'},
    'nav-main-judicialaAidCount': {'onclick': r'openJudicialAidDetail',
                                   'url': 'https://www.tianyancha.com/company/judicialAidDetail.json?id={id}&_={tim}'},
    # nav-main-judicialaAidCount
    # 改版 去除
    '_container_tmInfo': {'onclick': r'openTmDetail',
                          'url': 'https://www.tianyancha.com/company/tmDetail.json?regNo={regNo}&tmClass ={clas}-&_={tim}'},
    '_container_zhixing': {'onclick': r'openZhixingDetail',
                           'url': 'https://capi.tianyancha.com/cloud-newdim/company/getZhixingDetail.json?zid={zid}&_={tim}'},
    
    '_container_dishonest': {'onclick': r'openDishonestinfoDetail',
                             'url': 'https://capi.tianyancha.com/cloud-newdim/company/getDishonestinfoDetail?did={did}&_={tim}'}
}

parse_dicts = {
    
    'nav-main-cpoyRCount': 'tyc_Parse.html_parse_copyright(index=1)',
    'nav-main-baipin': 'tyc_Parse.html_parse_recruitment(index=1, job=job)',
    'nav-main-lawsuitCount': ' tyc_Parse.html_parse_lawsuit(law, index=1)',
    'nav-main-tmCount': 'tyc_Parse.html_parse_trademark(index=1)',
    'nav-main-inverstCount': 'tyc_Parse.html_parse_investInfo(index=1)',
    'nav-main-changeCount': 'tyc_Parse.html_parse_alterRecord(index=1)',
    'nav-main-branchCount': 'tyc_Parse.html_parse_branch(index=1)',
    'nav-main-equityCount': 'tyc_Parse.html_parse_pledge(index=1)',
    'nav-main-certificateCount': 'tyc_Parse.html_parse_certificateInfo(index=1)',
    'nav-main-icpCount': 'tyc_Parse.html_parse_website(index=1)',
    'nav-main-companyTeammember': 'tyc_Parse.html_parse_coreTeam(index=1)',
    'nav-main-jigouTzanli': 'tyc_Parse.html_parse_investEvent(index=1)',
    'nav-main-companyProduct': 'tyc_Parse.html_parse_entBusiness(index=1)',
    'nav-main-companyJingpin': 'tyc_Parse.html_parse_jpInfo(index=1)',
    'nav-main-courtCount': 'tyc_Parse.html_parse_announcement(index=1)',
    'nav-main-checkCount': 'tyc_Parse.html_parse_check(index=1)',
    'nav-main-patentCount': 'tyc_Parse.html_parse_patent(index=1)',
    'nav-main-copyrightWorks': 'tyc_Parse.html_parse_copyzzq(index=1)',
    'nav-main-weChatCount': 'tyc_Parse.html_parse_entWechat(index=1)',
    'nav-main-productinfo': 'tyc_Parse.html_parse_product(index=1)',
    'nav-main-zhixing': 'tyc_Parse.html_parse_executed(index=1)',
    'nav-main-bidCount': 'tyc_Parse.html_parse_bidding(index=1)',
    'nav-main-bondCount': 'tyc_Parse.html_parse_zhaiquan(index=1)',
    'nav-main-ownTaxCount': 'tyc_Parse.html_parse_taxesNotice(index=1)',
    'nav-main-mortgageCount': 'tyc_Parse.mortgageCount(index=1)',
    # 'nav-main-equityCount': 'tyc_Parse.html_parse_pledge(index=1)',
    'nav-main-punishment': 'tyc_Parse.html_parse_xingzhengchufa(index=1)',
    'nav-main-dishonest': 'tyc_Parse.html_parse_shixinren(index=1)',
    'nav-main-taxCreditCount': 'tyc_Parse.html_parse_tax(index=1)'
    
}
