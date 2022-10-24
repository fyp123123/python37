# coding=utf-8


'''
此模块是用来组建各个包的路径
'''

import os
#定义项目的路径
base_path = os.path.dirname(os.path.dirname(__file__))

#定义conf的路径
conf_path = os.path.join(base_path,'conf')


#定义data的路径
data_path = os.path.join(base_path,'data')

#定义repor的路径
report_path = os.path.join(base_path,'report')


#定义testcase的路径
testcase_path = os.path.join(base_path,'testcase')