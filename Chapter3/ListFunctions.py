functions = ['f-string','del','remove','sorted','reverse','sort','len','pop']

print(f'Starting list: {functions}')
print('This chapter attempted to teach me many things about lists.')

print('For example, del, pop, and remove can take items out of the list.')
del functions[1]
print(f'Functions[1] deleted: {functions}')
functions.pop()
print(f'Pop used: {functions}')
functions.remove('remove')
print(f'Remove removed: {functions}')

print('Append and insert can be used to add things after the list is made')
functions.insert(1,'insert')
print(f'Insert inserted: {functions}')
functions.append('append')
print(f'Append appended: {functions}')

print('The last major section is about ways to look at the data in different orders')
print(f'Sorted: {sorted(functions)}')
print(f'No actual change: {functions}')
functions.sort()
print(f'Sort used: {functions}')
functions.reverse()
print(f'Reversed: {functions}')

print(f'The final list count is: {len(functions)}')