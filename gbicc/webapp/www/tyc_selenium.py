# -*- coding:utf-8 -*-s
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from mysqlDb import *

def get_name_list():
    list = []
    sql = 'SELECT DISTINCT username FROM tyc_user'
    mysqlClient = MysqlClient()
    li = mysqlClient.mysql_find_by_sql(sql)
    for i in li:
        list.append(i[0].encode('utf8'))
    # with open("C:\\Users\\niu\\Desktop\\1.txt","r") as file:
    #     list = file.read().replace(r"'","").split(",")

    return list


over_file = file
error_file = file
error_phone_file = file


def open_file():
    global over_file, error_file, error_phone_file
    over_file = open(path, "ab+")
    error_file = open(error_name_path, "ab+")
    error_phone_file = open(error_phone_path, "ab+")


path = "C:\\Users\\niu\\Desktop\\namelist.txt"
error_name_path = "C:\\Users\\niu\\Desktop\\error_name_list.txt"
error_phone_path = "C:\\Users\\niu\\Desktop\\error_phone_list.txt"
with open(path, "r") as over_file:
    over_name_list = over_file.read().split(",")
with open(error_name_path, "r") as error_file:
    error_name_list = error_file.read().split(",")
with open(error_phone_path, "r") as error_phone_file:
    error_phone_list = error_phone_file.read().split(",")
nameList = get_name_list()
over_name_list=list(set(over_name_list))
error_name_list=list(set(error_name_list))
error_phone_list=list(set(error_phone_list))
driver = webdriver.Chrome()
name_length = len(nameList)
over_length = len(over_name_list)
error_length = len(error_name_list)
error_phone_length = len(error_phone_list)

print("代测试或者解封账号总数: %d" % name_length)
print("已测试或者解封账号总数: %d" % over_length)
print("已找到疑似被封账号总数: %d" % error_length)
print("已找到错误账号总数: %d" % error_phone_length)

if not (name_length > ( error_length + error_phone_length+over_length)):
    print ('evething is ok!!!!!!!!!! %d' % over_length)
else:
    length = over_length+error_length+error_phone_length
    try:
        for name in nameList :
            # if name not in over_name_list and name not in error_name_list and
            # name not in error_phone_list:
            if name not in over_name_list :
                name = str(name)
                length += 1
                try:
                    if not len(name)==11 :
                        with open(error_phone_path, "ab+") as w_error_phone_file:
                            w_error_phone_file.write(name + ",")
                        print ("发现错误账号：！！！！！")
                        continue
                    driver.get('https://www.tianyancha.com/login')
                    wait = WebDriverWait(driver, 15)    # 显示等待10s
                    # 通过css选择
                    locator = (By.CSS_SELECTOR, "html body div div#web-content div div.login_page.position-rel div.bgContent.top_container_new div.position-rel.container.company_container div.over-hide div.in-block.vertical-top.float-right.right_content.mt50.mr5.mb5 div.module.module1.module2.loginmodule.collapse.in div.modulein.modulein1.mobile_box.pl30.pr30.f14.collapse.in div.pb30.position-rel input._input.input_nor.contactphone")
                    # 等待输入框的出现，如果有就执行下一步
                    wait.until(EC.presence_of_element_located(locator))

                    # 登录
                    print("登录")
                    userName_node = driver.find_element_by_css_selector("div.modulein.modulein1.mobile_box.pl30.pr30.f14.collapse.in")\
                        .find_element_by_css_selector("input._input.input_nor.contactphone")
                    password_node = driver.find_element_by_css_selector("div.modulein.modulein1.mobile_box.pl30.pr30.f14.collapse.in")\
                        .find_element_by_css_selector("input._input.input_nor.contactword")
                    userName_node.send_keys(name.strip())
                    password_node.send_keys("123dashi")
                    password_node.send_keys(Keys.ENTER)    # 回车键
                    try:
                        time.sleep(0.1)
                        #手机号格式不正确
                        text = driver.find_element_by_css_selector(
                            "div.position-abs.new-err.collapse.errMsgphone.in").text
                        # text.find_element_by_link_text("手机号或密码错误").text
                        with open(error_phone_path, "ab+") as w_error_phone_file:
                            w_error_phone_file.write(name + ",")
                        print ("发现错误账号：！！！！！")
                        continue
                    except BaseException , e:
                        # print( e.args)
                        # print(e.message)
                        pass
                    try:
                        #手机号或密码错误 we herd: one,eight,zero,two,six,one,six,eight,three,eight,six
                        text = driver.find_element_by_css_selector(
                            "div.new-err.reg_error_msg_content.errMsgresErr.collapse.in").text
                        with open(error_phone_path, "ab+") as w_error_phone_file:
                            w_error_phone_file.write(name + ",")
                        print ("发现错误账号：！！！！！")
                        continue
                    except BaseException , e:
                        # print(e)
                        pass
                    print("验证码")

                    locator = (By.CSS_SELECTOR, "div.main-tab-body.in-block.js-tab-body.main-tab-company input#home-main-search.form-control.js-live-search.f16.sec-c1")
                    wait.until(EC.presence_of_element_located(locator))
                    input_node = driver.find_element_by_css_selector(
                        "div.main-tab-body.in-block.js-tab-body.main-tab-company input#home-main-search.form-control.js-live-search.f16.sec-c1")
                    input_node.send_keys(u"百度")
                    input_node.send_keys(Keys.ENTER)    # 回车键
                    locator = (By.CSS_SELECTOR, "div.search_contain_peo.mt25")
                    wait.until(EC.presence_of_element_located(locator))
                    with open(path, "ab+") as w_over_file:
                        w_over_file.write(name + ",")

                    print("已验证  %d" % length)
                except BaseException , e:
                    with open(error_name_path, "ab+") as w_error_file:
                        w_error_file.write(name + ",")
                    print(u"发现了疑似被封账号：%s 已加入errorname文件" % int(name.strip()))
                    print("已验证  %d" % length)
                    # print(e)
                    continue
    except Exception , e:
        print ("occour Exception %s" % e)
        raise
    finally:
        print("over!!!!!")
