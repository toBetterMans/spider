#!/usr/bin/env python
# -*- coding:utf-8 -*-

from db import MysqlClient as sqlClient

'''
*行政区划到村
* @ date 2016年2月29日
* @ authorwanghaiqi
* @ param
* @ return
'''

villageMap = {}  # 村
townMap = {}  # 镇，办事处
countyMap = {}  # 县，区

countyShortMap = {}  # 县，区简称
townShortMap = {}  # 镇，办事处简称
villageShortMap = {}  # 村简称

regOrgan = ""
companyName = ""
address = ""
'''
* 获取所有的县
* @ date 2016年2月29日
* @ author wanghaiqi
* @ param connurl
* @ param username
* @ param password
* @


return void
'''


def getCountyCode(connurl, username, password):
    sql = "select DISTINCT(countycode),county from areainfo where level='3'"
    # todo
    areaList = sqlClient.mysql_find_by_sql(sql)
    # #print*("【获取所有的县成功】"+sql)
    for maps in areaList:
        maps = dict(maps)
        # 区，县
        countyMap[maps["countycode"]] = maps["county"]
        # #print*("【县全称】" + map.get("county"))
        # 区，县简称
        countyShortMap[maps["countycode"]] = nameFilter(maps["county"])
        # #print*("【县简称】" + nameFilter(map.get("county")))
    # #print*("【获取所有的县失败】" + sql)


'''
*除去区域名里的后缀如 村、 镇 、居委会
* @ date 2016年2月29日
* @ author wanghaiqi
* @ param areaName
* @return
* @ return 
'''


def nameFilter(areaName):
    nameOnly = ""
    areaName = areaName(areaName)
    len = len(areaName)
    if areaName.endsWith("社区居民委员会"):
        return areaName.replace(len - 7, len, "")
    elif areaName.endsWith("居民委员会"):
        return areaName.replace(len - 5, len, "")
    elif areaName.endsWith("社区居委会"):
        return areaName.replace(len - 5, len, "")
    elif areaName.endsWith("管理委员会"):
        return areaName.replace(len - 5, len, "")
    elif areaName.endsWith("村委会"):
        return areaName.replace(len - 3, len, "")
    elif areaName.endsWith("居委会"):
        return areaName.replace(len - 3, len, "")
    elif areaName.endsWith("虚拟社区"):
        return areaName.replace(len - 4, len, "")
    elif areaName.endsWith("社区"):
        return areaName.replace(len - 2, len, "")
    elif areaName.endsWith("镇"):
        return areaName.replace(len - 1, len, "")
    elif areaName.endsWith("乡"):
        return areaName.replace(len - 1, len, "")
    elif areaName.endsWith("街道办事处"):
        return areaName.replace(len - 5, len, "")
    elif areaName.endsWith("办事处"):
        return areaName.replace(len - 3, len, "")
    elif areaName.endsWith("农场"):
        return areaName.replace(len - 2, len, "")
    elif areaName.endsWith("开发区"):
        return areaName.replace(len - 3, len, "")
    elif (areaName.endsWith("园区")):
        return areaName.replace(len - 2, len, "")
    elif areaName.endsWith("区"):
        return areaName.replace(len - 1, len, "")

    elif areaName.endsWith("集"):
        return areaName.replace(len - 1, len, "")
    elif areaName.endsWith("县"):
        return areaName.replace(len - 1, len, "")
    # elif (areaName.endsWith("村"))
    #
    # Buffer areaName=new Buffer(areaName)
    # int len=areaName.length()
    # return areaName.replace(len-1, len, "")
    # nameOnly=areaName
    #
    #
    else:
        return nameOnly


'''
	 * 获取县政府所在镇
	 * @date 2016年2月29日
	 * @author wanghaiqi
	 * @param code
	 * @param connurl
	 * @param username
	 * @param password
	 * @return void
'''


