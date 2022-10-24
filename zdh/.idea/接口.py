import requests
url="http://cms.duoceshi.cn/cms/manage/queryUserList.do"
data={'startCreateDate':'',
'endCreateDate':'',
'searchValue':'',
'page': 1}
header={'Content-Type': 'application/x-www-form-urlencoded'}
jpost=requests.post(url=url,data=data,json=header)
print(jpost.headers)
