#!/git/ijokerm
# -*- coding: UTF-8 -*-
"""
@Project ：mes-ams 
@File    ：电性能参数按批次号汇总.py
@Author  ：SpringBear
@Date    ：2024/6/6 17:33 
"""
import requests
import csv
import app


class TracerCollectCK():
    # 定义初始化方法，实例化之后的对象属性
    def __init__(self):

        self.session = requests.Session()
        self.token = "Bearer" + ' ' + app.token
        self.hearder = self.session.headers.update({"Authorization": self.token})


    def testcode(self):
        with open('../data/path.csv', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for i in reader:
                url = i[0]
                return app.base_url + url




    def testtime(self):
        url =app.base_url + '/datack/ng/list'
        payload = {"tagsContains":[],
                    "tagsNotContains":[],
                    "process":"10000",
                    "materialBatchNo":"",
                    "direction":"front",
                    "monitorType":"aoi",
                    "sideNo":0,
                    "trackNo":"",
                    "filter":"none",
                    "cutLineNoList":[],
                    "guideLineNoList":[],
                    "getteringLineNoList":[],
                    "texturingLineNoList":[],
                    "startTestTime":app.curbegin,
                    "endTestTime":app.curend
                   }
        return requests.post(url,json= payload,cookies = app.cookies)

if __name__ == '__main__':
    ces1 = TracerCollectCK()
    res = ces1.testcode()
    print(res)