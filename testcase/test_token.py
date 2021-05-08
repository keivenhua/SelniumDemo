import requests
# from ApiPageObject.test_gettoken import getToken
from api.get_token import getToke

class TestToken:

    def setup(self):
        self.gettoken = getToke()

    def test_gets_token(self):
        assert self.gettoken.test_get_tocken().json()["errcode"] == 0