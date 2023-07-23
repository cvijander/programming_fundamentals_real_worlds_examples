class jeans:

    def __init__(self,waist,length,color):
         self.waist = waist
         self.length =length
         self.color = color
         self.wearing = False

    def put_on(self):
       print('Putting on {} x {} {} jeans'.format(self.waist,self.length,self.color))
       self.wearing =True

    def take_off(self):
        print('Taking off {} x {} {} jeans' .format(self.waist, self.length,self.color))
        self.wearing = False


my_jeans = jeans(31,32,'blue')
# make an instance of jeans

print(type(my_jeans))
# give an info about my jeans object

print(dir(my_jeans))
# give an info about atributes and method about jeans class

print(my_jeans.put_on())
# print an info about putting my jeans

print(my_jeans.wearing)
#prints if i am wearing a jeans or not

print(my_jeans.take_off())
# prints an onfr about taking off jeans

print(my_jeans.wearing)
#prints info about wearing

