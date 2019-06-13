# -*- coding:utf-8 -*-
import time
# from db import single_mysql
#
# mysqlClient = single_mysql


def area_parse(area):
    print  ("area=%s"%area)
    address_1 = "null"
    address_2 = "null"
    address_3 = "null"

    i1 = area.find(u"省")
    i2 = area.find(u"市")

    k1 = area.find(u"区")
    k2 = area.find(u"县")

    if i1 != -1:
        address_1 = area[:i1 + 1]

    if i2 != -1:
        address_2 = area[i1 + 1:i2 + 1]
        address_3 = area[i2 + 1:]
    elif k1 != -1 or k2 != -1:
        address_3 = area[i1 + 1:]
    else:
        address_2 = area[i1 + 1:]

    return address_1, address_2, address_3


def address_parse(area):
    address_1 = "null"
    address_2 = "null"
    address_3 = "null"

    i1 = area.find(u"省")
    i2 = area.find(u"市")

    k1 = area.find(u"县")
    k2 = area.find(u"区")
    if k1 != -1:
        i3 = k1
    else:
        i3 = k2

    if i1 != -1:
        address_1 = area[:i1 + 1]

    if i2 > i3 != -1:
        i2 = -1

    if i2 != -1:
        address_2 = area[i1 + 1:i2 + 1]
        address_3 = area[i2 + 1:i3 + 1]
    elif k1 != -1 or k2 != -1:
        address_3 = area[i1 + 1:i3 + 1]
    else:
        address_2 = area[i1 + 1:i3 + 1]

    return address_1, address_2, address_3


def company_parse(area,address):

    area = area
    address = address
    if area:
        address_1, address_2, address_3 = area_parse(area)
        if address_2 != "" and address_3 != "":
            pass
        elif address_2 == "" and address_3 != "":
            n_1, n_2, n_3 = address_parse(address)
            n = n_3.replace("县", "")
            k = address_3.find(n)
            if k != -1:
                address_2 = address_3[:k]
                address_3 = address_3[k:]
        elif address_2 != "" and address_3 == "":
            n_1, n_2, n_3 = address_parse(address)
            if address_2.endswith("市"):
                address_3 = n_3
            else:
                n = n_3.replace("县", "")
                k = address_2.find(n)
                if k != -1 and k != 0:
                    address_2 = address_2[:k]
                    address_3 = n_3
                else:
                    address_3 = n_3
        elif address_2 == "" and address_3 == "":
            n_1, n_2, n_3 = address_parse(address)
            address_2 = n_2
            address_3 = n_3
    else:
        address_1, address_2, address_3 = address_parse(address)

    return address_1,address_2,address_3




if __name__ == "__main__":
    import sys
    # reload(sys)
    # sys.setdefaultencoding('utf-8')

    table = "11315_company"
    print ('main test')
    #
    # while True:
    #     try:
    #         result = mysqlClient.mysql_find_all(table)
    #         if result:
    #             for line in result:
    #                 company_parse(line)
    #         else:
    #             print("No company to parse!")
    #             time.sleep(60 * 60)
    #     except Exception, e:
    #         print(e.message)

