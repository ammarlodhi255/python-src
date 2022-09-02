def get_even_indexed_chars(input_str):
    for i in range(0, len(input_str)):
        if i % 2 == 0:
            print(input_str[i])

input_str = input("Enter your text: ")
print(f"Original String is: {input_str}\nPrinting only even index chars:")
get_even_indexed_chars(input_str)