# You can print the list:
sports = ["Hockey", "UFC", "Boxing", "Soccer"]
print(f"Sports = {sports}")

#Iterate through the list:
print()
for sport in sports:
    print(sport)

#Print a range:
print(f"\n{sports[0: 3]}")

# Last index can be accessed this way:
print(f"\nLast item in the list is: {sports[-1]}")

# Adding items to the list at the end:
print(f"\nSize Before Appending = {len(sports)}")
sports.append("Cricket")
print(sports)
print(f"Size After = {len(sports)}")

# Adding items at the specified index:
sports.insert(1, "Racing")
print(f"\nAfter inserting racing: {sports}")

# Removing item in list
sports.remove("Hockey")
print(f"\nAfter removing hockey: {sports}")

#Merging the two lists using extend() method 
additional_sports = ['Pool', 'Swimming']
sports.extend(additional_sports)
print(f"\nAfter extending: {sports}")

# You can use the list as a stack:
popped_value = sports.pop() # pops the last item of the list
print("\nSports after popping the item: {}".format(sports)) 
print(f"Popped value: {popped_value}")

#Reverse the list 
sports.reverse() 
print(f"\nSports list reversed: {sports}")

#Sorting the list:
sports.sort() 
print(f"\nSorted list: {sports}")

# Sorting numbers:
numbers = [2, 20, 0, 1, -1, 9, 3.0]
numbers.sort() 
print(f"\nNumbers = {numbers}")

numbers = [2, 20, 0, 1, -1, 9, 3.0]
numbers.sort(reverse = True)
print(f"\nNumbers sorted in reverse = {numbers}")

#Return the sorted list without altering the original list:
sorted_numbers = sorted(numbers)
print(f"\nsorted numbers = {sorted_numbers}")

# Get min and max from the list:
print(f"\nMin: {min(numbers)}, Max: {max(numbers)}")

# Get index of an item from the list:
print(f"\nIndex of Racing: {sports.index('Racing')}")

# Check whether an item exists in the list:
if 'Art' in sports:
    print("\nArt is in sports")
else: print("\nArt is not in sports\n")

#Enemurate through the list:
courses = ["Databases", "Object Orientation", "Philosophy", "Algebra", "Logic and Discrete Structures"]
for i, course in enumerate(courses):
    print(i, course)

print("\nFrom index = 1")

for i, course in enumerate(courses, start=1):
    print(i, course)

# How to convert list into string: join() method
course_str = ', '.join(courses)
print(f"\ncourse_str = {course_str}")

#split method
print(course_str.split(', ')[0])

# TUPLES: 
# They are immutable  
tuple_1 = (2, 3, 1, 12, 13)
print(f"\ntuple_1 = {tuple_1}")
# This is an error: tuple_1[0] = 2

#SETS: Unordered collection
college_courses = {"Math", "History", "Science", "Math"}
print(f"\ncollege_courses = {college_courses}")

phi_courses = {"History", "Philosophy", "Architecture and Design"}
print(f"\ncollege_courses intersection phi_courses : {college_courses.intersection(phi_courses)}")

print(f"\ncollege_courses difference phi_courses: {college_courses.difference(phi_courses)}")

print(f"\ncollege_courses union phi_courses = {college_courses.union(phi_courses)}")


# How to create empty lists, tuple, and SETS:
list_1 = [] 
# or 
list_1 = list()

tuple_1 = ()
# or
tuple_1 = tuple()

set_1 = {} # this is wrong for empty set
set_1 = set()