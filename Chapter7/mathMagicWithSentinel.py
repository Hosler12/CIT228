import random

correct = 0
play = True
while play:
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
    choice = input('Would you like to continue? Y or n:' ).lower()
    if choice == 'n' or choice == 'no':
        play = False
    

print(f'You got {correct} correct')