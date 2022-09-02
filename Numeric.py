# WORKING WITH NUMERIC DATA

# Checking the type of a variable  
num = 3
print(type(num))

num = 3.14
n1 = 3
n2 = 2
print(type(num))

# Basic Arithmetic
print(3 * 4)
print(4 / 2) # By default, division returns a float
print(4 / 3)
print(3 / 4) # Hence, there is no problem of improper fractions returning 0

print(3 + 2)
print(3 - 2)
print(3 % 2)

print(3 // 2) # floor division

print(3 ** 2) # (3 ** 2) = 3^2

print('3/2 = ' + str(n1/n2) + '\n' + '3//2 = ' + str(n1//n2))

# Increment and decrement
print(num)
num += 1
num -= 1
print(num)

# Numeric Functions
print(abs(-3))

print(round(3.55))
print(round(3.45, 1))
print(round(3.446, 2))

# Comparisons
print(n1 > n2)
print(n1 < n2)
print(n1 != n2)
print(n1 == n2)
print(n1 >= n2)
print(n1 <= n2)

# Casting strings to numbers
num_1 = '100'
num_2 = '200'

num_1 = int(num_1)
num_2 = int(num_2)

print(num_1 + num_2)
