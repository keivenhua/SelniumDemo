import pytest

# def test_one():
#     print("test_one")
#     x = 'this'
#     assert 'h' in x
#
# def test_two():
#     print("开始执行test_two方法")
#     x = 'this'
#     assert 'h' in x
#
# def test_three():
#     print("test_three")
#     x = 'this'
#     assert 'h' in x

@pytest.mark.parametrize(('a','b'),[(10,20),(100,200)])
def test_param(a,b):
    print(a+b)

if __name__ == '__main__':
    pytest.main('-v -x')