from unittest import TestCase
from api import test_for_base


class TestApiRequests(TestCase):

    res_data = {
        "method":"get",
        "url":'http://127.0.0.1:9999/demo1.txt',
        "headers":None,
        "encoding":"base64"
    }

    def test_send(self):
        ar = test_for_base.ApiRequests()
        print(ar.send(self.res_data))
