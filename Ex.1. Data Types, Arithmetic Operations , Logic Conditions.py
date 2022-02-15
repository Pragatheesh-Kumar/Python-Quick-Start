# Data types
my_int = 5
my_float = 5.7
my_bool = True
my_string = "text"
my_list = [1,2,3]

print(my_int)
print(my_float)
print(my_bool)
print(my_string)
print(my_list)

# Checking the data types
type_int = type(my_int)
type_float = type(my_float)
type_bool = type(my_bool)
type_str = type(my_string)
type_list = type(my_list)

print(type_int)
print(type_float)
print(type_bool)
print(type_str)
print(type_list)

# Converting data types
my_int = 5

my_float_num = float(my_int)
my_boolean = bool(my_int)
my_str = str(my_int)

print(my_int)
print(my_float_num)
print(my_boolean)
print(my_str)

# Arithmetic operations
a = 1
b = 5.6

my_sum = a + b

print(my_sum)
print(type(my_sum))

my_str1 = "Good"
my_str2 = "Morning !"

greeting = my_str1 + " " + my_str2

print(greeting)

# Logic Conditions
my_equal = 1==9
print(my_equal)
#NOT
not_myequal = not(my_equal)
print(not_myequal)
#OR
or_myequal = my_equal or not_myequal
print(or_myequal)
#AND
and_myequal = my_equal and not_myequal
print(and_myequal)