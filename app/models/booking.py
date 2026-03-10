from sqlalchemy import Column, Integer, Date, ForeignKey
from app.database import Base

class Booking(Base):

    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey("users.id"))
    room_id = Column(Integer, ForeignKey("rooms.id"))

    start_date = Column(Date)
    end_date = Column(Date)