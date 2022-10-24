#coding=utf-8
"""
===========================
Author:
Time:2021-01-19 9:35
Wechat:xiaoshubass
website:
===========================
"""

'''
ui自动化框架设计
此模块主要是放置所有的路径
'''
import os

#项目的路径
project_path = os.path.dirname(os.path.dirname(__file__))

#data的路径
data_path = os.path.join(project_path,'data')

#pages的路径
pages_path = os.path.join(project_path,'public','pages')


#utils的路径
utils_path = os.path.join(project_path,'public','utils')


#报告的路径
report_path = os.path.join(project_path,'report')

#testcase的路径
testcase_path = os.path.join(project_path,'testcase')






























