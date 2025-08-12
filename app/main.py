from fastapi import FastAPI
from app.routes import category, transaction

app = FastAPI(title="FinTrack API")

app.include_router(category.router, prefix="/categories", tags=["Categories"])
app.include_router(transaction.router, prefix="/transactions", tags=["Transactions"])

@app.get("/")
def root():
    return {"message": "Welcome to FinTrack API"}
