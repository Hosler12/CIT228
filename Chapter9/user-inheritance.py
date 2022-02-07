class User:
    def __init__(self,last_name,first_name,username,password,login_attempts = 0):
        self.last_name = last_name
        self.first_name = first_name
        self.username = username
        self.password = password
        self.login_attempts = login_attempts

    def describe_user(self):
        print(f'Name:{self.first_name} {self.last_name}')
        print(f'Username:{self.username}, Password:{self.password}')

    def greet_user(self):
        print(f'Welcome, {self.first_name}')

    def increment_login_attempts(self):
        self.login_attempts += 1
        print(f'{self.username} has attempted to login {self.login_attempts} times')

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f'{self.username} has failed to login, attempts set to {self.login_attempts}') 

class Admin(User):
    def __init__(self, permissions, last_name, first_name, username, password, login_attempts=0):
        super().__init__(last_name, first_name, username, password, login_attempts)
        self.privileges = Privileges(permissions)

class Privileges():
    def __init__(self,privileges):
        self.privileges = privileges

    def show_privileges(self):
        print('You have the following privileges')
        for i in self.privileges:
            print(i)

user1 = User('Alex','Albert','AA','1A')
user2 = User('Barbara','Betty','BB','2B')
user3 = User('Charlie','Charles','CC','3C')
user1.greet_user()
user1.describe_user()
user2.greet_user()
user2.describe_user()
user3.greet_user()
user3.describe_user()
admin1 = Admin(['ban user','add posts','delete posts','pin posts'],'Doe','John','Admin1','12345')
while True:
    user1.increment_login_attempts()
    if user1.login_attempts > 4:
        user1.reset_login_attempts()
        break

admin1.privileges.show_privileges()