from fastapi import FastAPI

from app.routes.auth_routes import router as auth_router
from app.routes.room_routes import router as room_router
from app.routes.booking_routes import router as booking_router

app = FastAPI(title="Room Booking",
    description="API for managing users, rooms and bookings",
    version="1.0.0"
    )

app.include_router(auth_router)
app.include_router(room_router)
app.include_router(booking_router)