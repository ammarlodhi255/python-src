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


