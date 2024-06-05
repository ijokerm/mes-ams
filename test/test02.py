#!/git/ijokerm
# -*- coding: UTF-8 -*-
"""
@Project ：mes-ams 
@File    ：test02.py
@Author  ：SpringBear
@Date    ：2024/6/5 16:00 
"""
from clickhouse_driver import Client

client = Client(host = '139.9.122.128',port = '9000',user = 'ckSpcUser'
                ,password = '22Honw8fevst',database ='maxwell_mes')
query = 'select wafer_id  from maxwell_mes.measure_his_wafer_printing_el_pl limit 2'
result = client.execute(query)
for row in result:
    print(row)