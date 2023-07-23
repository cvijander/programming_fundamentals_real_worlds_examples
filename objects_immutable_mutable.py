closet = [
    'shirt',
    'hat',
    'jacket',
    'socks',
    'pants',
]

print(closet)

print(id(closet))

closet.remove('hat')
#removes item from closet
print(closet)

print(id(closet))
# same id , but value of list object because it is mutable - it can be changed

words = "You are wearing that"

print(words)

print(id(words))
#print an id of words string 

words = words + ' because you look great!'

print(words)

# but id is now changed
print(id(words))
# string are immutable and then they created a new string  in new location 

