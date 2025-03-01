import mysql.connector # type: ignore

try:
    # Establish the connection
    conn = mysql.connector.connect(
        host='localhost',
        database='employee',
        user='root',
        password=''
    )

    # Create a cursor object
    mycursor = conn.cursor()
    mycursor = conn.cursor()


    while True:
        name = input("Enter firstname: ")
        age = input("Enter lastname: ")
        dept = int(input("Enter salary: "))

        sql = "INSERT INTO employees (firstname,lastname,salary) VALUES (%s, %s, %s)"
        
        val = (name, age, dept)
        
        mycursor.execute(sql, val)
        conn.commit()
        
        s = input("Do you want to continue (y/n)? ")
        if s.lower() == "n":
            break
except:
    print("No Database Found! ")
    mycursor.close()
    conn.close()