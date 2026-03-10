# room-booking-api-fastapi

This project is a backend REST API for a Room Booking System built using Python, FastAPI, SQLAlchemy, and MySQL. The purpose of the project is to allow users to register in the system, view available rooms, and book rooms for specific dates while preventing booking conflicts.
The API ensures that a room cannot be booked by multiple users during overlapping dates. If a booking already exists for the selected dates, the system returns an error instead of creating a new booking.
The project demonstrates basic backend development concepts including API development, database integration, request validation, and business logic for booking management.

Technology Used
The project is developed using Python and FastAPI for building the API. SQLAlchemy is used as the ORM for interacting with the database, and MySQL is used as the database management system. Uvicorn is used as the ASGI server to run the FastAPI application. Passwords are securely hashed using bcrypt.

Main Features
The system allows users to register with their name, email, and password. It provides an endpoint to retrieve the list of available rooms stored in the database. Users can book a room by providing a user ID, room ID, start date, and end date. The API checks for booking conflicts and prevents double bookings.

API Documentation
FastAPI automatically generates interactive API documentation using Swagger. The documentation allows developers to test the API endpoints directly from the browser.

