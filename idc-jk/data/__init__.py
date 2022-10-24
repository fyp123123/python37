# v="0b1111011"
# print(int(v,2))  转化10进制
# print(bin(123)) 转化2进制


import requests
import json

url="https://i.zjyundun.com/ims/user/channelUserLogin"
data={"username":"15355079216","password":"12345678aa","code":"","verificationCode":"209c"}
headers={"domain": "i.zjyundun.com",
"system":"channel",
"Content-Type": "application/json;charset=UTF-8"}

response=requests.post(url=url,json=data,headers=headers,timeout=1)
token=response.json()["data"]["token"]

url2="https://i.zjyundun.com/ims/ccCorportionPrice"
data2={"corporationCode":"202203011552570111","corporationName":"15342351126","productCode":"P220519000001","productName":"高防服务器","discountType":"1","discountPrice":"10"}
headers["token"]=token

a=requests.post(url=url2,json=data2,headers=headers)
print(a.json())

# print(response.json()["data"]["token"])
# time=response.elapsed.total_seconds()
# print(time)
# print(result)
