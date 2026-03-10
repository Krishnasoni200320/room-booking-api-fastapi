from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.room import Room

router = APIRouter(
    prefix="/rooms",
    tags=["Rooms"]
)

@router.get("/")
def get_rooms(db: Session = Depends(get_db)):

    rooms = db.query(Room).all()

    if not rooms:
        raise HTTPException(
            status_code=404,
            detail="No rooms found"
        )

    return rooms