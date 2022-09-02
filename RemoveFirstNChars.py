def remove_first_n_chars(my_str, n):
    return my_str[n:]

my_str = input("Enter your string: ")
n = int(input("Enter value for n: "))

print(f"Output: {remove_first_n_chars(my_str, n)}")