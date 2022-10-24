import requests
import time
from utlis.handle_conf import *
import json
import unittest
class Send_Requests(object):
    '''
    封装一个发送请求的工具类
    '''

    def __init__(self):
        '''
        用来保持会话
        '''
        self.session =requests.session()
    def get_token(object):
        headers=eval(conf.get_value('env','headers'))
        data=eval(conf.get_value("test_data","data"))
        url=conf.get_value("test_data","login_url")
        response=requests.post(url=url,headers=headers,data=json.dumps(data))
        # print(response.json()["data"]["token"])
        token=response.json()["data"]["token"]
        return token


    def send(self,method,url,data=None,json=None,params=None,headers=None,timeout=None):
        method = method.lower()#接口的请求全部改小写
        if method == 'get':
            response = self.session.get(url,params)
        elif method == 'post':
            response = self.session.post(url,data=data,headers=headers)
        elif method == 'post_json':
            response = self.session.post(url=url,json=json,headers=headers)
        elif method == 'delete':
            response = self.session.delete(url)

        return response


