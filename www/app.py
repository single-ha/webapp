# -*- coding: utf-8 -*-
import logging;logging.basicConfig(level=logging.INFO)
import asyncio, os,json,time
from datetime import datetime
from aiohttp import web

def index(request):
    return web.Response(body=b'<h1>Awesome</h1>', content_type='text/html')


async def init(loop):
    app = web.Application()
    app.router.add_route('GET', '/', index)
    apprunner = web.AppRunner(app)
    await apprunner.setup()
    srv = await loop.create_server(apprunner.server, '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv

def t(num):
    a=0
    b=1
    index=0
    while index<num:
        a,b=b,a+b
        print(a)
        index+=1

t(3)
# loop = asyncio.get_event_loop()
# loop.run_until_complete(init(loop))
# loop.run_forever()