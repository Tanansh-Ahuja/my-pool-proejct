from datetime import date
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database import get_db
from schemas.bookings import BookingCreate, BookingOut
from crud.bookings import create_booking, get_booking, get_all_bookings, update_booking, delete_booking, get_bookings_for_date

router = APIRouter(prefix="/bookings", tags=["Bookings"])

@router.post("/", response_model=BookingOut)
def create_booking_route(booking: BookingCreate, db: Session = Depends(get_db)):
    return create_booking(db, booking)

@router.get("/", response_model=list[BookingOut])
def read_all_bookings(db: Session = Depends(get_db)):
    return get_all_bookings(db)

@router.get("/{booking_id}", response_model=BookingOut)
def read_booking(booking_id: int, db: Session = Depends(get_db)):
    db_booking = get_booking(db, booking_id)
    if not db_booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    return db_booking

@router.get("/by-date/{booking_date}", response_model=list[BookingOut])
def get_bookings_by_date(booking_date: date, db: Session = Depends(get_db)):
    return get_bookings_for_date(db, booking_date)

@router.put("/{booking_id}", response_model=BookingOut)
def update_booking_route(booking_id: int, booking: BookingCreate, db: Session = Depends(get_db)):
    return update_booking(db, booking_id, booking)

@router.delete("/{booking_id}")
def delete_booking_route(booking_id: int, db: Session = Depends(get_db)):
    return delete_booking(db, booking_id)
