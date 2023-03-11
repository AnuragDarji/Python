class Student:  # outer class
    
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.laptop()
                
    def show(self):
        print(s2.name ,s2.rollno)
        
    class laptop:  # inner class
        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = 8
    
s1 = Student('tom',3)
s2 = Student('Anurag',7)

#print(s2.name ,s2.rollno)
s1.show()

# inner class call
print(s1.lap.brand)

lap1 = s1.lap
lap2 = s2.lap

print(id(lap1))
print(id(lap2))

print("=================================")

class Student:
    
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
       # self.lap = self.laptop()
                
    def show(self):
        print(s2.name ,s2.rollno)
        
    class laptop:
        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = 8
        
        def show(self):
            print(self.brand,self.cpu,self.ram)
            
s1 = Student.laptop()

s1.show()  

print("=================================")

class Student:
    
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.laptop()
                
    def show(self):
        print(s2.name ,s2.rollno)
        self.lap.show()
        
    class laptop:
        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = 8
        
        def show(self):
            print(self.brand,self.cpu,self.ram) 
            
s1 = Student('Anurag',7) 

s1.show()                      