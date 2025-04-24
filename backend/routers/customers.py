from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database import get_db
from schemas.customers import CustomerCreate, CustomerOut
from crud.customers import create_customer, get_customer, get_all_customers, update_customer, delete_customer

router = APIRouter(prefix="/customers", tags=["Customers"])

@router.post("/", response_model=CustomerOut)
def create_customer_route(customer: CustomerCreate, db: Session = Depends(get_db)):
    return create_customer(db, customer)

@router.get("/{customer_id}", response_model=CustomerOut)
def read_customer(customer_id: int, db: Session = Depends(get_db)):
    db_customer = get_customer(db, customer_id)
    if not db_customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return db_customer

@router.get("/", response_model=list[CustomerOut])
def read_all_customers(db: Session = Depends(get_db)):
    return get_all_customers(db)

@router.put("/{customer_id}", response_model=CustomerOut)
def update_customer_route(customer_id: int, customer: CustomerCreate, db: Session = Depends(get_db)):
    return update_customer(db, customer_id, customer)

@router.delete("/{customer_id}")
def delete_customer_route(customer_id: int, db: Session = Depends(get_db)):
    return delete_customer(db, customer_id)
