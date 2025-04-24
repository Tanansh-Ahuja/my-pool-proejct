from pydantic import BaseModel
from typing import List, Optional
from decimal import Decimal

class GroupMemberBase(BaseModel):
    group_id: str
    member_id: int
    booking_id: int
    full_name: str
    customer_id: Optional[int] = None
    age: Optional[int] = None
    gender: Optional[str] = None
    needs_swimwear: bool = False
    swimwear_type: Optional[str] = None
    swimwear_cost: Decimal = 0.00
    needs_tube: bool = False
    tube_cost: Decimal = 0.00
    needs_cap: bool = False
    cap_cost: Decimal = 0.00
    needs_goggles: bool = False
    goggles_cost: Decimal = 0.00
    band_color: Optional[str] = None
    special_notes: Optional[str] = None

class GroupMemberCreate(GroupMemberBase):
    pass

class GroupMemberUpdate(BaseModel):
    age: Optional[int]
    gender: Optional[str]
    needs_swimwear: Optional[bool]
    swimwear_type: Optional[str]
    swimwear_cost: Optional[Decimal]
    needs_tube: Optional[bool]
    tube_cost: Optional[Decimal]
    needs_cap: Optional[bool]
    cap_cost: Optional[Decimal]
    needs_goggles: Optional[bool]
    goggles_cost: Optional[Decimal]
    band_color: Optional[str]
    special_notes: Optional[str]

class GroupMemberOut(GroupMemberBase):
    group_id: str
    member_id: int
    booking_id: int
    full_name: str
    customer_id: Optional[int]
    age: Optional[int]
    gender: Optional[str]
    needs_swimwear: Optional[bool]
    swimwear_type: Optional[str]
    swimwear_cost: Optional[Decimal]
    needs_tube: Optional[bool]
    tube_cost: Optional[Decimal]
    needs_cap: Optional[bool]
    cap_cost: Optional[Decimal]
    needs_goggles: Optional[bool]
    goggles_cost: Optional[Decimal]
    band_color: Optional[str]
    special_notes: Optional[str]
    class Config:
        from_attributes = True


class GroupWithMembers(BaseModel):
    group_id: str
    group_members: List[GroupMemberOut]
