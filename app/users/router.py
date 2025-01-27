from http.client import HTTPException
from sys import prefix

from fastapi import APIRouter

from app.users.auth import get_password_hash
from app.users.dao import UsersDAO
from app.users.pycach.schamas import SUserRegister

router = APIRouter(
    prefix="/auth",
    tags=["Auth & Пользователи"]
)

@router.post("/register")
async def register_user(user_data: SUserRegister):
    exiting_user = await UsersDAO.find_one_or_none(email=user_data.email)
    if exiting_user:
        raise HTTPException(status_code=500)
    hash_password = get_password_hash(user_data.password)
    await UsersDAO.add(email=user_data.password, hashed_password=hash_password)
