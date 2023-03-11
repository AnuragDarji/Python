"""
<--- Error --->

1.syntax error or Compile time error
 e.g.
 missing(:)
 wrong spelling

 2.logical error 
 e.g.
 Wrong Output

 3.Runtime error
 e.g.
 divide by zero(6/0)
 wrong input

"""

# --> Exception Handling. -->

a = 5
b = 0

try:
    print(a/b)
  
except Exception as e:
    print("Hey,you cannot divide a Number by zero",e)
   
print("no error successfully done")

print("----------------------------------")


a = 5 # a = 5
b = 0 # b = 2

try:
    print("resource open")
    print(a/b)
    print("resource closed")
  
except Exception as e:
    print("Hey,you cannot divide a Number by zero",e)
 
print("----------------------------------")

a = 5 # a = 5
b = 2 # b = 0

try:
    print("resource open")
    print(a/b)
  
except Exception as e:
    print("Hey,you cannot divide a Number by zero",e)
    print("resource closed")  
    
print("----------------------------------")

# a = 5  # a = 5
# b = 2  # b = 0

try:
    print("resource open")
    print(a/b)
  
except Exception as e:
    print("Hey,you cannot divide a Number by zero",e)
 
finally: 
     print("resource closed") 
    
print("----------------------------------")

a = 5 # a = 5
b = 2 # b = 0

k = int(input("Enter a number: "))
print(k)

try:
    print("resource open")
    print(a/b)
  
except ZeroDivisionError as e:
    print("Hey,you cannot divide a Number by zero",e)
 
except ValueError as e: 
    print("Invalid Input") 
    
except Exception as e:
    print("Something went wrong...")
    
finally:
   print("resource closed") 