def getGovernmentDataByCode(code, connurl, username, password):
    # TODO给出县政府所在位置列表时实现
    getTownDataByCode(code, connurl, username, password)
    for i in townMap.keys():
        # print*("定位到县政府所在镇")
        return i


'''
 * 获取当前县下的所有镇
 * @date 2016年2月29日
 * @author wanghaiqi
 * @param code
 * @param connurl
 * @param username
 * @param password
 * @return void
'''


def getTownDataByCode(code, connurl, username, password):
    sql = "select * from areainfo where countycode = '" + code + "' and `level`='4'"
    listInfo = sqlClient.mysql_find_by_sql(sql)  # JdbcUtil.query(sql, connurl, username, password)
    # print*("【获取当前县下的所有镇成功】"+sql)
    for maps in listInfo:
        maps = dict(maps)
        townMap[maps["towncode"]] = maps["town"]
        # print*("【镇全称】"+map.get("town"))
        townShortMap[maps["towncode"]] = nameFilter(maps["town"])
    # #print*("【镇简称】"+nameFilter(map.get("town")))
    # #print*("【获取当前县下的所有镇失败】"+sql)


'''
获取当前县下的所有村
@date 2016年2月29日
@author wanghaiqi
@param code
@param connurl
@param username
@param password
@return void
'''


def getVillageDataByCode(code, connurl, username, password):
    sql = "select * from areainfo where countycode = '" + code + "' and `level`='5'"
    listInfo =sqlClient.mysql_find_by_sql(sql) # JdbcUtil.query(sql, connurl, username, password)
    # print*("【获得当前县下的所有村成功】"+sql)
    for maps in listInfo:
        villageMap[maps["villagecode"]] = maps["village"]
        # #print*("【村全称】" + map.get("village"))
        villageShortMap[maps["villagecode"]] = nameFilter(maps["village"])
        # #print*("【村简称】" + nameFilter(map.get("village")))
        # print*("【获得当前县下的所有村失败】" + sql)


'''
 * 获取当前镇下的所有村
	 * @date 2016年2月29日
	 * @author wanghaiqi
	 * @param code
	 * @param connurl
	 * @param username
	 * @param password
	 * @return void
'''


def getVillageDataByTownCode(code, connurl, username, password):
    sql = "select * from areainfo where towncode = '" + code + "' and `level`='5'"
    listInfo = sqlClient.mysql_find_by_sql(sql) # JdbcUtil.query(sql, connurl, username, password)
    # print*("【获得当前镇下的所有村成功 】"+sql)
    for maps in listInfo:
        villageMap[maps["villagecode"]] = maps["village"]
        villageShortMap[maps["villagecode"]] = nameFilter(maps["village"])
        # areaInfo = listInfo.get(0).get("county")
        # print*("【获得当前镇下的所有村失败 】" + sql)


'''
	 * 匹配当前公司所在县
	 * @date 2016年2月29日
	 * @author wanghaiqi
	 * @param address
	 * @param code
	 * @return
	 * @return String
'''


def getCode(companyName, address, regOrgan, code):
    # 判断县全称是否存在于经营地址地中
    addressstr = str(address)
    companyName = str(companyName)
    regOrgan = str(regOrgan)
    for i in countyMap.keys():
        mm = countyMap[i]
        if addressstr and mm in addressstr:
            # addressstr = addressstr.replace(mm, "")
            # companyName = companyName.replace(mm, "")
            # regOrgan = regOrgan.replace(mm, "")
            return str(i)
        # 判断县全称是否存在于公司名字中
        if companyName and mm in companyName:
            # companyName = companyName.replace(mm, "")
            # regOrgan = regOrgan.replace(mm, "")
            return str(i)
        # 判断县全称是否存在工商注册地中
        if mm in regOrgan:
            # regOrgan = regOrgan.replace(mm, "")
            return str(i)

    # 判断县简称是否存在经营地址地中
    for i in countyShortMap.keys():
        mm = countyShortMap[i]
        if addressstr and mm in addressstr:
            return str(i)

        # 判断县简称是否存在公司名字中
        if companyName and mm in companyName:
            return str(i)

        # 判断县的简称是否存在于工商注册地中
        if mm in regOrgan:
            return str(i)
        return code


