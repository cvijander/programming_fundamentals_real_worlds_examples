# dictionary full of friends

rolodex = {'Aaron': 5556069,
           'Bill' : 5559824,
           'Dad' : 5559623,
           'David': 5553333,
            'Dillon': 5557412,
           'Jim' : 5896412,
           'Olivia': 5556212,
            'Verne' : 555309,
                                      }


print(rolodex['Verne'])
print(hash('Verne'))

print('Adding Amanda to dictionary')
rolodex['Amanda']= 5559741
print("This is Amanda's number")
print(rolodex['Amanda'])


def caller_id(lookup_number):
    for name, num in rolodex.items():
        if num == lookup_number:
            return name
        

print(caller_id(5556212))