from check_prime import check_prime as is_prime

start = int(input("Start = "))
end = int(input("End = "))

for i in range(start, end + 1, 1):
    if is_prime(i):
        print(f"{i} is prime")