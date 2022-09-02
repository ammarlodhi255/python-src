def first_equal_last(list_1):
    return list_1[0] == list_1[-1]

nums_1 = [2, 23, 12, 1, 2, 3]
nums_2 = [23, 4, 1, 12, 23]

print(f"does {nums_1} have first and last numbers same: {first_equal_last(nums_1)}")
print(f"does {nums_2} have first and last numbers same: {first_equal_last(nums_2)}")