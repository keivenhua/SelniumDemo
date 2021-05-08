import pytest


@pytest.fixture()
def login():
    print("需要登录")


class TestDemo:

    #
    # def setup_class(self):
    #     print("setup_class")
    #
    # def setup(self):
    #     print("打开浏览器")
    #
    # def teardown(self):
    #     print("关闭浏览器")

    def test_a(self, login):
        print('test_a')

    def test_b(self, login):
        print('test_b')

    def test_c(self, login):
        print('test_c')
