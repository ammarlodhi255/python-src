def count_digits(num):
    count = 0
    while num > 0:
        num //= 10
        count += 1
    return count 

num = int(input("Enter any number: "))
print("Number of digits: {}".format(count_digits(num)))