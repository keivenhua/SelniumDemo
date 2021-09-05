import json
import unittest

from test_suit.department_interface import DepartmentInterface
from utils.get_keywords import GetKewords
from utils.utils import DumpJ


class DepartmentFlowTest(unittest.TestCase):


    def setUp(self):
        self.url = 'http://127.0.0.1:8000/api/departments/'
        self.dp = DepartmentInterface(self.url)
        self.gk = GetKewords()

    def test_flow(self):
        dep_id = 'T18'
        data = {
            "data": [
                {
                    "dep_id": dep_id,
                    "dep_name": "黄色学院",
                    "master_name": "Test-Master",
                    "slogan": "Here is Slogan"
                }
            ]
        }

        # add_result = json.loads(self.dp.add_department(data))
        # count = self.gk.get_keyword(add_result["create_success"],"count")
        # self.assertEqual(count,1,"新增失败")
        # print(add_result)
        # add_dep_id = self.gk.get_keyword(add_result["create_success"],"dep_id")
        # self.assertEqual(add_dep_id,dep_id,"新增失败")
        #
        # 查询
        datas = {"$dep_id_list":"T02"}
        get_result = self.dp.get_department(data=datas)
        print(get_result.json())
        # get_dep_id = self.gk.get_keyword(get_result,'dep_id')
        # print(get_dep_id)
        # self.assertEqual(get_dep_id,dep_id,"查询失败")


if __name__ == '__main__':
    unittest.main()