'''
 * 匹配当前公司所在镇
	 * @date 2016年2月29日
	 * @author wanghaiqi
	 * @param address
	 * @param code
	 * @return
	 * @return String
'''


def spiltTown(regOrgan, companyName, address, code):
    codeTownAndMatchInfo = ""
    if not companyName and not address and not regOrgan:
        return code

    # 通过地址匹配镇
    for i in townMap.keys():
        addinfo = townMap[i]
        if address:
            if addinfo in address:
                address = address.replace(addinfo, "")
                companyName = companyName.replace(addinfo, "")
                regOrgan = regOrgan.replace(addinfo, "")
                ss = str(i) + "," + address if len(address) != 0 else "无"
                return ss

        if companyName:
            # 通过企业名称匹配镇
            if addinfo in companyName:
                companyName = companyName.replace(addinfo, "")
                regOrgan = regOrgan.replace(addinfo, "")
                return str(i) + "," + companyName if len(companyName) != 0 else "无"

        if regOrgan:
            # companyName = companyName.sub(companyName.indexOf(countyInfo) + countyInfo.length(), companyName.length())
            # 通过工商注册地匹配镇
            if addinfo in regOrgan:
                regOrgan = regOrgan.replace(addinfo, "")
                return str(i) + "," + regOrgan if len(regOrgan) != 0 else "无"

    # 通过地址匹配镇
    for i in townShortMap.keys():
        addinfo = townShortMap[i]
        if address:
            if addinfo in address:
                return str(i) + "," + address

        if companyName:
            # 通过企业名称匹配镇
            if addinfo in companyName:
                return str(i) + "," + companyName

        if regOrgan:
            # companyName = companyName.sub(companyName.indexOf(countyInfo) + countyInfo.length(), companyName.length())
            # 通过工商注册地匹配镇
            if addinfo in regOrgan:
                return str(i) + "," + regOrgan
    return code + "," + code


'''
 * 匹配当前公司所在村
	 * @date 2016年2月2日
	 * @author wanghaiqi
	 * @param address
	 * @param code
	 * @return
	 * @return String
'''


def spiltVillage(comOrAdd, code):
    if not comOrAdd:
        return code
    # 通过地址或者公司匹配村全名
    for i in villageMap.keys():
        addinfo = villageMap[i]
        if addinfo in comOrAdd:
            return str(i)
    # 通过地址或者公司匹配村简称
    # 匹配简称存在问题，当村的名字和镇的名字相同时就会定位到此村而不会直接停留在当前镇，这样造成定位到镇成功但是村没有匹配上的这种情况不准确
    for i in villageShortMap.keys():
        addinfo = villageShortMap[i]
        if addinfo in comOrAdd:
            return str(i)
    return code


def matchTownisornotStandard(code, townCode, matchInfo):
    townInfo = townShortMap[townCode]
    if "镇" in matchInfo:
        return townCode
    else:
        # print*(townInfo + ":::" + matchInfo)
        if (matchInfo.find(townInfo) + len(townInfo)) != len(matchInfo) and matchInfo.find(townInfo) != -1:
            matchInfoEnd = matchInfo[
                           matchInfo.find(townInfo) + len(townInfo):matchInfo.find(townInfo) + len(townInfo) + 1]
            if "村" in matchInfoEnd or "居" in matchInfoEnd or "委" in matchInfoEnd or "社" in matchInfoEnd:
                return code

    return townCode


'''
	 * 更新区域代码
	 * @date 2016年2月29日
	 * @author wanghaiqi
	 * @param code
	 * @param tableName
	 * @param connurl
	 * @param username
	 * @param password
	 * @param type
	 * @return void
'''


