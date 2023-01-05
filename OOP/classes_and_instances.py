class Car:
    pass


car_1 = Car()
car_2 = Car()

car_1.color = 'red'
car_2.color = 'green'

car_1.model = 'E12'
car_1.speed = '12mph'

car_2.model = 'R14'
car_2.speed = '100mph'


print(f'Car 1: {car_1.color}, {car_1.model}, {car_1.speed}')
print(f'Car 2: {car_2.color}, {car_2.model}, {car_2.speed}')