def sum_exponents(num, max_exp): #Outputs: n + n^2 + n^3 +....+ n^max_exp
    sum = 0
    for i in range(1, max_exp + 1):
        mult = 1
        for j in range(i): mult *= num
        print()
        sum += mult
    return sum

def sum_concatenate(num): # Outputs: n+nn+nnn
    num_str = str(num)
    sum = 0
    for i in range(1, 4):
        temp_str = str()
        for j in range(1, i+1):
            temp_str += num_str
        sum += int(temp_str)
    return sum

print(sum_exponents(5, 3))
print(f"Sum = {sum_concatenate(5)}")