def updateRecord(code, tableName, connurl, username, password, type):
    sql = "select * from " + tableName + " where code='" + code + "'"
    # print*("【查询出默认县城内的所有企业】" + sql)
    sqlList = []
    # 获取所有的县
    getCountyCode(connurl, username, password)
    dataList = sqlClient.mysql_find_by_sql(sql)  # JdbcUtil.query(sql, connurl, username, password)
    for maps in dataList:
        regOrgan = maps["regOrgan"]
        companyName = maps["companyName"]
        address = maps["address"]
        villageCode = code
        updateSql = ""
        # 获得公司所在县
        newcode = getCode(companyName, address, regOrgan, code)
        # 获得当前县下的所有镇
        getTownDataByCode(newcode, connurl, username, password)
        # 通过企业名称和地址、工商注册地匹配镇
        townCodeAndMatchInfo = spiltTown(regOrgan, companyName, address, code)
        # print*(townCodeAndMatchInfo.to())
        townCode = townCodeAndMatchInfo.split(",")[0]
        matchInfo = townCodeAndMatchInfo.split(",")[1]
        # 判断是否为村镇同名的情况，匹配信息中含有村名而当镇名使用
        if not townCode == matchInfo:
            townCode = matchTownisornotStandard(code, townCode, matchInfo)
        # 标识当前镇为县政府所在镇，不准确
        notCorr = False
        # 判断是否匹配到镇
        if townCode == code:
            # 没有匹配到镇
            # 获取当前县下面的所有村
            getVillageDataByCode(code, connurl, username, password)
            # 判断公司名字匹配村是否成功
            villageCode = spiltVillage(companyName, code)
            if villageCode == code:
                villageCode = spiltVillage(address, code)
            # 判断地址匹配村是否成功
            if villageCode == code:
                # 都不包含村，定位到县政府所在镇
                townCode = getGovernmentDataByCode(code, connurl, username, password)
                notCorr = True
        else:  # 匹配到镇
            # 取出镇下面的所有村
            getVillageDataByTownCode(townCode, connurl, username, password)
            villageCode = spiltVillage(companyName, code)
        if not code == villageCode:  # 匹配到村成功
            updateSql = "update " + tableName + " set code='" + villageCode + "' where id='" + maps.get("id") + "'"
            # print*("【执行匹配结果】"+updateSql+"【匹配到村成功】")
            if type == "0":
                sqlClient.mysql_update_by_sqls(updateSql)# JdbcUtil.executeSql(updateSql, connurl, username, password)
                pass
            elif type == "1":
                sqlList.append(updateSql)
        elif not townCode == code:  # 匹配到村失败，匹配到镇成功
            if notCorr:  # 不准确在sql中增加不准确标识
                # updateSql = "update " + tableName + " set code='" + townCode + "',notcrrsign='1' where id='" + map.get("id")+ "'"
                updateSql = "update " + tableName + " set code='" + townCode + "' where id='" + maps.get("id") + "'"
            else:  # 准确在sql中不加加不准确标识
                updateSql = "update " + tableName + " set code='" + townCode + "' where id='" + maps.get("id") + "'"
            # print*("【执行匹配结果】"+updateSql+"【匹配到镇成功】")
            if type == "0":
                sqlClient.mysql_update_by_sqls(updateSql)  # JdbcUtil.executeSql(updateSql, connurl, username, password);
            elif type == "1":
                sqlList.append(updateSql)
    # print*("【匹配总数】"+sqlList.size())
    if type == "1":
        sqlClient.mysql_update_by_sqls(sqlList)# JdbcUtil.executeSqlList(sqlList, connurl, username, password)
        sqlList=[]


'''
 * 入口方法
	 * @date 2016年2月29日
	 * @author wanghaiqi
	 * @param args
	 * @return void
'''
if __name__ == "__main__":
    # updateRecord(args[0], args[1], args[2], args[3], args[4], "1")
    updateRecord("500237", "etl_company500237", "localhost:3306/info", "root", "root", "1")
