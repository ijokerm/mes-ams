"""
员工信息设定
"""

import requests

import app
from data.employeeinfo import list


class EmployeeInfoSet_API():
    # 定义初始化方法，实例化之后的对象属性
    def __init__(self):
        self.list_url = app.base_url + '/listPageAmsEmploye'
        self.add_url = app.base_url + '/addAmsEmploye'
        self.edi_url = app.base_url + '/ediTAmsEmploye'
        self.del_url = app.base_url + '/deleteAmsEmploye'

    def list_api(self):
        return requests.post(url= self.list_url, headers= app.header, json= list.chk_null), requests.post(url= self.list_url, headers= app.header, json= list.chk_employeeNo) \
            , requests.post(url= self.list_url, headers= app.header, json= list.chk_employeeName), requests.post(url= self.list_url, headers= app.header, json= list.chk_two)

    def add_api(self):
        return requests.post(url= self.add_url, headers= app.header,  json= app.employee_add)

    def edi_api(self):
        return requests.post(url= self.edi_url,headers= app.header,  json= app.employee_edi )

    def del_api(self):
        return requests.post(url= self.del_url,headers= app.header,  json= app.employee_del )

if __name__ == '__main__':
    ces1 = EmployeeInfoSet_API()
    w,x,y,z = ces1.list_api()
