import os

filepath = "file1.txt"
size = os.stat(filepath).st_size

if size != 0:
    with open(filepath, "r") as rf:
        for i, line in enumerate(rf, 1):
            if i == 4: print(line)        

