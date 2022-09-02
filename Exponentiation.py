def exponent(base, exp):
    out_str = str()
    result = 1
    for i in range(0, exp):
        result *= base
        out_str += str(base) + " * "
    out_str = out_str[:len(out_str) - 3]
    print(f"{base} raised to the {exp} power is: {result} i.e ({out_str} = {result})")


exponent(4, 4)