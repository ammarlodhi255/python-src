# get squares of of nums excluding the ones already present
nums = [1, 2, 3, 4, 5, 6, 7]
squares1 = [16, 49, 1]

squares2 = [num ** 2 for num in nums if num**2 not in squares1]
print(squares2)
