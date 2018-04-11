#!/usr/bin/env python
#-*- coding:utf-8 -*-
# 廖雪峰
print('%2d-%02d' % (3, 1))
s1 = 72
s2 = 85
s3 = (85 - 72) / 72 * 100
print('小明成绩去年提升{0:.1f}%'.format(s3))
# -*- coding: utf-8 -*-

L = [['Apple', 'Google', 'Microsoft'], ['Java', 'Python', 'Ruby', 'PHP'],
     ['Adam', 'Bart', 'Lisa']]
print(L[0][0])
sum = 0
for x in range(101):
    sum = sum + x
print(sum)


def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(-99))


def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


print(add_end())
print(add_end())


#计算平方和
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(calc([1, 2, 3]))
nums = [1, 2, 3]
print(calc(nums))


def person(name, age, **kw):
    print('name:', name, 'age', age, 'other:', kw)


person("bob", 7)
