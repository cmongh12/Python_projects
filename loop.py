# n=1

# while n<=5:
#     print(n)
#     n+=1

# n=5

# while n>=1:
#     print(n)
#     n-=1

# n=1
# while n<=10:
#     print("simon")
#     n+=1

# n=1

# while n<=10:
#     if n%2==0:
#         print(n)
#     n+=1

# n=1
# while n<=10:
#     if n%2!=0:
#         print(n)
#     n+=1

# n=1
# total=0

# while n<=10:
#     total+=n
#     n+=1

# print(total)

# n=1
# even=0
# odd=0

# while n<=25:
#     if n%2==0:
#         even+=1
#     else:
#         odd+=1
#     n+=1

#     print("Total even number is:",even)
#     print("Total odd number is:",odd)

# n=1
# while n<=10:
#     if n<=5:
#         print("Ram")
#         n+=1
#     else:
#         print("sita")
#         n+=1

# WAP to enter number of students : 5
# enter name of student

# a = int(input("Enter number of students: "))

# i=1
# while i<=a:
#     name =  input("Enter name of student: ")
#     print("Student name:",name)
#     i+=1

# print(range(10))

# for x in range(1,11):
#     # print(x)
#     print(x,end=" ")

# for x in range(10,0,-1):
#     print(x,end=" ")

# data=['ram','hari','gita','sita']
# for name in data:
#     print(name)

# numbers=[1,3,6,7,9,11,12,15,17]
# # for n in numbers:
# #     if n%2==0:
# #         print(n)

# for n in numbers:
#     if n==3 or n==9 or n==15 or n==17:
#         print(n)

# name=['ram','sita']
# n=1
# for n in range(1,16):
#     if n<=5:
#         print("ram")
#     elif n>5 and n<=10:
#         print("gita")
#     else:
#         print("sita")

# for n in range(1,11):
#     print("5x",n,"=",n*5)
    # print(f"5x{n}={5*n}")


# total_users=?
# total_male=?
# total_female=?

# data=[
#     {'name':'ram','gender':'male'},
#     {'name':'sita','gender':'female'}, 
#     {'name':'hari','gender':'male'},  
#     {'name':'gita','gender':'female'} 
# ]

# total_users = 0
# total_male = 0
# total_female = 0

# for users in data:
#     total_users += 1

#     if users['gender'] == 'male':
#         total_male += 1
#     elif users['gender'] == 'female':
#         total_female += 1

# print("Total_users:", total_users)
# print("Total_male:", total_male)
# print("Total_female:", total_female)

# 1
# 1,2,3,4,5,6,7,8,9,10
# 2
# 1,2,3,4,5,6,7,8,9,10

# for x in range(1,3):
#     print("==============",x,"===============")
#     for y in range(1,11):
#         print(y, end=" ")
#     print(" ")


# for x in range(2,0,-1):
#     print("=============",x,"=============")
#     for y in range(10,0,-1):
#         print(y, end=" ")
#     print(" ")


# for x in range(1,11):
#     for y in range(1,11):
#         print(f"{x}x{y}={x*y}")
#     print(" ")

# numbers=[
#     [12,45,75,67,87],
#     [56,78,98,70,98]
# ]
# print only even number.

# for n in numbers:
#     for x in n:
#         if x%2==0:
#             print(x)

# odd numbers.
# for num in numbers:
#     for n in num:
#         if n%2!=0:
#             print(n,end=' ')

# numbers=[
#     [12,45,75,67,87],
#     [56,78,98,70,98]
# ]

# total_even_sum=0
# total_odd_sum=0

# for num in numbers:
#     for n in num:
#         if n%2==0:
#             total_even_sum+=n
#         else:
#             total_odd_sum+=n


# print("Total even num: ",total_even_sum)
# print("Total odd sum: ",total_odd_sum)


# data=[
#     {'name':'ram','gender':'male','status':True},
#     {'name':'sita','gender':'female','status':False}, 
#     {'name':'hari','gender':'male','status':False},  
#     {'name':'gita','gender':'female','status':True},
#     {'name':'laxmi','gender':'female','status':True} 
# ]

# total_users=0
# total_male=0
# total_female=0
# total_active_male=0
# total_active_female=0
# total_inactive_male=0
# total_inactive_female=0


# for users in data:
#     total_users += 1
#     if users['gender'] == 'male':
#         total_male += 1
#         if users['status'] ==True:
#            total_active_male +=1
#         else:
#             total_inactive_male +=1
    
#     elif users["gender"] == 'female':
#         total_female +=1
#         if users['status'] == True:
#             total_active_female +=1
#         else:
#             total_inactive_female +=1


# print(f"Total_users: {total_users}")
# print(f"Total_male: {total_male}")
# print(f"Total_female: {total_female}")
# print(f"Total_active_male: {total_active_male}")
# print(f"Total_active_female: {total_active_female}")
# print(f"Total_inactive_male: {total_inactive_male}")
# print(f"Total_inactive_female: {total_inactive_female}")


# users=[ ]

# num=int(input("Enter number of users: "))

# x=1

# while x<=num:
#     name=input("Enter username: ")
#     users.append(name)
#     x+=1

# for user in users:
#     print(f"hello {user}")

# enter number of students
# five subject marks
# total,per,div

# students_marks=[ ]
# print("============Mark Sheet==============")


# num=int(input("Enter number of students: "))
# x=1

# while x<=num:
#     print(f"============Student no.=============")
#     nep =float(input("Enter nep marks: "))
#     math =float(input("Enter math marks: "))
#     eng =float(input("Enter eng marks: "))
#     sci =float(input("Enter sci marks: "))
#     sst =float(input("Enter sst marks: "))
#     total =nep+math+eng+sci+sst
#     students_marks.append(total)
#     x+=1

