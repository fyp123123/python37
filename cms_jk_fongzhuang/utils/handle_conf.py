# coding=utf-8

'''
此模块用来封装读取ini问价的工具类
python通过configparser这个模块当中的ConfigParser类来读取ini文件的
需要安装：
在dos窗口输入pip install configparser进行安装
或者通过python -m pip install configparser
'''


from configparser import  ConfigParser
from utils.handle_path import *
import os

class Handle_Conf(ConfigParser):
    '''
    当前这个类用来处理conf.ini文件的工具类
    '''
    def __init__(self,filname):
        super(Handle_Conf, self).__init__()  #继承父类的构造方法
        self.filname = filname  #把传入进来的形式参数赋值给到实例变量self,filname
        self.read(self.filname)  #打开ini文件进行读取

    def get_value(self,section,option):
        '''
        获取ini文件中对应的section和option的value值
        :param section:
        :param option:
        :return:
        '''
        value = self.get(section,option)
        return  value

path = os.path.join(conf_path,'conf.ini')  #拼接conf.ini文件的路径
conf = Handle_Conf(path)    #创建对象把conf.ini文件作为入参
print(conf.get_value('env','url'))  #通过conf对象调用get_value传入section核option拿到value值
print(conf.get_value('test_data','username'))


