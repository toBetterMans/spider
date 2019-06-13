#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import logging

from flask import Flask, request, jsonify
from gevent import pywsgi
from gevent import monkey
from get_company import ReqCompany
import json

""" 
@author: niuweidong 
@software: PyCharm 
@file: input_port.py 
@time: 2018/09/10 9:48 
"""

logging.config.fileConfig("../log_file/online.conf")
logger = logging.getLogger("loggerTxt")
monkey.patch_all()
app = Flask(__name__)


@app.route('/company', methods=['post'])
def get_company():
    ss = request.form
    # ss = request.get_data()
    # print(ss)
    logger.info('收到请求：{}'.format(ss))
    companyName = ss['ENTINFO'].encode('utf8')
    type=ss['TYPE']
    # print('ss={}'.format(ss))
    # print('companyName={}'.format(companyName))
    result_dic = {}
    result_dic['RESULT'] = '0'
    result_dic['DATA'] = {}

    try:
        mm = {}
        r = ReqCompany(type)
        mm = r.get_company_list(companyName.encode('utf8'))
        # print(mm)
        print(".........................................................")
        result_dic['DATA'] = r.result_dicts
        return jsonify(result_dic)
    except Exception as e:
        app.logger.exception(e)
        result_dic['RESULT'] = '1'
    logger.info('返回处理结果：{}'.format(result_dic))
    return jsonify(result_dic)
    # ss='123456789'
    # ss=ss[0:-4]
    # print(len('3777-67-67'))
    # return 'hello world'+ss


if __name__ == "__main__":
    app.config['JSON_AS_ASCII'] = False
    # app.run()
    http_server = pywsgi.WSGIServer(('', 5000), app)
    http_server.serve_forever()
