import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=RAHUL\SQLEXPRESS;'
                      'Database=UserData;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()

name = input("Enter your name")
password = input("Enter your password")
if name == "Rahul" and password == "admin":
    print("Welcome!!! Admin.")
    print("What would you like to do?\n 1. Register new User\n 2. Add new Album\n 3. Check album sales history")
    num = int(input("Enter the number you would like to do."))
    try:
        if num == 1:
            print("You choose to register new user. \n Please fill the details:")
            firstname = input("Enter you firstname")
            lastname = input("Enter your lastname")
            username = input("Enter your Username")
            email = input(" Enter your email address")
            age = int(input("Enter your age"))
            password = input("Enter your password")
            address = input("Enter your address")
            sex = input("Enter your gender")
            phone_no = int(input("Enter your Phone number"))
            cursor.execute("INSERT INTO User_Details  VALUES (?,?,?,?,?,?,?,?,?)", (username, firstname, lastname, email, password, address, age, sex, phone_no))
            conn.commit()
            print("Registration Complete")
        else:
            print("Your option is currently unavailable. Please try again later!!!")
    except Exception as e:
        print(e)
        print("Please Use different Username")
else:
    print("You are not admin")






#for row in cursor:
 #   print()
