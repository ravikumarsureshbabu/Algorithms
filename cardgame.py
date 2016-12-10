import random

class Card:
    def __init__(self, number, suite):
        self.number = number
        self. suite = suite

    def showcard(self):
        print( self.number, self.suite) 

class Deck:
    numbers = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']
    suites = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
    def __init__(self):
        self.deck = []
        for suite in self.suites:
            for num in self.numbers:
                self.deck.append(Card(num,suite))

    def showdeck(self):
        for card in self.deck:
             card.showcard() 

    def shuffle(self):
        random.shuffle(self.deck)    

d = Deck()
d.showdeck()
d.shuffle()
d.showdeck()

