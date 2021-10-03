import History
import Registration.NewRegistration
import pyodbc
import album

name = input("Enter your name")
password = input("Enter your password")
if name == "Rahul" and password == "admin":
    print("Welcome!!! Admin.")
    name = "Y".lower()
    while name == 'Y'.lower():
        print("What would you like to do?\n 1. Register new User\n 2. Add new Album\n 3. Check album sales history")
        num = int(input("Enter the number you would like to do."))
        if num == 1:
            Registration.NewRegistration.my_function()
        elif num == 2:
            album.album_func()
        elif num == 3:
            History.history_func()
        else:
            print("You entered wrong number.")
        name = str(input("Do you want to continue? Press 'Y' for yes and any alphabet for no ")).lower()


else:
    print("You are not admin")
