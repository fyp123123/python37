from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import Select
class dl():
    def __init__(self):
        self.d=webdriver.Chrome()
        self.d.get("http://www.shuyuninfo.com/")
        self.d.maximize_window()
        self.d.implicitly_wait(5)
    def login(self,zh,mi):
        self.d.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/div/div[3]/div/div[1]').click()
        self.d.find_element_by_xpath('//*[@id="__layout"]/div/div[2]/div/div/div[2]/div/div[1]/input').send_keys(zh)
        self.d.find_element_by_xpath('//*[@id="__layout"]/div/div[2]/div/div/div[2]/div/div[2]/input').send_keys(mi)
        sleep(2)
        self.d.find_element_by_xpath('//*[@id="__layout"]/div/div[2]/div/div/div[2]/div/button').click()
        sleep(1)
        self.d.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/div/div[2]/div[2]/a').click()
        sleep(1)
        self.d.find_element_by_class_name("btn").click()#点击立即选购按钮
        sleep(1)
        self.d.find_element_by_class_name("buy-btn").click()#点击立即购买按钮
        sleep(3)
        # self.d.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[2]/div[4]/label/span/input').click()#点击购买服务协议框
        #self.d.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[2]/div[5]/button').click()#点击确定支付按钮
        #sleep(3)
        # self.d.find_element_by_xpath('//*[@id="active"]/div[1]').click()#点击云服务器按钮
        # sleep(3)
        self.d.find_element_by_class_name('item').click()#点击云服务器按钮
        sleep(3)
        self.d.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[3]/div/div/div/div/div/div[2]/div/div/table/tbody/tr[1]/td/div/div[2]/button[1]').click()#点击升级按钮
        sleep(3)
        self.d.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[2]/div/form/div[2]/div[2]/div/span/div').click()#点击下拉框
        #Select(a).select_by_index(2)
        sleep(3)
        self.d.find_element_by_xpath('//*[@id="test-uuid"]/ul/li[3]').click()#选择4核
        sleep(3)
        # self.d.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[2]/div/form/div[3]/div[2]/div/span/div/div').click()  #16G
        # sleep(7)
        # self.d.find_element_by_xpath('//div[@id="test-uuid" and @class="ant-select-dropdown-content"]/ul/li[2]').click()#选择16G
        # sleep(7)
        # # self.d.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[2]/div/form/div[6]/div/div/span/button').click()    确定提交按钮
        # sleep(3)
        self.d.find_element_by_class_name('item').click()#回到云服务器界面
        sleep(3)
        self.d.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[3]/div/div/div/div/div/div[2]/div/div/table/tbody/tr[1]/td/div/div[2]/button[2]').click()#点击续费按钮
        sleep(2)
        self.d.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[3]/div[2]/div/span/div/div').click()#续费时间下拉框
        sleep(3)
        self.d.find_element_by_xpath('//*[@id="test-uuid"]/ul/li[3]').click()#续费3个月
        sleep(3)
        self.d.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[3]/div/button[1]').click()#取消按钮
        #self.d.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[2]/div[3]/div/button[2]').click()#续费提交按钮


if __name__ == '__main__':
 a=dl()
 a.login('15355079216','12345678aa@')