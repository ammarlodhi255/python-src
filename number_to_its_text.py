def get_num_text(num):
    nums_text = {
        1: 'One',
        2: 'Two',
        3: 'Three',
        4: 'Four',
        5: 'Five',
        6: 'Six',
        7: 'Seven',
        8: 'Eight',
        9: 'Nine',
        0: 'Zero'
    }

    return nums_text.get(num)


def get_num_digits(num):
    nums = []
    temp_num = num

    while temp_num > 0:
        nums.append(temp_num % 10)
        temp_num //= 10

    return list(reversed(nums))


user_input = int(input('Enter a whole number: '))
nums = get_num_digits(user_input)

for num in nums:
    print(get_num_text(num), end=" ")
