#!/usr/bin/env python.py
'''
#str()函数返回一个易读的表达形式
s = 'Hello,Runoob'
print(str(s))

#repr() 产生一个解释器易读的表达形式
print(repr(s))

print(str(1 / 7))
print(repr(1 / 7))

x = 10 * 3.25
y = 200 * 200
s = 'x的值为: ' + repr(x) + ', y的值为： ' + repr(y) + '...'
print(s)

#repr()可以转义字符串中的特殊字符
hello = 'hello,runoob\n'
hellos = repr(hello)
print(hello)
print(hellos)

#repr()的参数可以是Python的任意对象
print((x, y, ('Google', 'Runoob')))

#.rjust()方法将字符串向右靠齐，并在左边填充空格
#.ljust()左靠齐，右空格
#.center()居中
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x * x).rjust(3), end=' ')
    print(repr(x * x * x).rjust(4))
#.zfill()左边填零
print('-3.14'.zfill(7))
for x in range(1, 11):
    print('{0:2d}{1:3d}{2:4d}'.format(x, x * x, x * x * x))   #{:2d}两个宽度的10进制数

#str.format() 格式化输出
print('{}网址: "{}!"'.format('菜鸟教程', 'www.runoob,com'))
#大括号及其内的字符会被.format()后的字符替换掉
#与大括号内的定义相符
print('{0}和{1}'.format('Google', 'Runoog'))
print('{1}和{0}'.format('Google', 'Runoog'))
#format()中关键字参数的使用
print('{name}网址： {site}'.format(name='菜鸟教程', site='www.runoob.com'))
#位置及关键字参数可以任意组合
print('站点列表{0},{1},和{other}。'.format('Google', 'Runoob', other='Taobao'))

#!a 使用ascii()
#!s 使用str()
#!r 使用repr()
import math
print('常量PI的值近似为： {!a}。'.format(math.pi))
print('常量PI的值近似为：{!r}。'.format(math.pi))

### 读取键盘输入
#
import sys
str = input("请输入：")
print("你输入的内容是：", str) #?RuntimeError: input(): lost sys.stdin
#when I input these in powershell ,it is ok

'''
