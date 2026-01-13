import os
import getpass

os.makedirs("gui/bazzar", exist_ok=True)

files = [
    "gui/bazzar/users.txt",
    "gui/bazzar/categories.txt",
    "gui/bazzar/products.txt"
]

for file in files:
    if not os.path.exists(file):
        open(file,"a").close()

def register():
    print("~~~Create account~~~~")
    username = input("Enter username: ").strip().lower()
    if username in open("gui/bazzar/users.txt").read():
        print("Username already exits.Please try a different one.")
        exit()

    password = getpass.getpass("Enter password: ").strip()
    confirm_password= getpass.getpass("Confirm password: ").strip()
    if password != confirm_password:
        print("Password do not match.Please try again.")
        exit()

    storeData=f"username:{username},password:{password}\n"
    with open("gui/bazzar/users.txt","a") as file:
        file.write(storeData)
        print("Account created successfully")


def view_categories():
    print("~~~~Category~~~~")
    with open("gui/bazzar/categories.txt","r") as file:
        categories = file.readlines()
        if not categories:
            print("No categories found")
        for cat in categories:
            print("-", cat.strip())

def view_products():
    print("~~~~Products~~~")
    with open("gui/bazzar/products.txt","r") as file:
        products = file.readlines()
        if not products:
            print("No products available")
        for product in products:
            print(product.strip())


def dashboard():
    while True:
        print("""
1. View category
2. View products
3. Logout
""")
        choice = input("Choose option: ")
        if choice == "1":
            view_categories()
        elif choice == "2":
            view_products()
        elif choice == "3":
            break
        else:
            print("Invalid choice")


def login():
    print("~~~~~~~Login~~~~~~~")
    username = input("Enter username: ").strip().lower()
    password = getpass.getpass("Enter password: ").strip()
    with open("gui/bazzar/users.txt","r") as file:
        is_login=False
        for user in file.readlines():
            udata = user.split(",")
            uname=udata[0][9:]
            upass=udata[1][9:].strip()
            if username==uname and password==upass:
                is_login=True
        if is_login:
            print("welcome",username)

            dashboard()
        else:
            print("username and password do not match")

question = input("Do you have an account? (yes/no): ")

try:
    dashboard()
except KeyboardInterrupt:
    print("\nProgram exited by user")


if question=="yes":
    login()
else:
    register()