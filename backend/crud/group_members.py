from collections import defaultdict
from sqlalchemy.orm import Session
from models import GroupMember
from schemas.group_members import GroupMemberCreate, GroupMemberUpdate, GroupMemberOut


def create_group_member(db: Session, member: GroupMemberCreate):
    db_member = GroupMember(**member.model_dump())
    db.add(db_member)
    db.commit()
    db.refresh(db_member)
    return db_member

def get_group_members_by_group_id(db: Session, group_id: str):
    print("Get group member by group id")
    return db.query(GroupMember).filter(GroupMember.group_id == group_id).all()

def get_group_member(db: Session, group_id: str, member_id: int):
    return db.query(GroupMember).filter(
        GroupMember.group_id == group_id,
        GroupMember.member_id == member_id
    ).first()

def update_group_member(db: Session, group_id: str, member_id: int, data: GroupMemberUpdate):
    member = get_group_member(db, group_id, member_id)
    if member:
        for key, value in data.model_dump(exclude_unset=True).items():
            setattr(member, key, value)
        db.commit()
        db.refresh(member)
    return member

def delete_group_member(db: Session, group_id: str, member_id: int):
    member = get_group_member(db, group_id, member_id)
    if member:
        db.delete(member)
        db.commit()
        return True
    return False

def get_all_groups_with_members(db: Session):
    print("In Get All group with members")
    members = db.query(GroupMember).all()
    grouped = defaultdict(list)

    for member in members:
        grouped[member.group_id].append(member)

    # Prepare formatted output
    result = []
    for group_id, group_members in grouped.items():
        result.append({
            "group_id": group_id,
            "group_members": [GroupMemberOut.model_validate(m) for m in group_members]
        })

    return result

