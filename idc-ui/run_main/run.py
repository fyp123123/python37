import time
import unittest
from run_main.HTMLTestRunner3_New import HTMLTestRunner
from config import globalconfig

#测试报告所在路径
report_path = globalconfig.report_path
#测试用例路径
TestCase_path = globalconfig.TestCase_path

def auto_run():
    global filename
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTest(loader.loadTestsFromName("public.pages.login.TestLogin.testLogin"))
    suite.addTest(loader.loadTestsFromName('TestCase.Testcase.testcase'))
    #suite.addTests(loader.loadTestsFromName(['TestCase.Testcase.testcase.test01_case','TestCase.Testcase.testcase.test02_case']))
    #path=r"D:\python37\idc - ui\TestCase"
    #a=loader.discover(start_dir=path, pattern="Testcase.py")
    now = time.strftime('%Y-%m-%d %H_%M_%S')  #获取当前时间
    filename = report_path + '\\' + now + 'result.html'#拼接出测试报告名
    fp = open(filename,'wb')
    runner = HTMLTestRunner(stream=fp,title='自动化报告',description='用例执行情况如下：',tester="方耀平")
    runner.run(suite)

    fp.close()
if __name__ == '__main__':
    auto_run()