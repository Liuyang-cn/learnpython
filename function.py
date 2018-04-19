#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
def print_scores(**kw):
    print('      Name  Score')
    print('------------------')
    for name, score in kw.items():
        print('%10s  %d' % (name, score))
    print()

print_scores(Adam=99, Lisa=88, Bart=77)

data = {
    'Adam Lee': 99,
    'Lisa S': 88,
    'F.Bart': 77
}

print_scores(**data)

def print_info(name, *, gender, city='Beijing', age):
    print('Personal Info')
    print('---------------')
    print('   Name: %s' % name)
    print(' Gender: %s' % gender)
    print('   City: %s' % city)
    print('    Age: %s' % age)
    print()

print_info('Bob', gender='male', age=20)
print_info('Lisa', gender='female', city='Shanghai', age=18)


def ChangeInt( a ):
    a = 10

b = 2
ChangeInt(b)
print( b )

#可写函数说明
def changeme( mylist ):
   # "修改参数的列表"
   mylist.append([1,2,3,4])
   print("函数内取值：", mylist)
   return
#调用changeme函数
mylist= [10,20,30]
changeme(mylist)
print("函数外取值：",mylist)

#必须参数
#可写函数说明
def printme( str ):
   #打印任何传入的字符串
   print (str)
   return

#调用printme函数
printme()  #没有参数 语法错误

#关键字参数
#参数的复制顺序不定
def printinfo( name,age):
   print("名字：",name)
   print("年龄：",age)
   return

#调用
printinfo(age=50,name="bob")

#不定长参数
def printinfo( arg1,*vartuple):
    #打印任何传入的参数
    print("输出：",end =" ")
    print(arg1,end=" ")
    for var in vartuple:
        print(var,end =" ")
    return

#调用printinfo函数
printinfo(10)

printinfo(70,80,90)

#匿名函数 lambda

#求两参数和 定义 sum 的lambda函数
sum = lambda arg1, arg2: arg1 + arg2
#调用 lambda
print("相加后的值为：",sum(10,20))
print("相加后的值为：",sum(20,20))

##### return 语句
###退出函数
def sum(arg1,arg2):
    #返回和
    total = arg1 + arg2
    print("函数内：",total)
    return total

#调用sum
total = sum(10,20)
print("函数外：",total)

##### 函数作用域

x = int(2.9)    # 内建作用域
g_count = 0     #全局作用域
def outer():
    o_count = 1     # 闭包函数外的函数中
    def inner():
        i_count = 2  # 局部作用域


'''
#### global 和 nonlocal 关键字

num = 1


def fun1():
    # 调用 全局变量
    global num  #需要使用global关键字声明
    print(num)
    num = 123
    print(num)


fun1()


def outer():
    num = 10

    def inner():
        nonlocal num  # nonlocal 关键字声明
        num = 100
        print(num)

    inner()
    print(num)


outer()
