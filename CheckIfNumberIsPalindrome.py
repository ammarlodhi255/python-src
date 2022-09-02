# First Way: Use the stack
def check_palindrome(num):
    num_str = str(num)
    num_list = list()
    for i in range(len(num_str)):
        num_list.append(num_str[i])
    
    for i in range((len(num_str) // 2) + 1):
        if num_list.pop() != num_str[i]: return False
    
    return True

# Second way: Use two pointers
def check_palindrome_num(num): 
    num_str = str(num)
    j = len(num_str) - 1
    for i in range((len(num_str) // 2) + 1):
        if num_str[i] != num_str[j]: return False
        j -= 1
    return True

# Third way: Reverse the num and check if it equals the original:
def check_palindrome_3(num): 
    temp_num = num
    reverse_num = 0

    while temp_num > 0:
        remainder = temp_num % 10
        reverse_num = (reverse_num * 10) + remainder
        temp_num = temp_num // 10
    
    return num == reverse_num

print(check_palindrome(4334))
print(check_palindrome_num(4334))
print(check_palindrome_3(4334))