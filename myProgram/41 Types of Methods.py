""" Types of methods 
    1. instance method
        |-> 1.Accessor method
            2.Mutator method
    2. class method 
    3. static method
-> In case of variable class variable equal static variable 
but,in method class method and variable method are different.
"""
# <--- instance method --->
class Student:
    
    school = 'Telusko'
        
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        
    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3
        
    def get_m1(self):  # fetch value(getters) -> Accessor method
        return self.m1
      
    def set_m1(self,value): # change value(setters) ->Mutator Method
         self.m1 = value
        
s1 = Student(12,32,44)
s2 = Student(24,48,55)

print(s1.avg())
print(s2.avg()) 

s1.set_m1(20)
print(s1.get_m1())

print("=================================")

# <--- class method --->
class Student:
    
    school = 'Telusko'
        
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        
    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3
    
    @classmethod 
    def info(cls):
        return cls.school       
                    
s1 = Student(12,32,44)
s2 = Student(24,48,55)

print(Student.info())

print("=================================")

# <--- static method ---> 
class Student:
    
    school = 'Telusko'
        
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        
    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3
    
    @staticmethod 
    def info():
        print("this is static method...")      
                    
s1 = Student(12,32,44)
s2 = Student(24,48,55)

Student.info()  