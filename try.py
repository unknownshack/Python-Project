import tkinter as tk
from tkinter import *


class LoginApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.username = tk.Entry(self)
        self.password = tk.Entry(self, show="*")
        self.login_btn = tk.Button(self, text="Log in",
                                   command=self.print_login)
        self.register_btn = tk.Button(self, text="Register",
                                      command=self.register)
        self.username.place(relx=0.5, rely=0.3, anchor=CENTER)
        self.password.place(relx=0.5, rely=0.4, anchor=CENTER)
        self.login_btn.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.register_btn.place(relx=0.5, rely=0.6, anchor=CENTER)

    def print_login(self):
        print("Username: {}".format(self.username.get()))
        print("Password: {}".format(self.password.get()))

    def register(self):
        self.destroy()
        import Registration.interface


if __name__ == "__main__":
    app = LoginApp()
    app.title("Login Page")
    app['bg'] = '#ffbf00'
    app.mainloop()
