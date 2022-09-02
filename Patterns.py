# for i in range(1, 6):
#     for j in range(0, i):
#         print(i, end = " ") # This is how you avoid going to new line in python using print method
#     print()

# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print(j, end = ' ')
#     print()

# for i in range(5, 0, -1):
#     for j in range(i, 0, -1):
#         print(j, end = ' ')
#     print()

list_1 = [1, 2, 3, 4, 5, 6, 7]

print("[", end = "")
for i in range(len(list_1) - 1, -1, -1):
    print(list_1[i], end = "")
    if i != 0: print(", ", end = "")
    else: print("]")


for i in range(-1, -(len(list_1) + 1), -1):
    print(list_1[i])
