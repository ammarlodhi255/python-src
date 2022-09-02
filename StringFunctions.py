line = "The Universe is Expanding"
print(line.count('i'))
print(line.upper())
print(line.lower())
print(line[0:len(line)])  # this is equivalent to the line below
print(line[0:])

print("ammar".title())
print(line[line.find('U'):])

newline = line.replace("Universe", "Galaxy")
print(newline)

print(dir(str))
