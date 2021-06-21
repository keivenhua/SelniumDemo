import json

import requests


class TestSendMethod:

    @staticmethod
    def test_send_method(method,url,params=None,data=None):

        if method == "get" or method == "delete":
            response = requests.request(method=method, url=url, params=params)
        elif method == "post" or method == "put":
            response = requests.request(method=method, url=url, json=data)
        else:
            print("请求方式不正确")
            response = None
        if method == "delete":
            return response.status_code
        else:
            return response.json()


if __name__ == '__main__':
    url = "http://127.0.0.1:8000/api/departments/"
    method = "get"
    res = TestSendMethod.test_send_method(method=method,url=url)
    print(res)