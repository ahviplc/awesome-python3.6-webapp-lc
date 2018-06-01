
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Test for user
2018年6月1日18:09:46
'''

import sys
import orm, asyncio
from models import User, Blog, Comment


def test(loop):
    yield from orm.create_pool(loop=loop, user='root', password='root', db='awesome')
    u = User(name='LC1', email='ahlc1@sina.cn', passwd='LC1234', image='about:blank')
    yield from u.save()


if __name__ == '__main__':

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait([test(loop)]))
    loop.close()
    if loop.is_closed():
        sys.exit(0)