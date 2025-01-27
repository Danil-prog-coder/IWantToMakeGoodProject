from datetime import datetime

from fastapi import Request, HTTPException, Depends
from jose import jwt, JWTError
from watchfiles import awatch

from app.users.dao import UsersDAO


def get_token(request: Request):
    token = request.cookies.get("booking_access_token")
    if not token:
        raise HTTPException(401, detail=5)
    return token

async def get_current_user(token: str = Depends(get_token)):
    try:
        payload = jwt.decode(
            token, "dfghjmnfb3hbfhjfbh!", "HS256"
        )
    except JWTError:
        raise HTTPException(401, detail=1)
    expire: str = payload.get("exp")
    if (not expire) or (int(expire) < datetime.utcnow()):
        raise HTTPException(401, detail=2)
    user_id: str = payload.get("sub")
    if not user_id:
        raise HTTPException(401, detail=3)
    user = await UsersDAO.find_by_id(user_id)
    if not user:
        raise HTTPException(401, detail=4)
    return user