import unittest
from utlis_存放路径.handle_requestes import Send_Requests
from utlis_存放路径.handle_conf import Conf
import ddt
from utlis_存放路径.handle_excel import Handle_Excel
from utlis_存放路径.handle_path import *
import os

case_path= os.path.join(data_path,"case.xlsx")
@ddt.ddt
class Testcase(unittest.TestCase):
    excel=Handle_Excel(case_path,"nnn")
    cases=excel.read_data()
    request=Send_Requests()
    @ddt.data(*cases)
    def test_001(self,case):
        url= Conf.get_value("project","url") + case['url']
        data=eval(case['data'])
        headers=eval(Conf.get_value("project","headers"))
        mathod=case["mathod"]
        excepted=eval(case["excepted"])
        case_id=case["id"]
        case_id=case_id+1

        response = self.request.send(mathod=mathod, json=data, headers=headers, url=url,params=data)
        result = response.json()
        print(result)

if __name__ == '__main__':
    unittest.main()



