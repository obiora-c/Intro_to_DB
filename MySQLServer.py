

import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL Server (edit user, password, host if needed)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Lavida'  # replace with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

if __name__ == "__main__":
    create_database()