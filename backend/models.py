from sqlalchemy import Column, Integer, String, Date, Numeric, Time, Boolean, ForeignKey, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Bookings(Base):
    __tablename__ = 'bookings'

    booking_id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey('customers.customer_id'))
    group_id = Column(String(20))
    booking_time = Column(Date)
    booking_date = Column(Date, nullable=False)
    slot_start = Column(Time, nullable=False)
    slot_end = Column(Time, nullable=False)
    number_of_people = Column(Integer, nullable=False)
    needs_swimwear = Column(Boolean, default=False)
    needs_tube = Column(Boolean, default=False)
    needs_cap = Column(Boolean, default=False)
    needs_goggles = Column(Boolean, default=False)
    food_order = Column(Text)
    total_amount = Column(Numeric(10, 2), nullable=False)
    payment_status = Column(String(20), default='pending')
    band_color = Column(String(20))
    booking_type = Column(String(20), default='regular')
    swimwear_requested = Column(Boolean, default=False)
    deleted = Column(Boolean, default=False)

    # Relationship with Customer table
    customer = relationship('Customers', back_populates='bookings')

