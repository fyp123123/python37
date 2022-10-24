# coding=utf-8

import unittest
from utils.handle_path import *
from utils.handle_excel import Handle_Excel
from library.ddt import ddt,data   #从ddt模块中导入ddt和data装饰器
from utils.handle_conf import conf
from utils.handle_requests import Send_Requests
import os

'''
ddt模块：是用来做数据驱动的
作用：可以Excel表格里面循环读取接口的用例数据、依次发送请求
装饰器的作业：在不改变原有函数的功能基础上给函数增加新的功能
ddt装饰器：装饰类的
data装饰器：装饰方法的(比如有10条用例、会从第1条依次按顺序跑到第10条)
'''

case_file = os.path.join(data_path,'apicases.xlsx') #Excel表格所在路径

@ddt
class Test_Login(unittest.TestCase):
    excel = Handle_Excel(case_file,'login')  #进入Excel表格的login表单
    cases = excel.read_data()  #一个列表当中是4个字典,每个字典都是一条用例
    request = Send_Requests()  #创建一个发送接口的对象



    @data(*cases)    #cases 是一个列表,里面有4个字典
    def test01_login(self,case):     #case 是一个字典,data装饰器每次运行取cases列表中的一个元素,即为字典
        '''封装登录接口'''
        #1.准备接口的入参和参数
        #eval()函数来执行一个字符串表达式,并返回表达式的值
        url = conf.get_value('env','url')
        data = eval(case['data'])
        headers = eval(conf.get_value('env','headers'))
        method = case['method']
        excepted  = eval(case['excepted'])
        case_id = case['case_id']
        case_id = case_id+1


        #2.发送接口请求
        response = self.request.send(method=method,url=url,json=data,headers=headers)
        result = response.json()

        print(result)

        #3.对接口响应内容进行断言

        try:     #try 尝试去执行代码

            self.assertEqual(result['msg'],excepted['msg'],msg="a!=b")
            self.assertEqual(result['code'],excepted['code'],msg="a!=b")
        except Exception as e:
            self.excel.write_excel(case_id,8,'未通过')
            print(e)
        else:
            self.excel.write_excel(case_id,8,'通过')


if __name__ == '__main__':
        unittest.main()






