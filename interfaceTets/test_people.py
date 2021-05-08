
import requests
import pytest

def test_get_tocken():
    corpid = 'wwb183614ea47a13fc'
    corpsecret = 'cyd6sQ5dXTgKy3-RNg6iSnfDnzlywh7hGrRvRC1ApQE'

    res = requests.get(
        "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=%s&corpsecret=%s" % (corpid, corpsecret))
    return res.json()['access_token']

def test_post(userid,name,department):
    data = {
        "userid": userid,
        "name": name,
        "department": department,
        "mobile": 13883928982
    }
    res = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={test_get_tocken()}",
                       json=data)
    # return res.json()
    print(res.json())

test_post('hu123', 'kdjfalf',1)



    # def test_get(userid):
    #     res = requests.get(
    #         f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={test_get_tocken()}&userid={userid}")
    #     return res.json()
    #
    # def test_put(userid, name, mobile):
    #     data = {
    #         "userid": userid,
    #         "name": name,
    #         "mobile": mobile
    #     }
    #
    #     res = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={test_get_tocken()}",
    #                         json=data)
    #     return res.json()
    #
    # def test_delete(userid):
    #     res = requests.get(
    #         f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={test_get_tocken()}&userid={userid}")
    #     return res.json()


    # @pytest.mark.parametrize("userid,name,department", [("0005","CM","1")])
    # def test_all(userid,name,department):
    #     # try:
    #     assert "created. Warning: wrong json format. " == test_post(userid,name,department)["errmsg"]
    #     # except AssertionError as exL:
    #         # print(exl)
    #     assert name == test_get(userid)["name"]
    #     assert "updated" == test_put(userid,"CX",department)["errmsg"]
    #     assert "成霞" == test_get(userid)["name"]
    #     assert "deleted" == test_delete(userid)["errmsg"]
    #     assert 60111 == test_delete(userid)["errcode"]