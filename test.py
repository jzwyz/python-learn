#!/usr/local/bin/python3

'''
多行注释
keyword 是python提供一个包,显示当前版本的所有关键字
导入包关键字 import <packagename>;
'''
import keyword;



# 单行注释 像这样
print('Hello, World'); # 输出 字符串

print(keyword.kwlist);

nums = [str(n) for n in keyword.kwlist]

print(','.join(nums));