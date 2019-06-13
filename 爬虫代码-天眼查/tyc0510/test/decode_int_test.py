#!/usr/bin/env python  
# -*- encoding: utf-8 -*-  

""" 
@author: niuweidong 
@software: PyCharm 
@file: decode_int_test.py 
@time: 2019/05/22 11:57 
"""
import json
import re
import time

import requests

from test_abuyun import proxies
# old
_0x4fec = [
    'f9D1x1Z2o1U2f5A1a1P1i7R1u2S1m1F1',
    'o2A1x2F1u5~j1Y2z3!p2~r3G2m8S1c1',
    'i3E5o1~d2!y2H1e2F1b6`g4v7',
    'p1`t7D3x5#w2~l2Z1v4Y1k4M1n1',
    'C2e3P1r7!s6U2n2~p5X1e3#',
    'g4`b6W1x4R1r4#!u5!#D1f2',
    '!z4U1f4`f2R2o3!l4I1v6F1h2F1x2!',
    'b2~u9h2K1l3X2y9#B4t1',
    't5H1s7D1o2#p2#z1Q3v2`j6',
    'r1#u5#f1Z2w7!r7#j3S1']

ne = ['2633141825201321121345332721524273528936811101916293117022304236',
      '1831735156281312241132340102520529171363214283321272634162219930',
      '2332353860219720155312141629130102234183691124281413251227261733',
      '2592811262018293062732141927100364232411333831161535317211222534',
      '9715232833130331019112512913172124126035262343627321642220185148',
      '3316362031032192529235212215274341412306269813312817111724201835',
      '3293412148301016132183119242311021281920736172527353261533526224',
      '3236623313013201625221912357142415851018341117262721294332103928',
      '2619332514511302724163415617234183291312001227928218353622321031',
      '3111952725113022716818421512203433241091723133635282932601432216']
base64chars = "abcdefghijklmnopqrstuvwxyz1234567890-~!"
base66chars="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"


nn = []
def tt(e, t, n):
    
    global nn
    # print(e, t, n, nn)
    if n==[]:
        nn.append([])
    else:
        nn[int(e)].append(str(t))
# new
def get_chars_by_companyId(company_id):
    t_default = ",,06btf2,,0zl5whqisecpmu98y,,1,,118oszunvmb9fd7hcpy203j-ilktq46raw5exg,,,0kjrxn-034d1ao7vg,2s6h0pg3nmyldxeakzuf4rb-7oci8v219q,2wtj5,3x70digacthupf6veq4b5kw9s-jly3onzm21r8,4zj3l1us45gch7ot2ka-exybn8i6qp0drvmwf9,,68q-udk7tz4xfvwp2e9om5g1jin63rlbhycas0,5jhpx3d658ktlzb4nrvymga01c9-27qewusfoi,,,7d49moi5kqncs6bjyxlav3tuh-rz207gp8f1we,87-gx65nuqzwtm0hoypifks9lr12v4e8cbadj3,91t8zofl52yq9pgrxesd4nbuamchj3vi0-w7k6"
    t_defaults = t_default.split(",")
    
    for k in t_defaults:
        t = list(k)
        if len(t) > 0:
            for i in range(1,len(t)):
                tt(t[0], t[i],None)
        else:
            tt(None,None ,[])
    r = str(ord(str(company_id)[0]))
    print(r)
    rs=r[1] if len(r)>1 else r
    rs=int(rs)
    print(rs)
    return nn[rs]

# old
def gen_rsid(tid):
    r = str(ord(tid[0]))
    r = r[1] if len(r) > 1 else r
    i = ne[int(r)]
    u = 0
    o = _0x4fec[int(r)]
    
    a = []
    s = 0
    while u < len(o):
        if not ("`" != o[u] and "!" != o[u] and "~" != o[u]  ):
            a.append(i[s:(s + 1)])
            s += 1
        
        if "#" == o[u]:
            a.append(i[s:(s + 1)])
            a.append(i[(s + 1):(s + 3)])
            a.append(i[(s + 3):(s + 4)])
            s += 4
        
        if 96 < ord(o[u]) < 123:
            l = int(o[u + 1])
            c = 0
            while c < l:
                a.append(i[s:(s + 2)])
                s += 2
                c += 1
        
        if 64 < ord(o[u]) < 91:
            l = int(o[u + 1])
            c = 0
            while c < l:
                a.append(i[s:(s + 1)])
                s += 1
                c += 1
        u += 1
    return a

def gen_ucourt(key, fnStr):
    """生成Cookie中的_ucourt"""
    key = str(key)
    rsid = gen_rsid(key)
    i = 0
    chars = ''
    while i < len(rsid):
        chars += base64chars[int(rsid[i])]
        i += 1
    print(chars)
    print(fnStr)
    m = re.search("wtf=function\(\)\{return'(.*?)'\}\}\(window\)", fnStr, re.S)
    if not m:
        raise RuntimeError("未匹配上_ucourt")
    fxck = m.group(1).split(",")
    
    fxckStr = ''
    i = 0
    gen_chars=get_chars_by_companyId(key)
    while i < len(fxck):
        fxckStr += gen_chars[int(fxck[i])]
        i += 1
    print(fxckStr)
    return fxckStr

def get_cookie_by_request(company_id, url, re_key, json_obj_list):
    cookie_header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
    }
    graph_con = requests.get(url, headers=cookie_header, proxies=proxies)
    json_obj = json.loads(graph_con.text)
    fnStr = ''
    for item in eval(json_obj_list).split(","):
        fnStr += chr(int(item))
    print(fnStr)
    token = re.search(r'{}=(.*?);'.format(re_key), fnStr, re.S).groups()[0]
    # ps.tyc.set_cookies({'rtoken':rtoken})
    _u = gen_ucourt(company_id, fnStr)
    
    return [token, _u]


