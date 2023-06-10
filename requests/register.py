from tkinter import *
from tkinter import ttk
from generate_pwd import login_user, add_user


class Form(Tk):
    def __init__(self, title, width, height):
        super().__init__()
        self.title(title)
        self.geometry(f"{width}x{height}")

    def run_form(self):
        self.mainloop()


class Login(Form):
    def __init__(self, title, width, height):
        super().__init__(title, width, height)
        self.login = 'guest'

        self.label_title = ttk.Label(self, text="Authorization", font=('Georgia', 40), padding=20)
        self.label_title.pack()

        self.label_login = ttk.Label(self, text="Login", font=())
        self.label_login.pack()
        self.entry_login = ttk.Entry(self)
        self.entry_login.pack()

        self.label_pwd = ttk.Label(self, text="Password")
        self.label_pwd.pack()
        self.entry_pwd = ttk.Entry(self, show='*')
        self.entry_pwd.pack()

        self.btn_in = ttk.Button(self, text="Enter",
                                 command=lambda: self.login_user(self.entry_login.get(), self.entry_pwd.get()))
        self.btn_in.pack()

        self.btn_up = ttk.Button(self, text="Sign up", command=create_register_window)
        self.btn_up.pack()

        self.btn_guest = ttk.Button(self, text="Enter as guest", command=self.login_as_guest)
        self.btn_guest.pack()

    def login_as_guest(self):
        self.destroy()

    def login_user(self, login, password):
        if login_user(login, password):
            self.login = login
            self.destroy()

    def get_login(self):
        return self.login


class Registration(Form):
    def __init__(self, title, width, height):
        super().__init__(title, width, height)

        self.label_title = ttk.Label(self, text="Registration", font=('Georgia', 25), padding=20)
        self.label_title.pack()

        self.label_login = ttk.Label(self, text="Login", font=())
        self.label_login.pack()
        self.entry_login = ttk.Entry(self)
        self.entry_login.pack()

        self.label_pwd1 = ttk.Label(self, text="Password")
        self.label_pwd1.pack()
        self.entry_pwd1 = ttk.Entry(self, show='*')
        self.entry_pwd1.pack()

        self.label_pwd2 = ttk.Label(self, text="Password again")
        self.label_pwd2.pack()
        self.entry_pwd2 = ttk.Entry(self, show='*')
        self.entry_pwd2.pack()

        self.btn_up = ttk.Button(self, text="Sign up",
                                 command=lambda: self.add_user(self.entry_login.get(), self.entry_pwd1.get(),
                                                               self.entry_pwd2.get()))
        self.btn_up.pack()

    def add_user(self, login, pwd1, pwd2):
        if add_user(login, pwd1, pwd2):
            self.destroy()


def create_register_window():
    Registration('Register', 400, 300)
