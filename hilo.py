"""The hilo module contains the classes for playing the Hilo game of chance.

Author(s):      [Alec Swainston]
Email(s):       [swa15008@byui.edu]
"""

import random

class Deal:
    """A deal is a distribution of cards. The responsibility of Deal is to keep track of dealt cards and the score."""

    def __init__(self):
        self.cards = []
        self.score = 200
    
    def compare(self, turn):
        right = ((turn == "h" and self.cards[-1] > self.cards[-2]) or (turn == "l" and self.cards[-1] < self.cards[-2]))
        self.score = self.score + 100 if right else self.score - 75

    
    def new_card(self):
        self.cards.append(random.randrange(1, 20))

class HiLo:
    """Controls the Game"""

    def play(self):
        deal = Deal()
        deal.new_card()
        playing = True

        while playing:
            print(f"The card is: ", deal.cards[-1])
            print(f"Your score is: ", deal.score)
            turn = input("Higher or lower? [h/l] ")
            deal.new_card()
            deal.compare(turn)
            print(f"Your score is: ", deal.score)
            playing = deal.score > 0 and input("Keep playing? [y/n] ") in ('y')



if __name__ == "__main__":
    hilo = HiLo()
    hilo.play()
