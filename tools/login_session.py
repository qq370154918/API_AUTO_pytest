# -*- coding: utf-8 -*-
# @Time : 2020/11/6 11:12
# @Author : liang
# @Site : 
# @File : login_session.py
# @Software: PyCharm

import requests
requests.packages.urllib3.disable_warnings()   #忽略警告

def login():
    s = requests.session()  # 实例化会话对象
    loginUrl = "https://q.test.dos.lixinchuxing.cn/auth/wxlogin"
    data = {"username": "13800000000", "password": "123456"}
    header = {"Content-Type": "application/json; charset=UTF-8"}
    try:
        res = s.post(
            url=loginUrl,
            json=data,
            headers=header, verify=False)
        print(res.text)
        print(res.cookies)
        # 后续接口请求在header中要增加"X-CSRF-Token"属性，值为登录请求获取到的csrf-token值
        token = res.cookies["csrf-token"]
        s.headers.update = ({"X-CSRF-Token":token})
        #返回登录处理后的session对象
        return s
    except Exception as e:
        print("登录异常".format(e))
