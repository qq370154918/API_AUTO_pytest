import pytest
import time
time = time.strftime("%Y-%m-%d_%H%M", time.localtime())
if __name__ == '__main__':
    # pytest.main(['-v','-s','--reruns=2','TestCase/test_submitClues.py','--html=Out_Puts/html_report/test_submintClues.html','--alluredir=allure-results'])
    pytest.main(['-v', '-s', 'testcase/test_usedCar.py', r'--html=Out_Puts/html_report/report{}.html'.format(time)])



