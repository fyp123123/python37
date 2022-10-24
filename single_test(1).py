import json
import requests
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

res_time = []
OK = []

headers = {'Content-Type': 'application/json;charset=UTF-8'}


class interface_test():
    def do_post(self, URL2, params):
        try:
            r = requests.post(URL2, data=json.dumps(params), headers=headers, timeout=3)
            r.raise_for_status()
        except requests.RequestException as e:
            print(e)
        else:
            js = json.dumps(r.json())
            return [r.json(), r.elapsed.total_seconds(), js]

    def circulation(self, num, URL2, params):
        for i in range(int(num)):
            res_time.append(interface_test.do_post(URL2, params)[1])
            if json.loads(interface_test.do_post(URL2, params)[2])["msg"] == 'Success':
                OK.append(json.loads(interface_test.do_post(URL2, params)[2])["msg"])
                logger.info('请求第' + str(i + 1) + '次，请求' + json.loads(interface_test.do_post(URL2, params)[2])[
                    "msg"] + ',状态码：' + json.loads(interface_test.do_post(URL2, params)[2])["code"])
            else:
                logger.info('请求第' + str(i + 1) + '次，请求' + json.loads(interface_test.do_post(URL2, params)[2])[
                    "msg"] + ',状态码：' +
                            json.loads(interface_test.do_post(URL2, params)[2])["code"])
        print('测试次数：', num)
        print('响应次数：', len(res_time))
        print('正常响应次数：', len(OK))
        print('总响应最大时长：', max(res_time))
        print('总响应最小时长：', min(res_time))
        print('总响应时长：', sum(res_time))
        print('平均响应时长：', sum(res_time) / len(res_time))


# """"请求地址"""
# base_url = 'http://127.0.0.1:8081'
# request_path = '/das/aliyun/gameSecBox/getInfo'

#   http://127.0.0.1:8081/das/aliyun/gameSecBox/getInfo
#
# """请求参数"""
# params = {
#     "instanceId": 'ddos_gamesecuritybox_public_cn-2r42o0x1l0a',
#     "accessKeyId": "LTAI5tDceZHRLdQ5j7iJNgFb",
#     "accessKeySecret": "SrAaDXpW2mtlsVP3EFwq7Y3m72lo9Y"
# }

if __name__ == '__main__':
    interface_test = interface_test()
    num = input('输入请求次数：')
    request_path = input('输入请求地址：')
    params = input('输入请求参数：')
    interface_test.circulation(num, request_path, params)
    input('Press Enter to exit...')
