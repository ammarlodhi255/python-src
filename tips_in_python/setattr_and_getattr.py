class Person:
    pass


person = Person()

attr_name = 'first_name'
attr_value = 'Ammar'

# We can't just do this:
# person.attr_name = attr_value

# Solution:
setattr(person, attr_name, attr_value)

print(person.first_name)

# If you want to access the value of a particular attribute, give its name:
# We can't just that: print(person.attr_name)

# Solution:
value = getattr(person, attr_name)

print(value)


# Let us now create a another instance of Person and dynamically assign it attributes with values
person_info = {
    'first': 'Ammar',
    'last': 'Ahmed',
    'field_of_study': 'CompSci'
}

person = Person()

for key, value in person_info.items():
    setattr(person, key, value)

for key in person_info.keys():
    print(f'{key}: {getattr(person, key)}')
