from fastapi import FastAPI
from routers import customers, bookings, payments, monthly_packages,blocked_dates, group_members , settings, earnings, notice, auth
import logging
from fastapi.middleware.cors import CORSMiddleware

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Pool Party Roorkee API",
    version="1.0.0" 
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],  # or ["*"] for all origins (not recommended in production)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(customers.router)
app.include_router(bookings.router)
app.include_router(payments.router)
app.include_router(monthly_packages.router)
app.include_router(blocked_dates.router)
app.include_router(group_members.router)
app.include_router(settings.router)
app.include_router(earnings.router)
app.include_router(notice.router)
app.include_router(auth.router)


@app.get("/debug-test")
def debug_test():
    print("✅ This should print in terminal")
    logger.info("✅ Logger message")
    return {"status": "ok"}
# Run with uvicorn
# uvicorn main:app --reload
