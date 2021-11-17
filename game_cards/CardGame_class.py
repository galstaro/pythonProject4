from Player_class import *


class CardGame:

    # Initialize a card game with two names for the players, number of cards that each player will get.
    # In addition initialize new full deck, two players- using the input names and the cards for player
    # and call to new_game function which shuffle the deck and give cards to the players
    def __init__(self,name1:str,name2:str,cardsforplayer=26):
        if type(cardsforplayer)==int:
            if cardsforplayer>26 or cardsforplayer<10:
                self.cardsforplayer=26
            else:
                self.cardsforplayer=cardsforplayer
        else:
            raise TypeError("Number of cards for each player need to be integer type.")

        if type(name1)==str and type(name2)==str:
            if name1!=name2:
                self.player1 = Player(name1,self.cardsforplayer)
                self.player2 = Player(name2,self.cardsforplayer)
            else:
                raise TypeError("Names need to be different.")
        else:
            raise TypeError("Name need to be string type.")

        self.deck = DeckOfCards()
        self.__new_game()

    # __new_game is a private function which shuffle the deck and give cards to the players
    def __new_game(self):
        """Private function which shuffle the deck and give cards to the players."""
        if len(self.deck.cards_deck)==52:
            self.deck.cards_shuffle()
            self.player1.set_hand(self.deck)
            self.player2.set_hand(self.deck)
        else:
            raise TypeError("Deck is not full of cards.")

    # get_winner function returns the player which left with more cards
    def get_winner(self):
        """returns the player which left with more cards. if there is a draw the function returns None."""
        if len(self.player1.player_deck)>len(self.player2.player_deck):
            return self.player1
        if len(self.player2.player_deck)>len(self.player1.player_deck):
            return self.player2
        else:
            return None

    def __str__(self):
        return f"{self.player1}\n{self.player2}"




