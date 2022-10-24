import os
from public.utils.ReadConfigIni import ReadConfigIni

project_path = os.path.dirname(os.path.dirname(__file__))#获取当前运行的脚本的绝对路径
#print(project_path)    D:/python37/idc

TestCase_path = os.path.join(project_path,"TestCase")
#print(TestCase_path)  D:/python37/idc\TestCase  测试用例路径

report_path = os.path.join(project_path,"report","TestREPORt")
#print(report_path)  D:/python37/idc\report\TestREPORt  测试报告路径

data_path = os.path.join(project_path,"Data","TestData")
#print(data_path)  D:/python37/idc\Data\TestData          测试数据路径

ini_path = os.path.join(project_path,"config")
#print(ini_path)   D:/python37/idc\config     config.ini 路径

