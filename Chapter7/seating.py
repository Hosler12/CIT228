while True:
    choice = input('How many people are with you today? ')
    try:
        choice = int(choice)
        if choice > 8:
            print('Please wait for a larger table')
        else:
            print('Your table is ready')
        break
    except:
        print('Please enter a valid number.')