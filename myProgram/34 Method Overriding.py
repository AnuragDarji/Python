# <-- Method Overriding -->

class A:
    def meth1(self):
       print("meth1 of class A")

class B(A): # B extends A or inheritance
    def meth1(self):
       print("meth1 of class B")
    
    
a1 = A()
a1.meth1()

b1 = B()
b1.meth1()