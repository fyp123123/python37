import requests

class Send_Requests(object):
    def __init__(self):
        self.session=requests.session()
    def send(self,url,mathod,data=None,json=None,headers=None,params=None):
        mathod=mathod.lower()
        if mathod == "get":
            response=self.session.get(url,params=data)
        elif mathod == "post":
            response=self.session.post(url,data,headers)
        elif mathod == "post_json":
            response=self.session.post(url,json,headers)
        elif mathod == "delete":
            response = self.session.delete(url)
        return response

