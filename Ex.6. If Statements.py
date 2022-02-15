# If Statement
value = 0

if value%2 == 0:
    print("Value is Even")
else:
    print('Value is Odd')
    
# Elif (Else if)
value = 7

if value%2 == 0:
    print("Divisible by 2")
elif value%3 == 0:
    print('Divisible by 3')
else:
    print("Not divisible by 2 or 3")
    
# Shorthand if else statement
value = 7

print("Value is Even") if value%2 == 0 else print ("Value is Odd")