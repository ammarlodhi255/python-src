# Without using the count() method

def count_substring(my_str, sub_str):
    count = 0
    found_substr = True

    for i in range(len(my_str)):
        found_substr = True
        if my_str[i] == sub_str[0]:
            for j in range(len(sub_str)):
                if my_str[i + j] != sub_str[j]:
                    found_substr = False
                    break
            if found_substr: count += 1
    return count

print(count_substring("hello how how how ishow", "how"))