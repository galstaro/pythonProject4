import random
from Card_class import *


class DeckOfCards:

    # Initializes a complete deck of 52 cards
    def __init__(self):
        self.cards_deck = []
        count = 1
        suit_num = 1
        suits = {1: "Diamond", 2: "Spade", 3: "Heart", 4: "Club"}
        for i in range(52):
            self.cards_deck.append(Card(count, suits[suit_num]))
            count += 1
            if count == 14:
                count = 1
                suit_num += 1

    # Shuffle the deck
    def cards_shuffle(self):
        """Shuffle the deck."""
        random.shuffle(self.cards_deck)

    # Return one random card from deck
    def deal_one(self):
        """Pulls and return one random card from deck."""
        if len(self.cards_deck) > 0:
            card_deal = random.choice(self.cards_deck)
            if type(card_deal) == Card:
                return self.cards_deck.pop(self.cards_deck.index(card_deal))
            else:
                raise TypeError("Cards deck need to be a List which contains only Cards.")
        else:
            raise TypeError("Cards deck is empty.")

    def __str__(self):
        return f"{self.cards_deck}"

