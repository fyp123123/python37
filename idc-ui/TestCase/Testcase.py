import unittest
from public.pages.Page_Element import Page_Element as p
from public.pages.BaseTestCase import BaseTestCase

class testcase(BaseTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        BaseTestCase.sleep(1)
    @classmethod
    def tearDownClass(cls) -> None:
        BaseTestCase.sleep(1)
    def test01_case(self):
        CanpingBtn = BaseTestCase.find_element(p.CanpingBtn)#点击产品
        BaseTestCase.click(CanpingBtn)
        BaseTestCase.sleep(1)
    def test02_case(self):
        BuyBtn = BaseTestCase.find_element(p.BuyBtn)#点击购买按钮
        BaseTestCase.click(BuyBtn)
        BaseTestCase.sleep(3)
    def test03_case(self):
        buy_btn = BaseTestCase.find_element(p.buy_btn)#点击立即购买
        BaseTestCase.click(buy_btn)
        BaseTestCase.sleep(3)
    def test04_case(self):
        inputBtn = BaseTestCase.find_element(p.inputBtn)#点击购买协议
        BaseTestCase.click(inputBtn)
        BaseTestCase.sleep(8)
    # def test05_case(self):
        # zhifuBtn = BaseTestCase.find_element(p.zhifuBtn)#点击支付按钮
        # BaseTestCase.click(zhifuBtn)
        # BaseTestCase.sleep(5)
    def test06_case(self):
        fuwuqiBtn = BaseTestCase.find_element(p.fuwuqiBtn)#点击服务器按钮
        BaseTestCase.click(fuwuqiBtn)
        BaseTestCase.sleep(8)
        shengjiBtn = BaseTestCase.find_element(p.shengjiBtn)#点击升级按钮
        BaseTestCase.click(shengjiBtn)
        BaseTestCase.sleep(5)
        shengjikungBtn =  BaseTestCase.find_element(p.shengjikungBtn)#点击升级下拉框
        BaseTestCase.click(shengjikungBtn)
        BaseTestCase.sleep(5)
        heshuBtn = BaseTestCase.find_element(p.heshuBtn)#选择核数框
        BaseTestCase.click(heshuBtn)
        BaseTestCase.sleep(5)
        heshutijiaoBtn = BaseTestCase.find_element(p.heshutijiaoBtn)#核数提交按钮
        BaseTestCase.click(heshutijiaoBtn)
        BaseTestCase.sleep(5)
    def test07_case(self):
        fuwuqiBtn = BaseTestCase.find_element(p.fuwuqiBtn)  # 点击服务器按钮
        BaseTestCase.click(fuwuqiBtn)
        BaseTestCase.sleep(5)
        xufeiBtn = BaseTestCase.find_element(p.xufeiBtn)#点击续费按钮
        BaseTestCase.click(xufeiBtn)
        BaseTestCase.sleep(5)
        xufeikuangBtn = BaseTestCase.find_element(p.xufeikaungBtn)#续费框
        BaseTestCase.click(xufeikuangBtn)
        BaseTestCase.sleep(5)
        xufeishichangBtn = BaseTestCase.find_element(p.xufeishicahngBtn)#续费时长
        BaseTestCase.click(xufeishichangBtn)
        BaseTestCase.sleep(5)
        xufeitijiaoBtn = BaseTestCase.find_element(p.xufeitijiaoBtn)#续费提交
        BaseTestCase.click(xufeitijiaoBtn)
        BaseTestCase.sleep(5)
    # def test08_case(self):
    #     loginout = BaseTestCase.find_element(p.loginOut)#点击退出登录按钮
    #     BaseTestCase.click(loginout)
    #     BaseTestCase.sleep(1)
if __name__ == '__main__':
    unittest.main()