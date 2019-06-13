# -*- coding:utf-8 -*-s
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from mysqlDb import *
import threading
# nameList = [
#     '17095274572',
#     '17095274584',
#     '17095274585',
#     '17095274588',
#     '17095274590',
#     '17095274592',
#     '17095274593',
#     '17095274595',
#     '17095274596',
#     '17095274598',
#     '17095274599',
#     '17095274600',
#     '17095274601',
#     '17095274602',
#     '17095274603',
#     '17095274604',
#     '17095274607',
#     '17095274608',
#     '17095274614',
#     '17095274636',
#     '17095274642',
#     '17095274644',
#     '17095274645',
#     '17095274647',
#     '17095274650',
#     '17095274652',
#     '17095274653',
#     '17095274654',
#     '17095274657',
#     '17095274659',
#     '17095274662',
#     '17095274663',
#     '17095274664',
#     '17095274665',
#     '17095274667',
#     '17095274670',
#     '17095274671',
#     '17095274753',
#     '17095274758',
#     '17095274760',
#     '17095274761',
#     '17095274762',
#     '17095274768',
#     '17095274822',
#     '17095274827',
#     '17095274830',
#     '17095274834',
#     '17095274902',
#     '17095275044',
#     '17095275047',
#     '17095275056',
#     '17095275059',
#     '17095275061',
#     '17095275062',
#     '17095275063',
#     '17095275064',
#     '17095275067',
#     '17095275069',
#     '17095275070',
#     '17095275071',
#     '17095275072',
#     '17095275074',
#     '17095275080',
#     '17095275081',
#     '17095275082',
#     '17095275083',
#     '17095275084',
#     '17095275091',
#     '17095275092',
#     '17095275093',
#     '17095275102',
#     '17095275196',
#     '17095275203',
#     '17095275204',
#     '17095275213',
#     '17095275216',
#     '17095275242',
#     '17095275249',
#     '17095275251',
#     '17095275256',
#     '17095275259',
#     '17095275301',
#     '17095275312',
#     '17095275314',
#     '17095275340',
#     '17095275343',
#     '17095275344',
#     '17095275345',
#     '17095275348',
#     '17095275349',
#     '17095275350',
#     '17095275351',
#     '17095275363',
#     '17095275389',
#     '17095275391',
#     '17095275475',
#     '17095275476',
#     '17095275478',
#     '17095275480',
#     '17095275481',
#     '17095275482',
#     '17095275484',
#     '17095275485',
#     '17095275486',
#     '17095275491',
#     '17095275492',
#     '17095275493',
#     '17095275494',
#     '17095275495',
#     '17095275497',
#     '17095275498',
#     '17095275499',
#     '17095275501',
#     '17095275502',
#     '17095275503',
#     '17095275505',
#     '17095275516',
#     '17095275521',
#     '17095275523',
#     '17095275621',
#     '17095275625',
#     '17095275626',
#     '17095275627',
#     '17095275628',
#     '17095275632',
#     '17095275636',
#     '17095275637',
#     '17095275639',
#     '17095275646',
#     '17095275647',
#     '17095275649',
#     '17095275650',
#     '17095275651',
#     '17095275654',
#     '17095275661',
#     '17095275663',
#     '17095275664',
#     '17095275667',
#     '17095275671',
#     '17095275672',
#     '17095275673',
#     '17095275674',
#     '17095275675',
#     '17095275676',
#     '17095275685',
#     '17095275691',
#     '17095275692',
#     '17095275693',
#     '17095275696',
#     '17095275737',
#     '17095276192',
#     '17095276198',
#     '17095276213',
#     '17095276215',
#     '17095276217',
#     '17095276218',
#     '17095276223',
#     '17095276228',
#     '17095276267',
#     '17095276275',
#     '17095276284',
#     '17095276285',
#     '17095276287',
#     '17095276298',
#     '17095276304',
#     '17095276305',
#     '17095276306',
#     '17095276307',
#     '17095276308',
#     '17095276311',
#     '17186741968',
#     '17186746960',
#     '18423418411',
#     '18426106197',
#     '18426106253',
#     '18426119346',
#     '18426120006',
#     '18426120516',
#     '18426120596',
#     '18426120866',
#     '18426139573',
#     '18426140016',
#     '18426140200',
#     '18426147691',
#     '18426147716',
#     '18426148426',
#     '18426250411',
#     '18426278511']


