#coding=utf-8
"""
===========================
Author:多测师_王sir
Time:2021-01-19 14:59
Wechat:xiaoshubass
website:www.duoceshi.cn
===========================
"""

'''
此模块用来放所有页面的元素
'''

class Page_Element:

    #1.用户名
    userName = ('id', 'userAccount')
    #2.密码
    passWord = ('id', 'loginPwd')
    #3.登录按钮
    loginBtn = ('id', 'loginBtn')
    #4.我的桌面
    desktop = ('xpath', '//*[@id="min_title_list"]/li/span')

    #5.用户中心
    user_center = ('xpath','//*[@id="menu-user"]/dt')


'''
page object ==》页面对象、简称PO设计模式
页面对象的概念：
把所有的页面元素都当做是当前类的对象的的属性
1、把所有的元素定位和用例进行了分离
2、让代码的结构比较清晰、简洁
3、页面的元素如果发生改变需要修改、不会影响到功能的代码
4、目的就是为了让代码解耦、耦合性降低

'''















