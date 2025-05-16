# backend/database.py

import pymysql
from pymysql.cursors import DictCursor

DB_HOST = "hopper.proxy.rlwy.net"
DB_USER = "root"  # Replace with your MySQL username
DB_PASSWORD = "EjVQmdssDTlzaVZQayrqAUQrOYURYNFg"  # Replace with your MySQL password
DB_NAME = "railway"
DB_PORT = 52970

def create_connection():
    try:
        connection = pymysql.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME,
            port=DB_PORT,
            cursorclass=DictCursor
        )
        print("✅ Database connected successfully!")
        return connection
    except pymysql.MySQLError as e:
        print(f"❌ Error connecting to database: {e}")
        return None
    
def init_db():
    connection = create_connection()
    if connection:
        with connection.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS expenses (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    date DATE NOT NULL,
                    category VARCHAR(100) NOT NULL,
                    amount DECIMAL(10, 2) NOT NULL,
                    payment_method VARCHAR(50) NOT NULL,
                    description TEXT
                )
            """)
            connection.commit()
        connection.close()
        print("✅ Table checked/created.")


# Test connection
if __name__ == "__main__":
    conn = create_connection()
    if conn:
        conn.close()
