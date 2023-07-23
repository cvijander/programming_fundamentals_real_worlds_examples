# A garage full of classy vehicles

class Vehicle: #Base Vehicle class 

    def __init__(self,color, manuf):
        self.color = color
        self.manuf = manuf
        self.gas = 4 # a full tank of gas
        

    def drive(self):
        if self.gas > 0:
            self.gas -=1
            print('The {} {} goew VROOOM!'. format(self.color, self.manuf))

        else :
            print('The {} {} sputters out of gas.'.format(self.color, self.manuf))

class Car(Vehicle): #inherits from Vehicle class

    #turn the radio on
    def radio(self):
        print("Rockin' Tunes!")

    # open the window
    def window(self):
        print('Opening the window.. fresh air') 

class Motorcycle(Vehicle): # Inherits from Vehicle class
     
      # put on motorcycle helmet

      def helmet(self):
          print('Nice and safe!')


class eCar(Car):
      
      def drive(self):
          print('The {} {} goes ssshhhh!'.format(self.color,self.manuf))

          

my_car = Car('red','Mercedes' )
my_mc = Motorcycle('silver','Harley')
my_eCar = eCar('white','Nissan')


print(my_car.drive())
# prints my car drive method

print(my_mc.drive())
# prints my harley  

print(my_mc.drive())

print(my_mc.drive())

print(my_mc.drive())

print(my_mc.drive())
          
print(my_car.radio())

print(my_car.window())

print(my_mc.helmet())

print(my_eCar.window())
print(my_eCar.radio())

print(my_eCar.drive())

print(my_eCar.gas)