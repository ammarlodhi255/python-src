# Dictionaries: Used for working with key-value pairs.
# The 'key' is a unique identifier that we can use to access the associated value.

student = {'Name':'Ammar', 'Age':25, 'Courses':['Databases', 'Data Structures'], 0:'023-19-0107'}
print(student['Courses'])
print(student[0]) #These key-value pairs can be of any combination of data types

# get method: A better way to access values
print(student.get(0, 'Not Found')) # In case the key doesn't exist, 'Not Found' will be printed

# Add the key value pair:
student['phone'] = '444-444-444-777' # This is used for adding as well as updating the key, value pairs
print(student.get('phone', 'Not Found'))

# Update the key value pair:
student['Name'] = 'Ammar Ahmed'
print(student.get('Name', 'Not Found'))

# print the whole dict:
print(student)

#Update multiple values:
student.update({'phone':'1123-020255', 'Age':22})
print(f"After updating: {student}")

#Delete key-value pair:
del student['phone']
print(f"After deleting {student}")

# Pop a value from dictionary:
age = student.pop('Age')
print(student)
print(f"Age: {age}")

# getting keys, values, items:
print(student.keys())
print(student.values())
print(student.items())

#Iterate through the dictionary:
for key, value in student.items():
    print(key, ':', value)