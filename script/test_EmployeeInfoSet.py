"""
测试员工信息设定-增删改查
定义测试类，初始化已封装的测试接口
添加测试用例
"""
import logging
import unittest

import app
from api.EmployeeInfoSet import EmployeeInfoSet_API

class TestEmployeeInfoSet(unittest.TestCase):
    # 初始化方法
    @classmethod
    def setUp(cls) -> None:
        cls.empinfo_api = EmployeeInfoSet_API()

    # 查询（正常参数）
    def test01_list_A001(self):
        # 发送请求
        resNull,resNo,resName,resTwo = self.empinfo_api.list_api()
        resNull_json_data = resNull.json()
        resNo_json_data = resNo.json()
        resName_json_data = resName.json()
        resTwo_json_data = resTwo.json()
        # 记录日志
        logging.info(f"查询条件为员工编号，员工信息查询的结果为：{resNo_json_data}") # 记录测试日志
        logging.info(f"查询条件为员工名称，员工信息查询的结果为：{resName_json_data}")
        # 结果断言 --查询条件为空
        self.assertEqual(200, resNull.status_code)  # 验证状态码
        self.assertEqual(34, resNull_json_data['total'])  # 验证状态码
        # 结果断言 --查询条件为员工编号
        self.assertEqual(200,resNo.status_code)  # 验证状态码
        self.assertEqual(1,resNo_json_data['total'])
        self.assertEqual('006', resNo_json_data['list'][0]['employeeNo'])
        self.assertEqual('甜2', resNo_json_data['list'][0]['employeeName'])
        # 结果断言 --查询条件为员工名称
        self.assertEqual(200, resName.status_code)  # 验证状态码
        self.assertEqual([], resName_json_data['list'])
        self.assertEqual(0, resName_json_data['total'])
        # 结果断言 --查询条件为员工编号+名称
        self.assertEqual(200, resTwo.status_code)
        self.assertEqual(1, resTwo_json_data['total'])
        self.assertEqual('004', resTwo_json_data['list'][0]['employeeNo'])
        self.assertEqual('甜', resTwo_json_data['list'][0]['employeeName'])

    def test02_list2_A002(self):
        gtr = self.empinfo_api.list_api()
        res = gtr.json()
        # 记录日志
        logging.info(f"查询条件为员工编号，员工信息查询的结果为：{resNo_json_data}")  # 记录测试日志

    def test03_list2_A003(self):
        # 发送结果 + 结果断言
        pass

    def test04_list2_A004(self):
        # 发送结果 + 结果断言
        pass

    def test05_list2_A005(self):
        # 发送结果 + 结果断言
        pass