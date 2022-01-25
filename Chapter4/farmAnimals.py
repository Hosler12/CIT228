animals = ['horse','cow','rooster','chicken','pig','goat']
newAnimals = [animals[0:5]]
newAnimals.append('penguin')
newAnimals.append('cat')
newAnimals.append('dog')
newAnimals.append('monkey')

for i in animals:
    print(i)
for i in newAnimals:
    print(i)

print(f'The first three items are: {newAnimals[0:2]}')
print(f'The first three items are: {newAnimals[2:4]}')
print(f'The first three items are: {newAnimals[-3:]}')