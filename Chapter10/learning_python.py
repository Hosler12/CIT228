file = 'Chapter10/learning_python.txt'
print('#1')
with open(file) as fileObject:
    fileContents = fileObject.read()

print(fileContents)
print('#2')
with open(file) as fileObject:
    for i in fileObject:
        print(i)

print('#3')
with open(file) as fileObject:
    fileContents = fileObject.readlines()

for i in fileContents:
    print(i)

print('10-2')
with open(file) as fileObject:
    for i in fileObject:
        print(f'\nOriginal: {i}')
        print('Replaced:', {i.replace('python','c#')})