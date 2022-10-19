#!/usr/bin/env python
# -*- coding: utf-8 -*-
import jsonpath
import requests

# DS_135 订单详情-验证可以查看对应订单的详细信息
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
res = requests.post(url="http://shop-xo.hctestedu.com/index.php?s=api/user/login", params=params, json=data)
token_list = jsonpath.jsonpath(res.json(),'$..token')
token = token_list[0]
print(token)

# 03 查看当前用户所有的订单信息
params = {
    "application": "app",
    "application_client_type": "weixin",
    "token": token
}
res  =requests.post(url="http://shop-xo.hctestedu.com/index.php?s=api/order/index", params=params, json=data)
orderid_list = jsonpath.jsonpath(res.json(),'$..id')
orderid = orderid_list[0]
print(orderid)

# 03 查看订单详情
data = {
    "id": orderid
}
params = {
    "application": "app",
    "application_client_type": "weixin",
    "token": token
}
res = requests.post(url="http://shop-xo.hctestedu.com/index.php?s=api/order/detail", params=params, json=data)
print(res.text)