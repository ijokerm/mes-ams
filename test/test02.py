#!/git/ijokerm
# -*- coding: UTF-8 -*-
"""
@Project ：mes-ams 
@File    ：test02.py
@Author  ：SpringBear
@Date    ：2024/6/5 16:00 
"""
import app
from clickhouse_driver import Client
import json
import re
client = Client(host = '192.168.22.97',port = '9000',user = 'maxwell'
                ,password = '22Honw8fevst',database ='maxwell_mes')

starttime = app.curbegin
endtime = app.curend


query = "select printing_iv_line_no ,printing_iv_side_no ,printing_iv_comment ,count(1),"\
        "avg(printing_iv_eta) from measure_his_wafer_printing_iv "\
        " where printing_iv_test_time >= %(starttime)s  and printing_iv_line_no = 1 " \
        "group by printing_iv_line_no ,printing_iv_side_no ,printing_iv_comment order by printing_iv_side_no "

params = {'starttime' : starttime}

result = client.execute(query,params)
for i in result:
    print(i)

client.disconnect()


p1 = {"lineNo":0,"direction":"front","sideNo":0,"increment":10,"batchNoList":[],"process":40000,"monitorType":"aoi","startTestTime":"2024-06-25 07:30:00","endTestTime":"2024-06-26 07:30:00"}


j1 = json.dumps(p1)

pattern = re.compile(r',')
# 这一行，将逗号后面换行
res = pattern.sub(',\n',j1)
# 这一行，unicode编码转换为中文，防止中文输出byte格式
res2 = res.encode().decode("unicode_escape")
# print(res2)
