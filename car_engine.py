user_input = ""

while(True):
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
    elif user_input == 'quit':
        break
    else:
        print("I don't understand that")

print('You left the car.')
