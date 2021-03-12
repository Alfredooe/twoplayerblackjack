#'random' library import
import random
#rank list & suit dictionary
cardranks = ["Clubs", "Diamonds", "Hearts", "Spades"]
cardsuits = {"Ace":11, "One":1, "Two":2, "Three":3, "Four":4, "Five":5, "Six":6, "Seven":7, "Eight":8, "Nine":9, "Ten":10, "Jack":10, "Queen":10, "King":10}

#player class w/ public attributes
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.stuck = False
        self.score = 0

#deck class generates every possible card within the deck, appending each possiblity to a list
class Deck:
    def __init__(self):
        self.cards = []
        #Iterating through lists and appending created objects to deck
        for a in cardsuits:
            for b in cardranks:
                self.cards.append(Card(a, b))

    #dealing method assigns a random card at the beginning to each player              
    def deal(self, player):
        card = random.choice(self.cards)
        #randomly assigned card output
        print(f"{player.name}, you've been dealt card {card} with a value of {card.value}")
        player.hand.append(card)
        #Ace handling
        #if card.value == 11:
        #   aceswap = inputhandler("norm", player)
        #   if aceswap == "T":
        #       player.score = player.score + 11
        #   elif aceswap == "S":
        #       player.score = player.score + 1
        if card.value == 11:
            if player.score <= 10:
                player.score = player.score + 11
            elif player.score > 10:
                player.score = player.score + 1
        else:
            player.score = player.score + card.value
        self.cards.remove(card)
        return card

#card class
class Card:
    def __init__(self, r, s):
        self.rank = r
        self.suit = s
        self.value = cardsuits[self.rank]

    #return string representation, nice way of doing this.
    def __str__(self):
        return f"{self.rank} of {self.suit}"

#Input verification and looping to ensure correct input
def inputhandler(task, player):
    if task == "norm":
        print(f"{player.name}, T for twist or S for stick. : ")
    elif task == "ace":
        print(f"{player.name}, you've been dealt an ace! T for a value of 11 or S for 1 : ")
    while True:
        data = input().upper()
        if data not in ("T", "S"):
            print("Invalid input. Please re-enter.")
            continue
        else:
            return data
            
def turn(player):
    #Checking both stuck
    if player1.stuck == True & player2.stuck == True:
        #player 1 winning scenario
        if player1.score > player2.score:
            print(f"Congratulations {player1.name}, you won!")
            gameover()
        #player 2 winning scenario
        elif player1.score < player2.score:
            print(f"Congratulations {player2.name}, you won!")
            gameover()
        #draw scenario
        elif player1.score == player2.score:
            print(f"Congratulations i guess, you managed to come a draw.")
            gameover()

    elif player.stuck == True:
        return
    elif player.stuck == False:
        move = inputhandler("norm", player)
        #player choosing to stick
        if move == "S":
            player.stuck = True
        #player choosing to twist
        elif move == "T":
            card = deck.deal(player)
        #score above 21
        if player.score > 21:
            print(f"{player.name}. You went over 21, with a score of {player.score}, You lost!")
            gameover()
        else:
            #output for updated score
            print(f"{player.name}, you've now got a score of {player.score}.\n")
#lol
def gameover():
    quit()

#player name input request
player1 = Player(input("Player 1, enter your name. : "))
player2 = Player(input("Player 2, enter your name. : "))
#deck object is formed
deck = Deck()

print(f"I will now deal your initial cards, {player1.name} and {player2.name}.\n")
#first 2 random cards are generated for both players
deck.deal(player1)
deck.deal(player2)
print(f"Good luck, players.\n")

while True:
    turn(player1)
    turn(player2)

#!!!!!!!!!Adjust the code so that player has a hand object instead of player having a list for cards.!!!!!!!!!

#Settings n getters
