from fastapi import FastAPI
from app.routers import category, transaction

app = FastAPI(title="TaskNest API")

app.include_router(category.router, prefix="/categories", tags=["Categories"])
app.include_router(transaction.router, prefix="/transactions", tags=["Transactions"])
