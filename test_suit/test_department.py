import unittest
from utils.send_method import TestSendMethod
from utils.utils import dumpJ


class DepartmentTest(unittest.TestCase):


    def setUp(self):
        self.url =  "http://127.0.0.1:8000/api/departments/"
        self.send = TestSendMethod()


    def test_case_01(self):
        res = self.send.test_send_method("get",url=self.url)
        # print(dumpJ(res))
        count = res["count"]
        self.assertNotEqual(count,0,"查询学院失败")

    def test_case_02(self):
        data = {
            "data": [
                {
                "dep_id": "T09",
                "dep_name": "有码学院",
                "master_name": "Test-Master",
                "slogan": "Here is Slogan"
                }
            ]
        }
        res = self.send.test_send_method("post",self.url,data=data)
        print(dumpJ(res))










if __name__ == '__main__':
    unittest.main()