# coding=utf-8

import time
from utils.handle_path import *
from library.HTMLTestRunner3_New import HTMLTestRunner
# from library.mail3 import SendMail
import unittest


onw = time.strftime('%Y-%m-%d-%H-%M-%S')

filename = report_path+'\\'+ str(onw) +'_api_report.html'

def auto_run():
    discover = unittest.defaultTestLoader.discover(start_dir=testcase_path,pattern='test_*.py')
    f = open(filename,'wb')
    runner = HTMLTestRunner(stream=f,
                            title='CMS平台接口自动化用例报告',
                            description='用例报告情况如下:',
                            tester='方耀平')
    runner.run(discover)
    f.close()


# def sendMail():
#     sm = SendMail(send_msg=filename,attachment=filename)
#     sm.send_mail()


if __name__ == '__main__':
    auto_run()



