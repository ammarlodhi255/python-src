def get_first_last(list1, target):
    first_encounter = False
    track = 0
    indices = []
    for i in range(len(list1)):
        if (not first_encounter) and list1[i] == target:
            indices.append(i)
            first_encounter = True
        elif list1[i] == target:
            track = i
    indices.append(track)
    return indices


if __name__ == "__main__":
    my_numbers = [1, 6, 6, 6, 6, 6, 8, 9, 9, 9]
    indices = get_first_last(my_numbers, 6)
    print(indices)
