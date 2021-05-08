import requests


def test_get_tocken():
    corpid = 'wwb183614ea47a13fc'
    corpsecret = 'cyd6sQ5dXTgKy3-RNg6iShhKgUp9TM-prkXOxJt4Rbs'

    res = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=%s&corpsecret=%s" %(corpid, corpsecret))
    return res.json()['access_token']



def test_post():
    data = {
   "name": "成都研发中心",
   "name_en": "RDCD",
   "parentid": 1,
   "order": 1,
   "id": 2
}
    res = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={test_get_tocken()}", json=data)
    print(res.json())