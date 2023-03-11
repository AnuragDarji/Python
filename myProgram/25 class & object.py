class Computer:
    
    def config(self):
        print('i5','16gb','1TB')
 
x = 5
print(type(x))

a = '8'
print(type(a))

com1 = Computer() # <-- make object
print(type(com1))

print("\n")
Computer.config(com1)  # <--call method 

com1.config() # obj<-- call method              