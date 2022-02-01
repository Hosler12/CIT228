import random
while True:
    try:
        count = int(input('How many math problems would you like to practice: '))
        break
    except:
        print('Please enter a valid number')
y = 0
correct = 0
while y < count:
    rand1 = random.randrange(1,1000)
    rand2 = random.randrange(1,1000)
    answer = input(f'What is {rand1} + {rand2}: ')
    try:
        if int(answer) == rand1 + rand2:
            print('Good job')
            correct += 1
        else:
            print(f'The correct answer was {rand1+rand2}')
    except:
        print('That doesn\'t make sense')
    y += 1

print(f'You got {correct} correct')