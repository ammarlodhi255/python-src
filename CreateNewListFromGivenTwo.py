def get_even_odd_list(list_1, list_2):
    new_list = list()
    for i in range(len(list_1)):
        if list_1[i] % 2 != 0:
            new_list.append(list_1[i])
    
    for i in range(len(list_2)):
        if list_2[i] % 2 == 0:
            new_list.append(list_2[i])
    return new_list

nums_1 = [3, 2, 2, 7, 8, 9, 12, 21, 3]
nums_2 = [2, 4, 1, 12, 13, 4, 5, 67]

print(get_even_odd_list(nums_1, nums_2))