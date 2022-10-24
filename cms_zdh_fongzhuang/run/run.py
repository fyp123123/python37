#coding=utf-8
"""
===========================
Author:多测师_王sir
Time:2021-01-19 15:14
Wechat:xiaoshubass
website:www.duoceshi.cn
===========================
"""
import unittest
from config.config import *
from public.utils.HTMLTestRunner3_New import HTMLTestRunner
import time
from public.utils.mail3 import SendMail

#定位生成报告的绝对路径和文件名称
now = time.strftime('%Y-%m-%d-%H-%M-%S')
filename = report_path + "\\"+ str(now)+ '_ui_report.html'

def auto_run():
    discover = unittest.defaultTestLoader.discover(start_dir=testcase_path,
                                                   pattern='test_*.py')
    f = open(filename,'wb')
    runner = HTMLTestRunner(stream=f,
                            title='cms平台ui自动化测试报告',
                            description='用例执行情况如下：',
                            tester='方耀平')
    runner.run(discover)
    f.close()

def sendMail():
    sm = SendMail(send_msg=filename,attachment=filename)
    sm.send_mail()

if __name__ == '__main__':
    auto_run()   #运行测试用例生成报告
    sendMail()   #把报告发送到邮件中









