from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import date

from app.database import get_db
from app.models.booking import Booking

router = APIRouter(
    prefix="/booking",
    tags=["Bookings"]
)

@router.post("/book")
def book_room(
    user_id: int,
    room_id: int,
    start_date: date,
    end_date: date,
    db: Session = Depends(get_db)
):

    # validate dates
    if start_date >= end_date:
        raise HTTPException(
            status_code=400,
            detail="End date must be after start date"
        )

    # check booking conflict
    conflict = db.query(Booking).filter(
        Booking.room_id == room_id,
        Booking.start_date <= end_date,
        Booking.end_date >= start_date
    ).first()

    if conflict:
        raise HTTPException(
            status_code=400,
            detail="Room already booked for these dates"
        )

    booking = Booking(
        user_id=user_id,
        room_id=room_id,
        start_date=start_date,
        end_date=end_date
    )

    db.add(booking)
    db.commit()

    return {"message": "Booking successful"}