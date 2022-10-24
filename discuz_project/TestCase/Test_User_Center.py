#coding=UTF-8
import unittest

from public.pages.Page_Element import Page_Element as p
from public.pages.BaseTestCase import BaseTestCase


class Test_User_Center(BaseTestCase):

    @classmethod
    def setUpClass(cls):
        BaseTestCase.sleep(1)

    @classmethod
    def tearDownClass(cls):
        BaseTestCase.sleep(1)

    def test01_user_center(self):
        try:
            userCenter = BaseTestCase.find_element(p.userCenter)
            BaseTestCase.click(userCenter)
            BaseTestCase.sleep(5)
        except Exception as e:
            print (e.message)

if __name__ == "__main__":
    unittest.main()