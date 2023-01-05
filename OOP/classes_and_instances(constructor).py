class Car:

    def __init__(self, color, model, speed):
        self.color = color
        self.model = model
        self.speed = speed

    def show_details(self):
        print(
            f'Color: {self.color}\nSpeed: {self.speed}\nModel: {self.model}\n')


'''
Note we do not have to pass in the argument for 'self' parameter.
The object that we instantiate is automatically passed in for the self parameter.
'''
car_1 = Car('red', 'E12', '12mph')
car_2 = Car('green', 'R14', '100mph')

car_1.show_details()
car_2.show_details()
