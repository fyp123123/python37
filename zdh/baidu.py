from selenium import webdriver
from time import *
d=webdriver.Chrome()
d.get("http://www.baidu.com")
d.find_element_by_name("wd").send_keys("name定位")
sleep(2)
d.close()
from zdh.__init__.py import *