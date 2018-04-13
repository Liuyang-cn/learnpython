#!usr/bin/env python3
# -*- coding: utf-8 -*-
'''
# 排序
list = [2, 3, 1, 7, 6, 5]
list.sort()

print(list)
# 把列表当作堆栈用  last to arrive first to leave
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)
print(stack.pop())
print(stack)

# 把列表当作队列用  first to arrive first to leave
from collections import deque
queue = deque([
    "Eric",
    "John",
    "Michael",
])
queue.append("Terry")
queue.append("Graham")
print(queue)
print(queue.popleft())  #.popleft   the first to leave
print(queue)

# 列表推导式
vec = [2, 4, 6]
print([3 * x for x in vec])  # 用方括号表示推导出的是一个元组
print([[x, x * 2] for x in vec])
#如果少加外层方括号 报错
#<generator object <genexpr> at 0x0000014DB06C3CA8>
#对序列里每一个元素逐步调用某方法 weapon.strip()
freshfruit = ['banana', ' loganberry', 'passion fruit']
print([weapon.strip() for weapon in freshfruit])
#用if做过滤器
print([3 * x for x in vec if x > 3])
print([x * y for x in vec if x < 4 for y in vec if y > 4])
print([vec[i] * vec[i - 1] for i in range(len(vec))])  #vec[-1]倒数第一个元素
#float int str
print([float(round(355 / 113, i)) for i in range(1, 6)])
'''
#嵌套列表式
#转换矩阵
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
'''
print(matrix[1][1])
print(matrix[0])
print([[row[i] for row in matrix] for i in range(4)])
#以下两句解释了上一句的内在过程 内循环->外循环
print([[[i, j] for i in range(4)] for j in range(4)])
print([row for row in matrix])
'''
#另一种转换方法
transposed = []
for i in range(4):  #列循环
    # 接下来的三行进行转换
    transposed_row = []
    for row in matrix:  #行循环
        transposed_row.append(row[i])  #每次添加一个元素
    transposed.append(transposed_row)  #每次添加一个元组
print(transposed)