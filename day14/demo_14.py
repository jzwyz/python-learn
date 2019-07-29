#!/usr/local/bin/python3

"""
网络编程
"""

import requests
import json

tx_gdqs_url = 'http://api.tianapi.com/txapi/qingshi/?key=53b2ef1f4bc1d51fb6b51ca63bf01f30'

def main():
    response = requests.get(tx_gdqs_url)
    ret = response.json()
    print(ret)

if __name__ == '__main__':
    main()
    
    
