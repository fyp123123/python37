import requests
# s=requests.session()
# url= "https://i.zjyundun.com/ims/user/channelUserLogin"
headers={"Content-Type":"application/json","domain": "i.zjyundun.com","system": "channel","cookie":"Cookie: Hm_lvt_a9d6b8d928056204b5d244b49dfc9e64=1649416105,1650008601; Hm_lpvt_a9d6b8d928056204b5d244b49dfc9e64=1650510348"}
# data={"username":"15355079216","password":"12345678aa","code":"","verificationCode":"00bb"}
# response=s.post(url=url,headers=headers,json=data)
# result=response.json()
# print(result)
url2= "https://i.zjyundun.com/ims/ccBanner?currentPage=1&pageSize=10&total=0&sorter=asc-sort"
aa=requests.get(url=url2,headers=headers)
print(aa.json())

