def count_digits(num):
    count = 0
    while num > 0:
        num //= 10
        count += 1
    return count


def check_prime(num):
    if num % 2 == 0:
        return False

    for i in range(2, num // 2, 1):
        if num % i == 0:
            return False

    return True


def get_primes(start, end):
    primes = []
    for i in range(start, end + 1, 1):
        if is_prime(i):
            primes.append(i)
    return primes
