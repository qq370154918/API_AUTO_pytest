# -*- coding: utf-8 -*-
# @Time : 2020/11/9 18:19
# @Author : liang
# @Site : 
# @File : do_excel_pandas.py
# @Software: PyCharm
import pandas as pd
from tools.get_path import *

class DoExcle:
    def __init__(self,filename):
        self.filename=filename
    def get_data(self):
        df = pd.read_excel(self.filename)
        test_data = []
        # 获取表头
        keys = df.columns.values
        for i in df.index.values:  # 获取行号的索引，并对其进行遍历：
            # 根据i来获取每一行指定的数据 并利用to_dict转成字典,# loc为按列名索引 iloc 为按位置索引，使用的是 [[行号], [列名]]
            row_data = df.loc[i, keys].to_dict()
            # 将每一行转换成字典后添加到列表
            test_data.append(row_data)
        return test_data

if __name__ == '__main__':
    print(DoExcle(test_add_path).get_data())