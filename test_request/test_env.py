import requests
import yaml


class Api:

    env = yaml.safe_load(open("env.yaml"))


    def send(self,data:dict):
        data["url"] = str(data["url"]).replace("testing-studio",self.env["testing-studio"][self.env["default"]])
        r = requests.request(method=data["method"],url =data["url"],headers=data["headers"])
        print(r.text)