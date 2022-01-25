from audioop import avg
import random
number = random.randrange(10,100)
numList = list(range(0,number))
print(numList)
print(f'Min is {min(numList)}')
print(f'Max is {max(numList)}')
print(f'Avg is {avg(numList)}')