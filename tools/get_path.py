import os
#当前项目的绝对路径
project_path=os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]

test_data_path=os.path.join(project_path,'test_data','test_data.xlsx')
test_add_path=os.path.join(project_path,'test_data','test_add_data.xlsx')
config_path=os.path.join(project_path,'config','test.config')
test_report_path=os.path.join(project_path,'test_result','report.html')
logs_path=os.path.join(project_path,'test_result','log.txt')
upload_img=os.path.join(project_path,'test_data','uploadimg.img')
testcase_dir = os.path.join(project_path,'testcase')