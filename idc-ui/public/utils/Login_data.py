from public.utils import DoExcel
class Login_data(object):
    #获取网址
    @staticmethod
    def get_url_value():
        url_value = DoExcel.ReadExcel("Data.xlsx","Sheet1").read_excel(1,0)
        return url_value
    #获取用户名
    @staticmethod
    def get_username():
        username = DoExcel.ReadExcel("Data.xlsx","Sheet1").read_excel(1,1)
        return int(username)
    #获取密码
    @staticmethod
    def get_password():
        password =DoExcel.ReadExcel("Data.xlsx","Sheet1").read_excel(1,2)
        return password

if __name__ == '__main__':
    l = Login_data()
    print(l.get_url_value())
    print(l.get_username())
    print(l.get_password())
