num = int(input("Enter a number: "))
num = abs(num)

if num == 0: print("0")
else:
    while num > 0:
        print(num % 10, end = " ")
        num = num // 10

