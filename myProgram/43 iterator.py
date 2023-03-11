# iterator-> in c language i++ are working like iterator.

nums = [7,6,9,5]  
 
# 1. print(nums[0])

""" 2.
for i in nums:
    print(i)
    #print(i,end="") 
""" 
 
it = iter(nums) 
print(it.__next__())
print(it.__next__()) # it will preserve the state of last value.
# unother way to call.
print(next(it)) 
print(next(it)) 

print("=================================")

class TopTen:

    def __init__(self):
        self.num = 1
        
    def __iter__(self):
        return self
    
    def __next__(self):
       
        if self.num <= 10:
            val = self.num
            self.num += 1
        
            return val
        else:
            raise StopIteration 
 
values = TopTen()

print(next(values))

for i in values:
    print(i) 
    
#print(values.__next__()) 
#print(values.__next__()) 
    
print("=================================")                                                                