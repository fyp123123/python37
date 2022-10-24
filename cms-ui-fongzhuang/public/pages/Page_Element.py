#coding=utf-8

'''
PageElement这个模块很为关键，这个PageElement类当中封装了所有页面的网页元素
这里其实就是用到了让一个项目中的所有元素定位和用例流程和最终的用例进行分层处理
这个设计有点像RF框架当中的三层封装设计模式：元素层，流程层和案例层，但是这样处理
有一个问题就是代码量会很多。但是优势也是非常明显的
'''

'''
po设计模式 ==》page object页面对象设计模式解释：所有当前页面的控件和元素都为类或者对象的属性
po设计模式优势如下:
1.让元素定位，流程，案例进行了分离
2.前端代码关于元素定位有改动可以随时进行处理，修改非常方便
3.让代码间的耦合性降低、防止代码写死
4.降低代码的维护成本
5.代码的复用性高
6.采用标准的page object页面对象设计模式，符合现在主流ui自动化框架的标准搭配
'''

class Page_Element:

    #定义登录页面的元素
    userName = ("xpath", '//div[@class="formRow user"]/input')    #输入账号
    passWord = ("xpath", '//*[@id="loginPwd"]')    #输入密码
    loginBtn = ("id", 'loginBtn')           #点击登录
    loginOut = ("xpath", "//*[@title='退出']")   #断言消息

    #点击用户中心
    userCenter = ("xpath",'//*[@id="menu-user"]/dt')

















