message = "Hello World"
# .replace is not an inplace operation
message = message.replace("World", "Universe")
print(message)

new_message = f'{"I am afraid I cant do that"}, {"John!"}'
new_new_message = "{}, {}. Do you understand, john?".format(
    "I am afraid I cant do that", "John!")
print(new_message)
print(new_new_message[new_new_message.find('afraid'):])


print(help(str.capitalize))
print(message.capitalize())
