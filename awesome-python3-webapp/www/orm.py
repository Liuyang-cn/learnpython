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
    __pool = await aiomysql.create_pool
        host=kw.get('host', 'localhost'),
        port=kw.get('port', 'localhost'),
        user=kw['user'],
        password=kw['password'],
        db=kw['db'])


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