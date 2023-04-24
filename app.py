"""
配置文件
"""
import os
# 项目当前目录 --报告生成路径
base_dir = os.path.dirname(__file__)
# 暂时不用 不需要验证登录生成的token
login_url = "https://www.51tagger.com/maxwell-report/rest/login"

base_url = "https://www.51tagger.com/maxwell-report/maxwell-mes-ams"

header = {"Authorization": "bearer eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI0NyIsInN1YiI6Im1lc0FkbWluIiwiaWF0IjoxNjgyMTMyMTYzLCJleHAiOjE2ODI3MzY5NjN9.s9ZH2dUPEoxUJ1ZfC2ct9n0BrJQfBpG75osHeK0H5fA"}

chk_null = {"employeeNo":"","employeeName":"","pageNo":1,"pageSize":10,"beginTime":"","endTime":""}
chk_employeeNo = {"employeeNo":"006","employeeName":"","pageNo":1,"pageSize":10,"beginTime":"","endTime":""}
chk_employeeName = {"employeeNo":"","employeeName":"生产部","pageNo":1,"pageSize":10,"beginTime":"","endTime":""}
chk_two = {"employeeNo":"004","employeeName":"甜","pageNo":1,"pageSize":10,"beginTime":"","endTime":""}


add_NoNull = {"createTime":"2023-04-22 16:34:11","createUser":"mesAdmin","departmentId":"","ding":"","email":"","employeeName":"春天的熊","employeeNo":"212","esuperior":"","mobile":"","updateTime":"","updateUser":"","wechat":""}


employee_edi = {
        "alarmGroupDsc":"",
        "sysId":"",
        "pageNo":3,
        "pageSize":10
        }

employee_del = {
        "alarmGroupDsc":"",
        "sysId":"",
        "pageNo":3,
        "pageSize":10
        }