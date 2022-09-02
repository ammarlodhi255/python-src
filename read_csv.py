def read_csv(file):
    keys_and_lines = {}
    with open(file, 'r') as rf:
        for i, line in enumerate(rf):
            keys_and_lines[i] = (" ").join(line.split(','))
    return keys_and_lines

records = read_csv('D:\\Lab1\\iris.csv')

for key, record in records.items():
    print(key, record)
    
# list_1 = ['1', '2', '3', '4']
# str_nums = " ".join(list_1)

# print(str_nums)
