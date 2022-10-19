#!/usr/bin/env python
# -*- coding: utf-8 -*-
import jsonpath
import requests

# DS_010 用户名为不超过7位，注册成功
data = {
    "accounts": "JOJO001",
    "pwd": "123456",
    "type": "username"
}
res = requests.post(url="http://shop-xo.hctestedu.com/index.php?s=api/user/reg", json=data)
print(res.text)