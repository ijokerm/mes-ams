#!/git/ijokerm
# -*- coding: UTF-8 -*-
"""
@Project ：mes-ams 
@File    ：testcase.py
@Author  ：SpringBear
@Date    ：2024/6/11 16:45 
"""
import unittest
import requests
from data.excel_handler import ExcelHandle
import ddt
import app
import json
@ddt.ddt
class TestLogin(unittest.TestCase):
    # 读取excel中的数据
    excel = ExcelHandle('../data/testcase.xlsx')
    case_data = excel.read_excel('p1')
    # print(case_data)

    @ddt.data(*case_data)
    def test_login_success(self,items):
        # 请求接口
        res = requests.post(items['url'],data=items['payload'],cookies = app.cookies)
        print(dict(items['payload']))


# if __name__ == '__main__':
#     unittest.main()


