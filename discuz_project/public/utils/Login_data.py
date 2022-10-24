#coding=UTF-8
from public.utils import DoExcel

#此模块用于把Excel表格中的数据进行封装
class Login_data(object):

    #获取网址
    @staticmethod
    def get_url_value():
        url_value = DoExcel.ReadExcel("Data.xlsx", "Sheet1").read_excel(1, 0)
        return url_value

    #获取用户名
    @staticmethod
    def get_username():
        username = DoExcel.ReadExcel("Data.xlsx", "Sheet1").read_excel(1, 1)
        return username

    #获取密码
    @staticmethod
    def get_password():
        password = DoExcel.ReadExcel("Data.xlsx", "Sheet1").read_excel(1, 2)
        return int(password)

if __name__ == '__main__':
    l = Login_data()
    print (l.get_url_value())   #http://discuz.e70w.com/
    print(l.get_username())    #admin
    print (l.get_password())   #mN3BzsaeAd
    # print(Login_data.get_url_value())
















