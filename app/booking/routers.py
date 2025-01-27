from fastapi import Request, Depends

from fastapi import APIRouter
from sqlalchemy import select

from app.users.dependencies import get_current_user
from app.users.models import Users
from watchfiles import awatch

from app.booking.dao import BookingDAO
from app.schema import SBooking

router = APIRouter(
    prefix="/bookings",
    tags=["Бронирование"]
)

@router.get("")
async def get_bookings(user: Users = Depends(get_current_user)):
    print(user, type(user), user.email)

