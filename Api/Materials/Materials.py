import time
from fastapi import APIRouter, Body, Query
from fastapi import BackgroundTasks, Depends, FastAPI
from uuid import UUID
from fastapi import APIRouter
import json

router = APIRouter()
from pydantic import BaseModel

from starlette.responses import FileResponse


@router.get("/items/{item_id}")
async def read_item(item_id: str):
    print(item_id)
    return FileResponse('../.../images/' + item_id, )



@router.get("/jsondata")
async def jsondata():
    a= []
    for i in range(1,53):
        dic ={"id": i,
                "img_src": f"http//60.205.194.197:8019/api/items/{str(i)}.jpg"}
        a.append(dic)
    return  a

