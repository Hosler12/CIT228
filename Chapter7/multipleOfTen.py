choice = input('Please select a number, and I\'ll tell you if it\'s a multiple of 10. ')

try:
    if int(choice) % 10 == 0:
        print(f'{choice} is a multiple of ten.')
    else:
        print(f'{choice} is not a multiple of ten')
except:
    print('That is not a number')