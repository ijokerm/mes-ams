"""登录"""

import requests

import app

new_url = app.base_url + '/listPageAmsEmploye'

data = {"username": "mesAdmin",
    "password": "mesAdmin68"}
res0 = requests.post(url= app.login_url,json=data)
response = res0.json()

print(response)