import random as rnd
import sys
from die import Die
from pair_of_dice import PairOfDice


class GameController:

    """A controller for a simple Street Craps game"""

    def __init__(self):
        ''' create the PairOfDice object '''
        self.PairOfDice = PairOfDice()

    def start_play(self):
        ''' start the play '''
        print(input("Press Enter to roll the dice...\n"))
        self.play()

    def play(self):
        ''' check if the player loses or wins in the first throw according
to game rules. If not, go to the repeat function '''
        die_sum = self.PairOfDice.current_value()

        if die_sum in (2, 3, 12):
            ''' the player loses if s/he throws 2, 3 or 12 in the first
turn '''
            self.do_busted(die_sum)

        elif die_sum in (7, 11):
            ''' the player wins if s/he throws 7 or 11 in the first
turn '''
            self.do_win(die_sum)

        else:
            self.repeat(die_sum)

    def do_busted(self, x):
        print("You rolled", x, ". You lose!")
        sys.exit()

    def do_win(self, x):
        print("You rolled", x, ". You win!")
        sys.exit()

    def repeat(self, die_sum):
        ''' check until the next throw shows the value equal to the
first point thrown or until 7 shows, which ever is first. If 7
player loses. '''
        point = die_sum
        print("Your point is : ", point)
        new_sum = 0

        while new_sum != point:
            if new_sum == 7:
                print("You rolled 7. You lose.")
                sys.exit()

            input("Press Enter to roll the dice...\n")
            new_sum = self.PairOfDice.current_value()
            print("You rolled :", new_sum)

        print("You win!")
        sys.exit()
