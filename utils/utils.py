import json


def dumpJ(dict_data):
    """
    将字典格式化输出
    :param dict_data:
    :return:
    """
    json_str = json.dumps(dict_data,indent=2,ensure_ascii=False)
    return json_str