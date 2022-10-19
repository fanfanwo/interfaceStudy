#!/usr/bin/env python
# -*- coding: utf-8 -*-
import jsonpath
import requests

#DS_022 登陆-使用用户名能正确的登录用户
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
print(r1.status_code)
print(r1.text)
