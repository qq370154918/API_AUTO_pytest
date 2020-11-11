# -*- coding: utf-8 -*-
# @Time     : 2020/5/29 13:45
# @Author   : liang
# @File     : freestyle_thread.py
# @Software : PyCharm
import sys
import os
import multiprocessing
import threading
from threading import Thread
from queue import PriorityQueue
from tools.my_log import MyLog
from tools.get_path import *
import time

# try:
#     if sys.argv[1] == '-f':
#         ALLURE_DIR = '${WORKSPACE}/allure-results$BUILD_TIMESTAMP'
#         case_logger.info(f"allure报告依赖文件存储路径：{ALLURE_DIR}")
# except IndexError as e:
#     case_logger.info(f"allure报告依赖文件存储路径：{ALLURE_DIR}")


# try:
#     if sys.argv[2]:
#         threading_num = int(sys.argv[2])
#         MyLog.info(f"当前执行的线程数：{threading_num}")
# except IndexError as e:
#     threading_num = 6
#     MyLog.info(f"未设置线程数，默认为： {threading_num}")


def get_testpkg_path(dir_path):
    """返回TestCase目录下的所有testpkg目录"""
    init_testpkg_list = os.listdir(dir_path)

    testpkg_list = []
    for path in init_testpkg_list:
        if path.endswith(".py") or path.startswith(".") or path.startswith("__") or path.endswith("ini"):
            pass
        else:
            """找到文件夹目录"""
            testpkg_path = os.path.join(dir_path, path)
            testpkg_list.append(testpkg_path)

    return testpkg_list



def get_test_file(dir_path):
    '''获取目录下的所有测试用例py文件'''
    for root, dirs, files in os.walk(dir_path):
        filelist=[]
        for one_dir in dirs:
            filelist.append(os.path.join(root, one_dir))
        for one_file in files:
            filelist.append(os.path.join(root, one_file))
        print(filelist)
        test_files = []
        for file in list(filelist):
            file_name=os.path.split(file)[1]
            if file_name.endswith(".py") and file_name.startswith("test_"):
                test_files.append(file)
        return test_files




def worker(queue):
    if not queue.empty():
        timenow = time.strftime("%Y-%m-%d_%H%M", time.localtime())
        # os.system(f"pytest -sv {queue.get()[1]} --reruns 3 --color=no"
        #           f"--html={os.path.join(REPORTS_DIR, 'report.html')}")
        os.system(f"pytest -sv {queue.get()[1]} --html=Out_Puts/html_report/report{timenow}.html --alluredir=./allure-results")



class PyThread(Thread):

    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        while not self.queue.empty():
            worker(self.queue)


def main(queue):
    threading_num = 6
    t_obj_li = [PyThread(queue) for _ in range(threading_num)]
    for m in t_obj_li:
        m.start()

    print("The number of thread is:", threading.active_count())
    MyLog().info("The number of thread is:" + str(threading.active_count()))
    for n in t_obj_li:
        n.join()


if __name__ == '__main__':
    print("The number of CPU is:", multiprocessing.cpu_count())
    MyLog().info("The number of CPU is:" + str(multiprocessing.cpu_count()))

    pq = PriorityQueue()

    for i, j in enumerate(get_test_file(testcase_dir)):
        pq.put((i, j))
    main(queue=pq)


