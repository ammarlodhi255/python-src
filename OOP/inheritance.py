class Car:
    base_price = 100000

    def __init__(self, color, model, speed):
        self.color = color
        self.model = model
        self.speed = speed

    def display_details(self):
        print(f'Color: {self.color}\nSpeed: {self.speed}\nModel: {self.model}')

    @classmethod
    def get_base_price(cls):
        return cls.base_price  # Access class variable

# This subclass inherits all the methods and attributes of the base class 'Car'
class Volkswagen(Car):
    # This class variable has a value for 'base_price_ different than the subclass
    base_price = 800000

    def __init__(self, color, model, speed, inventor):
        super().__init__(color, model, speed)
        self.inventor = inventor

    # Overriding a method
    def display_details(self):
        print(
            f'Color: {self.color}\nSpeed: {self.speed}\nModel: {self.model}\nInventor: {self.inventor}')


'''
See all the methods and attributes inside of the subclass using help(cls_name)
The method resolution order shown in the output, is the order of execution when python looks for any attributes or methods.
'''

# help(Volkswagen)

# Create a Car instance and a Volkswagen instance:
car_1 = Car('red', 'Base', '100')
volks_1 = Volkswagen('blue', 'volkswagen', '900', 'Josef Ganz')

print(car_1.get_base_price())
print(volks_1.get_base_price())

volks_1.display_details()

# Check to see if volks_1 is an instance of Car
print(isinstance(volks_1, Car))

# Check to see if one class is a subclass of another class
print(issubclass(Volkswagen, Car))
