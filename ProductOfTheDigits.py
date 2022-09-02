def get_digits_product(num):
    product = 1
    while num > 0:
        product *= (num % 10)
        num = num // 10
    return product
    
num = int(input("Enter your number: "))
print(f"Product of its digits is: {get_digits_product(num)}")