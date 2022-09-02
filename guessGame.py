userInput = int(
    input('Jani write any number for the table, and i will give that table: '))

for i in range(11):
    if i == 0:
        continue
    print(f'{userInput} x {i} = {userInput * i}')
