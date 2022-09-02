# Get data type of any variable
num = 3
data_type = str(type(num))[str(type(num)).find("'") + 1 : str(type(num)).find("]") - 1]
print(data_type)

# String to int conversion
var = "3"
int_var = int(var)
print(int_var)

# Floor division
div_result = 5 // 6
print(div_result)

# Exponentiation in python
print(5 ** 2)

# Functions
div =  (11 / 3)
print(f"11 / 3 rounded up to one decimal digit: {round(div, 1)}, not rounded: {div}")

number = -23
print(abs(number))