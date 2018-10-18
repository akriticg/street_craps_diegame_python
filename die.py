import random as rnd


class Die:
    """A single die"""
    def __init__(self):
        self.current_value = rnd.randint(1, 6)

    def roll(self):
        ''' when the dice is rolled, it gets a random value between
1 and 6 '''
        self.current_value = rnd.randint(1, 6)
        return self.current_value
