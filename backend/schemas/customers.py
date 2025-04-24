from pydantic import BaseModel, StringConstraints
from typing import Optional, Annotated
from datetime import datetime

PhoneStr = Annotated[str, StringConstraints(min_length=10, max_length=15)]

class CustomerBase(BaseModel):
    full_name: str
    phone_number: PhoneStr
    gender: Optional[str] = None
    age: Optional[int] = None
    swimming_minutes: Optional[int] = None
    notes: Optional[str] = None

class CustomerCreate(CustomerBase):
    pass

class CustomerUpdate(BaseModel):
    full_name: Optional[str]
    phone_number: Optional[PhoneStr]
    gender: Optional[str]
    age: Optional[int]
    address: Optional[str]
    notes: Optional[str]

class CustomerOut(CustomerBase):
    customer_id: int
    registered_at: datetime
    swimming_minutes: Optional[int]

    class Config:
        from_attributes = True
