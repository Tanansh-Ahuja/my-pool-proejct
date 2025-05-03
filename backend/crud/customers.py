from sqlalchemy.orm import Session
from models import Customer
from schemas.customers import CustomerCreate, CustomerUpdate

def create_customer(db: Session, customer: CustomerCreate):
    db_customer = Customer(**customer.model_dump())
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

def get_customer(db: Session, customer_id: int):
    return db.query(Customer).filter(Customer.customer_id == customer_id).first()

def get_all_customers(db: Session):
    return db.query(Customer).all()

def update_customer(db: Session, customer_id: int, updated_data: CustomerCreate):
    db_customer = db.query(Customer).filter(Customer.customer_id == customer_id).first()
    if db_customer:
        for key, value in updated_data.model_dump().items():
            setattr(db_customer, key, value)
        db.commit()
        db.refresh(db_customer)
    return db_customer

def delete_customer(db: Session, customer_id: int):
    db_customer = db.query(Customer).filter(Customer.customer_id == customer_id).first()
    if db_customer:
        db.delete(db_customer)
        db.commit()
    return {"message": "Customer deleted"}

def update_customer_by_user_id(db: Session, user_id: int, updated_data: CustomerUpdate):
    customer = db.query(Customer).filter(Customer.user_id == user_id).first()
    if not customer:
        return None

    for key, value in updated_data.model_dump(exclude_unset=True).items():
        setattr(customer, key, value)

    db.commit()
    db.refresh(customer)
    return customer
