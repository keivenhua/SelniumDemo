from utils.send_method import TestSendMethod


class DepartmentInterment(object):
    def __init__(self,url):
        self.url = url
        self.send = TestSendMethod

    def add_department(self,data):
        """
        新增学院
        :param data:
        """
        return self.send.test_send_method("post", self.url, data=data)

    def get_department(self,data):
        return self.send.test_send_method("get",self.url, params=data)

    def update_department(self,dep_id,data):
        url = self.url + "{}/".format(dep_id)
        return self.send.test_send_method("put", url=url, data=data)

    def delete_department(self,data):
        return self.send.test_send_method("delete",self.url,params=data)