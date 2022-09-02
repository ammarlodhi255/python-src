def remove_dups(_list):
    new_list = list()
    for element in _list:
        if not element in new_list:
            new_list.append(element)
    return new_list


elems = ['Ammar', 'Manaf', 'Haseeb', 'Ammar', 'Haseeb']
elems = remove_dups(elems)

print(elems)
