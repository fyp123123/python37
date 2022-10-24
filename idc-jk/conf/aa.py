import requests
import json

url='https://ntm.zjyundun.com/rps/esResponse/selectByPager'
data={"currentPage":1,"pageSize":10}
headers={"Content-Type": "application/json;charset=UTF-8","token": "eyJUeXBlIjoiSnd0IiwidHlwIjoiSldUIiwiYWxnIjoiSFMyNTYifQ.eyJjdXJyZW50VXNlciI6IntcInVzZXJDb2RlXCI6XCI2NjY2NjZcIixcInVzZXJuYW1lXCI6XCJhZG1pblwiLFwiYXV0aGluZ0lkXCI6XCI2NjY2NjZcIixcInVzZXJUeXBlXCI6XCJNQU5BR0VSXCIsXCJ0ZW5hbnRJZFwiOlwiMVwiLFwiY29ycG9yYXRpb25Db2RlXCI6XCI2NjY2NjZcIixcIm1haW5cIjpmYWxzZSxcImNoYW5uZWxVc2VyXCI6ZmFsc2V9IiwiZXhwIjoxNjU1ODY2NTQ4fQ.JAdeITI8z-xbksU-AHdpzw46Hcyo3SVf8igODWh6Jl4"}

response=requests.post(url=url,data=json.dumps(data),headers=headers)
a=print(response.json()[0])
print(a)