import requests

url="http://i.zjyundun.com/server/user/login"
data={"phone": "15355079216", "password": "12345678aa@"}
header={"Content-Type": "application/json"}
a=requests.post(url=url,data=data,json=header)
print(a.json())