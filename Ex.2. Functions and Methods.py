# Functions
#len(variable)

my_list = [1,2,3,4,5]
my_string = "string"
length_mylist = len(my_list)
length_mystring = len(my_string)

print(length_mylist)
print(length_mystring)

# Methods

my_string = "this is a string"
string_upper = my_string.upper()
string_lower = my_string.lower()
string_title = my_string.title()

print(string_upper)
print(string_lower)
print(string_title)

# Methods (multiple, fields)

my_float = 9.581
my_round = round(my_float, 1)
print(my_round )

my_string = "My name is Pragatheesh"
my_split = my_string.split(" ", 1)
print(my_split)

# Finding Help

my_name = "My name is Pragatheesh"
my_help = dir(my_name)
print(my_help)

# Method - Object.__doc__
my_name = "My name is Pragatheesh"
my_help = my_name.split.__doc__
print(my_help)

# Importing Libraries
import math
print(math.pi)

# Importing Libraries (ALIAS)

import math as mt
print(mt.pi)

# Importing Attributes

from math import pi
print(pi)