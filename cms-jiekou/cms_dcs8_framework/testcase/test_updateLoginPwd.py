# coding=utf-8

import unittest
from cms_dcs8_framework.utils.handle_path import *
from cms_dcs8_framework.utils.handle_excel import Handle_Excel
from cms_dcs8_framework.library.ddt import ddt,data   #从ddt模块中导入ddt和data装饰器
from cms_dcs8_framework.utils.handle_conf import conf
from cms_dcs8_framework.utils.handle_requests import Send_Requests
import os

case_file = os.path.join(data_path,'apicases.xlsx')

@ddt
class UpdataLoginPwd(unittest.TestCase):
    excel = Handle_Excel(case_file,'updateLoginPwd')
    cases = excel.read_data()  #一个列表当中是2个字典,每个字典都是一条用例
    request = Send_Requests()  #创建一个发送接口的请求

    @classmethod
    def setUpClass(cls) -> None:
        '''在类的开始里面完成登录的操作'''
        #1.准备登录接口的入参
        url = conf.get_value('env','url') + '/cms/manage/loginJump.do'
        data = {
            'userAccount': 'admin',
            'loginPwd': 123456
        }
        headers = eval(conf.get_value('env','headers'))
        #2.发送请求
        response = cls.request.send(method='post',url=url,data=data,headers=headers)
    @data(*cases)
    def test01_updateLoginPwd(self,case):
        '''封装修改密码接口'''
        #1.准备接口的入参和参数
        #eval()函数来执行一个字符串表达式,并返回表达式的值
        url = conf.get_value('env','url') + case['url']
        data = eval(case['data'])
        headers = eval(conf.get_value('env','headers'))
        method = case['method']
        excepted  = eval(case['excepted'])
        case_id = case['case_id']
        case_id = case_id+1

        #2.发送接口请求
        response = self.request.send(method=method,url=url,data=data,headers=headers)
        result = response.json()
        print(result)

        #3.对接口响应内容进行断言
        try:     #try 尝试去执行代码
            self.assertEqual(excepted['msg'],result['msg'])
            self.assertEqual(excepted['code'],result['code'])
        except Exception as e:
            self.excel.write_excel(case_id,8,'未通过')
            print(e)
        else:
            self.excel.write_excel(case_id,8,'通过')

if __name__ == '__main__':
    unittest.main()








