import random


class Dice:
    def roll_a_dice(self):
        values = (random.randint(1, 6), random.randint(1, 6))
        return values


dice1 = Dice()

for i in range(10):
    print(dice1.roll_a_dice())
