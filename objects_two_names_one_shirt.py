class shirt:
     
     def __init__(self):
          self.clean = True
         
          

     def make_dirty(self):
          self.clean = False


     def make_clean(self):
          self.clean = True         


red = shirt()

crimson = red 
# now red and crimson are the same 

print(id(red))

print(id(crimson))

# the same id for red and crimson  the same thing 

print(red.clean)

# info about red is it clean or not 
print(crimson.clean)

# info about crimson is it clean or not

print(red.make_dirty())

print(red.clean)
print(crimson.clean)

print(red is crimson)
# to check is it the same object

crimson = shirt()
# now making a new shirt 
print(id(red))
print(id(crimson))
#print(crimson.clean) 
print(crimson.make_clean())
print(crimson.clean)
