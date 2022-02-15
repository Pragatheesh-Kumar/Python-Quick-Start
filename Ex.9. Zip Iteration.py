# Zip iteration
my_num = [5,4,3,2]
my_pow = [2,3,4,5]

my_list = []

for n,p in zip(my_num,my_pow):
    value =n**p
    my_list.append(value)
    
print(my_list)

# Zip Sorting
my_num = [3,2,4,1]
my_let = ['c','b','d','a']

my_sort = list(zip(my_num,my_let))
my_sort.sort()

var1, var2 = zip(*my_sort)

print(list(var1))
print(list(var2))