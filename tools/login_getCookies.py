#执行登录并保持，后续请求默认为同一个session会话
import requests
requests.packages.urllib3.disable_warnings()
import json
def login():
   '''登录接口:/auth/wxlogin'''
   cookies={}
   headers={}
   data = json.dumps({"username": "13800000000", "password": "123456"})
   header = {"Content-Type": "application/json; charset=UTF-8"}

   try:
      res1=requests.post(
         url='https://q.test.dos.lixinchuxing.cn/auth/wxlogin',
         data=data,headers=header,verify=False)
      cookies["session"] = res1.cookies["session"]
      print(res1.cookies["csrf-token"])
   except Exception as e:
      print("登录异常".format(e))

   res2=requests.get(url='https://q.test.dos.lixinchuxing.cn/auth/is_qymplogin',cookies=cookies, verify=False)
   cookies["csrf-token"] = res2.cookies["csrf-token"]
   headers["X-CSRF-Token"]=res2.cookies["csrf-token"]
   # headers["Content-Type"]="application/json"
   return cookies,headers

if __name__ == '__main__':
    print(login())