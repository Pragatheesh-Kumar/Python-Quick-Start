# Loops (List)
my_list = [1,2,3,4,5]

for i in my_list:
    print(i)

# Loops (String)
my_string = 'Ironman'

for i in my_string:
    print(i)

# Loops (Range)
my_range = range(1,5,1)

for i in my_range:
    print(i)
    
# Iterate to a new list
my_range = range(1,10,1)

my_list = []

for i in my_range:
    my_list.append(i)

print(my_range)
print(my_list)
print(type(my_range))
print(type(my_list))

#Looping a definition
def power (x,y=2):
    return x**y

my_range = range(1,10,1)

my_list = []

for i in my_range:
    value = power(i,2)
    my_list.append(value)
    
print(my_range)
print(my_list)
print(type(my_range))
print(type(my_list))

# Looping an If Statement
my_range = range(1,10,1)
divisor = 3

is_mult = []
isnt_mult = []

for i in my_range:
    if i%divisor == 0:
        is_mult.append(i)
    else:
        isnt_mult.append(i)

print(is_mult)
print(isnt_mult)

# Looping with a Try / Except
my_list = [1,'9',6.5,'Hello']

results = []

for i in my_list:
    try:
        val = i + 5
    except:
        val = 0
    finally:
        results.append(val)
        
print(results)

# While Loop
start = 10
divisor = 2
end = 1

current = start
result = []

while current > end:
    result.append(current)
    current = current/divisor
    
print(result)

#Shorthand for loop
[print(i*5) for i in range(1,5,1)]