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

