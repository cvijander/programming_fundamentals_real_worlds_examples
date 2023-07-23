#  a 3 dimensional valet service

# 2d list if lists
# index cars by rows , spot

lot_2d =[['Toyota','Audi','Bmw'],  # oth row
         ['Lexus','Jeep'],     # 1st row 
         ['Honda','Kia','Mazda']]  # 2nd row


# 3d list of lists of lists
# index cars by floor, row ,spot

lot_3d = [[['Tesla','Fiat','Bmw'], # oth floor
          ['Honda','Jeep'],
           ['Saab','Kia','Ford']],
           [['Subaru','Nissan'], #1 st floor
            ['Volvo']],
            [['Mazda','Chevy'],  # 2nd floor
             [],
             ['Volkswagen']]] 


print('print a lot 2d whole lot')
print(lot_2d)

print()
print('print a lot 2d [2] third index it means last of list -last items in that collection')
print(lot_2d[2])

print()
print('To acces individual car we need to know the row and the spot')
print('to see car on index 2 row and index spot 1 is ')
print(lot_2d[2][1])

print()
print('the same concept for list of lists of lists ....')

print(lot_3d)

print()
print('print the first floor')
print(lot_3d[0])

print()
print('if we get a second value then we get a flor and a row')
print(lot_3d[0][2])

print()
print('but to get a single car in that spot ')
print(lot_3d[0][2][1])

for car in lot_3d:
    print(car)

for floor in lot_3d:
    for row in floor:
        for car in row:
            print(car)    


