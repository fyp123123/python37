# coding=utf-8


'''
此模块是用来组建各个包的路径
'''

import os
#定义项目路径
base_path = os.path.dirname(os.path.dirname(__file__))  #获取当前脚本的运行的相对路径
conf_path = os.path.join(base_path,"conf") #定义conf路径
data_path = os.path.join(base_path,"data")#定义data路径
report_path = os.path.join(base_path,"report")#定义peport路径
testcase_path = os.path.join(base_path,"testcase")#定义testcase路径
#print(conf_path)


