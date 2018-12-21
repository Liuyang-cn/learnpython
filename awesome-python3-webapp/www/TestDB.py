#!/env/usr/bin python3
#-*- coding:utf-8-*-

import orm
from models import User,Blog,comment

async def test():
    await orm.creat_pool(user='www-data',password='www-data',database'awesome')

    u= User(name='Test',email='test@example.com',passwd='1234567890',image='about:blank')

    await u.save()

for x int test():
    pass