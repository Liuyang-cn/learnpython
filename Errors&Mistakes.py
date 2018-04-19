#!/usr/bin/env python3
#! -*- coding:utf 8 -*-
'''
while True:
    try:
        x = int(input("Please enter a number:"))
        break
    except ValueError:
        print("Oops! That was no valid number.Try again")
'''
import sys
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except IOError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close
