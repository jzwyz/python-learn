#!/usr/local/bin/python3

import sys
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


def list_main():
    list1 = [1, 2, 3, 4, 5, 'Jason']
    print(list1)
    print(len(list1))
    list2 = ['python'] * 5
    print(list2)
    print(list1[0])
    print(list1[-1])  # 如果该下标不存在,则抛出异常
    list1[2] = 100  # 根据下标修改元素
    print(list1)
    # 添加元素
    list1.append(200)
    list1.insert(1, 101)  # 指定下标 1 插入 101
    list1 += ['ads', 'ads']  # 同 append()
    print(list1)
    list1.remove(2)  # 删除指定下标的元素
    list2.clear()  # 清空列表
    print(list1)
    print(list2)
    # 列表跟字符串一样也可以通过切片来取值


def list_sort_main():
    lists = ['java', 'python', 'nodejs', 'go',
             '.net', 'c/c++', 'sql', 'php', 'shell']
    # sorted函数返回列表排序后的拷贝不会修改传入的列表
    # 函数的设计就应该像sorted函数一样尽可能不产生副作用
    list1 = sorted(lists)
    print(list1)
    list2 = sorted(lists, reverse=True)  # reverse 反向标示
    print(list2)
    print(lists)
    list3 = sorted(lists, key=len, reverse=True)  # 根据字符串长度排序,而非默认的字母表排序
    print(list3)
    lists.sort(reverse=True)  # 直接操作列表本身
    print(lists)


def list_create_main():
    """
    通过列表的生成式语法列创建列表
    """
    f = [x for x in range(1, 100)]
    print(f)
    f = [x + y for x in 'ABCDE' for y in '1234567890']
    print(sys.getsizeof(f))  # 查看对象占用内存的字节数
    print(f)
    """
    用这种方式创建列表之后元素已经准备好,所以会消耗较多的内存

    下面示例的是 通过生成器创建列表,这种方式生产的不是列表,而是一个生成器对象
    通过生成器可以获取到数据但是它不占用额外的内存空间
    每次使用数据时就通过内部计算的到数据,(需要消耗额外的时间)
    """
    f = (x ** 2 for x in range(1, 100))
    print(sys.getsizeof(f))
    print(f)  # 输出的是生成器对象
    for i in f:
        print(i)
    """
    通过 yield 关键字将普通函数转化为 生成器, 如斐波拉契数案例
    """
    def fil(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a+b
            yield a
    for i in fil(20):
        print(i)

"""
元组
"""

def tuple_main():
    t = ('Java', 'Python', 'c/c++', 'nodejs')
    # t = ('xm', 'xh', 'xq') # 重新给t赋值,前者会被回收
    # t[0] = 1  TypeError: 'tuple' object does not support item assignment
    print(t)
    lists = list(t) # 转数组
    print(lists)
    lists.sort(reverse=True)
    tt = tuple(lists) # 转元组
    print(tt)
    """
    思考: 为什么有了列表还要元组
    1. 在多线程环境下,避免一些元素不被修改、不变对象自动就是线程安全的、易维护、节省同步化开销方便共享访问
    2. 元组在创建时间和内存消耗上都优于列表
    """

"""
集合 set
"""
def set_main():
    sets = { 1,2,3,3,3,2,13,12,34,3,45,34,3,45,3,2,3,34 } # 创建集合
    print(sets) # 自动去重
    print(len(sets))
    sets1 = set(range(1, 50)) # 创建集合
    print(sets1)
    sets.add(44) # 添加元素
    sets.add(49)
    sets.update([3,333]) # 使用自己跟其他联合更新集合,(有的忽略,没有的添加)
    print(sets)
    t = (1,5,4,3,2,6,6,5)
    sets2 = set(t) # 将元组转为集合
    print(sets2)
    print(sets2.pop())
    if 333 in sets:
        sets.remove(333) # 移除不存在的元素会报错
    print(sets)
    for i in sets:
        print(i**2, end = ' ')
    '''
    求交、差、并集、对称插运算
    特殊运算符
    & set1.intersection(set2)
    | set1.union(set2)
    - set1.difference(set2)
    ^ set1.symmetric_difference(set2)
    '''
    print('')
    print('交集:', sets & sets1)
    print('并集:', sets | sets1)
    print('差集:', sets1 - sets)
    print('对称差:', sets1 ^ sets)
    # 判断子集和超集
    print(sets >= sets1)

"""
字典
"""
def dic_main():
    scores = { '小明': 60, '小红': 50 }
    print(scores)
    print(scores['小明'])
    for key in scores:
        print('%s = %d' % (key, scores[key]), end='; ')
    scores['Jason'] = 100
    scores['Abc'] = 99
    scores.update(Q=40, Z=87)
    print(scores)
    print(scores.get('xxh', 0)) # 如果不存在则返回 None get方法可以设置默认值
    print(scores.popitem()) # 从 字典末尾删除一个kv 并返回该kv
    print(scores.pop('Jasons', 5)) # 删除指定kv, 并返回该kv, 如果不存在则返回 5, 如果未指定 5 则抛出异常
    print(scores)
    scores.clear() # 清空字典
    print(scores)


"""
练习1：在屏幕上显示跑马灯文字
"""
import os
import time
def pmd_wenz():
    content = '北京欢迎你为你开天辟地…………'
    while True:
        # 清理屏幕上的输出
        os.system('clear')
        print(content.center(100))
        # 休眠200毫秒
        time.sleep(0.2)
        content = content[1:] + content[0]

if __name__ == "__main__":
    # main()
    # list_def()
    # list_sort_main()
    # list_create_main()
    # tuple_main()
    # set_main()
    # dic_main()
    pmd_wenz()
