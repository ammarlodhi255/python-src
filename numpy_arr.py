import numpy as np # BTW numpy has a whole sub module for matrix operations called numpy.mat    

#Numpy is the base for all the data structures in python

my_arr = np.array(94) #0D array
print(my_arr)

my_arr = np.array(['Ammar', 'Ahmed', 'Sukkur IBA', 'Computer Science']) #1D Array
print(my_arr)

my_arr = my_arr.reshape(2, 2) # reshape function reshapes the array into matrix like form
print(my_arr)

my_arr = np.array([[1, 2, 3], [4, 5, 6]])

for i in range(0, len(my_arr)):
    for j in range(0, len(my_arr[i])):
        print(my_arr[i][j], end=' ')

print('\n3D Array: ')
my_arr = np.array([[[7, 8, 9], [10, 11, 12]], [[1, 2, 3], [4, 5, 6]]])

for i in range(0, len(my_arr)):
    for j in range(0, len(my_arr[i])):
        for k in range(0, len(my_arr[i][j])):
            print(my_arr[i][j][k])

print(f'Dimension of my_arr: {my_arr.ndim}') # Shows the dimension of the array