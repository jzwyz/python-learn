def foo():
    print('Hello Module1')


def main():
    print('__name__ : %s' % __name__)
    print('这里是该文件被直接运行才会执行的代码')
    print('此模块被导入不会执行此处的代码')


print('模块任何时候都会执行的代码 __name__ : %s' % __name__)

# __name__是Python中一个隐含的变量它代表了模块的名字
# 只有被Python解释器直接执行的模块的名字才是__main__
if __name__ == '__main__':
    main()
