#!/usr/local/bin/python3

import math
# 或 from math import math

"""
python学习第二天, 基本语法
1. 变量类型
"""

"""
变量命名
变量使用
使用占位符格式化字符串输出(占位符貌似只能使用int类型赋值)
"""
a = 1
b = 2
print('除法 1 / 2 =', 1/2)
print('格式显示 取整: %d / %d = %d' % (a, b, 1//2))


"""
使用input()函数获取用户输入的值
使用int()将值进行类型转换
"""
# c = int(input('c = '))
# print('输入的: %d' % (c))


"""
type() 判断类型
"""
# d = input('d = ')
# e = 2
# f = 1.2j + e
# g = 'Hello'
# h = True
# print(type(d))
# print(type(e))
# print(type(f))
# print(type(g))
# print(type(h))


"""
练习1
将华氏温度转换为摄氏温度
F = 1.8C + 32
格式化处 %.2f 表示精确2位小数,f是单位
"""

# hs = float(input('输入华氏温度:'))
# ss = (hs - 32) / 1.8
# print('%.2f华氏度 = %.2f摄氏度' % (hs, ss))


"""
输入半径计算圆的周长和面积

圆的周长 = π*d
        = 2πr
圆的面积 = 𝞹rr
"""

# radius = float(input('请输入圆的半径:'))
# perimeter = 2 * radius * math.pi
# area = radius * radius * math.pi
# print('圆的周长:%.2f' % (perimeter))
# print('圆的面积:%.2f' % (area))


"""
输入年份 如果是闰年输出True 否则输出False

四年一润,百年不润,四百年又润

如果代码太长写成一行不便于阅读 可以使用\或()折行
"""

year = int(input('输入年份:'))
is_leap = (year % 4 == 0 and year % 100 != 0
            or year % 400 == 0)
print(is_leap)