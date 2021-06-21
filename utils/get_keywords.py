

class GetkeyWords(object):

    def get_keyword(self,data,keyword):
        """
        获取单个关键字的值
        :param data: 数据源字典
        :param keyword: 关键字的名字
        """
        if keyword in data.keys():
            return data[keyword]
        else:
            for v in data.values():
                if isinstance(v,list):
                    for item in v:
                        result = self.get_keyword(item,keyword)
                        if result or result == 0 or (result is not None and result is not False):
                            return result
                elif isinstance(v,dict):
                    result = self.get_keyword(v,keyword)
                    if result or result == 0 or (result is not None and result is not False):
                        return result

    def get_keywords(self,data,lebal,keyword):
        """
        根据关键字查询多个字段
        :param data: 数据源字典
        :param lebal: 对应关键字的上层关键字
        :param keyword: 关键字名字
        """
        newdata = self.get_keyword(data,lebal)
        if isinstance(newdata,list):
            value = []
            for item in newdata:
                value.append(item[keyword])
            return value


if __name__ == '__main__':
    data = {
        "count":1,
        "result":[
            {
                "username":"小三"
            },{
                "username":"李四"
            }
        ],
        "goods":[
            {
            "name":"肥皂",
             "status":[
                 {"name1":"av"},
                 {"name":"无码"}
             ]
            }
        ],
        "userinfo":{"username2":"kevin"}
    }

    gk = GetkeyWords()
    res = gk.get_keyword(data,"username")
    print(res)