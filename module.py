#!/usr/bin/env python3
#文件名：using_sys.py

import sys  #引入sys.py模块

print('命令行参数如下：')
for i in sys.argv:  #包含命令行参数的列表。
    print(i)

#sys.path 包含自动查找所需模块的路径列表
print('\n\nPython 路径为：', sys.path, '\n')
