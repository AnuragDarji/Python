"""f = open('MyData','w')
f.write("Hi anurag")

f = open('MyData','r')
print(f.read())

f1 = open('abc','w')

for Data in f:
    print(Data)"""

print("==================================")   
#f = open('xyz','w')
f = open('xyz','a') # append previous output exist

f.write("Hi anurag")
#f.write("alright")

f = open('xyz','r')
print(f.read())