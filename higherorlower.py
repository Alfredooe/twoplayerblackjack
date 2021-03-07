import random
import time
cardranks = ["Clubs", "Diamonds", "Hearts", "Spades"]
cardsuits = {"Ace":11, "One":1, "Two":2, "Three":3, "Four":4, "Five":5, "Six":6, "Seven":7, "Eight":8, "Nine":9, "Ten":10, "Jack":10, "Queen":10, "King":10}
deck = []
playerscore = 0
class Card:
    def __init__(self, r, s):
        self.rank = r
        self.suit = s
        self.value = cardsuits[self.rank]
    def __str__(self):
        return f"{self.rank} of {self.suit}"
def initialize():
    for a in cardsuits:
        for b in cardranks:
            deck.append(Card(a, b))
def pick():
    pickedcard = random.choice(deck)
    #deck.remove(pickedcard)
    return pickedcard

initialize()

while True:
    if (p := input("""\nPlay higher or lower? "Y" to play.""")) == "Y":
        playerscore = 0

        while True:
            card1 = pick()
            card2 = pick()
            if (p := input(f"""You've picked {card1} which has a value of {card1.value}. Choose either "H" or "L" to bet high or low, against the opposing card!.\n""")) == "H":
                print("You picked high!")
                highorlow = 1
            elif p == "L":
                highorlow = 0
            print(f"Your opponent picked {card2} which has a value of {card2.value}.")
            if card1.value == card2.value:
                print("Draw!")
            elif highorlow == 1:
                if card1.value > card2.value:
                    print("You won!")
                    playerscore = playerscore + 1
                else:
                    print("You Lost!")
                    break
            elif highorlow == 0:
                if card1.value < card2.value:
                    print("You won!")
                    playerscore = playerscore + 1
                else:
                    print("You Lost!")
                    break
        print(f"You finished with a score of {playerscore}.")
    else:
        break
