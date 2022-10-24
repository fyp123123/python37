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
    LoginBtn=("xpath" , '//*[@placeholder="请输入账号"]')                  #登录按钮
    userName=("xpath" ,'//div[@class="borderbule"]/input[1]')    #输入账号
    passWord=("xpath" , '//*[@id="__layout"]/div/div[2]/div/div/div[2]/div/div[2]/input')    #输入密码
    loginBtn = ("xpath" , '//*[@id="__layout"]/div/div[2]/div/div/div[2]/div/button')           #点击登录
    loginOut = ("class" , 'logout')   #退出登录
    CanpingBtn =("xpath",'//*[@id="__layout"]/div/div[1]/div/div[2]/div[2]/a') #产品按钮
    BuyBtn = ("class","btn")#购买按钮
    buy_btn = ("class","buy-btn")#点击立即购买
    inputBtn = ("xpath",'//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[2]/div[4]/label/span/input')#勾选购买协议
    zhifuBtn = ("xpath",'//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[2]/div[5]/button')#确认支付按钮
    fuwuqiBtn = ("class",'item') ##点击云服务器按钮
    shengjiBtn = ("xpath",'//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[3]/div/div/div/div/div/div[2]/div/div/table/tbody/tr[1]/td/div/div[2]/button[1]')#点击升级按钮
    shengjikungBtn = ("xpath",'//*[@id="app"]/div/div[2]/div[2]/div[2]/div/form/div[2]/div[2]/div/span/div')#升级下拉框
    heshuBtn = ("xpath",'//*[@id="test-uuid"]/ul/li[3]')#选择4核,升级核数
    heshutijiaoBtn = ("xpath",'//*[@id="app"]/div/div[2]/div[2]/div[2]/div/form/div[6]/div/div/span/button')#确定核数提交按钮
    xufeiBtn = ("xpath",'//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[3]/div/div/div/div/div/div[2]/div/div/table/tbody/tr[1]/td/div/div[2]/button[2]')#续费按钮
    xufeikaungBtn = ("xpath",'/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[3]/div[2]/div/span/div/div')#续费时间下拉框
    xufeishicahngBtn = ("xpath",'//*[@id="test-uuid"]/ul/li[3]')#续费时长
    xufeitijiaoBtn = ("xpath",'/html/body/div[3]/div/div[2]/div/div[2]/div[3]/div/button[2]')#续费提交按钮













