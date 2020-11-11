# -*- coding: utf-8 -*-
# @Time : 2020/11/6 17:13
# @Author : liang
# @Site : 
# @File : test_add.py
# @Software: PyCharm

import pytest
from tools.http_requests import HttpResuest
from tools.do_excel_pandas import DoExcle
from tools.get_path import *
from tools.login_getCookies import login
from tools.get_data import GetData
from tools.my_log import MyLog
from ddt import ddt,data
import json
test_data=DoExcle(test_add_path).get_data()

class TestAdd():

    @pytest.mark.parametrize('item', (test_data))
    def test_add(self,item):
        print(item)
        print("用例名称：{}".format(item["title"]))
        sum=int(item['a'])+int(item['b'])
        print(sum)
        my_except = int(item['c'])
        print(my_except)
        assert sum == my_except

