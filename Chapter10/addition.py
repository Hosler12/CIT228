while True:
    try:
        x = int(input('Please enter the first number: '))
    except:
        print('Please enter an integer')
        continue
    try:
        y = int(input('Please enter the second number: '))
    except:
        print('Please enter an integer')
        continue
    print(f'The answer is: {x+y}')
    if input('Enter q to quit. Any other input will continue: ') == 'q':
        break