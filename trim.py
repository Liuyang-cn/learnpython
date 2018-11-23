#!/user/env/bin python3
#! -*- codint:utf-8 -*-

def trim(s):
    print(len(s))
    while s[0:1] ==' ':
        s=s[1:]
        print("minus left once",len(s))
    while s[-2:-1] ==' ':
        s=s[:-1]
        print("minus right once",len(s))
    return s

s='  hello       '
s=trim(s)
print(s,len(s))