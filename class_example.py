#!/usr/bin/env python3
'''
#类定义
class people:
    #定义基本属性
    name = ''
    age = 0
    #定义私有属性，私有属性在类外部无法直接进行访问
    __weight = 0

    #定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s 说 ：我 %d 岁。" % (self.name, self.age))


#实例化类
p = people('runoob', 10, 30)
p.speak()


#继承   #######################
#类定义
class people:
    #定义基本属性
    name = ''
    age = ''
    #定义私有属性，私有属性在类外部无法直接进行访问
    __weight = 0

    #定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s 说：我 %d 岁。" % (self.name, self.age))


#单继承示例
class student(people):
    grade = ''

    def __init__(self, n, a, w, g):
        #调用父类的构函
        people.__init__(self, n, a, w)
        self.grade = g

    #撰写父类的方法
    def speak(self):
        print("%s 说：我 %d 岁了，我在读 %d 年纪" % (self.name, self.age, self.grade))


s = student('ken', 10, 60, 3)
s.speak()


#############
###多继承
#类定义
class people:
    #定义基本属性
    name = ''
    age = 0
    #定义私有属性，私有属性在类外部无法直接进行访问
    __weight = 0

    #定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s 说：我 %d 岁。" % (self.name, self.age))


#单继承示例
class student(people):
    grade = ''

    def __init__(self, n, a, w, g):
        #调用父类的构函
        people.__init__(self, n, a, w)
        self.grage = g

    #撰写父类的方法
    def speak(self):
        print("%s 说：我 %d 岁了，我在读 %d 年纪" % (self.name, self.age, self.grade))


#另一个类，多重继承之前的准备
class speaker():
    topic = ''
    name = ''

    def __init__(self, n, t):
        self.name = n
        self.topic = t

    def speak(self):
        print("我叫 %s,我是一个演说家，我的演讲主题是%s" % (self.name, self.topic))


#多继承
class sample(speaker, student):
    a = ''

    def __init__(self, n, a, w, g, t):
        student.__init__(self, n, a, w, g)
        speaker.__init__(self, n, t)


test = sample("Tim", 25, 80, 4, "Python")
test.speak()  #方法名同，默认调用的是在括号中排前的父类的方法



######################
###方法重写#####
class Parent:
    def myMethod(self):
        print('调用父类方法')


class Child(Parent):
    def myMethod(self):
        print('调用子类方法')


c = Child()
c.myMethod()
###super()函数是用于调用父类(超类)的一个方法
super(Child, c).myMethod()



###################
###类的私有方法
###__private_method
###类得私有属性实例
class JustCounter:
    __secretCount = 0  #私有变量
    publicCount = 0  #公开变量

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print(self.__secretCount)


counter = JustCounter()
counter.count()
counter.count()
print(counter.publicCount)
print(counter.__secretCount)  #报错，实例不能访问私有变量


class Site:
    def __init__(self, name, url):
        self.name = name  #public
        self.__url = url  #private

    def who(self):
        print('name:', self.name)
        print('url:', self.__url)

    def __foo(self):
        print('这是私有方法')

    def foo(self):
        print('这是公共方法')
        self.__foo()


x = Site('菜鸟教程', 'www.runoob.com')
x.who()
x.foo()
### x.__foo()   # 报错无法访问私有变量

'''


#### 运算符重载##############
class Vector:
    def __init__(self, a, b):
        self.a = b
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)


v1 = Vector(2, 10)
v2 = Vector(5, -2)
print(v1 + v2)
