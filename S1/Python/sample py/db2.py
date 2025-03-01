import MySQLdb

try:
    conn = MySQLdb.connect(host='localhost', user='root', 
                            password='', database="duk")

    if conn:
        print("Connection success", conn)
    else:
        print("No connection found")
except:
    print("Can't connect to DB")

mycursor = conn.cursor()


while True:
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    dept = input("Enter department: ")

    sql = "INSERT INTO students (name, age, dept) VALUES (%s, %s, %s)"
    
    val = (name, age, dept)
    
    mycursor.execute(sql, val)
    conn.commit()
    
    s = input("Do you want to continue (y/n)? ")
    if s.lower() == "n":
        break

mycursor.close()
conn.close()