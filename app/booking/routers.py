from fastapi import APIRouter
from sqlalchemy import select
from watchfiles import awatch

from app.booking.dao import BookingDAO
from app.schema import SBooking

router = APIRouter(
    prefix="/bookings",
    tags=["Бронирование"]
)

@router.get("/1")
async def get_bookings():
    result = BookingDAO.find_by_id(2)
    return await result

@router.get("/2")
async def get_bookings():
    result = BookingDAO.find_one_or_none(room_id=1)
    print(type(result))
    return await result

@router.get("/3")
async def get_bookings():
    result = await BookingDAO.find_all()
    return result
