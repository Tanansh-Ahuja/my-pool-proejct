from fastapi import FastAPI
from routers import customers, bookings, payments, monthly_packages,blocked_dates, group_members 
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Pool Party Roorkee API",
    version="1.0.0" 
)

# Include routers
app.include_router(customers.router)
app.include_router(bookings.router)
app.include_router(payments.router)
app.include_router(monthly_packages.router)
app.include_router(blocked_dates.router)
app.include_router(group_members.router)

@app.get("/debug-test")
def debug_test():
    print("✅ This should print in terminal")
    logger.info("✅ Logger message")
    return {"status": "ok"}


# Run with uvicorn
# uvicorn main:app --reload
