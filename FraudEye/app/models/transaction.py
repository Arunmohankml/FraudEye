from pydantic import BaseModel

class Transaction(BaseModel):
    transaction_id: str
    amount: float
    country: str
    device_id: str
    account_age_days: int
