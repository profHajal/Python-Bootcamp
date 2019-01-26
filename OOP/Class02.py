class Car:
    def __init__(self,name,color):  ## __init__() in py as constructor
      self.name = name
      self.color = color
      
    def start(self):
      return 'Starting with it !'
      
my_car = Car('BMW' , 'Black')
print(my_car)
print(my_car.name)
print(my_car.color)
print(my_car.start())


## Output >>
<__main__.Car object at 0x7f1ae81612e8>
BMW
Black
Starting with it



