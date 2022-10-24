#coding=utf-8
"""
===========================
Author:多测师_王sir
Time:2021-01-19 15:07
Wechat:xiaoshubass
website:www.duoceshi.cn
===========================
"""
from public.pages.BasePage import BasePage
from public.pages.Page_Element import Page_Element as p

class Test_User_Center(BasePage):

    @classmethod
    def setUpClass(cls) -> None:
        BasePage.sleep(1)

    @classmethod
    def tearDownClass(cls) -> None:
        BasePage.sleep(1)

    def test01_user_center(self):
        elem = BasePage.find_element(p.user_center)
        BasePage.click(elem)

































