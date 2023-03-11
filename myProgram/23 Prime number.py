print("==================================")
num = input("Enter Number: ")
num = int(num)

#for i in range(2,num):
#    if(num%i == 0):
#        print("not prime")
#    break;
#if(num%i != 0):
#    print("prime")
  
for i in range(2,num):
    if(num%i == 0):
        print("not prime") 
        break 
else:
    print("prime")
print("==================================")