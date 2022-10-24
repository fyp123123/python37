import openpyxl
from utlis_存放路径.handle_path import *

class Handle_Excel(object):

    def __init__(self,filename,sheet_name):
        self.filename=filename
        self.sheet_name=sheet_name

    def open(self):
        self.wb=openpyxl.load_workbook(self.filename)
        self.sh=self.wb[self.sheet_name]
    def read_data(self):
        self.open()
        datas=list(self.sh.rows)
        title=[i.value for i in datas[0]]
        cases=[]
        for j in datas[1:]:
            values=[k.value for k in j]
            case=dict(zip(title,values))
            cases.append(case)
        return cases
    def write_excel(self,row,column,value=None):
        self.open()
        self.sh.cell(row,column,value)
        self.wb.save(self.filename)
if __name__ == '__main__':

 case_path=os.path.join(data_path,"case.xlsx")
 read_excel=Handle_Excel(case_path,"nnn")
 print(read_excel.read_data())
 read_excel.write_excel(2,12,"通过")






