from sqlalchemy import select

from app.DAO.base import BaseDAO
from app.booking.models import Bookings
from app.database import async_session_maker

class BookingDAO(BaseDAO):
    model = Bookings

