# Following methods are inplace.

# .insert(,)
courses = ['Art', 'Mathematics', 'Biology', 'Computer Science', 'Physics']
courses.insert(1, 'Cosmology')
print(courses)

# .append()
courses[1] = 'Cosmos'
courses.append("Bio Engineering")
print(courses)

# .extend()
additional_courses = ['Design', 'Color Science']
courses.extend(additional_courses)
print(courses)

# .remove()
courses.remove('Color Science')
print(courses)

# .pop()
popped = courses.pop()
print(courses)
print(popped)
