#!/usr/bin/env python
#!-*-coding:utf-8-*-

import socket


def nonblocking_way():
    sock = socket.socket()
    socket.setblocking(False)
    try:
        sock.connect(('baidu.com', 80))
    except BlockingIOError:
        # 非阻塞过程中可能抛出异常
        pass
    request = 'GET /HTTP/1.0\r\nHost: baidu.com\r\n\r\n'
    data = request.encode('ascii')
    # 不知道socket何时就绪，所以不断尝试发送
    while True:
        try:
            sock.send(data)
            # 直到send不抛出异常，则发送完成
            break
        except OSError:
            pass

    response = b''
    while True:
        try:
            chunk = sock.recv(4096)
            while chunk:
                response += chunk
                chunk = sock.recv(4096)
            break
        except OSError:
            pass
    return response


def sync_way():
    res = []
    for i in range(10):
        res.append(nonblocking_way())
    return len(res)


def main():
    from time import time
    start = time()
    sync_way()
    end = time()
    print('Cost {} seconds'.format((end - start) / 5))
