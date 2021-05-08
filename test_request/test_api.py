from unittest import TestCase
from test_request import test_env


class TestApi(TestCase):

    data = {
        "method":"get",
        "url":"http://testing-studio:9999/demo1.txt",
        "headers":None
    }

    def test_send(self):
        ar = test_env.Api()
        print(ar.send(self.data))
