class Privileges():
    def __init__(self,privileges):
        self.privileges = privileges

    def show_privileges(self):
        print('You have the following privileges')
        for i in self.privileges:
            print(i)