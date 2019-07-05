#!/usr/local/bin/python3
"""
函数和模块的使用

函数不能重载
函数命名规则同变量命名规则

"""


"""
def 函数定义, 和实现阶乘
"""

def jcfun(num):
    """
    求阶乘
    
    :param num: 非负整数
    :return: num的阶乘
    """
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

print(jcfun(3))


"""
函数的参数:
"""

'函数的参数可以设置默认值'
def myfun(a=0):
    return a
print(myfun(), myfun(3))

'函数的参数可以设置为可变参数  在参数前加上*'
def my_fun_1(*args):
    for i in args:
        print(i, end = '\t')
my_fun_1(1,2,3,4,5,6,7)

'函数的参数赋值顺序可以不一致'
def my_fun_2(a=0,b=0,c=1):
    print(a, b, c)
my_fun_2()
my_fun_2(c=3, b=1, a='asd')
my_fun_2(3,4,5)


"""
模块的使用

对于任何一种编程语言来说，给变量、函数这样的标识符起名字都是一个让人头疼的问题，因为我们会遇到命名冲突这种尴尬的情况。
最简单的场景就是在同一个.py文件中定义了两个同名函数
由于Python没有函数重载的概念，那么后面的定义会覆盖之前的定义，也就意味着两个函数同名函数实际上只有一个是存在的

定义模块 1、 2

导入模块使用: import <modeul_name> / form <modeul_name> import <def> / import <modeul_name> as <alis>
import module1
from module2 import foo
import module1 as m1
"""

'使用模块名.函数名'
import module1, module2

module1.foo()
module2.foo()

'从模块中导出foo函数, 这种方式如果同时导出1、2中的foo,后面导入的会覆盖前面的foo'
from module1 import foo
foo()
from module2 import foo
foo()

'给模块设置别名'
import module1 as m1
import module2 as m2

m1.foo()
m2.foo()

'''
被导入的模块中可能会存在其他可以执行代码,这个时候我们导入模块,python解释器就会执行它们;
现实中我们可能不会希望如此,因此我们需要添加一些条件来限制可以执行代码的运行的时间
__name__是Python中一个隐含的变量它代表了模块的名字
只有被Python解释器直接执行的模块的名字才是__main__
'''


"""
练习:
1.实现计算求最大公约数和最小公倍数的函数。
2.实现判断一个数是不是回文数的函数。
3.实现判断一个数是不是素数的函数。
4.写一个程序判断输入的正整数是不是回文素数。
"""


"""
变量作用域的问题

内置作用域、全局作用域、嵌套作用域、局部作用域
"""

global_aaa = '全局作用域'
def aaa_def():
    bbb = '局部作用域'
    # global aaa # 指定该变量是全局作用域中的
    aaa = 200
    def bbb_def():
        print('在bbb_def中能使用bbb是因为bbb存在于bbb_def的 嵌套作用域 中 : %s' % bbb)
        """
        这里输出的值为200, 因为在 aaa_def函数中,并不是修改全局变量aaa=200, 而是重新创建了一个局部变量aaa.
        除非在创建变量前 加上 global 关键字, 指定该变量是全局作用域中的
        """
        print(aaa)
    bbb_def()

if __name__ == "__main__":
    aaa = 100
    aaa_def()
    
