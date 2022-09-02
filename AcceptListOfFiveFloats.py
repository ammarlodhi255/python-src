iterate = 0
list_of_floats = list()

while(iterate < 5):
    list_of_floats.append(float(input(f"Enter float number {iterate + 1}: ")))
    iterate += 1
print(f"Output: {list_of_floats}")