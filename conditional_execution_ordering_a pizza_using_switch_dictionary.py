print('The is no switch case in python, so use it if -else or dictionary')

today ='Saturday'

if today is 'Sunday':
    print('Order the spinach pizza.')
elif today is 'Monday':
   print('Order the mushroom pizza.')
elif today is 'Tuesday':
    print('Order the pepperoni pizza.')
elif today is 'Wednesday':
    print('Order the veggie pizza.')
elif today is 'Thursday':
    print ('Order the bbq chicken pizza.')
elif today is 'Friday':
    print ('Order the sausage pizza')
elif today is 'Saturday':
    print('Order the Hawaiian pizza')





specials = {'Sunday' : 'spinach',
            'Monday': 'mushroom',
            'Tuesday': 'pepperoni',
            'Wednesday':'veggie',
            'Thursday': 'bbq chicken',
            'Friday' : 'sausage',
            'Saturday':'Hawaiian'
            }


def order(day):
    pizza = specials[day]
    print('Order the {} pizza'.format(pizza))


order('Saturday')