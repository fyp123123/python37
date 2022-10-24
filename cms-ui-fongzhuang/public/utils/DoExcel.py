#coding=UTF-8
import xlrd
import os
from config import globalconfig
data_path = globalconfig.data_path   #测试数据的路径

# ****************
# 读取Excel封装到一个类中
# 实现数据驱动测试
# 读取Excel表格需要下载一个库xlrd
# 在dos窗口用命令：pip install xlrd
# ****************
class ReadExcel(object):
    """
    打开excel，读取测试数据
    """
    # 打开Excle，读取某个sheet
    def __init__(self,filename,sheetname):

        datapath = os.path.join(data_path,filename) #D:\project\discuz_project\Data\TestData\Data.xlsx
        # print(datapath)
        # 打开测试数据文件TestData包中的Data.xlsx文件
        self.workbook = xlrd.open_workbook(datapath)
        self.sheetName = self.workbook.sheet_by_name(sheetname)

    # 获取某个单元格的数据（索引获取）
    def read_excel(self,rownum,colnum):
        value = self.sheetName.cell(rownum,colnum).value
        return value


# #*************************
# # 验证ReadExcel类的正确性
# #*************************
# 获取某个单元格的数据（索引获取）
# cellValue = ReadExcel("Data.xlsx","Sheet1").read_excel(1,0)
# cellValue = ReadExcel("Data.xlsx","Sheet1").read_excel(1,1)
# cellValue = ReadExcel("Data.xlsx","Sheet1").read_excel(1,2)
# print (cellValue)        #运行结果：http://discuz.e70w.com/













