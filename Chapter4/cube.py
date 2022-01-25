cubeList = []
for i in range(1,11):
    print(f'{i} cubed is {i**3}')
    cubeList.append(i**3)
print(cubeList)

cubeComprehension = [i ** 3 for i in range(1,11)]
print(cubeComprehension)