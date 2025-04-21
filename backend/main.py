from fastapi import FastAPI, Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import psycopg2
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Date, Numeric, Time, Boolean, ForeignKey, Text, text
from sqlalchemy.orm import Session
from fastapi import Depends
from dotenv import load_dotenv
import os


# Load environment variables from .env file
load_dotenv()

# Read variables
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
# Construct the connection URL
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# FastAPI App Setup
app = FastAPI()

# Dependency to get the DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic Models for API Response
class EarningsResponse(BaseModel):
    daily_earnings: float

# Define your SQLAlchemy models (use models.py for better organization)
class Bookings(Base):
    __tablename__ = "bookings"
    booking_id = Column(Integer, primary_key=True, index=True)
    total_amount = Column(Numeric(10, 2))

@app.get("/earnings", response_model=EarningsResponse)
def get_earnings(db: Session = Depends(get_db)):
    result = db.execute("SELECT SUM(total_amount) FROM bookings WHERE booking_date = CURRENT_DATE AND deleted = FALSE")
    earnings = result.fetchone()[0]
    return EarningsResponse(daily_earnings=earnings)

@app.get("/daily-earnings")
def get_daily_earnings(db: Session = Depends(get_db)):
    query = text("""
        SELECT 
            SUM(payment_amount) AS total_earnings
        FROM 
            payments
        WHERE 
            DATE(payment_date) = CURRENT_DATE
            AND payment_status = 'completed';
    """)
    
    result = db.execute(query).fetchone()
    total_earnings = result[0] if result[0] is not None else 0.0
    return {"total_earnings": float(total_earnings)}


# Run with uvicorn
# uvicorn main:app --reload
