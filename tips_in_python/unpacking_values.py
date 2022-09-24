# Unpacking
a, b = (1, 2)
print(a, b)

# But what if I only need the value 1?
# The convention is to use the underscore as the variable name for the value you don't need

a, _ = (1, 2)
print(a)


# Following are incorrect instructions and will throw an error:

# a, b, c = (1, 2)
# ValueError: not enough values to unpack (expected 3, got 2)

# a, b, c = (1, 2, 3, 4)
# ValueError: too many values to unpack (expected 3)

# We can fix the preceding problem with:

a, b, *c = (1, 2, 3, 4, 5)
print(a, b)
print(c)

# If you dont need the rest of the values, use an underscore
a, b, *_ = (1, 2, 3, 4, 5)

# If you want to access the last value:
*_, last = (1, 2, 3, 4, 5, 6)
print(last)