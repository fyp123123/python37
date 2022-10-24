import json
import requests
import time
import concurrent.futures
import threading

SUCCESS = 0
FAIL = 0

# url = 'http://site.sailayun.com/ims/user/channelUserLogin'
url = 'http://site.zjyundun.com/ims/user/login'

params = {
    "username": "17692546657",
    "password": "aaa111..."
}

headers = {
    'Content-Type': 'application/json;charset=UTF-8',
    'system': 'idc',
    'domain': 't647893.site.zjyundun.com'
}


def execute():
    try:
        response = requests.post(url, data=json.dumps(params), headers=headers, timeout=3)
        json.loads(response.text)
    except Exception as ex:
        global FAIL
        FAIL += 1
        print('失败次数={}'.format(FAIL))
        print(str(ex))
    finally:
        global SUCCESS
        SUCCESS += 1

    # resObj = json.loads(response.text)
    # print((resObj['data']['identifier']))


class MyThread(threading.Thread):
    """线程类"""

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        """线程创建后会直接运行run函数"""
        execute()


class single_test:
    def simple(self, num):
        """单线程，不做任何处理"""
        for i in range(num):
            execute()

    def _BatchRegister(self, num):
        execute()

    def _BatchRegisterAll(self, numList):
        """
        并发
        这里创建一个线程池，总共有5个线程可以分配使用
        executor.map()与map()函数类似，表示对sites中的每一个元素，并发地调用函数
        """
        with concurrent.futures.ThreadPoolExecutor(max_workers=80) as executor:
            executor.map(self._BatchRegister, numList)

    def mult(self, num):
        """线程池"""
        numList = []
        for i in range(num):
            numList.append(i)
        self._BatchRegisterAll(numList)

    def mult_thread(self, num):
        """新建多个线程"""
        threadArr = []
        for i in range(num):
            thread = MyThread()
            thread.start()
            threadArr.append(thread)


if __name__ == '__main__':
    startTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    """单线程测试"""
    pre = single_test()
    # pre.simple(100);
    """线程池"""
    # pre.mult(100);
    pre.mult_thread(30)
    endTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print('开始时间：{}'.format(startTime))
    print('结束时间：{}'.format(endTime))
