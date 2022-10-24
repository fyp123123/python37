from utlis.handle_conf import *
from utlis.handle_excel import Handle_Excel
from utlis.handle_requests import Send_Requests
from library.ddt1 import ddt,data
from utlis.handle_path import *
import unittest
import os
import json
from testcase.test_login import *

@ddt
class Test_Workorder(unittest.TestCase):
    excel=Handle_Excel(case_file,"workOrder")
    cases=excel.read_data()
    request=Send_Requests()

    @classmethod
    def setUpClass(cls) -> None: #类的开始
        Send_Requests().get_token()

        # url=conf.get_value("env","url")+"/ims/user/login"
        # headers=eval(conf.get_value("env","headers"))
        # data=eval(conf.get_value("test_data","data"))
        # respones=cls.request.send(method="post",url=url,data=json.dumps(data),headers=headers)
        # a=respones.json()
        # print(a)
    @data(*cases)
    def testcase_01(self,case):
        Send_Requests().get_token()
        url=conf.get_value("env","url")+case["url"]
        data=eval(case["data"])
        header=eval(conf.get_value("env","headers"))
        header["token"]=Send_Requests().get_token()
        method=case["method"]
        excepted = eval(case['excepted'])
        case_id = case["case_id"]
        case_id = case_id + 1
        # print(header)

        respones=self.request.send(method=method,url=url,data=json.dumps(data),headers=header)
        result=respones.json()
        print(result)

        try:
            self.assertEqual(excepted["msg"],result["msg"])
            self.assertEqual(excepted["code"],result["code"])
        except Exception as e:
            self.excel.write_excel(1,8,"未通过")
            print(e)
        else:
            self.excel.write_excel(1,8,"通过")
if __name__ == '__main__':
    unittest.main()












