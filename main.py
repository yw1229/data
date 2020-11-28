# !/usr/bin/python3
# -*- coding: utf-8 -*-

"""
名称:         数据桥梁实现类
功能:         定义协议规范
版本:         beta 0.1
"""

from Api.Materials import Materials

from Middleware.Middleware import app

app.include_router(Materials.router,prefix='/api')


# app.include_router(WebsocketTest.router)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app='main:app', host="0.0.0.0", port=8019, reload=True, use_colors=True)
