#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 导入第三库
import jsonpath
import requests

# 01 DS_022 登陆-使用用户名能正确的登录用户
data = {
    "accounts": "zz",
    "pwd": "123456",
    "type": "username"
}

# app才会返回token
# r1 = request(method="post", url="http://shop-xo.hctestedu.com/index.php?s=api/user/login", json=data)
# r1 = request(method="post", url="http://shop-xo.hctestedu.com/index.php?s=api/user/login&application=web&application_client_type=pc", json=data)
# r1 = request(method="post", url="http://shop-xo.hctestedu.com/index.php?s=api/user/login&application=app&application_client_type=weixin", json=data)
params = {
    "application": "app",
    "application_client_type": "weixin",
}
r1 = requests.post(url="http://shop-xo.hctestedu.com/index.php?s=api/user/login", params=params, json=data)
print(r1.status_code)
print(r1.text)
print(r1.request.path_url)
token_list = jsonpath.jsonpath(r1.json(),'$..token')
token = token_list[0]
print(token)

