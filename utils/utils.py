import json


def DumpJ(dict_json):
    """
    格式化字典数据
    :param dict_json:
    :return:
    """
    res = json.dumps(dict_json, indent=2, ensure_ascii=False)
    return res
