#!/usr/bin/env python3
#!-*-coding:utf-8-*-

import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#筛选端口：
#为什么要双括号？
s.bind(('127.0.0.1',9999))
print('Bind UDP on 9999...')
while True:
    #接收数据：
    data,addr=s.recvfrom(1024)
    s.sendto(b'Hello,%s!'%data,addr)
    
    