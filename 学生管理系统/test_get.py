import json

import pytest
import requests


class TestGetText():

    def test_get(self):
        url = "http://127.0.0.1:8000/api/departments/"

        data = {"$dep_id_list":"T01,T03,T05"}


        response = requests.get(url=url,params=data)

        print(response.status_code)
        print(response.text)
        print(type(response))
        print(json.dumps(response.json(), indent=2, ensure_ascii=False))


if __name__ == '__main__':
    pytest.main()