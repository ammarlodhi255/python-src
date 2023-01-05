class Car:

    num_of_chairs = 4  # Class Variable

    def __init__(self, color, model, speed):
        self.color = color
        self.model = model
        self.speed = speed

    def show_details(self):
        print(
            f'Color: {self.color}\nSpeed: {self.speed}\nModel: {self.model}\n')

    def show_num_of_chairs(self):
        print(Car.num_of_chairs)  # Access class variable


car = Car('blue', 'OP90', '190mph')
# Let us see the instance variable of this object:
print(car.__dict__)

print(Car.num_of_chairs)
# The instance will first check whether it has the 'num_of_chairs; instance variable, then it checks whether it is a class variable
print(car.num_of_chairs)
