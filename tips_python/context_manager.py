with open('file1.txt', 'r') as f:
    file_contents = f.read()

words = file_contents.split('\n')
print(len(words))
