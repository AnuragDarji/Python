# --> in-built function <--
#int()
#str()
#bool()

# --> module function <--
#import math
#print(dir(math)) # <-- all math module functions

#from math import sqrt
#print(sqrt(16))

#from math import * # select all function *
#print(sqrt(16))

# --> user-defined function <--

#def print_sum(first,second):
#    print(first + second)
    
#print_sum(2,3)

def print_sum(first,second=4):
    print(first + second)
    
print_sum(2)