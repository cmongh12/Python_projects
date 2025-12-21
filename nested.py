# x=4
# y=5

# if x>y:
#     print("x is greater than y")
# elif x==y:
#     print("x is equal to y")
# else:
#     print("x is not greater than y")

# x=6
# y=7
# z=2

# if x>y and x>z:
#    print ("x is greater than y and z") 
# elif y>x and y>z:
#    print("y is greater than x and z")
# else:
#    print("z is greater than x and y")

# x=60
# y=70
# z=20
# a=50

# if x>y and x>z and x>a:
#     print ("x is the greatest")
# elif y>x and y>z and y>a:
#     print("y is the greatest")
# elif z>x and z>y and z>a:
#     print("z is the greatest")
# else:
#     print("a is the greatest")

# username= "admin"
# password="admin123"
# if username=="admin" and password=="admin123":
#     print("login successful")
# elif username=="hari" and password=="hari123":
#     print("login successful")
# elif username=="john" and password=="john123":
#     print("login successful")
# else:
#     print("login unsuccessful")

# WAP to enter age of person and check whether the person is eligible to vote or not.
# is eligible to vote or not 18<40.

# age=int(input("Enter your age: "))

# if age>=18  and age<=40:
#     print("you are eligible to vote")
# elif age<18:
#    print("you are underage to vote",age)
# else:
#     print("you are a senior citizen",age)

# party (age 18<40>)
# drinks >18 25< fanta
# 25<35 beer
# 35<40 whiskey

# age=int(input("Enter your age: "))

# if age>=18 and age<40:
#     print("You are eligible to enter the party")
#     if age>18 and age<25:
#         print("You can drink fanta")
#     else:
#        if age>=25 and age<35:
#             print("You can drink beer")
#        else:
#             if age>=35 and age<40:
#                 print("you can drink whiskey")
#             else:
#                 print("You are not allowed to drink")

# else:
#     print("You are not allowed to enter the party")
            
# match case

# lang ='english'

# match lang:
#     case 'nepali':
#         print("Namaste")
#     case 'english':
#         print("Hello")
#     case __:
#         print("Invalid language")


# WAP to enter two number and an operator (+,-,*,/) and perform.

# num1=int(input("Enter first number: "))
# num2=int(input("Enter second number: "))
# operator=input("Enter an operator (+,-,*,/): ")
# match operator:
#     case '+':
#         print(num1 + num2)
#     case '-':
#         print(num1 - num2)
#     case '*':
#         print(num1 * num2)
#     case '/':
#         print(num1 / num2)
#     case __:
#         print("Invalid operator")


# name = input("Enter your name:")
# name =="admin"
# if name == "admin":
#     print("Welcome admin")
#     gender = input("Enter your gender: ")
#     if gender =="male":
#         print("Welcome admin sir")
#     elif gender == "female":
#         print ("Welcome admin ma'am")
#     else:
#         print("Invalid gender")
# else:
#     print("Invalid username")


# WAP to enter student ID , name , five subject marks and calculate total percentage and grade


# student_id = int(input("Enter student ID: "))
# student_name = input("Enter student name: ")
# nepali = int(input("Enter nepali marks: "))
# english = int(input("Enter english marks: "))
# math = int(input("Enter math marks:"))
# social = int(input("Enter social marks: "))
# science = int(input("Enter science marks:"))

# total_marks = nepali + english + math + social + science
# percentage = (total_marks / 500)*100

# if percentage >=35 and percentage >50:
#     print("C")
# elif percentage >=50 and percentage >70:
#     print("B")
# elif percentage >=70 and percentage >90:
#     print("A")
# elif percentage >=90:
#     print("A+")
# else:
#     print("F")

# data=['Ram','Shyam','Hari','Gita','Sita']

# name=input("Enter your name: ")

# if name in data:
#     print(f"{name} is found")
# else:
#     print(f"{name} is not found")

# WAP to enter emp ID, name , and salary
# if salary <10000: 20% bonus
# if salary 80 - 100000: 15%
# 50 - 80000 : 10%
# below 50000: 5%

# nested if else and dictionary data types padhera aaune.


# emp_id = int(input("Enter employee_ID: "))
# emp_name = input("Enter employee_name: ")
# salary= int(input("Enter your salary: "))

# if salary <100000:
#      bonus = salary * 0.20

# elif salary >= 80000 and salary <= 100000:
#     bonus = salary * 0.15

# elif salary >= 50000 and salary < 80000:
#     bonus = salary * 0.10

# elif salary >=50000:
#     bonus = salary*0.50

# total_salary = salary + bonus

# print(f"Employee_ID: {emp_id}")
# print(f"Employee_name: {emp_name}")
# print(f"Salary: {salary}")
# print(f"Bonus: {bonus}")
# print(f"Total_salary: {total_salary}")