def get_name_list():
    list = []
    sql = "SELECT DISTINCT username FROM tyc_user"
    mysqlClient = MysqlClient()
    li = mysqlClient.mysql_find_by_sql(sql)
    for i in li:
        list.append(i[0].encode('utf8'))
    return list


over_file = None
error_file = None
error_phone_file = None


def open_file():
    global over_file, error_file, error_phone_file
    over_file = open(path, "ab+")
    error_file = open(error_name_path, "ab+")
    error_phone_file = open(error_phone_path, "ab+")


def close_file():
    if over_file:
        over_file.close()
    if error_file:
        error_file.close()
    if error_phone_file:
        error_phone_file.close()


def init_list():
    global over_name_list, error_name_list, error_phone_list
    over_name_list = over_file.read().split(",")
    error_name_list = error_file.read().split(",")
    error_phone_list = error_phone_file.read().split(",")


lock = threading.Lock()
path = "C:\\Users\\niu\\Desktop\\namelist.txt"
error_name_path = "C:\\Users\\niu\\Desktop\\error_name_list.txt"
error_phone_path = "C:\\Users\\niu\\Desktop\\error_phone_list.txt"
open_file()
over_name_list = []
error_name_list = []
error_phone_list = []
init_list()
close_file()
open_file()
nameList = get_name_list()

nameList_one = nameList[:500]
nameList_two = nameList[500:]
nameList_three = nameList[100:]
nameList_four = nameList[1500:]

name_length = len(nameList)
over_length = len(over_name_list)
error_length = len(error_name_list)
error_phone_length = len(error_phone_list)

print("代测试或者解封账号总数: %d" % name_length)
print("已测试或者解封账号总数: %d" % over_length)
print("已找到疑似被封账号总数: %d" % error_length)
print("已找到错误账号总数: %d" % error_phone_length)

# if not (name_length > (over_length + error_length + error_phone_length)):
#     print ('evething is ok!!!!!!!!!! %d' % over_length)
#     exit()
# else:
error_list_write = []
error_phone_write = []
name_list_write = []


