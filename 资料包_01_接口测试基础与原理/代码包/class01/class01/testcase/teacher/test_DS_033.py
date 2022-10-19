#!/usr/bin/env python
# -*- coding: utf-8 -*-
import jsonpath
import requests

# DS_033 加入购物车-验证无规格值可以加入到对应商品
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

# 02 加入购物车
data = {
    "goods_id":"10",
    "spec": "",
    "stock": 1
}

params = {
    "application": "app",
    "application_client_type": "weixin",
    "token": token
}

res  =requests.post(url="http://shop-xo.hctestedu.com/index.php?s=api/cart/save", params=params, json=data)
print(res.json())