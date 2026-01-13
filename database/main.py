import sqlite3

conn = sqlite3.connect("database/college.sqlite3")
mycrs = conn.cursor()

def create_table():
    table = """
    CREATE TABLE IF NOT EXISTS student(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        address TEXT NOT NULL
    )
    """
    mycrs.execute(table)
    conn.commit()

def insert(name, email, address):
    insert_query = """
    INSERT INTO student(name, email, address)
    VALUES (?, ?, ?)
    """
    mycrs.execute(insert_query, (name, email, address))
    conn.commit()
    print("Data inserted successfully")

create_table()

name = input("Enter your name: ")
email = input("Enter your email: ")
address = input("Enter your address: ")

insert(name, email, address)



def create_employee_table():
    table="""
    CREATE TABLE IF NOT EXISTS employee (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    address TEXT NOT NULL
    )
    """
    mycrs.execute(table)
    conn.commit()


def insert_employee(name,email,address):
    insert_query= """
    INSERT INTO employee (name,email,address)
    VALUES (?,?,?)
    """
    mycrs.execute(insert_query, (name, email, address))
    conn.commit()
    print("Employee Data inserted successfully")

create_employee_table()
emp_name=input("Enter your name:")
emp_email=input("Enter your email:")
emp_address=input("Enter your address:")
insert_employee(emp_name,emp_email,emp_address)




def display():
    sql = "SELECT * FROM student"
    data = mycrs.execute(sql)
    # print (data.fetchall())
    # print (data.fetchone())
    print(data.fetchmany(3))

display()

def update(name,email,address,id):
    updateSql="""UPDATE student SET name=?,email=?,address=? WHERE id=?"""
    mycrs.execute(updateSql,(name,email,address,id))
    conn.commit()
    print ("Data updated successfully")
update("sam","sam@gmail.com","bkt",2)

def delete(id):
    sql = "DELETE FROM student Where id=?"
    mycrs.execute(sql,(id,))
    conn.commit()
    print("Data deleted duccessfully")

delete(2)