def start(name_list):
    try:
        lock.acquire()
        driver = webdriver.Chrome()
        length = over_length
        for name in name_list:
            name = str(name)
            if name not in over_name_list and name not in error_name_list:
                try:
                    driver.get('https://www.tianyancha.com/login')
                    wait = WebDriverWait(driver, 15)    # 显示等待10s
                    # 通过css选择
                    locator = (By.CSS_SELECTOR, "html body div div#web-content div div.login_page.position-rel div.bgContent.top_container_new div.position-rel.container.company_container div.over-hide div.in-block.vertical-top.float-right.right_content.mt50.mr5.mb5 div.module.module1.module2.loginmodule.collapse.in div.modulein.modulein1.mobile_box.pl30.pr30.f14.collapse.in div.pb30.position-rel input._input.input_nor.contactphone")
                    # 等待输入框的出现，如果有就执行下一步
                    wait.until(EC.presence_of_element_located(locator))

                    # 登录
                    print("登录")
                    userName_node = driver.find_element_by_css_selector(
                        "html body div div#web-content div div.login_page.position-rel div.bgContent.top_container_new div.position-rel.container.company_container div.over-hide div.in-block.vertical-top.float-right.right_content.mt50.mr5.mb5 div.module.module1.module2.loginmodule.collapse.in div.modulein.modulein1.mobile_box.pl30.pr30.f14.collapse.in div.pb30.position-rel input._input.input_nor.contactphone")
                    password_node = driver.find_element_by_css_selector(
                        "html body div div#web-content div div.login_page.position-rel div.bgContent.top_container_new div.position-rel.container.company_container div.over-hide div.in-block.vertical-top.float-right.right_content.mt50.mr5.mb5 div.module.module1.module2.loginmodule.collapse.in div.modulein.modulein1.mobile_box.pl30.pr30.f14.collapse.in div.pb40.position-rel input._input.input_nor.contactword")
                    userName_node.send_keys(name)
                    password_node.send_keys("123dashi")
                    password_node.send_keys(Keys.ENTER)    # 回车键
                    # try:
                    #     txt=userName_node.find_element_by_xpath("//./following-sibling::div[1]").text
                    #     error_phone_file.write(name + ",")
                    #     print ("发现错误账号：%d！！！！！" % name)
                    #     continue
                    # except:
                    #     pass
                    try:
                        driver.find_element_by_css_selector(
                            "div.new-err reg_error_msg_content errMsgresErr collapse in")
                        # error_phone_file.write(name+",")
                        error_phone_list.append(name)
                        print ("发现错误账号：%d！！！！！" % name)
                        continue
                    except BaseException:
                        pass
                    print("验证码")
                    locator = (By.CSS_SELECTOR, "html body div div#web-content div.mainv2_container div.mainV3_tab1_enter.position-rel div.mainv2_tab1.position-rel div.text-center div.main-tab-outer div div.main-tab-body.in-block.js-tab-body.main-tab-company div.js-search-container div.input-group.inputV2 form div.live-search-wrap.index-search input#home-main-search.form-control.js-live-search")
                    try:
                        wait.until(EC.presence_of_element_located(locator))
                    except BaseException:
                        # error_phone_file.write(name + ",")
                        error_phone_list.append(name)
                        print ("发现错误账号：%d！！！！！" % str(name))
                        continue
                    input_node = driver.find_element_by_css_selector(
                        "html body div div#web-content div.mainv2_container div.mainV3_tab1_enter.position-rel div.mainv2_tab1.position-rel div.text-center div.main-tab-outer div div.main-tab-body.in-block.js-tab-body.main-tab-company div.js-search-container div.input-group.inputV2 form div.live-search-wrap.index-search input#home-main-search.form-control.js-live-search")
                    input_node.send_keys(u"百度")
                    input_node.send_keys(Keys.ENTER)    # 回车键
                    locator = (By.CSS_SELECTOR, "html body div div#web-content div.top_container_new.b-c-gray div.container.company_container div.row.pb20 div.col-9.search-2017-2.pr15.pl0 div.b-c-white.search_result_container div.search_result_single.search-2017.pb25.pt25.pl30.pr30 div.search_right_item.ml10 div a.query_name.sv-search-company.f18.in-block.vertical-middle span")
                    wait.until(EC.presence_of_element_located(locator))
                    # over_file.write(name + ",")
                    name_list_write.append(name)
                    length += 1
                    print("已验证  %d" % length)
                except BaseException:
                    # error_file.write(name + ",")
                    error_list_write.append(name)
                    print(u"发现了疑似被封账号：%s 已加入errorname文件" % name)
                    print("已验证  %d" % length)
                    continue
    except Exception as e:
        print ("occour Exception %s" % e)
        raise
    finally:
        lock.release()


t1 = threading.Thread(target=start(nameList_one), name='nameList_one')
t2 = threading.Thread(target=start(nameList_two), name='nameList_two')
t3 = threading.Thread(target=start(nameList_three), name='nameList_three')
t4 = threading.Thread(target=start(nameList_four), name='nameList_four')
t1.start()
t2.start()
t3.start()
t4.start()
t1.join()
t2.join()
t3.join()
t4.join()
over_file.write("".join(name_list_write))
error_file.write("".join(error_list_write))
error_phone_file.write("".join(error_phone_write))
close_file()
