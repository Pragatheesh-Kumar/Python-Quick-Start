#unhandled error
#var1 = 4.5
#var2 = '5'

#sum = var1 + var2
#print(sum)

#Handled ! Using Try - Except
var1 = 4.5
var2 = '5'

try:
    sum = var1 + var2
    print(sum)
except:
    print('Inputs must be integer/float or string')

# Else / Finally
var1 = 4.5
var2 = 5

try:
    sum = var1 + var2
    print(sum)
except:
    print('Inputs must be integer/float or string')
else:
    print('Script was successful')
finally:
    print('Script was run')