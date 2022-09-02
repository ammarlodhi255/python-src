user_input = ""

while(user_input != 'quit'):
    user_input = input('> ').casefold()

    if user_input == 'start':
        print('Car started ...')
    elif user_input == 'stop':
        print('Car stopped ...')
    elif user_input == 'help':
        print('''
        start - to start the car
        stop - to stop the car
        quit - to leave the car
        ''')
    else:
        print("I don't understand that")

print('You left the car.')
