import yaml


def test_yaml():
    corpid = 'wwb183614ea47a13fc'
    corpsecret = 'cyd6sQ5dXTgKy3-RNg6iSv0jM8pdhLb7jYHCj_WlLQM'
    req = {
        "method": "get",
        "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
        "params": {
            "corpid": corpid,
            "corpsecret": corpsecret
        }
    }

    with open("get_token.yaml","w") as f:
        yaml.safe_dump(data=req,stream=f)
