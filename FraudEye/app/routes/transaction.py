from fastapi import APIRouter
from app.models.transaction import Transaction
from app.services.fraud_engine import analyze_transaction

router = APIRouter()

@router.post("/analyze")
def analyze(txn: Transaction):
    return analyze_transaction(txn)
