class Card(object):
    #A playing card
    RANKS = {"Ace", "2", "3", "4", "5",
             "6", "7", "8", "9",
             "10", "Jack", "Queen", "King"}
    SUITS = {"Club", "Diamond", "Hearts", "Spades"}
    def __init__(self, rank, suits, isFaceUpd = True):
        self.rank = rank
        self.suit = suits
        self.isFaceUp = isFaceUpd

    def __str__(self):
        if self.isFaceUp :
            display_card = self.rank + ' of '+ self.suit
        else:
            display_card = "Card face down"
        return display_card
    def flip(self):
        self.isFaceUp = not self.isFaceUp

class Hand(object):
    "A hand of playing cards"
    def __init__(self):
        self.cards = []
    def __str__(self):
        if self.cards:
            playingCards = ""
            for card in self.cards:
                playingCards += str(card) + " \t"
        else:
            playingCards = "There is no cards left to be played"
        return playingCards
    def clear(self):
        ## Im clearing all cards from hand
        self.cards = []
    def adding(self, card):
        self.cards.append(card)

    def giving(self, card, otherHand):
        # A distributing method
        self.cards.remove(card)
        otherHand.add(card)
class Deck(Hand):
    """ A deck of playing cards. """

    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank, suit))

    def shuffle(self):
        """A method tha shuffle the deck of cards"""
        import random
        random.shuffle(self.cards)

    def deal(self, hands, card_per_hand=1):
        """A method that deal the cards to the hand. It accepts the list of hand and cards per hand """
        for rounds in range(card_per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print("Can't continue deal. Out of cards!")







