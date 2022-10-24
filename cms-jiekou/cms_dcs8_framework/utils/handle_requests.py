# coding=utf-8


import requests

class Send_Requests(object):
    '''
    封装一个发请求的工具类
    '''

    def  __init__(self):
        '''用来保持会话'''
        self.session = requests.session()

    def send(self,method,url,data=None,json=None,params=None,headers=None):
        method = method.lower()  #把接口的请求全部改为小写
        if method == 'get':
            response = self.session.get(url,params)
        elif method == 'post':
            response = self.session.post(url,data,headers)
        elif method == 'post_json':
            response = self.session.post(url,json,headers)
        elif method == 'delete':
            response = self.session.delete(url)

        return response