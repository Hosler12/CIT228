import random as rand

class Die():
    def __init__(self,sides = 6):
        self.sides = sides

    def roll_dice(self):
        for i in range(1,11):
            print(f'Roll {i}: {rand.randint(1,self.sides)}')

die1 = Die()
print('Rolling die 1')
die1.roll_dice()
die2 = Die(10)
print('Rolling die 2')
die2.roll_dice()
die3 = Die(20)
print('Rolling die 3')
die3.roll_dice()