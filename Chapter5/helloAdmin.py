usernames = ['admin','Ben','Catherine','Daniel','Elinor']
if len(usernames) == 0:
    print('We need users!')
else:
    for i in usernames:
        if i == 'admin':
            print('Hello admin, would you like to see a status report.')
        else:
            print(f'Hello {i}, thank you for logging in again.')
print('usernames wiped')
usernames = []
if len(usernames) == 0:
    print('We need users!')
else:
    for i in usernames:
        if i == 'admin':
            print('Hello admin, would you like to see a status report.')
        else:
            print(f'Hello {i}, thank you for logging in again.')