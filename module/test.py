#!usr/bin/python3
#
#导入模块 import
import support
import fibo
import sys

#导入模块的指定部分 from import
#from fibo import fib, fib2
#导入模块的全部内容
#from modname import *
'''
support.print_func("Liuyang")
#import fibo test
fib = fibo.fib
print(fib(100))

#__name__  __main__ test
import using_name

a = [1, 2, 3, 4, 5]
fib = fibo.fib
#dir()函数
print(dir())
#print(dir(sys))
del a
print(dir())

#标准模块
import sys
sys.ps1 = 'a' 
print(sys.ps1)
#E1101:Modulesys.ps1 is only defined for the
#python interactive interpreter, so it's undefined in
#IDLE until set。 'sys' has no 'ps1' member
'''
'''
#导入包与模块
#导入..echo模块，每次输入都要..echo
#注意最后一项可以是模块或包 而不能是类、函数、变量
import soound.effects.echo #注意最后一块
sound.effects.echo.function() #调用
#用from...import的模式就不需要输入前缀
from sound.effects import echo
echo.function() #调用
#直接导入函数
form sound.effects.echo import function
funciton() #调用

#from sound.effects import *
#知识导入包定义文件__all__类似的列表变量
#包定义文件
__init__.py

'''