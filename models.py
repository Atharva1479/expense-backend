# backend/models.py

from pydantic import BaseModel
from datetime import date

# Pydantic model for expense data
class Expense(BaseModel):
    date: date
    category: str
    amount: float
    payment_method: str
    description: str | None = None  # Optional field
