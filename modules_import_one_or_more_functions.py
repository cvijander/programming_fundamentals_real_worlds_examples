import random
print(random.randint(1,20))

# because it is whole module, it has to be always entered

from random import randint
# for uploading only one function from module 
# 
print(randint(1,20))
#random int function between 1 -20

print(random.random())
# random number

from random import random
# now points to single function instead of function 

import random as rand 
# changing the name of the module to eliminate the mistake of dupling it 
print(rand.random())
print(rand.randint(1,20))

import urllib.request
print(urllib.request.urlopen('http://www.google.com'))




