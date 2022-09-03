def remove_dups(_list):
    new_list = list()
    for element in _list:
        if not element in new_list:
            new_list.append(element)
    return new_list


def get_even_indexed_chars(input_str):
    for i in range(0, len(input_str)):
        if i % 2 == 0:
            print(input_str[i])


def check_palindrome(text):
    chars = []
    for i in range(len(text)):
        chars.append(text[i])

    upto = (len(text) // 2) + 1
    if len(text) % 2 == 0:
        upto = len(text) / 2

    for i in range(upto):
        if(text[i] != chars.pop()):
            return False
    return True


def remove_first_n_chars(my_str, n):
    return my_str[n:]