# def test(t=''):
#     a = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
#     e = [0, 2, 1][len(t) % 3],
#     i = t[0] << 16 | (t[1] if len(t)> 1 else 0) << 8 | (t[2] if len(t)> 2 else 0)
#     return "" + a[i >>> 18] + a[i >>> 12 & 63] + (e >= 2 if "=" else a[i >>> 6 & 63]) + ( "=" if e >=1 else a[63 & i])

if __name__ == "__main__":
    
    # company_id='24416401'
    # equal_cookie_url = 'https://capi.tianyancha.com/cloud-equity-provider/v4/qq/name.json?id={id}?random={tim}'.format(
    #     id=company_id, tim=str(int(time.time() * 1000)))
    #
    # graph_url='https://dis.tianyancha.com/qq/{id}.json?random={tim}'.format(
    #                             id=company_id,tim=str(int(time.time() * 1000)))
    # josn_list='json_obj["data"]["v"]'
    # ss=get_cookie_by_request(company_id,graph_url,'rtoken',josn_list)
    # print(ss)
    
    lll='33,102,117,110,99,116,105,111,110,40,110,41,123,100,111,99,117,109,101,110,116,46,99,111,111,107,105,101,61,39,114,116,111,107,101,110,61,56,99,99,100,53,100,57,56,97,99,99,57,52,51,48,102,57,50,55,102,98,98,99,52,97,53,100,56,55,101,50,101,59,112,97,116,104,61,47,59,39,59,110,46,119,116,102,61,102,117,110,99,116,105,111,110,40,41,123,114,101,116,117,114,110,39,56,44,49,52,44,50,50,44,52,44,50,51,44,50,50,44,49,51,44,50,50,44,50,51,44,50,53,44,49,52,44,56,44,49,52,44,53,44,51,48,44,50,52,44,50,49,44,51,52,44,51,48,44,50,52,44,50,49,44,49,51,44,50,49,44,56,44,50,49,44,55,44,51,52,44,51,52,44,50,50,44,53,44,56,44,50,53,39,125,125,40,119,105,110,100,111,119,41,59'
    # rtoken=8ccd5d98acc9430f927fbbc4a5d87e2e
    # 	_rutm=840310b019484decafecaba8a5ff0d89

    lll='33,102,117,110,99,116,105,111,110,40,110,41,123,100,111,99,117,109,101,110,116,46,99,111,111,107,105,101,61,39,99,108,111,117,100,95,116,111,107,101,110,61,52,100,49,56,49,57,55,97,100,48,101,50,52,98,100,48,56,97,50,57,54,49,101,48,56,57,56,53,99,99,49,97,59,112,97,116,104,61,47,59,100,111,109,97,105,110,61,46,116,105,97,110,121,97,110,99,104,97,46,99,111,109,59,39,59,110,46,119,116,102,61,102,117,110,99,116,105,111,110,40,41,123,114,101,116,117,114,110,39,50,49,44,49,52,44,50,49,44,49,51,44,50,50,44,50,52,44,50,55,44,50,55,44,50,55,44,49,52,44,49,52,44,50,50,44,49,52,44,51,52,44,49,51,44,55,44,50,53,44,53,44,52,44,50,53,44,54,44,51,48,44,50,56,44,50,50,44,50,49,44,51,52,44,54,44,56,44,50,51,44,50,51,44,50,49,44,49,51,39,125,125,40,119,105,110,100,111,119,41,59'
    # cloud_token=4d18197ad0e24bd08a2961e08985cc1a;
    # cloud_utm=  a4ab0c2224404fb59d396e70af6811ab
    
    lls='33,102,117,110,99,116,105,111,110,40,110,41,123,100,111,99,117,109,101,110,116,46,99,111,111,107,105,101,61,39,116,111,107,101,110,61,49,51,100,48,101,49,101,54,55,102,97,54,52,57,99,57,97,56,57,53,52,51,99,52,102,57,55,99,48,50,99,97,59,112,97,116,104,61,47,59,39,59,110,46,119,116,102,61,102,117,110,99,116,105,111,110,40,41,123,114,101,116,117,114,110,39,50,56,44,49,50,44,49,49,44,50,48,44,50,57,44,57,44,49,51,44,51,49,44,57,44,49,44,51,52,44,51,49,44,50,56,44,51,52,44,49,53,44,57,44,49,44,51,52,44,48,44,49,44,50,48,44,50,48,44,49,51,44,49,51,44,51,51,44,48,44,57,44,51,52,44,57,44,48,44,49,49,44,51,51,39,125,125,40,119,105,110,100,111,119,41,59'
    strs=''
    for i in lls.split(','):
        strs+=chr(int(i))
    print(strs)
    print(gen_ucourt('1205478280',strs))

    # print(get_chars_by_companyId(7957194))  24131717107@qq.com

# c1642c66b45244e682ad9180f9a2ad35
# 5c4776ba59f04e5c8c6f878cab8e76a4
# c1642c66b45244e682ad9180f9a2ad35
# 5c4776ba59f04e5c8c6f878cab8e76a4
'''
Host: dis.tianyancha.com
Connection: keep-alive
Accept: application/json, text/plain, */*
DNT: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36
Referer: https://dis.tianyancha.com/dis/old
Accept-Language: zh-CN,zh;q=0.9
Cookie: ssuid=7685102350; RTYCID=780d591bf6664dca97d68ea5ccaa377a;rtoken=126133aa61544b5fa58205b7661380f2; _rutm=d5f8ffa898644d63bcc451d6a496ed40
Accept-Encoding: gzip, deflate



'''
