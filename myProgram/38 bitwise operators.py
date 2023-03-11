print(~12) # Complement(NOT)
"""
12 ->  1100         13 -> 1101 
       ====              1's comp.
       0011 -> -13        0010
      -   1              +   1          
       ====              =====
       0010               0011 -> 2's comp.(-13)
       1101 -> 13
"""
print(12&13) # AND
"""                     A B | C
12 -> 1100              ======= 
13 -> 1101              0 0 | 0
      ====              0 1 | 0
      1100 -> 12        1 0 | 0
                        1 1 | 1
"""
print(12|13) # OR
"""                     A B | C
12 -> 1100              ======= 
13 -> 1101              0 0 | 0
      ====              0 1 | 1
      1101 -> 13        1 0 | 1
                        1 1 | 1
"""
print(12^13) # XOR
"""                     A B | C
12 -> 1100              ======= 
13 -> 1101              0 0 | 0
      ====              0 1 | 1
      0001 -> 1.        1 0 | 1
                        1 1 | 0
"""
print(11<<2) # Left shift
"""
11 ->  1011
      10110    __  -> 1st time shift
     101100 ->|44| -> 2nd time shift 
    
you can find => print(0b101100)= 44 
 
"""
print(11>>2) # Right shift
"""
11 ->  1011
        0101    ___  -> 1st time shift
         0010 ->|2|  -> 2nd time shift 
         
"""    