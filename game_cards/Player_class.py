from DeckofCards_class import *
import random


class Player:

    # Initialize a player with his name, number of cards that he will get from deck and empty deck of him
    def __init__(self,name:str,cards_for_player=26):
        if type(name)==str:
            self.name=name
        else:
            raise TypeError("Player name need to be a string.")
        if type(cards_for_player)==int:
            if cards_for_player>26 or cards_for_player<10:
                self.cards_for_player=26
            else:
                self.cards_for_player=cards_for_player
        else:
            raise TypeError("The number of cards for player need to be an integer.")

        self.player_deck=[]

    # Get a deck of cards and give the player number of cards according to the number they defined.
    def set_hand(self,deck_of_cards:DeckOfCards):
        """Get a deck of cards and give the player number of cards according to the number which defined."""
        if type(deck_of_cards)==DeckOfCards:
            for i in range(self.cards_for_player):
                card=deck_of_cards.deal_one()
                if type(card) is Card:
                    if self.player_deck.count(card)==0:
                        self.player_deck.append(card)
                    else:
                        raise TypeError("This card is already in the deck.")
                else:
                    raise TypeError("The value which returned from deal_one function is not Card.")
        else:
            raise TypeError("Input attribute type need to be DeckOfCards.")

    # Return a random card from player deck.
    def get_card(self):
        """Pull and return a random card from player deck."""
        rand_card = random.choice(self.player_deck)
        if type(rand_card) == Card:
            return self.player_deck.pop(self.player_deck.index(rand_card))
        else:
            raise TypeError("Card type must be Card.")

    # Add card to player deck.
    def add_card(self,card:Card):
        """Add card to player deck."""
        if type(card) == Card:
            self.player_deck.append(card)
        else:
            raise TypeError("Input attribute type need to be Card.")

    def __str__(self):
        return f"Player name: {self.name}\nNumber of cards: {self.cards_for_player}\nCards Deck: {self.player_deck}"
