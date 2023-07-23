class shirt:
     
     def _init_(self):
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

# print(red.clean)

# info about red is it clean or not 
# print(crimson.clean)

# info about crimson is it clean or not
