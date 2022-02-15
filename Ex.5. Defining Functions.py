#Define (def)
def squared(x):
    return x*x

result = squared(5)

print(result)

#Multiple Variable
def power(x,y):
    return x**y

result = power(2,3)

print(result)

#Default Values
def power(x,y=2):
    return x**y

result = power(2)

print(result)

#Local Enclosing Global Built-In
def enclosed(x):
    e_enclosing = 'enclosing'
    
    def local(y):
        l_local = 'local'
        
g_global = 1

b_built_in = range(1,5,1)

#Another Example
def divisible(number, divisor):
    remainder = number%divisor
    return remainder==0

check1 = divisible(15,4)
check2 = divisible(15,3)

print(check1, check2)
