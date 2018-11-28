#!/user/env/bin python3
#! -*- codint:utf-8 -*-


def trim(s):
    print(len(s))
    while s[0:1] == ' ':
        s = s[1:]
        print("minus left once", len(s))
    while s[-1:] == ' ':
        print("'%s'" % s[-2:-1])
        s = s[:-1]
        print("'%s'" % s)
        print("'%s'" % s[:-1])
        print("'%s'" % s[-2:-1])
        print("minus right once", len(s))
    return s


s = '  hello         '
s = trim(s)
print("the string s is'%s',its lenth is" % s, len(s))

from collections import Iterable


def findMinAndMax(L):
    if not (L):
        return (None, None)
    else:
        max = min = L[0]
        for i in L:
            if i > max:
                max = i
            if i < min:
                min = i
    return (min, max)


if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
