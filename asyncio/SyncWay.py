#!/usr/bin/env python
#!-*-coding:utf-8-*-

import socket
import time


def blocking_way():
    sock = socket.socket()
    #blocking
    sock.connect(('baidu.com', 80))
    request = 'GET / HTTP/1.0\r\nHost:obaidu.com\r\n\r\n'
    sock.send(request.encode('utf8'))
    response = b''
    chunk = sock.recv(4096)
    while chunk:
        response += chunk
        #blocking
        chunk = sock.recv(4096)
    return response


def sync_way():
    res = []
    for i in range(10):
        res.append(blocking_way())
    return len(res)


def main():
    start = time.clock()
    print(start)
    sync_way()
    end = time.clock()
    print(end - start)