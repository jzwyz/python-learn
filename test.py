#!/usr/bin/python3

'''
多行注释
keyword 是python提供一个包,显示当前版本的所有关键字
导入包关键字 import <packagename>;
'''
import keyword

# 单行注释 像这样
print('Hello, World') # 输出 字符串

print(keyword.kwlist)

nums = [str(n) for n in keyword.kwlist]

print(','.join(nums))

# import this

print("----------\n")

ffg = (x for x in range(1,200))
fft = (1,2,3,4,4.5,5,6,7)

for f in fft:
    print('-----> f: %s' % (f))


import numpy