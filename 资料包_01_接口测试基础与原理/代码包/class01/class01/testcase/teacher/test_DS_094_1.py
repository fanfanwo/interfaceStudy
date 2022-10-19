#!/usr/bin/env python
# -*- coding: utf-8 -*-
import jsonpath
import requests

# DS_094 提交订单-【线下支付】验证能正确的下单个商品 (不添加购物车，直接购买提交订单)
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

# 02 不添加购物车，直接购买
data = {
    "buy_type": "goods", # 类型（cart购物车、goods直接购买），不需要添加购物车
    "goods_id": "10",
    "stock": "1",
    "spec": [],
    "address_id": 921,
    "payment_id": "2",
    "site_model": 0,
    "is_points": 0,
    "user_note": ""
}
params = {
    "application": "app",
    "application_client_type": "weixin",
    "token": token
}

res  =requests.post(url="http://shop-xo.hctestedu.com/index.php?s=api/buy/add", params=params, json=data)
print(res.json())