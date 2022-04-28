#Libraries needed are pyenchant and itertools. 
# Enchant is a language processing library while itertools is for iterables

import enchant 
from itertools import permutations

#Defines a dictionary object for US english
eng = enchant.Dict("en_US") 
engu = enchant.Dict("en_GB")

#Accepts input from user 
inp1 = input("Gib sCRAMBLED WORD ")
up1 = inp1.upper() 

#Turns string input to a list and sorts it 
srt_inp1 = sorted(up1) 

#Performs permutation on the sorted list 
perm_inp = permutations(srt_inp1)

#iterates through the permutations and finds the ones that are in the dictionary then prints all that match
for p in perm_inp:
    c ="".join(p) 
    if eng.check(c) == True or engu.check(c) == True:
        print(c) 
    

