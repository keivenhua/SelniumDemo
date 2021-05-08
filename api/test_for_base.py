import base64

import requests
import json

# def test_for_base4():
#     url = "http://127.0.0.1:9999/demo1.txt"
#     r = requests.get(url=url)
#     res = json.loads(base64.b64decode(r.content))
#     print(res)

class ApiRequests:

    def send(self,data:dict):
        res = requests.request(data["method"],data["url"],headers =data["headers"])
        if data["encoding"] == "base64":
            return json.loads(base64.b64decode(res.content))
        elif data["encoding"] == "private":
            return requests.post("url",data = res.content)