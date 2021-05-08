from string import Template

import requests
import yaml

from api.base_api import BaseApi


class getToke(BaseApi):

    corpid = 'wwb183614ea47a13fc'
    corpsecret = 'cyd6sQ5dXTgKy3-RNg6iSv0jM8pdhLb7jYHCj_WlLQM'

    def template(self):
        with open("./get_token.yaml") as f:
            # print(f.read())
            # print(type(f.read()))
            data = {
                "corpid": self.corpid,
                "corpsecret": self.corpsecret
            }
            re = Template(f.read()).substitute(data)
            return yaml.safe_load(re)


    def test_get_tocken(self):

        # url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        # params = {
        #     "corpid":self.corpid,
        #     "corpsecret":self.corpsecret
        # }
        # res = requests.get(url=url,params=params)
        # print(res.json())

        # return res.json()['access_token']
        # return res
        req = self.template()
        r = self.requests_http(req)
        print(r.json())
        return r
if __name__ == '__main__':
    a = getToke()
    a.test_get_tocken()
