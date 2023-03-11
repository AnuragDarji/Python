# <----- instance variable  ---->

class Car:

    def __init__(self):
        self.mil = 10     # <-|
        self.com = "BMW"  # <-| this two instance variables.
       
c1 = Car()
c2 = Car()

c1.mil = 8 

print(c1.mil , c1.com)
print(c2.mil , c2.com )

"""
class variable also call static variable
 ______________
 | wheels = 5 | --> class variable
 |____________|
 | __init__() |
 | mil = 10   | --> instance variable
 | com = BMW  | 
 |____________|

"""

print("----------------------------------")

class Car:
    
    wheels = 4    # class variable
    
    def __init__(self):
        self.mil = 10
        self.com = "BMW"
       
c1 = Car()
c2 = Car()

c1.mil = 8 

print(c1.mil , c1.com , c1.wheels)
print(c2.mil , c2.com , c2.wheels)