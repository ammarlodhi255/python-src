import os

# get current working directory
print(os.getcwd())

# change current working directory
os.chdir(r'C:\Users\Ammar\Desktop')
print(os.getcwd())

# get list of all file names in the cwd, or pass in the path inside listdir(path)
print(os.listdir())

# Other methods:

# os.mkdir(path)
# os.makedirs(path1/path2/path3/..)
# os.rmdir(path)
# os.removedirs(path1/path2/path3/..)
# os.rename(filename, new_name)

# os.walk() generates three tuples: current directory, directories with that dir, and all the filenames
for curr_dir, dirs, filenames in os.walk(os.getcwd()):
    for file in filenames:
        print(file)
