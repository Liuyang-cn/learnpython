#!/user/bin/env python3
#-*- coding: utf-8 -*-

__author__ = 'Lewis Liu'

import aiomysql
import asyncio, logging


def log(sql, args=()):
    logging.info('SQL:%s' % sql)


#@async.coroutine
async def create_pool(loop, **kw):
    logging.info('create database connection pool...')
    global __pool
    __pool = await aiomysql.create_pool(
        host=kw.get('host', 'localhost'),
        port=kw.get('port', 3306),
        user=kw['user'],
        password=kw['password'],
        db=kw['db'],
        charset=kw.get('charset', 'utf8'),
        autocommit=kw.get('autocommit', True),
        maxsize=kw.get('maxsize', 10),
        minisize=kw.get('minisize', 1),
        loop=loop)


#select
async def select(sql, args, size=None):
    log(sql, args)
    global __pool
    async with __pool.get() as conn:
        async with conn.cursor(aiomysql.DictCursor) as cur:
            await cur.execute(sql.replace('?', '%s'), args or ())
            if size:
                rs = await cur.fetchmany(size)
            else:
                rs = await cur.fetchall()
        logging.info('rows returned:%s' % len(rs))
        return rs


# insert,update,delete 语句定义一个通用的execute()
async def execute(sql, args, autocommit=True):
    log(sql)
    async with (await __pool) as conn:
        if not autocommit:
            await conn.begin()
        try:
            async with conn.cursor(aiomysql.DictCursor) as cur:
                await cur.execute(sql.replace('?', '%s'), args)
                affected = cur.rowcount
            if not autocommit:
                await conn.commit()
        except BaseException as e:S
            if not autocommit:
                await conn.rollback()
            raise
        return affected

def creat_args_string(num):
    L=[]
    for n in range (num):
        L.append('?')
    return ', '.join()

class Field(object):

    def __init__(self,name,column_type,primary_key,default):
        self.name = name
        self.column_type=column_type
        self.primary_key=primary_key
        self.default=default
    def __str__(self):
        return '<%s,%s:%s>' % (self.__class__.__name__,self.column_type,self.name)

