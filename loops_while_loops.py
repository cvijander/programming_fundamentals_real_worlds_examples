import  random

dirty = True # state of the pan
scrob_count = 0 # number of scrubs

while (dirty):

    scrob_count +=1
    print('Scrub the pan: {} '.format(scrob_count))

    print('Rinse and check if the pan is clean.')

    if not random.randint(0,9):
        print('All clean!')
        dirty =False
    else:
        print('Still dirty...') 


