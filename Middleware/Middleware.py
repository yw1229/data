# !/usr/bin/python3
# -*- coding: utf-8 -*-

"""
名称:         中间件
功能:         添加响应信息，跨域
版本:         beta 0.1
"""
import time
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request
from fastapi import FastAPI
# from Api.WebsocketMonitor.test import routes
app = FastAPI()


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    # print(request.auth)
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
