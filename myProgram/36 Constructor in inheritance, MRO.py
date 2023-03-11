# <---   Constructor in inheritance.   ---> 

class A: 
    def __init__(self):
        print("init in A")
        
    def feature1(self):
        print("feature1  working")
        
    def feature2(self):
        print("feature2  working")
        
class B(A):
    def __init__(self):
        super().__init__()
        print("init in B")
        
    def feature3(self):
        print("feature3  working")
        
    def feature4(self):
        print("feature4  working")      
                    
b1 = B() 
 
print("----------------------------------")
# <-- Method Resolution Order.-->

class A: 
    def __init__(self):
        print("init in A")
        
    def feature1(self):
        print("feature1  working")
        
    def feature2(self):
        print("feature2  working")
        
class B:
    def __init__(self):
        print("init in B")
        
    def feature3(self):
        print("feature3  working")
        
    def feature4(self):
        print("feature4  working")   
        
class C(A,B):
    def __init__(self):
        super().__init__()
        print("init in c")
        
c1 = C() # it is call left to right (MRO)
 
print("----------------------------------")

# in method -->  called left to right (MRO)

class A: 
    def __init__(self):
        print("init in A")
        
    def feature1(self):
        print("feature1 of A working")
        
    def feature2(self):
        print("feature2  working")
        
class B:
    def __init__(self):
        print("init in B")
        
    def feature1(self):
        print("feature1 of B  working")
        
    def feature4(self):
        print("feature4  working")   
        
class C(A,B):
    def __init__(self):
        super().__init__()
        print("init in c")
        
c1 = C()   
c1.feature1()   