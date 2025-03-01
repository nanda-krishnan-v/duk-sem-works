import mysql.connector

connection = mysql.connector.connect(
    host="localhost",      # Replace with your MySQL server address
    user="root",  # Replace with your MySQL username
    password="root",  # Replace with your MySQL password
    database="intro2py"   # Replace with the database name
)

cursor = connection.cursor()
cursor.execute("SELECT * FROM python   ")  # Fetch all rows from 'marks' table

row = cursor.fetchone()  # Fetch the first row

# Iterate over the remaining rows
while row is not None:
    print(row)  # Print the current row
    row = cursor.fetchone()  # Fetch the next row

cursor.close()  # Close the cursor
connection.close()  # Close the connection (only once)
