from sqlalchemy import Column, String, JSON, Integer, ForeignKey, Date, Computed
from app.database import Base

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)


