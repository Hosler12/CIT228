import os, random as rand

file = 'Chapter10/guest.txt'
'''
name = input("What is your name (q to quit)? ")
with open(file) as File:
    while name!='q':
        name += "\n"
        File.write(name)   
        print(f'Nice to meet you {name}')

        name = input("What is your name (q to quit)? ")
''' 

if os.path.exists(file):
    os.remove(file)

name = input('Please enter your name or q to quit: ')
rooms = []
maxRooms = 50
with open(file,"w") as File:
    while name!='q':
        if len(rooms) == maxRooms:
            print(f'Rooms full. Please return on a later date {name}')
            break
        while True:
            x = rand.randint(1,maxRooms)
            if x not in rooms:
                print(f'Nice to meet you {name}, your room is {x}')
                rooms.append(x)
                break
        
        File.write(f'{name} : room {x}\n')   
        
        name = input("What is your name (q to quit)? ")

with open(file) as File:
    for line in File:
        print(line)