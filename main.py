# backend/main.py

from fastapi import FastAPI, HTTPException
from models import Expense
from crud import add_expense, get_all_expenses, update_expense, delete_expense
from database import init_db

app = FastAPI()

@app.on_event("startup")
def on_startup():
    init_db()


# POST: Add a new expense
@app.post("/expenses")
def create_expense(expense: Expense):
    result = add_expense(expense)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    return result

# GET: Get all expenses
@app.get("/expenses")
def read_expenses():
    return get_all_expenses()

# PUT: Update an expense
@app.put("/expenses/{expense_id}")
def modify_expense(expense_id: int, expense: Expense):
    result = update_expense(expense_id, expense)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    return result

# DELETE: Delete an expense
@app.delete("/expenses/{expense_id}")
def remove_expense(expense_id: int):
    result = delete_expense(expense_id)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    return result
