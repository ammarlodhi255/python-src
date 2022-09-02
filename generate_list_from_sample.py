def get_list(text):
    return text.split(', ')

def get_tuple(text):
    text_list = text.split(', ')
    return tuple(text_list)

text = input("Enter sequence of numbers followed by a comma: ")

list_1 = get_list(text)
print(f"LIST: {list_1}")

tuple_1 = get_tuple(text)
print(f"Tuple: {tuple_1}")