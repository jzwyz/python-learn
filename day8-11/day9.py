#!/usr/local/bin/python3
from time import time, localtime, sleep
from abc import ABCMeta, abstractmethod

"""
面向对象进阶

装饰器:
在day8中,说到了私有属性, 我们可以通过装饰器来实现属性的 get/set 方式,从而使得属性的访问既安全又方便

__slots__ 魔法:
Python 是一个动态语言,所以Python可以在运行时给类添加属性或方法;
如果我们需要限定类只能绑定部分属性,可以通过__slots__来限定;
需要注意的是__slots__只对当前类生效;

静态方法和类方法:
静态方法使用 @staticmethod 装饰器, 类名.调用;
类方法 @classmethod 装饰器, 类方法的第一个参数约定名为cls，它代表的是当前类相关的信息的对象（类本身也是一个对象，有的地方也称之为类的元数据对象
    通过这个参数我们可以获取和类相关的信息并且可以创建出类的对象。

类与类的关系:
is-a  继承关系, 如:学生和人、手机与电子产品
has-a 合成关系, 如:部门和员工、汽车和引擎
use-a 依赖关系, 如:司机和驾驶行为

继承和多态:
在已有类的基础上创建新类;
提供继承信息的我们称之为父类，也叫超类或基类；得到继承信息的我们称之为子类，也叫派生类或衍生类;
里氏替换原则;
子类实现父类的方法,并给出新的版本, 这个动作称之为方法重写(override)
    通过方法重写不同子类出现不同的行为,这个就是多态(poly-morphism)
    多态简单点说就是:同样的方法做了不同的事情;

"""


class Person(object):

    '''
    __slots__ 限定Person对象只能绑定_name, _age和_gender属性
    '''
    __slots__ = ('_name', '_age', '_gender')

    def __init__(self, name, age):
        self._name = name
        self._age = age

    # 访问器 - getter 方法
    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    # 修改器 - setter 方法
    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age >= 18:
            print('%s 正在玩扑克' % self._name)
        else:
            print('%s 正在玩飞行棋' % self._name)

    def watch_av(self):
        if self._age >= 18:
            print('%s 大于18岁, 可以看点不一样的视频哦' % self._name)
        else:
            print('%s 只能观看 熊出没 哦' % self._name)


class Triangle(object):
    """
    示范 静态方法
    三角形工具
    """

    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    @staticmethod
    def is_valid(a, b, c):
        '''
        是否可以构成三角形
        '''
        return a + b > c and a + c > b and b + c > a

    def perimeter(self):
        '''
        计算三角形周长
        '''
        return self._a + self._b + self._c

    def area(self):
        '''
        计算三角形面积
        '''
        return 'wait...'


class Clock(object):
    """
    示范 类方法
    数字时钟
    """

    def __init__(self, hour=0, minute=0, second=0):
        self._hour = hour
        self._minute = minute
        self._second = second

    @classmethod
    def now(cls):
        """
        获取当前时间为开始的数字时钟
        """
        ctime = localtime(time())
        return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)

    def run(self):
        """
        运行数字时钟
        """
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        """
        显示当前时间
        """
        print('%02d:%02d:%02d' % (self._hour, self._minute, self._second))


class Student(Person):
    """
    示例: 继承 Person 类 
    学生
    """

    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        self._grade = grade

    def study(self, course):
        print('学生 %s 正在学习 %s' % (self._name, course))


class Tencher(Person):
    """
    示例: 继承 Person 类
    老师
    """

    def __init__(self, name, age, title):
        super().__init__(name, age)
        self._title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    def teach(self, course):
        print('%s %s 正在讲述 %s' % (self.title, self.name, course))


class Pet(object, metaclass=ABCMeta):
    """
    将Pet类处理成一个抽象类;
    抽象类就是不能够创建对象的类;
    Python从语法层面并没有像Java或C#那样提供对抽象类的支持;
    通过abc模块的ABCMeta元类和abstractmethod包装器来达到抽象类的效果;
    如果一个类中存在抽象方法那么这个类就不能够实例化;

    宠物
    """

    def __init__(self, nickname):
        self._nickname = nickname

    @abstractmethod
    def make_voice(self):
        """发出声音的方法"""


class Dog(Pet):
    """狗"""

    def make_voice(self):
        print('狗狗 %s 汪汪汪...' % self._nickname)


class Cat(Pet):
    """猫"""

    def make_voice(self):
        print('猫咪 %s 喵喵喵...' % self._nickname)


def main():
    a = Person('asd', 10)
    a.play()
    a.age = 33
    a.play()
    a._gender = 'dadss'
    # a._is_noe = 'assd'; error: 'Person' object has no attribute '_is_noe'

    if Triangle.is_valid(2, 3, 4):
        tri = Triangle(2, 3, 4)
        print(tri.perimeter())
        print(tri.area())
    else:
        print('无法构成三角形')

    stu = Student('小明', 16, '高三')
    ter = Tencher('老张', 33, '初级教授')
    stu.play()
    ter.play()
    stu.watch_av()
    ter.watch_av()
    stu.study('数学')
    ter.teach('地理')

    pets = [Dog('旺财'), Cat('汤姆')]
    for pet in pets:
        pet.make_voice()


def clock_main():
    clock = Clock.now()
    while True:
        clock.show()
        sleep(1)
        clock.run()


if __name__ == "__main__":
    main()
