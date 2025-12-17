# print("hello,python!")

# data={
#     "name":"simon",
#     "age":20,
#     "address":"kathmandu",
#     "contact":{
#         "email":"simon@gmail.com",
#         "phone":8493878565
#     }
# }
# print(data['contact']['email'])

# data=[
#     {'name':'ram','age': 20},
#     {'name':'sita','age':21},
#     {'name':[{'username':"admin","address":['ktm']}]}

#      ]
# print(data[2]['name'][0]['address'][0])

# data=[
#     [{"name":"ram" ,"city":"ktm"}],
#     [{"name":"sita" , "city":"bkt"}]
    
# ]

# print(data[0][0]['name'])
# print(data[1][0]['name'])

# data={
#     "users":[
#         {"name":"ram","address":"ktm"}
#     ],
#     "students":[
#         {"name":"sita","address":"bkt"},
#     ]
# }

# print(data["users"][0]["name"])
# print(data["students"][0]["name"])


# data={
#     "teachers":[
#         {"name":"annie","id":123},
#     ],
#     "students":[
#         {"name":"bailey","id":1},
#     ]
# }

# print(data["teachers"][0]["name"]),print(data["students"][0]["name"])

# data = {
#     "teachers": [
#         {"name": "john", "id": 456},
#         {"name": "emma", "id": 789}
#     ],
#     "students": [
#         {"name": "alex", "id": 2},
#         {"name": "sophia", "id": 3}
#     ]
# }

# print(data["teachers"][1]["name"]),print(data["students"][0]["id"])

#what is operator?

#arithmetic operators : +,-,*,/,%,**,//
# + = addition
# - = subtraction
# * = multiplication
# / = division
# % = remainder
# ** = power
# // = whole division

#comparison operators
# | Operator | Meaning                  | Example  | Result  |
# | -------- | ------------------------ | -------- | ------- |
# | `==`     | Equal to                 | `5 == 5` | `True`  |
# | `!=`     | Not equal to             | `5 != 3` | `True`  |
# | `>`      | Greater than             | `7 > 4`  | `True`  |
# | `<`      | Less than                | `2 < 6`  | `True`  |
# | `>=`     | Greater than or equal to | `5 >= 5` | `True`  |
# | `<=`     | Less than or equal to    | `3 <= 2` | `False` |

#logical operators
# | Operator | Meaning              |
# | -------- | -------------------- |
# | `and`    | Both conditions true |
# | `or`     | At least one true    |
# | `not`    | Reverse result       |


#assignment operators
# | Operator | Example  |
# | -------- | -------- |
# | `=`      | `a = 5`  |
# | `+=`     | `a += 2` |
# | `-=`     | `a -= 2` |
# | `*=`     | `a *= 2` |
# | `/=`     | `a /= 2` |

#bitwise operators
# | Operator | Meaning     |    |
# | -------- | ----------- | -- |
# | `&`      | AND         |    |
# | `        | `           | OR |
# | `^`      | XOR         |    |
# | `~`      | NOT         |    |
# | `<<`     | Left shift  |    |
# | `>>`     | Right shift |    |

#membership operators
# | Operator | Example            |
# | -------- | ------------------ |
# | `in`     | `'a' in 'apple'`   |
# | `not in` | `5 not in [1,2,3]` |

#identity operators
# | Operator | Example      |
# | -------- | ------------ |
# | `is`     | `a is b`     |
# | `is not` | `a is not b` |








# x=30
# y=25
# if x>y:
#      print("x is gretaer than y")
# else:
#      print("x is not greater than y")

# WAP to enter two person's age and who is older.

# ram= int (input("Enter age of ram:"))
# hari= int (input("Enter age of hari:"))

# if ram>hari:
#     print("ram is older than hari")
# else:
#     print("ram is not older than hari")

# annie= int (input("enter age of annie:"))
# bailey= int (input("enter age of bailey:"))

# if annie>bailey:
#     print("annie is older than bailey")
# else:
#     print("bailey is older than annie")


# x=50
# y=60
# z=70
# if x>y and x>z:
#     print("x is greater than y and z")
# elif y>x and y>z:
#     print("y is graeter than x and z")
# else:
#     print("z is greater than x and y")

# if same add (==) instead of >,<

# x=25
# y=30
# z=35
# a=40
# if x>y and x>z and x>a:
#     print("x is grater than y,z and a")
# elif y>x and y>z and y>a:
#     print("y is greater than x,z and a")
# elif z>x and z>y and z>a:
#     print ("z is greater than x,y and a")
# else:
#     print ("a is greater than x,y and z")

# num=12

# if num%2==0:
#     print("even number")
# else:
#     print("odd number")

#WAP to enter any number and check whether it is divisibe=le by 3 and 5.

# num=30
# if num%3==0 and num%5==0:
#     print("it is divisible by 3 and 5")
# else:
#     print("it is not divisible by 3 and 5")

#per>35 and per<50 -> C
#per>=50 and per<65 -> B
#per>=65 and per<80 -> A
#per>80 -> A+

# percentage = int (input("enter students percentage:"))

# if percentage >=35 and percentage<50:
#     print("C")
# elif percentage >=50 and percentage<65:
#     print("B")
# elif percentage >=65 and percentage<80:
#     print("A")
# elif percentage >=80:
#     print ("A+")
# else:
#     print("F")


