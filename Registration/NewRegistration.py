import dbsConnection
from datetime import datetime


def my_function():
    conn, cursor = dbsConnection.main_function()

    try:
        now = datetime.now()
        print("You choose to register new user. \nPlease fill the details:")
        firstname = input("Enter you firstname: ")
        lastname = input("Enter your lastname: ")
        username = input("Enter your Username: ")
        email = input("Enter your email address: ")
        age = int(input("Enter your age: "))
        password = input("Enter your password: ")
        address = input("Enter your address: ")
        sex = input("Enter your gender: ")
        phone_no = int(input("Enter your Phone number: "))
        cursor.execute("INSERT INTO User_Details  VALUES (?,?,?,?,?,?,?,?,?)",
                       (username, firstname, lastname, email, password, address, age, sex, phone_no))
        cursor.execute("Insert INTO albumhistory values (?,?,?)", (username, email, now))
        conn.commit()
        print("Registration Complete")

    except Exception as e:
        print(e)
        print("Please Use different Username")
