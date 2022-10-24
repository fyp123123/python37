import unittest
import requests
from time import *
class Cms_api(unittest.TestCase): #定义一个类继承单元测试
  @classmethod
def setUpClass(cls) -> None: #类的开始
 cls.s=requests.Session() # 创建对象保持会话
      @classmethod
def tearDownClass(cls) -> None: #类的结束
 print("类的结束")
def setUp(self) -> None:
 print("方法开始")
def tearDown(self) -> None:
 print("方法的结束")
def test001(self):
 dl_post_url = "https://i.zjyundun.com/ims/user/channelUserLogin"
 data = data={"username":"15355079216","password":"12345678aa","code":"","verificationCode":"00bb"}
 headers =headers={"Content-Type":"application/json","domain": "i.zjyundun.com","system": "channel","cookie":"Cookie: Hm_lvt_a9d6b8d928056204b5d244b49dfc9e64=1649416105,1650008601; Hm_lpvt_a9d6b8d928056204b5d244b49dfc9e64=1650510348"}
 jpost = self.s.post(url=dl_post_url, json=data, headers=headers)
 print(jpost.text)
def test002(self):
 url2= "https://i.zjyundun.com/ims/ccBanner?currentPage=1&pageSize=10&total=0&sorter=asc-sort"
 headers = headers = {"Content-Type": "application/json", "domain": "i.zjyundun.com", "system": "channel",
                      "cookie": "Cookie: Hm_lvt_a9d6b8d928056204b5d244b49dfc9e64=1649416105,1650008601; Hm_lpvt_a9d6b8d928056204b5d244b49dfc9e64=1650510348"}

 aa=requests.get(url=url2,headers=headers)
 print(aa.text)

if __name__ == '__main__':

 unittest.main()
