import requests

class getToken:

    corpid = 'wwb183614ea47a13fc'
    corpsecret = 'cyd6sQ5dXTgKy3-RNg6iSv0jM8pdhLb7jYHCj_WlLQM'
    def test_get_tocken(self):

        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        params = {
            "corpid":self.corpid,
            "corpsecret":self.corpsecret
        }
        res = requests.get(url=url,params=params)
        # print(res.json())

        # return res.json()['access_token']
        return res

# if __name__ == '__main__':
#     a = TestToken()
#     a.test_get_tocken()
