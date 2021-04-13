import unittest


class demo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('setupclass')

    @classmethod
    def tearDownClass(cls):
        print('teardownclass')

    def setUp(self):
        print("setup")

    def tearDown(self):
        print("teardown")

    def test_case01(self):
        print("test_case01")
        self.assertEqual(2, 2, "判断相等")
        # self.assertIn("h", "this")

    # @unittest.skip()
    def test_case02(self):
        print("test_case02")
        # self.assertEqual(2, 2, "判断相等")
        self.assertIn("h", "this")


if __name__ == '__main__':
    # unittest.main()
    suit = unittest.TestSuite()
    suit.addTest(demo(""))