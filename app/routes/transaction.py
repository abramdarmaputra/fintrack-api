# app/routes/transaction.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_transactions():
    return {"message": "List semua transaksi"}
