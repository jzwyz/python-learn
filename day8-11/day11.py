#!/usr/local/bin/python3
"""
文件操作和异常处理及JSON数据
"""


def read():
    """读取文件"""
    try:
        fs = open('a.txt', 'r', encoding='utf-8')
        print(fs.read())
    except FileNotFoundError:
        print('文件不存在')
    finally:
        if fs:
            fs.close()


def writh(cmd = 'w'):
    """写文件"""
    try:
        txt = (x for x in range(600, 1000))
        fs = open('b.txt', cmd, encoding='utf-8')
        for t in txt:
            fs.write(str(t) + '\n')
    except IOError:
        print('IO异常')
    finally:
        if fs:
            fs.close()

if __name__ == "__main__":
    # read()
    writh('a')
