# uvicorn app.main:app --reload
# alembic revision --autogenerate -m "Initial migration"
# alembic upgrade head
# alembic downgrade -4
import asyncio

from fastapi import FastAPI
import uvicorn
from app.booking.routers import router as router_booking
from app.database import engine, Base
from app.users.router import router as router_users

app = FastAPI()

async def init_db():
    async with engine.begin() as conn:
        # Создание всех таблиц
        await conn.run_sync(Base.metadata.create_all)

@app.get("/")
async def welcome() -> dict:
    return {"message": "My e-commerce app"}

app.include_router(router_users)
app.include_router(router_booking)

if __name__ == "__main__":
    asyncio.run(init_db())
    uvicorn.run("app.main:app", reload=True)
