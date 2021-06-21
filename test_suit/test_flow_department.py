"""
流程测试：
新增-查询-修改-查询-删除-查询
"""
import unittest

from test_suit.department_interface import DepartmentInterment
from utils.get_keywords import GetkeyWords
from utils.utils import dumpJ


class DepartmentFlowTest(unittest.TestCase):

    def setUp(self):
        self.url = "http://127.0.0.1:8000/api/departments/"
        self.dp = DepartmentInterment(self.url)
        self.gk = GetkeyWords()

    def test_flow(self):
        dep_id = "T03"
        data = {
            "data": [
                {
                    "dep_id": dep_id,
                    "dep_name": "三级片学院",
                    "master_name": "阅尽天下a片",
                    "slogan": "心中无码"
                }
            ]
        }

        # 新增
        add_result = self.dp.add_department(data)
        # print(dumpJ(add_result["create_success"]))
        count = self.gk.get_keyword(add_result["create_success"], "count")
        self.assertEqual(count, 1, "添加账户失败")

        add_dep_id = self.gk.get_keyword(add_result["create_success"], "dep_id")
        self.assertEqual(add_dep_id, dep_id, "添加失败")

        # 查询
        get_result = self.dp.get_department({"$dep_id_list": dep_id})
        # print(dumpJ(get_result))
        get_dep_id = self.gk.get_keyword(get_result, "dep_id")
        self.assertEqual(get_dep_id, dep_id, "查询失败")

        # 更新
        dep_name = "av学院"
        update_data = {
            "data": [
                {
                    "dep_id": dep_id,
                    "dep_name": dep_name,
                    "master_name": "阅尽天下a片",
                    "slogan": "心中无码"
                }
            ]
        }
        update_result = self.dp.update_department(dep_id, update_data)
        # print(dumpJ(update_data))
        get_dep_name = self.gk.get_keyword(update_result, "dep_name")
        self.assertEqual(get_dep_name, dep_name, "更新失败")


        # 删除
        delete_data = {
            "$dep_id_list": dep_id
        }
        delete_result = self.dp.delete_department(delete_data)
        # print(dumpJ(delete_result))
        self.assertEqual(delete_result,204,"删除失败")

        # 查询
        get_results = self.dp.get_department({"$dep_id_list":dep_id})
        # print(dumpJ(get_results))
        self.assertEqual(self.gk.get_keyword(get_results,"count"),0,"删除后查询失败")


if __name__ == '__main__':
    unittest.main()
