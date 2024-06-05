"""
配置文件
请求头 信息头 cookie管理
"""
import os
# 项目当前目录 --报告生成路径
base_dir = os.path.dirname(__file__)
#
login_url = "https://www.51tagger.com/maxwell-report/rest/login"

base_url = "https://www.51tagger.com/maxwell-report/maxwell-mes-ams"

# 请求头
header ={
    "Authorization": "bearer eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI0NyIsInN1YiI6Im1lc0FkbWluIiwiaWF0IjoxNjg0MzA2OTc3LCJleHAiOjE2ODQ5MTE3Nzd9.7Sycl1AXOw0H73gkozkvzim53UWpCj0bZV83zFrXdGU"
}

