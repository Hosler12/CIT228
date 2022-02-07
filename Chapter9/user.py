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
