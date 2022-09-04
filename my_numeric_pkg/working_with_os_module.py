import os

# get current working directory
print(os.getcwd())

# change current working directory
os.chdir(r'C:\Users\Ammar\Desktop')
print(os.getcwd())

# get list of all file names in the cwd, or pass in the path inside listdir(path)
print(os.listdir())

# Other important methods:

# os.mkdir(path)
# os.makedirs(path1/path2/path3/..)
# os.rmdir(path)
# os.removedirs(path1/path2/path3/..)
# os.rename(filename, new_name)

# os.walk() generates three tuples: current directory, directories with that dir, and all the filenames
for curr_dir, dirs, filenames in os.walk(os.getcwd()):
    for file in filenames:
        print(file)

# concatenate path with a filename:
print(os.path.join(os.getcwd(), 'SLACK.INK'))

# basename(If you only want the filename in the path) and dirname(If you only want the dirname)

print(os.path.basename('p/r/s.txt'))
print(os.path.dirname('dir1/t.txt'))

# Useful methods:

# os.path.split()
# os.path.exists()
# os.path.isfile()
# os.path.isdir()

# os.path.splittext() -> use this to get extension (check its output first)
