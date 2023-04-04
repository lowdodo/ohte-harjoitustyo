import tkinter as tk
from tkinter import ttk, constants
from tkinter import messagebox 

class CreateUserUI:
    def __init__(self, root, user_repository, login_ui) -> None:
        self._root = root
        self._newuser = user_repository
        self._login = login_ui
        self._username_entry = None
        self._password_entry = None
        self._base= ttk.Frame(self._root)

        tkk.Label(self._base, text="Create a new user").pack()


        # Create username label and entry
        username_label = ttk.Label(self._base, text="Username:")
        username_label.pack()
        self._username_entry = ttk.Entry(self._base)
        self._username_entry.pack()

        # Create password label and entry
        password_label = ttk.Label(self._base, text="Password:")
        password_label.pack()
        self._password_entry = ttk.Entry(self._base, show="*")
        self._password_entry.pack()

        # Create "Create User" button
        create_button = ttk.Button(self._base, text="Create User", command=self.create_user)
        create_button.pack()  

    def pack(self):
        self._base.pack(fill=constants.X)
    
    def destroy(self):
        self._base.destroy()

    def newuser(self):
        username = self._username_entry.get()
        password = self._password_entry.get()

        if len(username) < 4 or len(password) <4:
            messagebox.showerror(title=None, message= "Username and password must be atleast 4 characters long.")
        
        else:
            # Create new user and add it to the user repository
            user = self._user_repository.create_user(username, password)
            messagebox.showinfo(title=None, message="User created successfully.")
            self._username_entry.delete(0, constants.END)
            self._password_entry.delete(0, constants.END)
            self._login.show()  # Go back to login UI            

root = tk.Tk()

user_repository = UserRepository()
login_ui = LoginUI(root, user_repository)

create_user_ui = CreateUserUI(root, user_repository, login_ui)
create_user_ui.pack()

root.mainloop()
        