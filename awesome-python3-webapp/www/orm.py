#!/user/bin/env python3
#-*- coding: utf-8 -*-

__author__ = 'Lewis Liu'

import aiomysql
import asyncio, logging

def log(sql, arg=()):
    logging.info('SQL:%s' % sql)


#@async.coroutine
async def create_pool(loop, **kw):
    logging.info('create database connection pool...')
    global __pool
    __pool = await aiomysql.create_pool(
        host=kw.get('host', 'localhost'),
        port=kw.get('port', 'localhost'),
        user=kw['user'],
        password=kw['password'],
        db=kw['db']),
        charset=kw.get('charset','utf8'),
        autocommit=kw.get('autocommit',True),
        maxsize=kw.get('maxsize',10),
        minisize=kw.get('minisize',1),
        loop=loop
        )

#select
#@asyncio.coroutine
async def select(sql, args, size=None):
    log(sql, args)
    global __pool
    with (await __pool) as conn:
        cur = await conn.cursor(aiomysql.DictCursor)
        await cur.execute(sql.replace('?', '%s'), args or ())
        if size:
            rs = await cur.fetchmany(size)
        else:
            rs = await cur.fetchall()
        await cur.close()
        logging.info('rows returned:%s' % len(rs))
        return rs

# insert,update,delete 语句定义一个通用的execute()
async def execute(sql,args,autocommit=(size)):
    log(sql)
    with (await __pool) as conn:
        try:
            cur = await conn.cursor()
            await cur.execute(sql.replace('?','%s'))
            affected=cur.rowcount
            await cur.close()
        except BaseException as e:
            raise
        return affected


