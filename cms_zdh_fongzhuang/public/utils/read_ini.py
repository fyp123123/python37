#coding=utf-8
"""
===========================
Author:多测师_王sir
Time:2021-01-19 10:00
Wechat:xiaoshubass
website:www.duoceshi.cn
===========================
"""

'''
此模块就是用来读取ini文件的
如果要读取ini文件必须要安装configparser库
在dos窗口执行
pip install configparser
'''

from configparser import ConfigParser     #通过configparser模块导入ConfigParser类
from config.config import *
import os

class Read_Ini(ConfigParser):

    def __init__(self,filename):
        super(Read_Ini, self).__init__()    #继承父类的构造函数
        self.read(filename)   #读取具体的ini文件

    def get_data_ini(self,section, option):
        '''
        封装一个工具方法来获取ini文件当中的section对应option的value值
        :return:
        '''
        return self.get(section, option)

path = os.path.join(data_path,'data.ini') #C:\project\cms_dcs10\data\data.ini
read = Read_Ini(path)
url = read.get_data_ini('test_data','url')
username = read.get_data_ini('test_data','username')
pwd = read.get_data_ini('test_data','pwd')
# print(url)
# print(username)
# print(pwd)




















