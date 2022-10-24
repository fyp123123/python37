#coding=utf-8
"""
===========================
Author:多测师_王sir
Time:2021-01-19 10:52
Wechat:xiaoshubass
website:www.duoceshi.cn
===========================
"""

'''
此模块封装的是所有页面的公共的方法
'''

import unittest
from time import sleep

#调试代码
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.maximize_window()

class BasePage(unittest.TestCase):

    @classmethod
    def set_driver(cls,driver):         #单例模式：谷歌浏览器类的对象只会被创建一次
        cls.driver = driver    #把传进来的driver对象赋值给到当前基类的类变量、变成当前类的一个属性

    @classmethod
    def get_driver(cls):
        return cls.driver    #谁调用这个get_driver谁就拿到driver对象

    @classmethod
    def find_element(cls,element):
        '''
        封装一个定位网页元素的方法
        :return:
        '''
        type = element[0]
        value = element[1]
        if type == 'id':
            elem = cls.driver.find_element_by_id(value)
        elif type == 'name':
            elem = cls.driver.find_element_by_name(value)
        elif type == 'class':
            elem = cls.driver.find_element_by_class_name(value)
        elif type == 'css':
            elem = cls.driver.find_element_by_css_selector(value)
        elif type == 'xpath':
            elem = cls.driver.find_element_by_xpath(value)
        elif type == 'link':
            elem = cls.driver.find_element_by_link_text(value)
        else:
            raise ValueError('please input correct webelement')
        return elem

    @classmethod
    def senKeys(cls,elem,value):
        return elem.send_keys(value)

    @classmethod
    def click(cls,elem):
        return elem.click()

    @classmethod
    def wait(cls,sec):
        return cls.driver.implicitly_wait(sec)

    @classmethod
    def sleep(cls,sec):
        return sleep(sec)

    @classmethod
    def get_text(cls,element):
        text = BasePage.find_element(element).text
        return text


if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.get('http://www.baidu.com')
    driver.maximize_window()
    baidu_input = ('id', 'kw')
    elem = BasePage.find_element(baidu_input)
    elem.send_keys('多测师')




























