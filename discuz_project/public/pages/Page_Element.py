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
    userName = ("id", "userAccount")    #输入账号
    passWord = ("id", 'loginPwd')    #输入密码
    loginBtn = ("id", 'loginBtn')           #点击登录
    loginOut = ("xpath", "//*[@title='退出']")   #断言消息

    #点击用户中心
    userCenter = ("xpath",'//*[@id="menu-user"]/dt')


'''
UI自动化面试题：
1.你讲一下ui自动化用selenium是怎么做的？
2.你是怎么封装
3.对于数据你怎么管理的 ==》用ini或者Excel表格管理、然后通过封装工具类来进行读取
4.po是什么？你对po的理解是什么？
5.你用了哪些装饰器？装饰器的原理是什么？ #@classmethod   @staticmethod
6.你写了多少条自动化用例、大概的执行时间是多少？  ==》100多条、40多分钟
7.自动化测试用例覆盖率有多少？  ==》场景能覆盖70-80%、但是自动化测试用例占相关功能测试用例的只有10-20%
8.除了unittest单元测试框架、还有没有对其他框架有了解的？  ==》pytest框架、Java里面有testNG、Junit
9.unittest单元测试框架里面如果要跳过一个用例怎么操作  ==》unittest.skip()这个装饰器
10.如果在unittest单元测试框架里面进行数据驱动怎么操作 ==》用ddt装饰器、当然也可以用Excel表格和ini文件进行数据驱动和参数化
'''














