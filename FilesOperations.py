#!/usr/bin/env python3
'''
#To checkout filepath
import os
cwd = os.getcwd()
files = os.listdir(cwd)
print("Files in '%s': %s" % (cwd, files))

#打开一个文件
f = open("tmp/foo.txt", "w+")

#关闭打开文件
f.write("Python is a good program language.\n Yes,it is.\n")

#关闭打开的文件
f.close()

#file.read(size) to read 'size'of data in file
f = open("tmp/foo.txt", "r")
str = f.read()
print(str)
f.close()

#file.readline() to read a line of data in file,take '\n' as line break
f = open("tmp/foo.txt", "r")
str1 = f.readline()
print(str1)
f.close()

#f.readlines() to read all lines in file
f = open("tmp/foo.txt", "r")
str2 = f.readlines()

print(str2)
#迭代一个文件对象逐行读取
#for line in f:
#    print(line, end='')


f.close()

f = open("tmp/foo.txt", "a")
num = f.write("Python 是一个很好的语言。\n 是的，的确很好。\n")
print(num)
f.close()

#file.readline() to read a line of data in file,take '\n' as line break
f = open("tmp/foo.txt", "r")
str1 = f.read()
print(str1)
f.close()

#如果要写入一些不是字符串的东西要先进行转换

f = open("tmp/foo.txt", "a+")
value = ('www.github.com', 14)
s = str(value)
f.write(s)

#f.tell()返回文件对象当前所处的位置
#f.seek(offset,form_what) 改变文件的位置 from_what=0,1,2 开头，当前，结尾
print(f.tell())
f.close

f = open('tmp/foo.txt', 'rb+')
f.write(b'1234567890abc')
print(f.seek(5, 0))
print(f.read())
print(f.seek(-2, 2))  #移动到文件的倒数第2个字节
#str = f.read()
print(f.read())
f.close()

#pickle 模块
#pickle.dump(obj,file,[,protocol]) 基本接口

#打开一个文件
import pickle

#使用pickle模块将数据对象保存到文件
data1 = {
    'a': [1, 2.0, 3, 4 + 6j],
    'b': ('string', u'Unicode string'),
    'c': None
}
selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)

output = open('tmp/data.pkl', 'wb')

# pickle dictionary using protocol 0.
pickle.dump(data1, output)
#Pickle the list using the highest protocol available.
pickle.dump(selfref_list, output, -1)
output.close()
'''
import pprint, pickle
#使用pickle模块从文件中重构python对象
pkl_file = open('tmp/data.pkl', 'rb')

data2 = pickle.load(pkl_file)
pprint.pprint(data2)
pkl_file.close()