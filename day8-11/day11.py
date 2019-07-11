#!/usr/local/bin/python3
"""
文件操作和异常处理及JSON数据
"""

import json


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


def writh(cmd='w'):
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


def with_def():
    """
    使用with关键字,指定文件对象的上下文环境并在离开上下文环境时自动释放文件资源
    """
    try:
        """一次读取所有文件"""
        with open('a.txt', 'r', encoding='utf-8') as f1:
            print(f1.read())

        """使用for-in逐行读取"""
        with open('a.txt', encoding='utf-8', mode='r') as f2:
            for line in f2:
                print(line, end='')
    except Exception:
        print('错误', Exception)


def buffer_file_def():
    """读取二进制文件(拷贝图片)"""
    try:
        """复制文件"""
        with open('/Users/aolei/Pictures/my images/32916897.jpg', mode='rb') as f:
            data = f.read()
            print(data)

        """粘贴到当前目录下"""
        with open('head.jpg', mode='wb') as f:
            f.write(data)
            print('Copy Success')
    except FileNotFoundError :
        print('文件不存在')
    except UnicodeEncodeError:
        print('编码异常')


def json_data_def():
    """python对json数据的处理"""
    myuser = {
        'name':'李黑',
        'sex': '男',
        'age': 0,
        'qq': 957658,
        'friends': ['王大锤', '白元芳'],
        'cars': [
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320}
        ]
    }

    try:
        """将python字典对象序列化为json文件"""
        with open('users.json', 'w', encoding='utf-8') as f:
            json.dump(myuser, f)

        """将json文件反序列化为python字典对象"""
        with open('users.json', 'r', encoding = 'utf-8') as f:
            curr_user = json.load(f)
            print(curr_user)
    except IOError:
        print('文件写入失败')


if __name__ == "__main__":
    # read()
    # writh('a')
    # with_def()
    # buffer_file_def()
    json_data_def()
