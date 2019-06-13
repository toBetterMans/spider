#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
from requests.packages import urllib3
import logging.config
logging.config.fileConfig("../log_file/req.conf")
logger = logging.getLogger("loggerTxt")
urllib3.disable_warnings()  # 证书验证，如果不加这句话，还会有警告





if __name__ == "__main__":
    tyc = RequestClass()
