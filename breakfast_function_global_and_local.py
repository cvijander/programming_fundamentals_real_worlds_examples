cheese ='cheddar'

def mix_and_cook():
    print('Mixing the ingredients')
    print('Greasing the frying pan')
    print('Pouring the mixture into a frying pan')
    print('Cooking the first side')
    print('Flipping it!')
    print('Cooking the other side')
    
def make_omelette():
    cheese='swiss'
    #because we have  a local variable, first we are going to use the local 
    mix_and_cook()
    omelette = 'a {} omelette'.format(cheese)
    print(omelette)    

def make_pancake():
    # no local variable, using global
    mix_and_cook()
    pancake='a {} pancake'.format(cheese)
    print(pancake)


def fancy_omelette(*ingredients):
    mix_and_cook()
    omelette = 'a fancy omelette with {} ingredients '.format(len(ingredients))
    print(omelette) 




make_omelette()
make_pancake()    
fancy_omelette('sausage','onion','pepper','spinach','mushroom','tomato','goat cheese')
print(cheese)
#cheddar - global cheese 
