from pydantic_extra_types.epoch import Integer
from pydantic_settings import BaseSettings
from sqlalchemy import String


# class Settings(BaseSettings):
#
#     class Config:
#         env_file = "C:\\Users\\danil\\PycharmProjects\\IWantToMakeGoodProject\\.env"
#
#     DB_HOST: str
#     DB_PORT: int
#     DB_USER: str
#     DB_PASS: int
#     DB_NAME: str
#
#     DATABASE_URL = f'postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
#
# settings = Settings()
#
# print(settings.DB_PASS)

# class Settings(BaseSettings):
#
#     DB_HOST: String
#     DB_PORT: Integer
#     DB_USER: String
#     DB_PASS: Integer
#     DB_NAME: String
#
#     class Config:
#         env_file = "C:\\Users\\danil\\PycharmProjects\\IWantToMakeGoodProject\\.env"
#
#     DATABASE_URL = f'postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
#
# settings = Settings()
# print(settings.DATABASE_URL)
#

