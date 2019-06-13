#!/usr/bin/env python  
# -*- encoding: utf-8 -*-  
import requests
from hashlib import md5
""" 
@author: niuweidong 
@software: PyCharm 
@file: ruokuai.py.py 
@time: 2018/08/08 9:42 
"""


class RClient(object):

    def __init__(self, username, password, soft_id, soft_key):
        self.username = username
        self.password = md5(password).hexdigest()
        self.soft_id = soft_id
        self.soft_key = soft_key
        self.base_params = {
            'username': self.username,
            'password': self.password,
            'softid': self.soft_id,
            'softkey': self.soft_key,
        }
        self.headers = {
            'Connection': 'Keep-Alive',
            'Expect': '100-continue',
            'User-Agent': 'ben',
        }

    def rk_create(self, im, im_type=6900, timeout=60):
        """
		软件ID 1
软件key b40ffbee5c1cf4e38028c197eb2fc751
        im: 图片字节
        im_type: 题目类型
		196,148  .   113,134  .  281,97   .  240,136
        """
        params = {
            'typeid': im_type,
            'timeout': timeout,
        }
        params.update(self.base_params)
        files = {'image': ('a.jpg', im)}
        r = requests.post('http://api.ruokuai.com/create.json', data=params, files=files, headers=self.headers)
        return r.json()

    def rk_report_error(self, im_id):
        """
        im_id:报错题目的ID
        """
        params = {
            'id': im_id,
        }
        params.update(self.base_params)
        r = requests.post('http://api.ruokuai.com/reporterror.json', data=params, headers=self.headers)
        return r.json()
