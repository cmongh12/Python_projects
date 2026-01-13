import sqlite3

con=sqlite3.connect("database/colleges.sqlite3")
mycrsr=con.cursor()

def create_table():
    table = """
    CREATE TABLE IF NOT EXISTS student_marksheet(
        sid INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        nepali INTEGER NOT NULL,
        maths INTEGER NOT NULL,
        social INTEGER NOT NULL,
        science INTEGER NOT NULL,
        english INTEGER NOT NULL,
        total INTEGER NOT NULL,
        percent REAL NOT NULL
    )
    """
    mycrsr.execute(table)
    con.commit()

create_table()

def insert_data(name, nepali, maths, social, science, english, total, percent):
    insert_query = """
    INSERT INTO student_marksheet
    (name, nepali, maths, social, science, english, total, percent)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """
    mycrsr.execute(insert_query,
                   (name, nepali, maths, social, science, english, total, percent))
    con.commit()
    print("Data inserted successfully!")

times = int(input("How many students info do you want to add? "))
x = 1

while x <= times:
    name = input("Enter your name: ")
    nep = int(input("Enter marks in nepali: "))
    math = int(input("Enter marks in maths: "))
    soc = int(input("Enter marks in social: "))
    sci = int(input("Enter marks in science: "))
    eng = int(input("Enter marks in english: "))

    total = nep + math + soc + sci + eng
    percent = total / 5

    insert_data(name, nep, math, soc, sci, eng, total, percent)
    x += 1
