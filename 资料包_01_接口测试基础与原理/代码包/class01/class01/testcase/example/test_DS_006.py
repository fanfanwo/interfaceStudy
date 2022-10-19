#!/usr/bin/env python
# -*- coding: utf-8 -*-
import jsonpath
import requests

# DS_006 商品详情-验证输入的参数非整数提示用户
# 01 执行登陆获取token
data = {
    "accounts": "zz",
    "pwd": "123456",
    "type": "username"
}

params = {
    "application": "app",
    "application_client_type": "weixin",
}
r1 = requests.post(url="http://shop-xo.hctestedu.com/index.php?s=api/user/login", params=params, json=data)
token_list = jsonpath.jsonpath(r1.json(),'$..token')
token = token_list[0]
print(token)

# 02 查询商品详情，传非整数
data = {
    "goods_id": "啊啊"
}
params = {
    "application": "app",
    "application_client_type": "weixin",
    "token": token
}

res = requests.post(url="http://shop-xo.hctestedu.com/index.php?s=api/goods/detail", params=params, json=data)
print(res.text)