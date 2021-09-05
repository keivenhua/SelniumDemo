import requests

from utils.utils import DumpJ


class DepartmentInterface(object):

    def __init__(self, url):
        self.url = url

    def add_department(self, data):
        res = requests.request("post", url=self.url, json=data)
        return res

    def get_department(self, data):
        res = requests.request("get", url=self.url, data=data)
        return res

    def update_department(self, dep_id, data):
        url = self.url + "{}/".format(dep_id)
        res = requests.request("put", url=url, json=data)
        return res

    def delete_department(self, data):
        res = requests.request("delete", url=self.url, data=data)
        return res
