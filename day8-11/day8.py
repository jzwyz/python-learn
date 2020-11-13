#!/usr/local/bin/python3

"""
第八天: 面向对象
"""

'''
创建类 使用关键字 class
特殊方法 __init__() 初始化类时执行的方法
'''
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def study(self, course_name):
        print('%s正在学习%s.' % (self.name, course_name))

    def watch_movie(self):
        if self.age < 18:
            print('%s 小于18岁,只能观看《熊出没》' % self.name)
        else:
            print('%s 正在...' % self.name)

def main():
    stu = Student('小明', 17)
    stu.study('《Python100天》')
    stu.watch_movie()
    stu1 = Student('老明', 33)
    stu1.study('《...》')
    stu1.watch_movie()


'''
访问可见性
python 中只有两种 公开的和私有的
实现: 使属性私有,只需要在属性名称前加两个 _ (下划线)
实际上,Python并没有从语法上严格保证私有属性或方法的私密性,只是通过语法限制了属性或方法的访问,
'''

if __name__ == "__main__":
    main()
