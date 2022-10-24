# -*- coding: utf-8 -*-

"""
登录
UI自动化框架设计
date:2020-02-27
author:
"""
import unittest
from selenium import webdriver
from public.pages.BaseTestCase import BaseTestCase
from public.utils.Login_data import Login_data as login
from public.pages.Page_Element import Page_Element as p

url = login.get_url_value()   #获取测试的网址
username = login.get_username()  #获取用户名admin
pwd = login.get_password()   #获取密码

class TestLogin(BaseTestCase):

    @classmethod
    def setUpClass(cls):
        """
        测试前准备操作
        :return:
        """
        driver = webdriver.Chrome()   #创建一个driver对象作为单例模式
        BaseTestCase.set_driver(driver)

    @classmethod
    def tearDownClass(cls):
        """
        测试结束后清理操作
        :return:
        """
        BaseTestCase.sleep(3)

    def testLogin(self):
        """
        测试登录
        :return:
        """
        driver = BaseTestCase.get_driver()
        driver.get(url)
        driver.maximize_window()
        BaseTestCase.sleep(1)
        #点击登录框输入用户名  userName=cls.driver.find_element_by_id('ls_username')
        userName = BaseTestCase.find_element(p.userName) #userName = ("id", "ls_username")
        BaseTestCase.send_keys(userName,username)
        #点击密码框输入密码

        passWord = BaseTestCase.find_element(p.passWord)   #("id", 'ls_password')
        BaseTestCase.send_keys(passWord,pwd)
        #点击登录
        loginBtn = BaseTestCase.find_element(p.loginBtn)
        BaseTestCase.click(loginBtn)
        BaseTestCase.sleep(2)
        text = BaseTestCase.get_text(p.loginOut)
        assert text == "退出"

#调试代码
if __name__ == "__main__":
    unittest.main()



