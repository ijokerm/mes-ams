#!/git/ijokerm
# -*- coding: UTF-8 -*-
"""
@Project ：mes-ams 
@File    ：test1.py
@Author  ：SpringBear
@Date    ：2024/6/26 15:33 
"""
import openpyxl

class ExcelHandle:
    def __init__(self,file):
        self.file = file

    def open_excel(self,sheet_name):
        """ 打开Excel，获取sheet"""
        wb = openpyxl.load_workbook(self.file)
        sheet = wb[sheet_name]
        return sheet

    def get_header(self,sheet_name):
        """ 获取表头 """
        wb = self.open_excel(sheet_name)
        header = []
        # 遍历第一行
        for i in wb[2]:
            # 将遍历出来的表头字段加入列表
            header.append(i.value)
        return header



if __name__ == "__main__":
    # 以下为测试代码
    excel = ExcelHandle('../data/testcase.xlsx')
    data = excel.get_header('p1')
    print(data[5])
