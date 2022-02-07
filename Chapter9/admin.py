from user import *
from privileges import *

class Admin(User):
    def __init__(self, permissions, last_name, first_name, username, password, login_attempts=0):
        super().__init__(last_name, first_name, username, password, login_attempts)
        self.privileges = Privileges(permissions)
