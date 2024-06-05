#!/git/ijokerm
# -*- coding: UTF-8 -*-
"""
@Project ：mes-ams 
@File    ：test01.py
@Author  ：SpringBear
@Date    ：2024/6/5 13:49 
"""

from clickhouse_driver import Client


# from clickhouse_driver import connect

# 基于Clickhouse数据库基础数据对象类
class DB_Obj(object):

    def __init__(self, db_name):
        self.db_name = db_name
        host = '139.9.122.128'  # 服务器地址
        port = '9000'  # '8123' #端口
        user = 'ckSpcUser'  # 用户名
        password = '22Honw8fevst'  # 密码
        database = db_name  # 数据库
        send_receive_timeout = 25  # 超时时间
        self.client = Client(host=host, port=port, database=database)


if __name__ == '__main__':
    db_obj = DB_Obj('maxwell_mes')
    query = 'select wafer_id  from maxwell_mes.measure_his_wafer_printing_el_pl'



