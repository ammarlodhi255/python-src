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

    @classmethod
    def set_num_of_chairs(cls, num_of_chairs):
        cls.num_of_chairs = num_of_chairs


car_1 = Car('red', 'UN', '100')
car_2 = Car('red', 'UN1', '100')

print(car_1.num_of_chairs)
print(car_2.num_of_chairs)
print(Car.num_of_chairs)

Car.set_num_of_chairs(5)

print(car_1.num_of_chairs)
print(car_2.num_of_chairs)
print(Car.num_of_chairs)
