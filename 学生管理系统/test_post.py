"""
post请求四种传送正文方式：
　　（1）请求正文是application/x-www-form-urlencoded
　　（2）请求正文是multipart/form-data
　　（3）请求正文是raw
　　（4）请求正文是binary
"""
import json
from requests_toolbelt import MultipartEncoder

import pytest
import requests


class TestPost():


    def test_post(self):

        # url = "http://httpbin.org/post"
        # data = {
        #     'userid': 'admin',
        #     'pwd': '123456',
        #     'date': '20180917'
        # }
        # # response = requests.post(url=url,data=data)
        # response = requests.post(url=url,json=data)
        # # res = json.dumps(response.json(),indent=2,ensure_ascii=False)
        # print(response.text)


        url = "https://httpbin.org/post"
        data = {
            'userid': 'admin',
            'pwd': '123456',
            'date': '20180917'
        }
        m = MultipartEncoder(fields=data)
        headers = {
            "contentType":m.content_type

        }

        response = requests.post(url=url,data=data,headers = headers)

        print(response.text)



if __name__ == '__main__':
    pytest.main('-s','-v')