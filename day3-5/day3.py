#!/usr/local/bin/python3

import getpass

"""
分支结构

if elif else
"""

# username = input('输入用户名:')
# password = getpass.getpass('输入密码:') # getpass 模块可以让控制台输入的密码不可见

# if username == 'admin' and password == 'json':
#     print('login success!')
# else:
#     print('login error: tar ager')


"""
分段函数求值

        3x - 5  (x > 1)
f(x) =  x + 2   (-1 <= x <= 1)
        5x + 3  (x < -1)
"""

x = float(input('输入x(最多两位小数):'))
if x > 1:
    y = 3 * x - 5
elif x >= -1 and x <= 1:
    y = x + 2
else:
    y = 5 * x + 3
print('f(%.2f) = %.2f' % (x, y))