'''登录封装方法
'''
import unittest
from selenium import webdriver
from public.pages.BaseTestCase import BaseTestCase
from public.pages.Page_Element import Page_Element as p
from public.utils.Login_data import Login_data as login

url = login.get_url_value()#获取测试网站
username = login.get_username()#获取用户名
pwd = login.get_password() #获取密码

class TestLogin(BaseTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        driver = webdriver.Chrome() #创建一个driver 对象作为单列模式
        BaseTestCase.set_driver(driver)
    @classmethod
    def tearDownClass(cls) -> None:
        BaseTestCase.sleep(3)
    def testLogin(self):
        driver = BaseTestCase.get_driver()
        driver.get("https://i.zjyundun.com/shop/login")
        driver.maximize_window()
        BaseTestCase.sleep(1)
        LoginBtn = BaseTestCase.find_element(p.LoginBtn)#点击登录按钮
        BaseTestCase.send_keys(LoginBtn,"1131")
        BaseTestCase.sleep(1)
        userName = BaseTestCase.find_element(p.userName)#输入用户名
        BaseTestCase.send_keys(userName,username)
        BaseTestCase.sleep(1)
        passWord = BaseTestCase.find_element(p.passWord)#输入密码
        BaseTestCase.send_keys(passWord,pwd)
        BaseTestCase.sleep(1)
        loginBtn = BaseTestCase.find_element(p.loginBtn)#点击登录
        BaseTestCase.click(loginBtn)
        BaseTestCase.sleep(1)
        # CanpingBtn = BaseTestCase.find_element(p.CanpingBtn)#点击产品
        # BaseTestCase.click(CanpingBtn)
        # BaseTestCase.sleep(2)
        # text = BaseTestCase.get_text(p.loginOut)
        # assert text == "退出"
#
if __name__ == '__main__':
    unittest.main()
