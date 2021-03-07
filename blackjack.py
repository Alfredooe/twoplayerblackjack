import random
cardranks = ["Clubs", "Diamonds", "Hearts", "Spades"]
cardsuits = {"Ace":11, "One":1, "Two":2, "Three":3, "Four":4, "Five":5, "Six":6, "Seven":7, "Eight":8, "Nine":9, "Ten":10, "Jack":10, "Queen":10, "King":10}

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.stuck = False
        self.score = 0

class Deck:
    def __init__(self):
        self.cards = []
        for a in cardsuits:
            for b in cardranks:
                self.cards.append(Card(a, b))

                
    def deal(self, player):
        card = random.choice(self.cards)
        print(f"{player.name}, you've been dealt card {card} with a value of {card.value}")
        player.hand.append(card)
        if card.value == 11:
            aceswap = inputhandler("norm", player)
            #aceswap = input(f"{player.name}, you've been dealt an ace! T for a value of 11 or S for 1 : ")
            if aceswap == "T":
                player.score = player.score + 11
            elif aceswap == "S":
                player.score = player.score + 1
        else:
            player.score = player.score + card.value
        self.cards.remove(card)
        return card

class Card:
    def __init__(self, r, s):
        self.rank = r
        self.suit = s
        self.value = cardsuits[self.rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"

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
    if player1.stuck == True & player2.stuck == True:
        if player1.score > player2.score:
            print(f"Congratulations {player1.name}, you won!")
            gameover()
        elif player1.score < player2.score:
            print(f"Congratulations {player2.name}, you won!")
            gameover()
        elif player1.score == player2.score:
            print(f"Congratulations i guess, you managed to come a draw.")
            gameover()

    elif player.stuck == True:
        return
    elif player.stuck == False:
        move = inputhandler("norm", player)
        #move = input(f"{player.name}, T for twist or S for stick. : ")
        if move == "S":
            player.stuck = True
        elif move == "T":
            card = deck.deal(player)
        if player.score > 21:
            print(f"{player.name}. You went over 21, with a score of {player.score}, You lost!")
            gameover()
        else:
            print(f"{player.name}, you've now got a score of {player.score}.\n")

def gameover():
    quit()

player1 = Player(input("Player 1, enter your name. : "))
player2 = Player(input("Player 2, enter your name. : "))
deck = Deck()

print(f"I will now deal your initial cards, {player1.name} and {player2.name}.\n")
deck.deal(player1)
deck.deal(player2)
print(f"Good luck, players.\n")

while True:
    turn(player1)
    turn(player2)
