import tkinter as tk
from tkinter import *
from tkinter import messagebox

# class interface(tk.Tk):
# def __init__(self):

# super.__init__(self)
ws = Tk()
ws.geometry('400x300')
ws.title('Registration')
ws['bg'] = '#ffbf00'

# def registration(ws):
Label(ws, text="First Name: ").grid(row=2, column=0, pady=4)
Entry(ws).grid(row=2, column=1, pady=2)

Label(ws, text="Last Name: ").grid(row=3, column=0, pady=4)
Entry(ws).grid(row=3, column=1, pady=2)

Label(ws, text="Password: ").grid(row=4, column=0, pady=4)
Entry(ws, show="*").grid(row=4, column=1, pady=2)

Label(ws, text="Password: ").grid(row=5, column=0, pady=4)
Entry(ws, show="*").grid(row=5, column=1, pady=2)


# for all the entries in registration page


def display():
    messagebox.showinfo('Sorry', "This action is currently not available")


Button(ws, text="Register", command=display).grid(row=6, column=2, pady=4)

# self.flabel.pack()
ws.mainloop()

# if __name__ == "__main__":
#  app = interface()
# app.mainloop()
