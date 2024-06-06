#!/git/ijokerm
# -*- coding: UTF-8 -*-
"""
@Project ：mes-ams 
@File    ：电性能参数按批次号汇总.py
@Author  ：SpringBear
@Date    ：2024/6/6 17:33 
"""
import requests

import app

class TracerCollectCK():
    # 定义初始化方法，实例化之后的对象属性
    def __init__(self):
        self.url = app.base_url + '/datack/get/halm/summary/charts'
        self.data = {
    "sideNo":0,
    "LineNoList":[1,2],
    "tagsContains":[],
    "tagsNotContains":[],
    "comment":"",
    "trackLabel":"",
    "startTime":app.curbegin,
    "endTime":app.curend
}

    def testcode(self):
        return requests.post(self.url,self.data)

