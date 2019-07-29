#!/usr/local/bin/python3

"""
天行数据
菜谱大全
http://api.tianapi.com/txapi/caipu/
请求方式 https/http GET
参数
key  天行账户KEY
num  返回结果数
word 查询关键字
"""

import requests
import json

http_url = 'http://api.tianapi.com/txapi/caipu/'


def get_caipu(word, num=10):
    """查询关键字"""
    params = {'key': '53b2ef1f4bc1d51fb6b51ca63bf01f30',
              'num': num, 'word': word}
    response = requests.get(http_url, params=params)
    result = response.json()
    print(result)

if __name__ == "__main__":
    get_caipu('土豆', 10)