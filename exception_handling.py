def floor_division(num1, num2):
    try:
        result = num1 / num2
    except ArithmeticError as e:
        print('Arithmetic Error')
        return None
    return result

num1 = float(input('Enter num1: '))
num2 = float(input('Enter num2: '))

print(floor_division(num1, num2))

