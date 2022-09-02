#Working with textual data
line = "big bob bites banannas"

def contains(ch, chars):
    for i in range(0, len(chars)):
        if chars[i] == ch:
            return True
    return False

def countChars(line):
    chars = "{"
    count = 0
    charsEncountered = ""

    for i in range(len(line)):
        char = line[i]
        if not contains(char, charsEncountered):
            charsEncountered = charsEncountered + str(char)
            for j in range(i, len(line)):
                if(line[j] == char):
                    count += 1
            chars = chars + (char + str(count)) + ", "
        count = 0

    chars = chars[0:len(chars)-2] + "}"
    return chars


print(f"Frequency: {countChars(line)}")