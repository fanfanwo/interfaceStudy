#!/usr/bin/env python
# -*- coding: utf-8 -*-
import jsonpath
import requests


# DS_144 取消订单-验证待支付的状态能正确取消-字符串
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

# 03 查询购物车
params = {
    "application": "app",
    "application_client_type": "weixin",
    "token": token
}
res  = requests.get(url="http://shop-xo.hctestedu.com/index.php?s=api/cart/index", params=params, json=data)
print(res.text)
# 获取购物车id
cartid_list = jsonpath.jsonpath(res.json(),'$..id')
cartid = cartid_list[0]
print(cartid)

# 04 提交订单
data = {
    "goods_id": 10,
    "buy_type": "cart",
    "stock": 1,
    "spec": "",
    "ids": cartid,
    "address_id": 921,
    "payment_id": 4,
    "user_note": "",
    "site_model": 0
}
params = {
    "application": "app",
    "application_client_type": "weixin",
    "token": token
}
res  =requests.post(url="http://shop-xo.hctestedu.com/index.php?s=api/buy/add",
                    params=params, json=data)
print(res.text)
# 获取订单id
orderid_list = jsonpath.jsonpath(res.json(),'$..order_ids')
orderid = orderid_list[0][0]
print(orderid)

# 05 取消订单
data = {
    "id": f"{orderid}"
}
params = {
    "application": "app",
    "application_client_type": "weixin",
    "token": token
}
res = requests.post(url="http://shop-xo.hctestedu.com/index.php?s=api/order/cancel",
                    params=params, json=data)
print(res.text)
