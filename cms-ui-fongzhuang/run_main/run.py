#coding=UTF-8
import time
import unittest
from run_main.HTMLTestRunner3_New import HTMLTestRunner
from config import globalconfig
from public.utils.mail import SendMail

# 测试报告所在路径
report_path = globalconfig.report_path
# 测试用例
TestCase_path = globalconfig.TestCase_path

def auto_run():
    '''
    按用例进行加载
    :return:
    '''
    global filename   #定义一个全局变量
    suite = unittest.TestSuite() #
    loader = unittest.TestLoader()  #创建一个用例加载器和defaultTestLoader是一样的
    suite.addTest(loader.loadTestsFromName("public.pages.login.TestLogin.testLogin"))
    suite.addTest(loader.loadTestsFromName('TestCase.Test_User_Center.Test_User_Center.test01_user_center'))

    now = time.strftime('%Y-%m-%d %H_%M_%S') #获取当前系统时间
    filename = report_path + '\\' + now + 'result.html' #拼接出测试报告名
    fp = open(filename,'wb')
    runner = HTMLTestRunner(stream=fp,title=u'cms自动化测试报告',description=u'用例执行情况如下:'
                            ,tester=u'多测师_王sir')
   # print (suite)
    runner.run(suite)
    fp.close()

#定义一个发邮件的方法
def send_mail():
    sm = SendMail(send_msg=filename,attachment=filename)
    sm.send_mail()  #创建一个对象调用SendMail类中的send_mail方法进行邮件的发送

if __name__ == "__main__":
    auto_run()
    # send_mail()   #调用send_mail()方法发送邮件

