import requests

headers={"Content-Type":"application/json","domain": "i.zjyundun.com","system": "channel","cookie":"Cookie: Hm_lvt_a9d6b8d928056204b5d244b49dfc9e64=1649416105,1650008601; Hm_lpvt_a9d6b8d928056204b5d244b49dfc9e64=1650510348"}


# 构造一个全局session对象
S = requests.session()

# 使用session对象即S模拟登录成功后请求首页接口，更新S
h_url = url= "https://i.zjyundun.com/ims/user/channelUserLogin"
data={"username":"15355079216","password":"12345678aa","code":"","verificationCode":"00bb"}
h_res = S.post(url=h_url, headers=headers,json=data).json()
print(h_res)
# 使用session对象S请求个人通知消息接口
n_url =  "https://i.zjyundun.com/ims/ccBanner?currentPage=1&pageSize=10&total=0&sorter=asc-sort"
n_res = S.get(url=n_url,headers=headers).json()
print(n_res)

