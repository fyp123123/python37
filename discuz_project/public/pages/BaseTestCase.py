#coding=UTF-8
from public.pages.Page_Element import Page_Element as p
import unittest
import time

class BaseTestCase(unittest.TestCase):
    """
    BaseTestCase封装所有的页面的公共方法
    """

    @classmethod
    def set_driver(cls,driver):   #入参是一个driver对象
        cls.driver = driver       #把传进来的谷歌浏览器对象做为当前类/基类的属性、基类的类变量

    @classmethod
    def get_driver(cls):   #单例设计模式  #作用就是保证所有的用例拿到的driver对象都是同一个driver对象
        return cls.driver

    # baidu_input = ('id','kw')
    @classmethod
    def find_element(cls,element):  #("id", "ls_username")
        try:
            type = element[0]
            value = element[1]
            if type == "id" or type == "ID" or type == "Id":
                elem = cls.driver.find_element_by_id(value)   #elem=driver.find_element_by_id('kw')
            elif type == "name" or type == "NAME" or type == "Name":
                elem = cls.driver.find_element_by_name(value)
            elif type == "class" or type == "CLASS" or type == "Class":
                elem = cls.driver.find_element_by_class_name(value)
            elif type == "link" or type == "LINK" or type == "link":
                elem = cls.driver.find_element_by_link_text(value)
            elif type == "xpath" or type == "Xpath" or type == "Xpath":
                elem = cls.driver.find_element_by_xpath(value)
            elif type == "css" or type == "CSS" or type == "Css":
                elem = cls.driver.find_element_by_css_selector(value)
            else:
                raise  NameError("Please input correct the type parameter!")
        except Exception:
            raise  NameError("This element not found!" + str(element))
        return elem

    @classmethod
    def sleep(cls,sec):
        return time.sleep(sec)

    @classmethod
    def send_keys(cls,element,text):
        element.send_keys(text)  #element就是cls.driver.find_element_by_id(value)

    @classmethod
    def click(cls,element):
        element.click()

    @classmethod
    def quit(cls):
        cls.driver.quit()

    #获取title信息
    @classmethod
    def get_title(cls):
        title = cls.driver.title
        return title

    @classmethod
    def get_text(cls,locator):
        text = cls.find_element(locator).text  #baidu_input = ('id','kw')
        return text

    @classmethod
    def wait(cls,sec):
        return cls.driver.implicitly_wait(sec)










