def mix_and_cook():
    print('Mixing the ingredients')
    print('Greasing the frying pan')
    print('Pouring the mixture into a frying pan')
    print('Cooking the first side')
    print('Flipping it!')
    print('Cooking the other side')
    
def make_omelette(ingredient):
    mix_and_cook()
    omelette = 'a {} omelette'.format(ingredient)
    print(omelette)    

def make_pancake():
    mix_and_cook()
    pancake='a delicious pancake'
    print(pancake)

make_omelette('bacon')
make_pancake()    