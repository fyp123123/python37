import unittest
from utlis.handle_path import *
from utlis.handle_excel import Handle_Excel
from library.ddt1 import ddt,data  #从ddt模块中导入ddt和data装饰器
from utlis.handle_conf import conf
from utlis.handle_requests import Send_Requests
import os
import json
import time

'''
ddt模块：是用来做数据驱动的
作用：可以Excel表格里面循环读取接口的用例数据、依次发送请求
装饰器的作业：在不改变原有函数的功能基础上给函数增加新的功能
ddt装饰器：装饰类的
data装饰器：装饰方法的(比如有10条用例、会从第1条依次按顺序跑到第10条)
'''

case_file = os.path.join(data_path,'apicases.xlsx')#excel表格的路径

@ddt
class Test_Login(unittest.TestCase):
    excel = Handle_Excel(case_file,'login')#进入Excel表格的login表单
    cases = excel.read_data()
    request = Send_Requests()#创建一个发送接口的对象
    @data(*cases)
    def test01_login(self,case):#case 是一个字典,data装饰器每次运行取cases列表中的一个元素,即为字典
        '''封装登录接口'''
        # 1.准备接口的入参和参数

        url = conf.get_value('env', 'url')+case["url"]
        # print(url)
        data = eval(case['data'])
        # print(data)
        # datas=json.dumps(data)
        # print(datas)
        headers = eval(conf.get_value('env','headers'))
        method = case['method']
        excepted = eval(case['excepted'])
        case_id = case["case_id"]
        case_id = case_id+1

        # 发送接口请求
        response = self.request.send(method=method,data=json.dumps(data),headers=headers,url=url,timeout=3)
        result=response.json()
        #result=response.elapsed.total_seconds()
        # print(result)
        # 3.对接口响应内容进行断言
        try:#try尝试执行代码aaa
            self.assertEqual(excepted['msg'],result['msg'],msg="a!=b")
            self.assertEqual(excepted['code'],result['code'],msg="a!=b")

        except Exception as e:
            self.excel.write_excel(case_id,column=8,value='未通过')
            # print(e)
        else:
            self.excel.write_excel(case_id,8,'通过')


if __name__ == '__main__':
    unittest.main()

