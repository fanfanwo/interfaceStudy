#!/usr/bin/env python
# -*- coding: utf-8 -*-
import jsonpath
import requests

# DS_055 删除购物车-能删除当前用户对应的购物车数据（单个）
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

# 03 查询购物车
params = {
    "application": "app",
    "application_client_type": "weixin",
    "token": token
}
res  = requests.get(url="http://shop-xo.hctestedu.com/index.php?s=api/cart/index", params=params, json=data)
print(res.text)
id_list = jsonpath.jsonpath(res.json(),'$..id')
id = id_list[0]
print(id)

# 04 删除购物车
data = {
    "id": id
}

params = {
    "application": "app",
    "application_client_type": "weixin",
    "token": token
}
res  = requests.get(url="http://shop-xo.hctestedu.com/index.php?s=api/cart/delete", params=params, json=data)
print(res.text)