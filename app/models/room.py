from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class Room(Base):

    __tablename__ = "rooms"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    price_per_night = Column(Float)