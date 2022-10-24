#coding=utf-8
import os
from public.utils.ReadConfigIni import ReadConfigIni

#获取项目路径的第一种方法
# 获取config.ini的路径
# file_path = os.path.split(os.path.realpath(__file__))[0]
# print(file_path)  #D:\project\discuz_project\config

# 读取配置文件
# read_config = ReadConfigIni(os.path.join(file_path,"config.ini"))
# print(read_config)


# 通过config.ini获取项目的绝对路径的参数
# project_path = read_config.getConfigValue("project","project_path")
# print(project_path)

# 获取项目路径的第二种方法
project_path = os.path.dirname(os.path.dirname(__file__))
print(project_path)  #D:/project/discuz_project

# 测试用例路径
TestCase_path = os.path.join(project_path,"TestCase")
# print(TestCase_path)  D:\project\discuz_project\TestCase

# 测试报告路径
report_path = os.path.join(project_path,"report","TestReport")
# print(report_path)  D:\project\discuz_project\report

# 测试数据路径
data_path = os.path.join(project_path,"Data","TestData")
# print(data_path)

#config.ini路径
ini_path = os.path.join(project_path,"config")
# print(ini_path)






