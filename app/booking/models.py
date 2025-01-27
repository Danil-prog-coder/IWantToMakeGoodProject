from sqlalchemy import Column, Integer, ForeignKey, Date, Computed

from app.DAO.base import BaseDAO
from app.database import Base

class Bookings(BaseDAO):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True)
    room_id = Column(ForeignKey("rooms.id"))
    user_id = Column(ForeignKey("users.id"))
    data_from = Column(Date, nullable=False)
    data_to = Column(Date, nullable=False)
    price = Column(Integer, nullable=False)
    total_cost = Column(Integer, Computed("((data_from - data_to) * price)"))
    total_days = Column(Integer, Computed("(data_from - data_to)"))


# INSERT INTO users (id, email, hashed_password) VALUES
# (1, '111111', '1234')
# INSERT INTO hotels (name, location, services, rooms_quantity, image_id) VALUES
# ('1', '1', '["1"]', 22, 5)
# INSERT INTO rooms (hotel_id, name, price, quantity, services, image_id) VALUES
# (1, 'hi', 24500, 5, '["hello"]', 8)
# INSERT INTO bookings (room_id, user_id, data_from, data_to, price) VALUES
# (1, 1, '2023-06-15', '2023-06-30', 24500)
# INSERT INTO users (id, email, hashed_password) VALUES
# (2, '22222', '1234')
# INSERT INTO hotels (name, location, services, rooms_quantity, image_id) VALUES
# ('2', '2', '["2"]', 33, 10)
# INSERT INTO rooms (hotel_id, name, price, quantity, services, image_id) VALUES
# (2, 'hi2', 20500, 4, '["hello2"]', 10)
# INSERT INTO bookings (room_id, user_id, data_from, data_to, price) VALUES
# (2, 2, '2023-07-15', '2023-07-30', 20500)