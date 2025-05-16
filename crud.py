# backend/crud.py

from .database import create_connection
from .models import Expense

# Function to add a new expense
def add_expense(expense_data: Expense):
    connection = create_connection()
    if connection:
        with connection.cursor() as cursor:
            sql = """
                INSERT INTO expenses (date, category, amount, payment_method, description)
                VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (
                expense_data.date,
                expense_data.category,
                expense_data.amount,
                expense_data.payment_method,
                expense_data.description
            ))
            connection.commit()
        connection.close()
        return {"message": "✅ Expense added successfully!"}
    return {"error": "❌ Failed to add expense"}

# Function to fetch all expenses
def get_all_expenses():
    connection = create_connection()
    if connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM expenses")
            expenses = cursor.fetchall()
        connection.close()
        return expenses
    return []

# Function to update an expense
def update_expense(expense_id: int, expense_data: Expense):
    connection = create_connection()
    if connection:
        with connection.cursor() as cursor:
            sql = """
                UPDATE expenses
                SET date = %s, category = %s, amount = %s, payment_method = %s, description = %s
                WHERE id = %s
            """
            cursor.execute(sql, (
                expense_data.date,
                expense_data.category,
                expense_data.amount,
                expense_data.payment_method,
                expense_data.description,
                expense_id
            ))
            connection.commit()
        connection.close()
        return {"message": "✅ Expense updated successfully!"}
    return {"error": "❌ Failed to update expense"}

# Function to delete an expense
def delete_expense(expense_id: int):
    connection = create_connection()
    if connection:
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM expenses WHERE id = %s", (expense_id,))
            connection.commit()
        connection.close()
        return {"message": "✅ Expense deleted successfully!"}
    return {"error": "❌ Failed to delete expense"}
