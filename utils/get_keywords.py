class GetKewords(object):


    def get_keyword(self,data,keyword):
        if keyword in data.keys():
            return data[keyword]
        else:
            for item in data.values():
                if isinstance(item,list):
                    for v in item:
                        result = self.get_keyword(v,keyword)
                        if result or result == 0 or (result is not None and result is not False):
                            return result
                elif isinstance(item,dict):
                    result = self.get_keyword(item,keyword)
                    if result or result == 0 or (result is not None and result is not False):
                        return result


    def get_keywords(self,data,label,keword):
        """
        获取多个值
        :param data:
        :param label:
        :param keword:
        :return:
        """
        new_data = self.get_keyword(data,label)
        if isinstance(new_data,list):
            values = []
            for v in new_data:
                values.append(v[keword])
            return values

if __name__ == '__main__':
    # data = {
    #     "count":1,
    #     "results":[
    #         {
    #             "username":"小三"
    #         },
    #         {
    #             "username":"李四"
    #         }
    #     ],
    #     "goods":[
    #         {
    #             "name":"肥皂",
    #             "status":[
    #                 {"status_name":"精品"},
    #                 {"status_name":"新品"}
    #             ]
    #         }
    #     ],
    #     "userinfo":{"username2":"xiaosan"}
    # }
    data = {
        "already_exist": {
            "count": 0,
            "results": []
        },
        "create_success": {
            "count": 1,
            "results": [
                {
                    "dep_id": "T88",
                    "dep_name": "黄色学院",
                    "master_name": "Test-Master",
                    "slogan": "Here is Slogan"
                }
            ]
        }
    }

    gk = GetKewords()
    print(gk.get_keywords(data, "status","status_name"))
    print(gk.get_keyword(data["create_success"],"count"))
    print(type(gk.get_keyword(data["create_success"],"count")))