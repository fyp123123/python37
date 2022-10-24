import unittest
from selenium import webdriver
from time import sleep
class testcase():
    def __init__(self):
        pass
    def anli1(self):


        sleep(3)
        # 2.实例化浏览器对象:类名（）
        driver = webdriver.Chrome()
        # 3.打开网页
        driver.get('http://www.shuyuninfo.cn')
        # 最大化
        driver.maximize_window()
        # 关闭
        # driver.close()
        # 点击登录按钮
        login = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/div/div[3]/div/div[1]').click()
        sleep(1)
    def anli2(self):
        print("按钮2")
if __name__ == '__main__':
    