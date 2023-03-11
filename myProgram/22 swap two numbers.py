print("==================================")
#<------ 1.swap two numbers -------->
a = 5
b = 6

temp = a
a = b
b = temp

print("a="+str(a))
print("b="+str(b))

print("----------------------------------")
# <-- 2.swap two numbers -->
a = 5
b = 6

a = a+b # 11
b = a-b # 11-6=5
a = a-b # 11-5=6

print("a="+str(a))
print("b="+str(b))

print("----------------------------------")
# <-- 3.swap two numbers -->
a = 5
b = 6

a = a^b 
# 5^6
# 0101^0110
#  0101
#^ 0110
# ======
#  0011 = 3
b = a^b
#  0011
#^ 0110
# ======
#  0101 = 5 
a = a^b 
#  0011
#^ 0101
# ======
#  0110 = 6

print("a="+str(a))
print("b="+str(b))

print("----------------------------------")
# <-- 4.swap two numbers -->
a = 5
b = 6

a,b = b,a

print("a="+str(a))
print("b="+str(b))
print("==================================")