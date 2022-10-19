#!/usr/bin/env python
# -*- coding: utf-8 -*-
import jsonpath
import requests

# DS_026 验证用户名为空提示用户
data = {
    "accounts": "",
    "pwd": "123456",
    "type": "username"
}
res = requests.post(url="http://shop-xo.hctestedu.com/index.php?s=api/user/reg", json=data)
print(res.text)