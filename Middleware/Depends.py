
from fastapi import HTTPException,Body

async def token_is_true(data:dict=Body(...)):
    """签名验证，全局使用,超过60秒或者验证失败就会报错"""
    print(data,'data')
    if not data.get('user_id'):
        raise HTTPException(
            status_code=403,
            detail="please Login",
            headers={"X-Error": "There goes my error"},
        )
    return True
