import sys
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from registration_client import RegistrationClient


class Form(Tk):
    def __init__(self, title, width, height):
        super().__init__()
        self.title(title)
        self.geometry(f"{width}x{height}")
        self.protocol("WM_DELETE_WINDOW", lambda: sys.exit())

    def run_form(self):
        self.mainloop()


class Login(Form):
    def __init__(self, client: RegistrationClient, title='Login', width=600, height=400):
        super().__init__(title, width, height)
        self.client = client
        self.login = 'guest'
        self.password = ''

        self.label_title = ttk.Label(self, text="Authorization", font=('Georgia', 40), padding=20)
        self.label_title.pack()

        self.label_login = ttk.Label(self, text="Login")
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

        self.btn_up = ttk.Button(self, text="Sign up", command=self.create_register_window)
        self.btn_up.pack()

        self.btn_guest = ttk.Button(self, text="Enter as guest", command=self.login_as_guest)
        self.btn_guest.pack()

        self.btn_results = ttk.Button(self, text="Show results", command=self.create_results_window)
        self.btn_results.pack()

    def login_as_guest(self):
        self.withdraw()
        self.quit()

    def login_user(self, login, password):
        try:
            if self.client.login_user(login, password).key:
                self.login = login
                self.password = password
                self.withdraw()
                self.quit()
            else:
                messagebox.showwarning("Warning", "Unknown login or wrong password!")
        except:
            messagebox.showerror("Error", "DataBase connection lost... Try to login as a guest...")

    def create_register_window(self):
        Registration(self.client, 'Register', 400, 300)

    def create_results_window(self):
        Results(self.client, 'Results', 400, 300)


def dismiss(window):
    window.grab_release()
    window.destroy()


class TopWindow(Toplevel):
    def __init__(self, title, width, height):
        super().__init__()
        self.title(title)
        self.geometry(f"{width}x{height}")
        self.protocol("WM_DELETE_WINDOW", lambda: dismiss(self))
        self.grab_set()


class Registration(TopWindow):
    def __init__(self, client: RegistrationClient, title, width, height):
        super().__init__(title, width, height)
        self.client = client

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
        try:
            if pwd1 == pwd2:
                if self.client.add_user(login, pwd1).key:
                    dismiss(self)
                else:
                    messagebox.showwarning("Warning",
                                           "Password and login can't be empty! Login can't be 'guest'!\n"
                                           "Probably a user with this login exists")
            else:
                messagebox.showwarning("Warning", "Passwords doesn't equal!")
        except:
            messagebox.showerror("Error", "DataBase connection lost... Try to login as a guest...")


class Results(TopWindow):
    def __init__(self, client: RegistrationClient, title, width, height):
        super().__init__(title, width, height)
        self.client = client

        self.label_title = ttk.Label(self, text="Results", font=('Georgia', 25), padding=10)
        self.label_title.pack()

        columns = ("Login", "Games", "Wins")
        tree = ttk.Treeview(self, columns=columns, show="headings")
        tree.heading("Login", text="Login", anchor=W)
        tree.heading("Games", text="Games", anchor=W)
        tree.heading("Wins", text="Wins", anchor=W)

        tree.column("#1", width=175)
        tree.column("#2", width=100)
        tree.column("#3", width=100)
        try:
            for player in self.client.get_results().result:
                tree.insert("", END, values=(player.login, player.games, player.wins))
        except:
            messagebox.showerror("Error", "DataBase connection lost... Restart client and try again...")
        scroll = ttk.Scrollbar(self)
        scroll.configure(command=tree.yview)
        tree.configure(yscrollcommand=scroll.set)
        scroll.pack(side=RIGHT, fill=BOTH)
        tree.pack()
