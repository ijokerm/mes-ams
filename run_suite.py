""" 批量执行测试用例
1、导包
2、创建测试套件对象
3、添加测试用例到套件
4、批量执行测试用例
"""
import unittest

import app
from script.test_EmployeeInfoSet import TestEmployeeInfoSet

from unittestreport import TestRunner
suite = unittest.TestSuite()

suite.addTest(unittest.makeSuite(TestEmployeeInfoSet))

# runner = unittest.TextTestRunner()  # 实例化执行器对象
# runner.run(suite)

# 5.生成测试报告
# 5.1定义测试报告文件
rep_file = app.base_dir + '/report/test00.html'
# 5.2创建第三方执行器对象
runner = TestRunner(suite,      # 测试套件对象
                    filename=rep_file, # 测试报告文件
                    title="测试框架是否可行",
                    tester="春天的熊",
                    desc="V1.0",
                    templates=1)  # 报告的模板

runner.run()

# 5.3执行器调用run方法执行生成测试报告