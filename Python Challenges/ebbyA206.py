import random

class Card:
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    ranks = ["","Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
    def __init__(self, suit=0, rank=0):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return (self.ranks[self.rank] + " of " + self.suits[self.suit])
    def cmp(self, other):
        if self.suit > other.suit: return 1
        if self.suit < other.suit: return -1
        if self.rank > other.rank: return 1
        if self.rank < other.rank: return -1
        return 0
    def __eq__(self, other):
        return self.cmp(other) == 0
    def __le__(self, other):
        return self.cmp(other) <= 0
    def __ge__(self, other):
        return self.cmp(other) >= 0
    def __gt__(self, other):
        return self.cmp(other) > 0
    def __lt__(self, other):
        return self.cmp(other) < 0
    def __ne__(self, other):
        return self.cmp(other) != 0

class Deck:                   # Collection of card objects
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                self.cards.append(Card(suit, rank))
    def print_deck(self):
        for card in self.cards:
            print(card)
    def __str__(self):
        s = ""
        for i in range(len(self.cards)):
            s = s + " " * i + str(self.cards[i]) + "\n"
        return s
    def shuffle(self):
        random.shuffle(self.cards)
    def remove(self,card):
        if card in self.cards:
            self.cards.remove(card)
            return True
        else: return False
    def pop(self):
        return self.cards.pop()
    def is_empty(self):
        return self.cards == []

def multadd (x, y, z):      # Polymorphism, works on any data type that can be multiplied or added
    return x * y + z

class Hand(Deck):                     # Inheritance, Hand is a modified Deck object
    def __init__(self, name=""):
       self.cards = []
       self.name = name
    def deal(self, hands, num_cards=999):
        num_hands = len(hands)
        for i in range(num_cards):
            if self.is_empty(): break
            card = self.pop()
            hand = hands[i % num_hands]
            hand.add(card)
    def __str__(self):
        s = "Hand " + self.name
        if self.is_empty():
            s += " is empty\n"
        else:
            s += " contains\n"
        return s + Deck.__str__(self)

