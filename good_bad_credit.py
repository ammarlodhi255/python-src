def get_payment(house_price, good_credit):
    payment = 0
    if good_credit:
        payment = house_price * 1.1
    else:
        payment = house_price * 1.2
    return round(payment, 2)


house_price = float(input('Enter your house price: '))
credit = input('Do you have good credit? Y/N: ')
credit = True if credit.casefold() == 'y' else False

print(f'Your Payment Is: {get_payment(house_price, credit)}')
