from ui.login_ui import LoginUI
from ui.create_user_ui import CreateUserUI
from ui.tasks_ui import Tasklist


class BasicUI:
    def __init__(self, root):
        self._root = root
        self._view = None
    
    def start(self):
        self._open_login()

    def close_current(self):

        if self._view is not None:
            self._view.destroy()

        self._view = None
        
    def open_login(self):
        self.close_current()

