num = int(input("Enter a number: "))

list_of_digits = list()
while(num > 0):
    list_of_digits.append(str(num % 10))
    num = num // 10

# First method:
list_of_digits.reverse()
digits_str = " ".join(list_of_digits)
print(digits_str)

#Second method:
list_of_digits.reverse()
for i in range(len(list_of_digits)): print(list_of_digits.pop(), end = " ")

