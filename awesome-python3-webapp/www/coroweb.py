#!/usr/bin/env python3
#-*- coding:utf-8 -*-

__author__ = 'lewis liu'

import asyncio, os, inspect, logging, functools

from urllib import parse

from aiohttp import web

from apis import APIError


def get(path):
    '''
    Define decorator @get('/path')
    '''

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            return func(*args, **kw)

        wrapper.__method__ = 'GET'
        wrapper.__route__ = path
        return wrapper

    return decorator