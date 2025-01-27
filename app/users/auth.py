from datetime import datetime
from http.client import HTTPException

import jwt

from asyncpg.pgproto.pgproto import timedelta
from passlib.context import CryptContext
from pydantic import EmailStr
from sqlalchemy.util import deprecated

from app.users.dao import UsersDAO

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def verifi_password(plain_password, hashed_password) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    encode_jwt = jwt.encode(
        to_encode, "dfghjmnfb3hbfhjfbh!", "HS256"
    )
    return encode_jwt

async def authenticate_user(email: EmailStr, password: str):
    print(1)
    user = await UsersDAO.find_one_or_none(email=email)
    print(2)
    if not user or not verifi_password(password, user.hashed_password):
        print(3)
        return None
    return user

