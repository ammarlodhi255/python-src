# Sample: 3
# Output: 3 + 33 + 333

def get_concatenated_sum(num):
    num_str = str(num)
    temp_str = str()
    sum = 0

    for i in range(1, num + 1):
        temp_str = str()
        for j in range(1, i + 1):
            temp_str += num_str
        sum += int(temp_str)
    return sum


def get_count_sum(num):
    sum = 0
    for i in range(1, num+1):
        num = 0
        for j in range(0, i):
            num += (3 * 10**j)
        sum += num
    return sum


user_input = int(input("Enter your number: "))
print(f"Sum = {get_count_sum(user_input)}")
