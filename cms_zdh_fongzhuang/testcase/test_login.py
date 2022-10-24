#coding=utf-8
"""
===========================
Author:多测师_王sir
Time:2021-01-19 11:13
Wechat:xiaoshubass
website:www.duoceshi.cn
===========================
"""

'''
此模块是用来编写登录测试用例的
'''
from public.pages.BasePage import BasePage   #导入基类
from selenium import webdriver
from public.utils.read_ini import *
import unittest
from public.pages.Page_Element import Page_Element as p


class Test_Login(BasePage):

    @classmethod
    def setUpClass(cls) -> None:
        '''
        保证只会在登录之前创建一个driver对象、以后所有的用例都会使用这个driver对象 ==》单例设计模式
        :return:
        '''
        driver = webdriver.Chrome()
        BasePage.set_driver(driver)

    @classmethod
    def tearDownClass(cls) -> None:
        BasePage.sleep(1)

    def test01_login(self):
        '''
        编写登录测试用例
        :return:
        '''
        driver = BasePage.get_driver()
        driver.get(url)
        driver.maximize_window()
        BasePage.wait(10)
        #1.输入用户名
        elem = BasePage.find_element(p.userName)
        BasePage.senKeys(elem,username)
        #2.输入密码
        elem = BasePage.find_element(p.passWord)
        BasePage.senKeys(elem,pwd)
        #3.点击登录
        elem = BasePage.find_element(p.loginBtn)
        BasePage.click(elem)
        #4.断言
        value = BasePage.get_text(p.desktop)
        if value == '我的桌面':
            print('断言成功')
        else:
            raise ValueError('断言失败')

if __name__ == '__main__':
    unittest.main()





























