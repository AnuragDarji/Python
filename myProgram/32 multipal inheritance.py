# <-- multipal inheritance -->  

class A:
    def feature1(self):
        print("feature1  working")
    def feature2(self):
        print("feature2  working")
        
class B: 
    def feature3(self):
        print("feature3  working")
    def feature4(self):
        print("feature4  working") 

class C(A,B):
    def feature5(self):
        print("feature5  working")        
                    
a1 = A()

a1.feature1()
a1.feature2() 

print("==================================")
b1 = B()

b1.feature3()
b1.feature4() 

print("==================================")
c1 = C()

c1.feature1()
c1.feature2()
c1.feature3()
c1.feature4()
c1.feature5()