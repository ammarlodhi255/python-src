#File Objects

f = open("text.txt", "r") # pass lower case 'w' for writing, 'a' for appending, and 'r+' for reading and writing
print(f"Name of the file: {f.name}")
f.close()

# Better way is to use context manager:

with open("text.txt", "r") as f:
    all_contents = f.read(100)
    print(all_contents) 

    f.seek(0) # Start again from 0th position of the file

    for line in f:
        print(line, end='')

    f.seek(0)

    line = f.readline()
    while line != '': # Or check if len(line) > 0
        print(line, end='') 
        line = f.readline()

    f.seek(0)

    f_contents = f.read(10)
    while f_contents != '':
         # f.tell() is the current cursor position of the file
        print(f"{f.tell()}{f_contents}", end='')
        f_contents = f.read(10)

print()

with open("text2.txt", "w") as f:
    f.write("Test file for writing\nThis is new line already?")
    f.seek(0)
    f.write("First line lol\n") # this will overwrite the characters in the first line
    

