# Building a List

my_list = [1,2,3,4,5]
my_type = type(my_list)

print(my_list)
print(my_type)

# Item at Index

my_object = my_list[4]
print(my_object)

# Item at Index (Sub-Lists)

my_list = [1,2,3],[4,5,6]
my_object = my_list[0][2]
print(my_list)

# Replace Item at Index

my_list = [1,2,3,4,5,6]
my_list[2] = 'A'
print(my_list)

# Remove Item at Index

my_list = [1,2,3,4,5,6]
del(my_list[0])
print(my_list)

# Append Item

my_list = [1,2,3]
my_list.append(4)
print(my_list)

# Length Function

my_list = [1,2,3]
my_length = len(my_list)
print(my_length)

# Slicing

my_list = [0,1,2,3,4,5]
my_slice = my_list[2:4]
print(my_slice)

# Slicing (to/from index)

my_list = [0,1,2,3,4,5]
my_slice1 = my_list[:4]
my_slice2 = my_list[2:]
print(my_slice1)
print(my_slice2)

# Replace slice

my_list = [0,1,2,3,4,5]
my_list[1:4] = ["x", "y", "z"]
print(my_list)

# Striding

my_list = [0,1,2,3,4,5,6,7,8,9]
my_stride = my_list[0:11:2]
print(my_stride)

# Ranges

my_range = range(0,10,1)
print(my_range)

for i in my_range:
    print(i)
    
# Function( Min / Max )

my_list = [0,2,5,10,99]

my_min = min(my_list)
my_max = max(my_list)

print([my_min,my_max])

# Sorted

my_list = [0,7,5,3,4,9]

my_sort = sorted(my_list)
my_sort_reverse = sorted(my_list, reverse = True)

print(my_sort)
print(my_sort_reverse)

# Reversed

my_list = [1,2,3,4,5]

my_rev = reversed(my_list)
my_list_reverse = list(my_rev)

print(my_list_reverse)

# Get Index of Item

my_list = [1,2,3,4,5]

my_index = my_list.index(2)

print(my_index)

# Recursive Lists

my_list = [1,2,3,4,5]
your_list = my_list

my_list.append(6)

print(your_list)

# Dictionaries

my_dictionary = {1:['a','b'], 2: ['c','d']}
my_type = type(my_dictionary)

print(my_type)

# Lists and Arithmetic

list_1 = [1,2,3]
list_2 = [4,5,6]

list_3 = list_1 + list_2

print(list_3)

# Numpy Arrays

list_1 = [1,2,3,4]
list_2 = [4,5,6,7]

#print(list_1*list_2)
# List has to be converted to Arrays for parallel fucntions

import numpy as np

list_1 = [1,2,3,4]
list_2 = [4,5,6,7]

array1 = np.array(list_1)
array2 = np.array(list_2)

print(array1*array2)
