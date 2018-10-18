import random as r
from die import Die


class PairOfDice:
    """Calculating sum of a double roll of die"""
    def __init__(self):
        ''' inititialise the two Die objects '''
        self.d1 = Die()
        self.d2 = Die()

    def roll_dice(self):
        ''' to roll the two Die objects, and then use the final value
for summing up for the purpose of using in the game'''
        y = list()
        d1_val = self.d1.roll()
        d2_val = self.d2.roll()
        y.append(d1_val)
        y.append(d2_val)
        return y

    def current_value(self):
        ''' use the roll_dice function and add the individual items in
the returned list for the final value of die throw '''
        y = self.roll_dice()
        current_sum = y[0] + y[1]
        return current_sum
