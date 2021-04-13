import pytest
import yaml


class Testdemo:
    # @pytest.mark.parametrize(("a,b"),[(10,20)])
    # def test1(self,a,b):
    #     print(a+b)

    @pytest.mark.parametrize('env',yaml.safe_load(open("./env.yml")))
    def test2(self, env):
        if "test" in env:
            print("这是测试环境", env['test'])
        elif "dev" in env:
            print("这是开发环境")

