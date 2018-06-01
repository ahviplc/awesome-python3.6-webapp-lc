#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'LC'

' url handlers '

import re, time, json, logging, hashlib, base64, asyncio

from coroweb import get, post
from aiohttp import web
from models import User, Comment, Blog, next_id

@get('/')
async def index(request):
    users = await User.findAll()
    return {
        '__template__':'test.html',
        'users': users
    }


@get('/lc')
def indexlc(request):
    return web.Response(body=b'<h1>Awesome LC</h1>', content_type='text/html', charset='UTF-8')