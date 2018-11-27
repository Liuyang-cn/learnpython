#!/user/bin/env python3
#-*- coding: utf-8 -*-

__author__ = 'Lewis Liu'

@async.coroutine
def creat_pool:
   logging.info('create database connection pool...') 
   global __pool
   __pool = yield form aiomysql.creat_pool(
       host = kw.get('host','localhost'),
       port = kw.get('port','localhost'),
       user = kw['user'],
       password = kw['password'],
       db = kw['db'],
       
   )