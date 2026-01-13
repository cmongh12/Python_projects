# import tkinter as tk


# app = tk.Tk()
# app.title("My GUI application")
# app.geometry("500x500")


# num1 = tk.Label(app,text="Enter number: ").pack()
# num2 = tk.Label(app,text="Enter number: ").pack()

# rn = tk.Label(app,text="result")
# rn.pack()

# num1 = tk.Entry(app)
# num1.pack()

# num2 = tk.Entry(app)
# num2.pack()


# def sayHello():
#     x = int(num1.get())
#     y = int(num2.get())
#     total = x+y
#     rn.config(text=f"Total numer is: {total}")


# btn = tk.Button(app,text='click',command=sayHello).pack()

# app.mainloop()

# import tkinter as tk


# app = tk.Tk()
# app.title("My GUI application")
# app.geometry("400x700")

# data = ""

# screen = tk.Label(app,text="",font=("arial",24),bg="white",width=20,height=5,anchor="e")
# screen.grid(row=0,column=0,columnspan=5)

# def get_value(val):
#     global data
#     data = data + str(val)
#     screen.config(text=data)

# def get_operator(op):
#     global data
#     data = data + op
#     screen.config(text=data)

# def get_result():
#     global data
#     try:
#         result = eval(data)
#         data = str(result)
#         screen.config(text=data)
#     except:
#         screen.config(text="error")
#         data = ""

# def clear_screen():
#     global data
#     data = ""
#     screen.config(text="")

# one = tk.Button(app,text="1",command=lambda:get_value(1),pady=30,padx=30)
# one.grid(row=1,column=0)
# two = tk.Button(app,text="2",command=lambda:get_value(2),pady=30,padx=30)
# two.grid(row=1,column=1)
# three = tk.Button(app,text="3",command=lambda:get_value(3),pady=30,padx=30)
# three.grid(row=1,column=2)
# four = tk.Button(app,text="4",command=lambda:get_value(4),pady=30,padx=30)
# four.grid(row=2,column=0)
# five = tk.Button(app,text="5",command=lambda:get_value(5),pady=30,padx=30)
# five.grid(row=2,column=1)
# six = tk.Button(app,text="6",command=lambda:get_value(6),pady=30,padx=30)
# six.grid(row=2,column=2)
# seven = tk.Button(app,text="7",command=lambda:get_value(7),pady=30,padx=30)
# seven.grid(row=3,column=0)
# eight = tk.Button(app,text="8",command=lambda:get_value(8),pady=30,padx=30)
# eight.grid(row=3,column=1)
# nine = tk.Button(app,text="9",command=lambda:get_value(9),pady=30,padx=30)
# nine.grid(row=3,column=2)
# zero = tk.Button(app,text="0",command=lambda:get_value(0),pady=30,padx=30)
# zero.grid(row=4,column=1)
# add = tk.Button(app,text="+",command=lambda:get_operator("+"),pady=30,padx=30)
# add.grid(row=1,column=4)
# sub = tk.Button(app,text="-",command=lambda:get_operator("-"),pady=30,padx=30)
# sub.grid(row=2,column=4)
# multiply = tk.Button(app,text="*",command=lambda:get_operator("*"),pady=30,padx=30)
# multiply.grid(row=3,column=4)
# div = tk.Button(app,text="/",command=lambda:get_operator("/"),pady=30,padx=30)
# div.grid(row=4,column=4)
# equal = tk.Button(app,text="=",command=get_result,pady=30,padx=30)
# equal.grid(row=4,column=2)
# clear = tk.Button(app,text="C",command=clear_screen,padx=30,pady=30)
# clear.grid(row=4,column=0)


# app.mainloop()



# ~~~~~~~~~~~~~~~~~REGEX~~~~~~~~~~~~~~~~~~~~

# import re

# name = 'ram rai'

# patterns = r"[a-z\s]+"

# if re.fullmatch(patterns,name):
#     print("matched")
# else:
#     print("not matched")

# import re

# phone = "9389902681"

# pattern = r"\d{10}"
# if re.fullmatch(pattern,phone):
#     print("matched")
# else:
#     print("not matched")

# import re

# email = "ram@gmail.com"

# pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
# if re.fullmatch(pattern,email):
#     print("matched")
# else:
#     print("not matched")

# try:
#     print(10/0)
# except Exception as e:
#     print(e)

# print("Hello python")

# def add(x,y):
#     if y==0:
#         raise Exception("y should not be zero")
#     return x+y

# try:
#     print(add(10,0))
# except Exception as e:
#     print(e)

# def zero_check(anyfunction):
#     def test(x,y):
#         if y==0:
#             return "Y should not be zero"
#         return anyfunction(x,y)
#     return test

# @zero_check
# def add(x,y):
#     return x+y

# print(add(5,9))

# def zero_check(anyfunction):
#     def test(x,y):
#         if y>100 or x>100:
#             return"number should not be more than 100"
#         return anyfunction(x,y)
#     return test

# @zero_check
# def add(x,y):
#     return x+y

# print(add(30,20))

# what is file handling?
# types of File
# mode of file handling
# r,w,a,r+,wb,rb,ab
# csv file

