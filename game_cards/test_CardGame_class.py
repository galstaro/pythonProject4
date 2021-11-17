from unittest import TestCase
from CardGame_class import *


class TestCardGame(TestCase):
    def setUp(self):
        print("setUp")
        self.cardGame = CardGame("Gal","Moshe",11)

    def tearDown(self):
        print("tearDown")

    # Test case- check constructor function with valid values
    def test__init__valid1(self):
        cardGame1 = CardGame("Gal", "Moshe", 12)
        self.assertEqual(cardGame1.player1.name,"Gal")
        self.assertEqual(cardGame1.player2.name, "Moshe")
        self.assertEqual(cardGame1.cardsforplayer, 12)

    # Test case- check constructor function default cardsforplayer value
    def test__init__valid2(self):
        cardGame1 = CardGame("Gal", "Moshe")
        self.assertEqual(cardGame1.cardsforplayer, 26)

    # Test case- invalid type of name1
    def test__init__invalid1(self):
        with self.assertRaises(Exception) as context:
            self.cardGame = CardGame(1, "Moshe", 12)

    # Test case- invalid type of name2
    def test__init__invalid2(self):
        with self.assertRaises(Exception) as context:
            self.cardGame = CardGame("Gal", 300, 12)

    # Test case- invalid type of cardsforplayer
    def test__init__invalid3(self):
        with self.assertRaises(Exception) as context:
            self.cardGame = CardGame("Gal", "Moshe", "twenty")

    # Test case- check that private function new_game return the same amount of cards for both players.
    def test__new_game(self):
        m = CardGame("g", "k", 20)
        m.deck = DeckOfCards()
        m.player1.player_deck=[]
        m.player2.player_deck=[]
        m._CardGame__new_game()
        self.assertEqual(len(m.player1.player_deck), len(m.player2.player_deck), m.cardsforplayer)

    # Test case- check that private function new_game raise an exception while calling her after initialize a game
    # because the deck becomes empty
    def test__new_gameInvalid(self):
        m = CardGame("g", "k", 20)
        with self.assertRaises(Exception) as context:
            m._CardGame__new_game()

    # Test case- check if error was raised when put the same player names
    def test__init__invalid4(self):
        with self.assertRaises(Exception) as context:
            self.cardGame = CardGame("Gal","Gal", 20)

    # Test case- check that the winner is the player who has the most cards
    def test_get_winner(self):
        self.cardGame.player1.add_card(self.cardGame.player2.player_deck[0])
        self.assertEqual(self.cardGame.get_winner(),self.cardGame.player1)

