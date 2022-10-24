import unittest
import time
from selenium.webdriver import ActionChains
class Element(unittest.TestCase):
    @classmethod
    def set_driver(cls,driver):
        cls.driver=driver
    #把driver做为传参传入
    @classmethod
    def get_driver(cls):
        return cls.driver
    @classmethod
    def find_element(cls,element):
        try:
            type=element[0]
            value=element[1]
            if type=="id" or type=="ID" or type=="Id":
                ele=cls.driver.find_element_by_id(value)
            elif type=="name" or type=="Name" or type=="NAME":
                ele=cls.driver.find_element_by_name(value)
            elif type=="class" or type=="Class" or type=="CLASS":
                ele=cls.driver.find_element_by_class_name(value)
            elif type=="xpath" or type=="Xpath" or type=="XPATH":
                ele=cls.driver.find_element_by_xpath(value)
            elif type=="css" or type=="CSS" or type=="Css":
                ele=cls.driver.find_element_by_css_selector(value)
            else:
                raise NameError("请输入正确的定位方式")
        except Exception:
            raise NameError("这个定位方法没有找到"+str(element))
    @classmethod
    def sleep(self,sec):
        return time.sleep(sec)
    @classmethod
    def click(cls,element):
        element.click()
    @classmethod
    def send_keys(cls,element,text):
        element.send_keys(text)
    @classmethod
    def click_and_hold(cls,elemrnt):
        cls.driver(ActionChains).click_and_hold(elemrnt)
    @classmethod
    def move_by_offset(cls,x,y):
        cls.driver(ActionChains).move_by_offset(x,y)
    @classmethod
    def release(cls):
        cls.driver(ActionChains).release()
    @classmethod
    def perform(cls):
        cls.driver(ActionChains).perform()











