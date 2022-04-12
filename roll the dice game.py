import random

class Dice:

        def roll(self):

            first = random.randint(1, 6)
            second = random.randint(1, 6)
            return (first, second)


dice= Dice()  #we made the object of the class Dice to call it through its object
print(dice.roll())




