numbers = [7, 8, 3, 1, 5, 0]


def bubble_sort(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers) - 1):
            if numbers[j] > numbers[j + 1]:
                temp = numbers[j]
                numbers[j] = numbers[j + 1]
                numbers[j + 1] = temp

    return numbers


def selection_sort(numbers):
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            if numbers[i] > numbers[j]:
                temp = numbers[i]
                numbers[i] = numbers[j]
                numbers[j] = temp

    return numbers


print(selection_sort(numbers))
