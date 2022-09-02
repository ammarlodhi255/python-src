user_input = input('> ').casefold()

while(user_input != 'quit'):
    if user_input == 'start':
        print('Car started ...')
    elif user_input == 'stop':
        print('Car stopped ...')
    else:
        print("I don't understand that")

    user_input = input('> ').casefold()

print('You left the car.')
