"""
配置文件
请求头 信息头 cookie管理
"""
import os
import requests
import json
# 项目当前目录 --报告生成路径
base_dir = os.path.dirname(__file__)
#
login_url = 'https://www.51tagger.com/maxwell-report/rest/login'
header ={   "Content-Type": "application/json;charset=UTF-8",
            "Authorization": "bearer eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI2MyIsInN1YiI6ImNrYWRtaW4iLCJpYXQiOjE3MTc2NTczOTUsImV4cCI6MTcxODI2MjE5NX0.TH1aGC1WzncysLxjrwnzMf961UKjexJ4kK3zgcI_WNI"
          }
base_url = "https://www.51tagger.com/maxwell-report/"

userpwd = {"username":"ckadmin","password":"401155"}
res = requests.post(login_url,headers=header,json=userpwd)
token = res.json()['token']

time_url = 'https://www.51tagger.com/maxwell-report/data-api/1/picker-options'
curbegin = requests.get(time_url).json()[3]['begin']
curend = requests.get(time_url).json()[3]['end']
print(curbegin)
