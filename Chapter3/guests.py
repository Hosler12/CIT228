print('Excerise 3-4')

guests = ['Dad','Mom','Grandma']

for i in guests:
    print(f'{i}, can you make it to dinner this Saturday?')

print('Excerise 3-5')

print(f'{guests[0]} can\'t make it')
guests[0] = 'Bumpa'

for i in guests:
    print(f'{i}, can you make it to dinner this Saturday?')

print('Excerise 3-6')

print('A bigger table has been permanently "borrowed"')
guests.insert(0,'Aunt Tish')
guests.insert(2,'Aunt Erica')
guests.append('Dad')
print(f'I have {len(guests)} people on the list.')
for i in guests:
    print(f'{i}, can you make it to dinner this Saturday?')

print('Excerise 3-7')

print('The table owner took offense to my borrowing.')

for i in range(0,len(guests)-2):
    t = guests.pop()
    print(f'Sorry {t} there\'s only enough room for three of us.')
    

for i in guests:
    print(f'{i}, can you make it to dinner this Saturday?')