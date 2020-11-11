from tools.http_requests import HttpResuest
import json
from tools.get_data import *
from tools.login_getCookies import login


class Datasource():
    #调用login获取登录后的cookies和headers
    global cookies,headers
    cookies,headers = login()
    def new_clue(self):
        url = 'https://q.test.dos.cheanjia.net/api/v1/used_car/tickets'
        car_num=getattr(GetData,'car_num')
        print(car_num)
        data={"plate_number":car_num,"vin": random_vin(),"jzg_car_model_id": "1261","jzg_car_model_name": "宝马 5系 2005款 3.0L 自动 530Li","license_issued_on":"2019-08-16","owner_name": "接口测试数据","owner_mobile":"13163750276","mileage": "111111","jzg_color_id": "1","transfer_count": "0", "province_code": "440000","province": "广东省","city_code": "440300","city": "深圳市","channel": "1","replace_detail": "1","from_employee_name": "李晓良","from_employee_id": "1817","note": "备注内容","district": "南山区","district_code": "440305" }
        res = HttpResuest.http_request(url,headers=headers, data=data,method="put",cookies=cookies, verify=False)
        res = json.loads(res.text)
        car_id = res["data"]["id"]
        return car_id

    def get_carInfoId(self,car_id):
        url = 'https://q.test.dos.cheanjia.net/api/v1/used_car/ticket/{}/evaluation/car_info'.format(car_id)
        data={"is_from_car_manage": "false"}
        res = HttpResuest.http_request(url, headers=headers, data=data, method="put", cookies=cookies, verify=False)
        res = json.loads(res.text)
        car_info_id = res["data"]["car_info_id"]
        return (car_info_id)

    def pinggu(self,car_id):
        #1.评估车辆信息
        pass




