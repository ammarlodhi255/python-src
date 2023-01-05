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


car_1 = Car('blue', 'OP90', '190mph')
car_2 = Car('brown', 'I8', '100mph')
# Let us see the instance variable of this object:
print(car_1.__dict__)

print(Car.num_of_chairs)
# The instance will first check whether it has the 'num_of_chairs; instance variable, then it checks whether it is a class variable
print(car_1.num_of_chairs)
print()

# Following is interesting:

# If we change num_of_chairs using the class:
Car.num_of_chairs = 5

print(Car.num_of_chairs)
print(car_1.num_of_chairs)
print(car_2.num_of_chairs)
print()

# But if I change using one of the instances:
car_1.num_of_chairs = 4

print(Car.num_of_chairs)
print(car_1.num_of_chairs)
print(car_2.num_of_chairs)

# This is because the line 'car_1.num_of_chairs = 4' creates a new instance variable for the object car_1
print(car_1.__dict__)