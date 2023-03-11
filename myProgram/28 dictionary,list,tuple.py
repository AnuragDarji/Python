d1 ={}
print(type(d1)) # dictionary 
d1 =[]
print(type(d1)) # list
d1 =()
print(type(d1)) # tuple

print("==================================")

d2 ={"Anurag":"burger","Rohan":"Fish","pintu":"lolipop","Naitik":{"B":"maggi","L":"roti","D":"pasta"}}
print(d2)
print(d2["Anurag"])
print(d2["Rohan"])
print(d2["pintu"])
print(d2["Naitik"])
print(d2["Naitik"]["B"])

# --> add new dictionary
d2["shubham"] = "Pizza"
print(d2)   