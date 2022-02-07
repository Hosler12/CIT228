import random as rand

ticketOptions = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e']
winner = []
for i in range(0,4):
    winner.append(rand.choice(ticketOptions))

print(f'Any ticket that has {winner} wins!')
tries = 0
while True:
    tries += 1
    myTicket = []
    for i in range(0,4):
        myTicket.append(rand.choice(ticketOptions))
    if myTicket == winner:
        print(f'It took {tries} attempts to win.')
        break