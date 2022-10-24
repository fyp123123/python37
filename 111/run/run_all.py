import time
import os
# from utlis.handle_path import *
from libriary.HTMLTestRunner3_New import HTMLTestRunner
import unittest
base_path=os.path.dirname(os.path.dirname(__file__))
report_path=os.path.join(base_path,"report")
tesecase_path=os.path.join(base_path,"test")
now = time.strftime('%Y-%m-%d-%H-%M-%S')
filename = report_path+'\\'+str(now)+'api_report.html'

def auto_run():
    discover = unittest.defaultTestLoader.discover(start_dir=tesecase_path,pattern='testcase.py')
    f = open(filename,'wb')
    runner = HTMLTestRunner(stream=f,title='接口自动化报告',description='用例报告情况如下:',tester='方耀平')
    runner.run(discover)
    f.close()


if __name__ == '__main__':
    auto_run()