# WAP to enter username and password and check whether the user can log in or not.

# username = "admin"
# password = "123456789"

# username = (input("Enter user name:"))
# password = (input("Enter password:"))

# if username == "admin" and password == "123456789":
#     print("login successful")
# else:
#     print("login unsuccessful")

# Write a program to check whether a person is eligible to vote (age ≥ 18).

# age = int(input("Enter age:"))

# if age >= 18 :
#     print("eligible")
# else:
#     print("not eligible")


# username="admin"
# password="admin123"

# if username =='admin':
#     if password =='admin123':
#         print("login successful")
#     else:
#         print("incorrect password")
# else:
#     print("username not found")  


# print("============welcome to computer bazar============")
# print("1.Dell(Rs 20000) 2.HP(Rs 25000) 3.Lenovo(Rs 30000) 4.Apple(Rs 35000)")
# option =int(input("Select your option:"))
# if option==1:
#     qu =int(input("Enter quamtity:"))
#     name =input("Enter your name:")
#     total=20000*qu
#     print(f"Hello {name}")
#     print(f"Total amount: {total}")
# elif option==2:
#     qu =int(input("Enter quantity:"))
#     name=input("Enter your name:")
#     total=25000*qu
#     print(f"Hello {name}")
#     print(f"Total amount: {total}")
# elif option==3:
#     qu =int(input("Enter quantity:"))
#     name=input("Enter your name:")
#     total=30000*qu
#     print(f"Hello {name}")
#     print(f"Total amount: {total}")
# elif option==4:
#     qu =int(input("Enter quantity:"))
#     name=input("Enter your name:")
#     total=35000*qu
#     print(f"Hello {name}")
#     print(f"Total amount: {total}")    
# else:
#     print("invalid option")


# print("==========Welcome to ATM==========")
# pin = int(input("Enter your pin: "))
# if pin==1234:
#     amount=10000
#     print("1. Withdraw 2. Balance Enquiry")
#     option =int(input("Select your option: "))
#     if option==1:
#         wamount=int(input("Enter amount to withdraw: "))
#         if wamount>amount:
#             print("insufficent balance")
#         else:
#             namount =amount - wamount
#             print(f"Please collect your cash")
#             print(f"Withdrawn amount is: {wamount}")
#             print(f"Your remaining balance is: {namount}")
#     elif option==2:
#         print(f"your balance is {amount}")
#     else:
#         print("Invalid option")
# else:
#     print("Incorrect pin") 


# print("===============Welcome to compter bazaar==============")
# print("1. Dell(Rs 25000)  2.HP(Rs 30000)  3.Lenovo(Rs 35000)  4. Apple(Rs40000)")
# option = int(input("Select your option:"))
# productname=''
# dell_price=0
# hp_price=0
# lenovo_price=0
# apple_price=0
# if option==1:
#     qu = int(input("Enter quantity:"))
#     dell_price=qu*25000
#     productname='Dell'
# elif option==2:
#     qu = int(input("Enter quantity:"))
#     hp_price=qu*30000
#     productname='HP'
# elif option==3:
#     qu = int(input("Enter quantity:"))
#     lenovo_price=qu*35000
#     productname='Lenovo'
# elif option==4:
#     qu = int(input("Enter quantity:"))
#     apple_price=qu*40000
#     productname='Apple'
# else:
#     print("Invalid option")




# print("Delivery option: 1. Home(Rs 1000) 2. Store pickup (Rs 0)")
# delivery_option = int(input("Select your delivery option:"))
# delivery_price=0

# if delivery_option==1:
#     delivery_price=1000

# print("Packing option : 1. Plastic(Rs 1000) 2. Bag(Rs 2000) 3. gift box (Rs 3000)")
# packing_price=0
# packing_option=int(input("Select your packing option:"))
# if packing_option==1:
#     packing_price=1000
# elif packing_option==2:
#     packing_price=2000
# elif packing_option==3:
#     packing_price=3000

# print("Location 1. KTM(Rs:13%) 2.BKT(Rs:0) 3.LTP(Rs:0)")

# total = dell_price+ hp_price + lenovo_price + apple_price
# tax_amount=0
# location_option=int(input("Select your location option:"))
# if location_option==1:
#     tax_amount=total*0.13

# name =input("Enter your name:")
# grand_total= total + delivery_price + packing_price + tax_amount


# print("------------Invoice--------------")
# print(f"Customer name: {name}")
# print(f"Product name: {productname}")
# print(f"Total amount: {total}")
# print(f"Delivery price: {delivery_price}")
# print(f"Packing price: {packing_price}")
# print(f"Tax amount: {tax_amount}")
# print(f"Grand total: {grand_total}")

# users=[
#     {"username":"admin","password":"admin123"},
#     {"username":"harry","password":"harry123"}
# ]

# username=input("Enter username: ")
# password=input("Enter password: ")

# if username==users[0]['username'] and password==users[0]['password']:
#     print("Login successful.")
# elif username==users[1]['username'] and password==users[1]['password']:
#     print("Login successful.")
# else:
#     print("Login unsuccessful.")