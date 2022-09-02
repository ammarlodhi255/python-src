# Working With Textual Data

# Backslash to handle double quote in between the string
message = "Reservoir\" Dogs" 
print(message)

# Following is the way to store multiple lines in a string variable
multiple_line = """Courage the cowardly dog was 
a good cartoon in the 1990's, 
Also dexter"""  
print(multiple_line)

# Length of the string
print(len(message))

# Accessing individual characters
print(message[0] + message[1] + message[len(message) - 1])

# Accessing range of characters
print(message[0:9])
print(message[0:len(message)-1])

print(message[:9])
print(message[11:])

# String functions
print(message.lower())
print(message.upper())

print(message.count("Dogs")) # count() function finds the number of occurrence of a string within a string
print(message.count('o'))

print(message.find('Dogs')) # find() function finds the starting index of the string, returns -1 if string doesn't appear 
print(message.find('"'))

message2 = message.replace("\"", "") # replace() function replaces the specified string within a string
print(message2)
message = message2
print(message)

# Concatenation 
greeting = 'Hello'
name = ' Ammar'
print(greeting + name)

greet = greeting + name
print(greet)

# More robust way to concatenate

welcome = 'Welcome!'

greet = '{} {}. {}'.format(greeting, name, welcome)
new_greet = f'{greeting} {name.upper()}. {welcome}' # fstrings, more easy way

print(greet)
print(new_greet)

# To see the number of methods available for a particular datatype
#print(dir(message))

#print(help(str))

#print(help(str.isalpha))

print(message[message.find(' ') + 1:])

