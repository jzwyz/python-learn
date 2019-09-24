#!/usr/local/bin/python3

"""
字符串与正则表达式
"""

import re


def main():
    # p = r'\?'
    # str = 'https://images.unsplash.com/photo-1563220552-d1c3e94df113?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max'
    # print(re.split(r'photo-', re.split(p, str)[0])[1])
    strr = r'^(http:\/\/)?(?<site>[a-zA-Z]+\.)?jzwyz.com$'
    site = 'http://jzwyz.com'
    print(site.partition(strr))


if __name__ == "__main__":
    main()
