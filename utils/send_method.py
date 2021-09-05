import requests

from utils import DumpJ


class SendMethod(object):
    def send_get(self, url, data=None, **kwargs):
        """
        发送get请求
        :param url:
        :param data:
        :param kwargs:
        :return:
        """
        response = requests.get(url=url, params=data, **kwargs)
        return response.json()

    def send_post(self, url, data=None, json=None, **kwargs):
        """
        发送post求
        :param url:
        :param data:
        :param kwargs:
        :return:
        """
        response = requests.post(url=url, json=json, data=data, **kwargs)
        return response.json()

    def send_put(self, url, data=None, **kwargs):
        """
        发送put请求
        :param url:
        :param data:
        :param kwargs:
        :return:
        """
        response = requests.put(url=url, params=data, **kwargs)
        return response.json()

    def send_delete(self, url, **kwargs):
        """
        发送delete请求
        :param url:
        :param data:
        :param kwargs:
        :return:
        """
        response = requests.delete(url=url, **kwargs)
        return response.json()

    def send_main(self, method, url, data=None, json=None, **kwargs):
        """
        总方法
        :param method:
        :param url:
        :param data:
        :param json:
        :param kwargs:
        :return:
        """
        if method == 'get':
            res = self.send_get(url=url, data=data, **kwargs)
        elif method == 'post':
            res = self.send_post(url=url, data=None, json=None, **kwargs)
        elif method == 'put':
            res = self.send_put(url=url, data=None, json=None, **kwargs)
        elif method == 'delete':
            res = self.send_delete(url=url, **kwargs)
        else:
            res = None
        return res


if __name__ == '__main__':
    url = 'http://127.0.0.1:8000/api/departments/'
    data = {
        "data": [
            {
                "dep_id": "T333",
                "dep_name": "黄色学院",
                "master_name": "Test-Master",
                "slogan": "Here is Slogan"
            }
        ]
    }
    send = SendMethod()
    print(send.send_main('post', url=url,json=data))
    # print(requests.request('post', url=url,json=data))