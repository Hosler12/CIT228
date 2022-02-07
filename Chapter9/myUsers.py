from user import *
from admin import *

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