#coding=UTF-8
import configparser
import os

'''
configparser这个模块本身就是用来读取ini文件的
在dos窗口用如下命令安装：
pip install configparser

'''

class ReadConfigIni(object):
    """
    实例化configparser
    """
    def __init__(self,filename):
        self.cf = configparser.ConfigParser()   #创建对象self.cf
        self.cf.read(filename)

    # 读ini文件的操作
    def getConfigValue(self,section, option):
        value = self.cf.get(section, option)
        return value

# # ****************************
# # 验证ReadConfigIni是否可以读取ini文件，该部分为测试代码，实际框架中可以删除
# # ****************************
# file_path = os.path.split(os.path.realpath(__file__))[0]   #获取当前目录的绝对路径
# path = os.path.join(file_path,"config.ini")
# print (path)  #D:\project\discuz_project\public\utils\config.ini
# read_config = ReadConfigIni(path)
#
# value = read_config.getConfigValue("project","project_path")
# print(value)  #D:\project\discuz_project
# #
# username= read_config.getConfigValue("test_data","username")
# print(username)
# pwd= read_config.getConfigValue("test_data","pwd")
# print(pwd)





