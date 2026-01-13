import os
import getpass

if not os.path.exists("gui/facebook/database.txt"):
    handle = open("gui/facebook/database.txt","w")
    handle.close()

def register():
    print("========Create new account=========")
    username = input("Enter username: ").strip().lower()
    if username in open("gui/facebook/database.txt").read():
        print("username already exists.Please try a different one.")
        exit()
    password = getpass.getpass("Enter password: ").strip()
    confirm_password= getpass.getpass("confirm your password: ").strip()
    if password != confirm_password:
        print("password do not match.Please try again ")
        exit()

    storeData=f"username:{username},password:{password}\n"
    with open("gui/facebook/database.txt","a") as file:
        file.write(storeData)
        print("Account cretaed successfully")

def login():
    print("========Login account=========")
    username = input("Enter username: ").strip().lower()
    password = getpass.getpass("Enter password: ").strip()
    with open("gui/facebook/database.txt","r") as file:
        is_login=False
        for user in file.readlines():
            udata = user.split(",")
            uname=udata[0]
            uname=uname[9:] 
            upass=udata[1]
            upass=upass[9:].strip()
            if username==uname and password==upass:
                is_login=True
        if is_login:
            print("welcome",username)
        else:
            print("username and password do not match")

question = input("Do yoou have an account? (yes/no): ")

if question=="yes":
    login()
else:
    register()

# insert username&password , make 2 files, add product and category
# user.txt-> id,name,email,phone
# category.txt-> id,userid,cat_name
# products.txt->id,cid,uid,title,quantity,price
