def check_palindrome(text):
    chars = []
    for i in range(len(text)):
        chars.append(text[i])
        
    upto = (len(text) // 2) + 1
    if len(text) % 2 == 0: upto = len(text) / 2

    for i in range(upto):
        if(text[i] != chars.pop()):
            return False
    return True


print(f"is madam a palindrome? {check_palindrome('madam')}")

