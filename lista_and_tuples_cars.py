
row= ['Ford', 'Audi', 'Bmw', 'Lexus']
# list of cars in list - like an array in C# 

print('now we are printing the row of cars')
print(row)

print()
print('Here is a id of this list')
print(id(row))

print()
print('Here is again id of this list ')
print(id(row))
print('it is the same list - mutable ')

print()
print('Now we are inserting a new  car')
# now insert a new car
row.append('Mercedes')

print()
print('look at list now')
print(row)
print(id(row))
print('it has one more item on the end ')

# now print a new list 
print()
print('print the location of the item on position 5 but it is index 4')
print(row[4])

print()
print('how to replace car bmw with the jeep ')
print()
row[2]='Jeep'
print()
print(row)

print('the cars have been replaced')
print()

print('Add more cars to the end of list')
row.append('Honda')
print()
print(row)
print()

print('still show on index 4')
print(row[4])
print()

print('now we are adding a car on front of the list, and everything is changed') 
row.insert(0,'Kia')
print()
print(row)

print('show me now index 4')
print(row[4])
print()
print('it is not mercedes ')
print()
print('show me where is mercedes ')
print(row.index('Mercedes'))
print()

print('leaving list with pop function ')
#row.pop(5)
print(row.pop(5))
print(row)
print()

row.remove('Lexus')
print(row)