# SId=1
# for total in students_marks:
#     per=total/5
#     print(f"=========SId: {SId}==========")
#     print(f"Total: {total}")
#     print(f"Percentage: {per}")
#     if per>35 and per<50:
#         print("B Gradde")
#     elif per>50 and per<70:
#         print("A Grade")
#     elif per>70 and per<100:
#         print("A+ Grade")
#     else:
#         print("C Grade")

#     SId+=1    


# for x in range(1,11):
#     if x==5:
#         break
#     print(x)

# for x in range(1,11):
#     if x==5:
#         continue
#     print(x)

# for x in range(1,11):
#     if x==3 or x==7 or x==9:
#         continue
#     print(x)

# students=['ram','hari','gita','sita']

# name=input("Enter name: ")

# is_found=False
# for st in students:
#     if st==name:
#         is_found=True


# if is_found:
#     print(f"welcome: {name}")
# else:
#     print(f"Name not found: {name}")


# studentsData=[
#     {'username':'admin','password':'admin002'},
#     {'username':'hari','password':'hari001'},
#     {'username':'sita','password':'sita123'}
# ]

# user=input("Enter username: ")
# password=input("Enter password: ")

# is_found=False
# for data in studentsData:
#     if data['username'] == user and data['password'] == password:
#         is_found=True


# if is_found:
#     print(f"welcome: {user}")
# else:
#     print(f"login failed")

# category=[
#     {'cid':1,'name':'Laptop'},
#     {'cid':2,'name':'Mobile'},
#     {'cid':3,'name':'TV'}
# ]

# Products=[
#     {'pid':1,'cid':1,'product_name':'Dell','price':20000,'quantity':5},
#     {'pid':2,'cid':1,'product_name':'MAC','price':50000,'quantity':10},
#     {'pid':3,'cid':2,'product_name':'Mi','price':15000,'quantity':50},
#     {'pid':4,'cid':3,'product_name':'Sony','price':17000,'quantity':10},
#     ]

# print("=== Welcome to Tech Plaza ===")

# print("categories:")
# for c in category:
#     print(c['cid'],c['name'])

# cid= int(input("Enter Category ID: "))

# print("products:")
# for p in products:
#     if p['cid'] == cid:
#         print(p['pid'],p['name'],p['price'])

# pid = int(input("Enter Product ID: "))

# for p in products:
#     if p['pid'] == pid:
#         q = int(input("Enter Quantity: "))
#         total = q * p['price']

# print("=======BILL=======")
# print(f"You have bought {q} {p['name']} for rs {p['price']}")
# print(f"Total bill: {total}")


# # pid:1,product_name:Dell,price:20000,Qy:5,Total:100000.

# category = [
#     {'cid': 1, 'name': 'Laptop'},
#     {'cid': 2, 'name': 'Mobile'},
#     {'cid': 3, 'name': 'TV'}
# ]

# products = [
#     {'pid': 1, 'cid': 1, 'name': 'Dell', 'price': 20000, 'qty': 5},
#     {'pid': 2, 'cid': 1, 'name': 'MAC', 'price': 50000, 'qty': 10},
#     {'pid': 3, 'cid': 2, 'name': 'Mi', 'price': 15000, 'qty': 50},
#     {'pid': 4, 'cid': 3, 'name': 'Sony', 'price': 17000, 'qty': 10},
# ]


# search =  input("Enter category name: ").title()
# is_found=False
# for cat in category:
#     if search==cat['name']:
#         is_found=True
#         for product in products:
#             if cat['cid']==product['cid']:
#                 print(product)

# if not is_found:
#     print("Product not found")

# authors =[
#     {'author_id':1,'username':'admin','password':'admin002'},
#     {'author_id':2,'username':'hari','password':'hari002'},
#     {'author_id':3,'username':'sophia','password':'sophia002'},
#     {'author_id':4,'username':'laxmi','password':'laxmi002'}
# ]

# books=[
#     {'bid':1,'author_id':1,'title':'Python and Django','price':2000,'quantity':5},
#     {'bid':2,'author_id':1,'title':'Javascript','price':6000,'quantity':2},
#     {'bid':3,'author_id':2,'title':'Java','price':2000,'quantity':5},
#     {'bid':4,'author_id':3,'title':'html and css','price':8000,'quantity':2},
#     {'bid':5,'author_id':2,'title':'Database','price':9000,'quantity':5}
# ]

# user=input("Enter username: ").lower()
# password=input("Enter password: ").lower()

# is_found=False
# for data in authors:
#     if data['username']==user and data['password']==password:
#         is_found=True
#         aID= data['author_id']

# if is_found:
#     print("Login successful")
#     for book in books:
#         if book['author_id']!= aID:
#             print(book)
# else:
#     print("login failed")


# sir le garako->

# books=[
#     {'bid':1,'title':'Python and Django','price':2000,'quantity':5},
#     {'bid':2,'title':'Javascript','price':6000,'quantity':2}
# ]

# num=int(input("Enter number of books: "))
# x=1
# while x<=num:
#     title=input("Enter book title: ")
#     price=float(input("Enter book price: "))
#     quantity=int(input("Enter book quantity: "))
#     insertData={
#         'title':title,
#         'price':price,
#         'quantity':quantity
#     }
#     books.append(insertData)
#     x+=1
# print(books)


# "==================WELCOME TO BOOK SHOP==================="
# 1. ADD BOOK
# 2. VIEW BOOKS
# 3. DELETE
# 4. UPDATE BOOK
# 5. EXIT

# data=['ram','sita','gita']
# # data.append('gita
# # data.pop()
# # data.pop(1)
# print(data)

            
            
