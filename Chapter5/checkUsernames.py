currentUsers = ['admin','ben','catherine','daniel','elinor']
newUsers = ['daniel','elinor','Frank','Grace','Hank']
print(currentUsers)
for i in range(0,len(newUsers)):
    newUsers[i] = newUsers[i].lower()

for i in newUsers:
    if i in currentUsers:
        print(f'Username {i} is taken.')
    else:
        print(f'Welcome to the club, {i}')
        currentUsers.append(i)

print(currentUsers)