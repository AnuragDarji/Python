#<-- Method Overloading-->
class Student:
    def sum(self,a=None,b=None,c=None):
              
        if a!=None and b!=None and c!=None: 
            print('Sum is:', a+b+c) 
        elif a!=None and b!=None: 
            print('Sum is:', a+b) 
        elif a!=None: 
            print("Sum is:",a)
        else:
            print("Sum is: 0")
            
s1 = Student()

s1.sum(3,4)    