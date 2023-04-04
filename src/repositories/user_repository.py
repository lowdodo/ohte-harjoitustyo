from entities.user import User


class UserRepository:

    def __init__(self) -> None:
        self.users = []

    def create_user(self, username:str, password:str):
        user = User(username, password)
        self.users.append(user)
        return user

    def get_user(self, username):
        for user in self.users:
            if user.username == username:
                return user
        return None


    def login_user(self, username: str, password: str):
        user = self.get_user(username)
        if user and user.password == password:
            return True
        return False
    
    