from datetime import date
from sqlalchemy.orm import Session
from models import Booking
from schemas.bookings import BookingCreate

def create_booking(db: Session, booking: BookingCreate):
    db_booking = Booking(**booking.model_dump())
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking

def get_booking(db: Session, booking_id: int):
    return db.query(Booking).filter(Booking.booking_id == booking_id).first()

def get_all_bookings(db: Session):
    return db.query(Booking).all()

def get_bookings_for_date(db: Session, booking_date: date):
    return db.query(Booking).filter(Booking.booking_date == booking_date).all()

def update_booking(db: Session, booking_id: int, updated_data: BookingCreate):
    db_booking = db.query(Booking).filter(Booking.booking_id == booking_id).first()
    if db_booking:
        for key, value in updated_data.model_dump().items():
            setattr(db_booking, key, value)
        db.commit()
        db.refresh(db_booking)
    return db_booking

def delete_booking(db: Session, booking_id: int):
    db_booking = db.query(Booking).filter(Booking.booking_id == booking_id).first()
    if db_booking:
        db.delete(db_booking)
        db.commit()
    return {"message": "Booking deleted"}


