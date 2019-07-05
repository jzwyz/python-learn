#!/usr/local/bin/python3

"""
字符串和常用数据结构
"""


def main():
    str = 'hello Python'
    print('计算字符串的长度: len(str) =  %d' % len(str))
    print('将首字母大写: str.capitalize() %s' % str.capitalize())
    print('将字符串转为大写: str.upper() %s' % str.upper())
    print('将字符串转为小写: str.lower() %s' % str.lower())
    print('查找字符串中指定的字符: str.find("Py")  %s' % str.find('Py'))  # 6
    print('查找字符串中指定的字符: str.find("py")  %s' % str.find('py'))  # -1
    # print('查找字符串中指定的字符: str.index("Py")  %s' % str.index('Py'))
    # print('查找字符串中指定的字符: str.index("py")  %s' % str.index('py')) # 与 find 一样,但找不到会抛出异常
    print('是否以指定字符开始: str.startswith("he") %s' % str.startswith('he'))  # True
    print('是否以指定字符开始: str.startswith("He") %s' % str.startswith('He'))  # False
    print('是否以指定字符结束: str.endswith(\'on\') %s' % str.endswith('on'))  # True
    print('指定宽度居中,在两边填充指定字符: str.center(50, \'*\') %s' % str.center(50, '*'))
    print('指定宽度靠[l/r]放置,在对边填充指定字符: str.rjust(50, \'*\') %s' %
          str.rjust(50, '*'))  # str.ljust(50, '*')
    str = 'abc123456789'  # 字符串的切片
    print('根据下标截取: str[2]  %s' % str[2])  # 0正序开始, -1倒叙开始
    print('取区间: str[2:5] %s' % str[2:5])  # 包含开始,不包含结束字符
    print(str[2:])  # c123456789 从下标2开始 到最后
    print(str[2::2])  # c2468    从下标2开始,增量为2,到结束
    print(str[::-1])  # 987654321cba  反序
    print(str[-3:-1])  # 78
    print(str[-1:-3])  # 无输出
    print('是否由数字构成 %s' % str.isdigit())
    print('是否由字母构成 %s' % str.isalpha())
    print('是否由数字和字母构成 %s' % str.isalnum())
    str = '  jiangzwyz@qq.com  '
    print('字符串去两边空格: a%sb' % str.strip())


"""
除了字符串, python还有多种类型的数据结构: 列表、元组、集合和字典

[1,2,'json']            列表: 数组
(1,2,3,4,5)            元组: 不可修改列表
{1,2,3,4,5}            集合: 同数学中的集合, 不可重复, 可以技术 交集、并集、差集等运算
{'name':'json','sex':'男'} 字典: 每一个元素都是由 “键值对” 组成
"""



if __name__ == "__main__":
    main()
