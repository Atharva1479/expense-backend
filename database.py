# backend/database.py

import pymysql
from pymysql.cursors import DictCursor

DB_HOST = "localhost"
DB_USER = "root"  # Replace with your MySQL username
DB_PASSWORD = "Example@2024#"  # Replace with your MySQL password
DB_NAME = "expense_tracker"

def create_connection():
    try:
        connection = pymysql.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME,
            cursorclass=DictCursor
        )
        print("✅ Database connected successfully!")
        return connection
    except pymysql.MySQLError as e:
        print(f"❌ Error connecting to database: {e}")
        return None

# Test connection
if __name__ == "__main__":
    conn = create_connection()
    if conn:
        conn.close()
