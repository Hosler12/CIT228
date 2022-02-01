import random

y = 0
correct = 0
incorrect = 0
while y < 10:
    rand1 = random.randrange(1,1000)
    rand2 = random.randrange(1,1000)
    answer = input(f'What is {rand1} + {rand2}: ')
    try:
        if int(answer) == rand1 + rand2:
            print('Good job')
            correct += 1
        else:
            print(f'The correct answer was {rand1+rand2}')
            incorrect += 1
    except:
        print('That doesn\'t make sense')
        incorrect += 1
    if incorrect > 5:
        print('You should study some.')
        break
    y += 1

print(f'You got {correct} correct')