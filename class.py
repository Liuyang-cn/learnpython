#!/usr/bin/env python3
#
#面向对象
#


class MyClass:
    '''a simple class'''
    i = 12345

    def f(self):
        return 'hello world'


#实例化类

x = MyClass()

#访问类的属性和方法
print("MyClass 类的属性 i 为：", x.i)
print("MyClass 类的方法 f 输出为：", x.f())


# __init__()方法可以有参数
class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart


x = Complex(3.0, -4.5)
print(x.r, x.i)
'''
#self 代表累的实例 代表当前对象的地址，self.class指向类
class Test:
    def prt(self):
        print(self)
        print(self.__class__)


t = Test()
t.prt()


class Test:
    def prt(runoob):
        print(runoob)
        print(runoob.__class__)


t = Test()
t.prt()
'''
