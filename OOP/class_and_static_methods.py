class Car:

    num_of_chairs = 4  # Class Variable

    def __init__(self, color, model, speed):
        self.color = color
        self.model = model
        self.speed = speed

    def show_details(self):
        print(f'Color: {self.color}\nSpeed: {self.speed}\nModel: {self.model}')

    def show_num_of_chairs(self):
        print(Car.num_of_chairs)  # Access class variable

    @classmethod  # This decorator alters the functionality of our regular method to now accept the class instead of an instance of the class
    def set_num_of_chairs(cls, num_of_chairs):
        cls.num_of_chairs = num_of_chairs

    # Class method as an alternative constructor
    @classmethod
    def from_string(cls, car_str):
        color, model, speed = car_str.split('-')
        return cls(color, model, speed)


car_1 = Car('red', 'UN', '100')
car_2 = Car('red', 'UN1', '100')

print(car_1.num_of_chairs)
print(car_2.num_of_chairs)
print(Car.num_of_chairs)

Car.set_num_of_chairs(5)

print(car_1.num_of_chairs)
print(car_2.num_of_chairs)
print(Car.num_of_chairs)

# Class method as an alternative constructor
car_3 = Car.from_string('Blue-7HY-100mph')
car_3.show_details()
