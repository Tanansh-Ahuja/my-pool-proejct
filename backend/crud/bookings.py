from datetime import date, datetime
import random
from typing import List
from fastapi import HTTPException
from sqlalchemy import func
from sqlalchemy.orm import Session
from models import Booking, GroupMember
from schemas.bookings import BookingCreate
from schemas.group_members import GroupMemberCreate
from utils.get_customer_id_from_user import get_customer_id_from_user_id
from crud.group_members import create_group_members



def create_booking_with_members(db, user_id: int, members_data: List[GroupMemberCreate]):
    if not members_data:
        raise HTTPException(status_code=400, detail="No group members provided.")

    # Use the first member's timing for booking
    first_member = members_data[0]
    slot_start = first_member.slot_start
    slot_end = first_member.slot_end
    # Convert times into datetime objects on a dummy date to find the difference
    dummy_date = datetime(2025, 1, 1)  # any date is fine
    start_datetime = datetime.combine(dummy_date, slot_start)
    end_datetime = datetime.combine(dummy_date, slot_end)

    # Calculate the time difference
    duration = end_datetime - start_datetime
    minutes = duration.total_seconds() / 60  # convert seconds to minutes

    # Price calculation
    price_per_minute = 5 / 3  # as per your logic
    amount_per_person = round(minutes * price_per_minute)
    final_band_color = random.choice(['red','greem','yellow','white','blue','grey'])
    # Create the booking
    new_booking = Booking(
        customer_id = get_customer_id_from_user_id(db, user_id),  # you will create this function
        booking_date = first_member.booking_date,
        slot_start = first_member.slot_start,
        slot_end = first_member.slot_end,
        number_of_people = len(members_data),
        total_amount = len(members_data)*amount_per_person,  # we'll calculate below
        payment_status = "pending",
        band_color = final_band_color,
        deleted = False
    )
    db.add(new_booking)
    db.commit()
    db.refresh(new_booking)
    create_group_members(db, members_data,new_booking,amount_per_person)
    return new_booking

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


