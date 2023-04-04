from tkinter import Tk, ttk, constants

class LoginUI:
    def __init__(self, root, ok_destroy):
        self._root = root
        self._base = None
        self._login = None
        self._username_entry = None
        self._password_entry = None
        self._ok_destroy = ok_destroy


    def pack(self):
        self._base.pack(fill=constants.X)

    def destroy(self):
        self._base.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="Hello!")
        
        button = ttk.Button(
            master=self._frame,
            text="Say good bye",
            command=self._ok_destroy
        )

        label.grid(row=0, column=0)
        button.grid(row=1, column=0)


#seuraavaksi tähän usernamet ja passwordit ja loginbuttonit tkinter ohjeen mukaan:::        
        

    # def _login(self):
    #     username_value = self._username_entry.get()
    #     password_value = self._password_entry.get()

        # try:
        #     otatama_service.login(username, password)
        #     self._execute_login()

        # #failed::

        # except


window = Tk()
window.title("TkInter example")
ui = LoginUI(window)
ui.pack()

window.mainloop()