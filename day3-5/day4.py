#!/usr/local/bin/python3
import random
from math import sqrt

"""
循环结构

for-in循环
while循环
"""


"""
for-in循环

range可以用来产生一个不变的数值序列
range(101) 产生 0 - 100 的整数
range(1,101) 产生 1 - 100 的整数
range(1, 101, 2) 产生一个1到99的奇数序列，其中的2是步长，即数值序列的增量。
"""
sum = 0
for i in range(1, 101, 2):
    sum += i
    # print(i)
print(sum)

"""
while 循环

猜数字游戏
计算机出一个1~100之间的随机数由人来猜
计算机根据人猜的数字分别给出提示大一点/小一点/猜对了
"""

sjs = random.randint(1, 100)
count = 0
msg = '猜一个数字:'
while False:
    count += 1
    younum = int(input(msg))
    if younum > sjs:
        msg = '小一点:'
    elif younum < sjs:
        msg = '大一点:'
    else:
        print('猜对了, 答案为: %d' % (sjs))
        break
print('你总共猜了%d次' % (count))
if count > 7:
    print('智商堪忧呀,小伙子')


"""
练习1：输入一个数判断是不是素数。

素数: 一个正整数除了1和他本身外,不会再有其他的因数(不能被整除)
"""

number = int(input('请输入一个正整数:'))
numpfg = int(sqrt(number))
is_ss = True
for i in range(2, numpfg):
    if number % i == 0:
        is_ss = False
        break
if is_ss and number != 1:
    print('%d 是素数' % (number))
else:
    print('%d 不是素数' % (number))

"""
练习2：输入两个正整数，计算最大公约数和最小公倍数。
"""

"""
练习3：打印三角形图案。
"""

"""
练习4: 打印9x9乘法表
"""

for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d * %d = %d' % (j, i, i*j), end = '\t')
    print('')
