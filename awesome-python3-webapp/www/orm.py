#!/user/bin/env python3
#-*- coding: utf-8 -*-

__author__ = 'Lewis Liu'

@async.coroutine
def creat_pool:
   logging.info('create database connection pool...') 
   global __pool
   __pool = yield form aiomysql.creat_pools
       host=kw.get('host', 'localhost'),
       port=kw.get('port', 'localhost'),
       user=kw['user'],
       password=kw['password'],s
       db=kw['db']pip
   )

@asyncio.coroutine
def select(sql, args, size=none):
    lof(sql, args)
    global __pool
    with(yield from __pool) as conn:
        cur = yield from conn.cursor(aiomysql.DictCursor)
        yield from cur.execute(sql.replace('?', '%s'), args or())
        if size:
            rs = yield from cur.fetchmany(size)
        else:
            rs = yield form cur.fetchall()
        yield from cur.close()
    loggint.info('rows returned:%s' % len(rs))
    return rs