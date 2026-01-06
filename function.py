# print("hello pyhton")

# output to be:
#  *
# * *
# * * *
# * * * *
# * * * * *

# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         print("*",end="")
#     print()

# output to be:
# * * * * *
# * * * *
# * * *
# * *
# *

# for i in range(6,0,-1):
#     for j in range(1,i+1):
#         print("*",end="")
#     print()

# output to be:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5 

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()

# output to be:
# 0
# 0 1
# 0 1 2 
# 0 1 2 3 
# 0 1 2 3 4

# for i in range(0,5):
#     for j in range(0,i+1):
#         print(j,end="")
#     print()

# for i in range(0,5):
#     for j in range(0,i+1):
#         print(j,end="")
#     print()
# for i in range(0,5):
#     for j in range(0,i+1):
#         print(j,end="")
#     print()

# def total(x,y):
#     return x+y

# def my_total(a,b,cb):
#     print(cb(a+b))

# my_total (5,6,total)

# def cal(a,b):
#         print(a+b)

# cal(4,6)

# even_or_odd

# def num(n):
#     if n%2==0:
#         print("even")
#     else:
#         print("odd")

# num(4)

# a,b,c

# def greater(a,b,c):
#     if a>b and a>c:
#         print("a is greater")
#     elif b>a and b>c:
#         print("b is greater")
#     else:
#         print("c is greater")

# greater(4,7,8)

#  ascending. number lai pass garne , descending order ma ni pass garne, loop chalayera sum nikalna try garne

# def sort_ascending (numbers):
#     return sorted (numbers)

# nums=[8,6,7,5,2,1]

# ascending_result= sort_ascending(nums)
# print("ascending_order:",ascending_result)

# def sort_descending (numbers):
#     return sorted (numbers)

# nums=[9,8,5,3,4,2]

# descending_results= sort_descending(nums)
# print("descending_order:",descending_results)


# data=[
#     {'name':'ram','gender':'male'},
#     {'name':'sita','gender':'female'},
#     {'name':'hari','gender':'male'},
#     {'name':'laxmi','gender':'female'}
# ]

# def gender_diff(users):
#     male=[]
#     female=[]
#     for user in users:
#         if user['gender']=='male':
#             male.append(user)
#         else:
#             female.append(user)
#     return[male,female]
# result = gender_diff(data)
# print(result)

# search=input("Enter name: ")

# def search(users):
#     for user in users:
#             if search==data['name']:
#                 is_found=True
#                 print("user available")
#             else:
#                  print("user not available")

# 
# def take_value():
#     p=10
#     t=10
#     r=10
#     return[p,t,r]

# def calculate():
#     a,b,c = take_value()
#     return a*b*c/100

# def display():
#     print (calculate())

# display()
# def get_marks():
#     subject=['english','nepali','math','sst','science']

#     eng=int(input("Enter marks of english: "))
#     nep=int(input("Enter marks of nepali: "))
#     math=int(input("Enter marks of maths: "))
#     sst=int(input("Enter marks of sst: "))
#     sci=int(input("Enter marks of science: "))
#     return [eng,nep,math,sst,sci]

# def calculate():
#     eng,nep,math,sst,sci= get_marks()
#     total = eng + nep+ math+ sst+ sci
#     percentage = total/5
#     return percentage

# def grade(percentage):
#     if 35< percentage <50:
#         print("D")
#     elif 50<percentage <65:
#         print("C")
#     elif 65<percentage <75:
#         print("B")
#     elif 75<percentage <100:
#         print("A")
#     else:
#         print("Fail")

# pct = calculate()
# grade(pct)


# users=[
#     {'username':'hari','password':'hari002','role':'admin'},
#     {'username':'ram','password':'ram002','role':'user'},
#     {'username':'sita','password':'sita002','role':'user'}
# ]

# def role_login():
#     username = input("Ente username: ")
#     password = input("Enter password: ")

#     is_found = False

#     for user in users:
#         if user['username'] == username and user['password']== password:
#             is_found = True
#             print("Login successful")

#             if user['role'] == 'admin':
#                 print("Welcome admin")
#                 print("List of all users: ")

#                 for u in users:
#                     print("-",u['username'])

#             else:
#                 print("Welcome user")
#                 print("Your username is:", user['username'])

#     if not is_found:
#         print("Invalid username or password")

# role_login()

#     pass


# import calculator

# print(calculator.add(5,6))

# import calculator as cal
# print (cal.add(6,7))

# from calculator import add,sub
# print(add(5,6))
# from calculator import *

# import datetime

# today = datetime.datetime.now()
# print(today)

# today = datetime.datetime.now()
# bday = datetime.datetime(2005,9,12)
# print(today-bday)

# today = datetime.datetime.now()
# bday = datetime.datetime(2005,9,12)
# if today.month>bday.month:
#     print("bday gone")
#     print(f"{today.month-bday.month} months left")
#     print(f"{today.day-bday.day}days left")
# else:
#     print("bday coming")
#     print(f"{today.month-bday.month} months left")
#     print(f"{today.day-bday.day}days left")

# import tkinter

