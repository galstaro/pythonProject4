from unittest import TestCase, mock
from unittest.mock import patch
from Player_class import *
from DeckofCards_class import *


class TestPlayer(TestCase):

    def setUp(self):
        print("setUp")
        self.player = Player("Gal",26)

    def tearDown(self):
        print("tearDown")

    # Test case- check init function with valid values
    def test__init__valid1(self):
        player = Player("Gal",15)
        self.assertEqual(15, player.cards_for_player)

    # Test case- check init function with valid values
    def test__init__valid2(self):
        player = Player("Gal", 10)
        self.assertEqual("Gal", player.name)
        self.assertEqual(10, player.cards_for_player)

    # Test case- check init function with valid values
    def test__init__valid3(self):
        player = Player("Gal")
        self.assertEqual(26,player.cards_for_player)

    # Test case- check init function with valid values
    def test__init__valid4(self):
        player = Player("moshe",27)
        self.assertEqual(26, player.cards_for_player)

    # Test case- check init function with valid values
    def test__init__valid5(self):
        player = Player("Moshe",9)
        self.assertEqual(26, player.cards_for_player)

    # Test case- check init function with invalid input values
    def test__init__invalid1(self):
        with self.assertRaises(Exception) as context:
            player = Player("gal","shalom")

    # Test case- check init function with invalid input values
    def test__init__invalid2(self):
        with self.assertRaises(Exception) as context:
            player = Player(15, 15)

    # Test case- check the function works and put only cards in deck
    def test_set_hand_inputIsDeskOfCardsValid(self):
        self.player.set_hand(DeckOfCards())
        self.assertNotEqual(self.player.player_deck,[])
        for i in self.player.player_deck:
            if type(i) is not Card:
                self.fail()

    # Test case- check that input object is desk of Cards invalid input
    def test_set_hand_inputIsDeskOfCardsInvalid(self):
        self.player.set_hand(DeckOfCards())
        with self.assertRaises(Exception) as context:
            self.player.set_hand([1,4,6])

    # Test case- check that all cards are different in the deck
    def test_set_hand_allCards_differentValid(self):
        self.player.set_hand(DeckOfCards())
        self.assertTrue(len(self.player.player_deck)==len(set(self.player.player_deck)))

    # Test case- check that all cards are different in the deck invalid
    def test_set_hand_allCards_differentInValid(self):
        with patch('DeckofCards_class.DeckOfCards.deal_one') as mock_deal_one:
            mock_deal_one.return_value = Card(5,"Heart")
            with self.assertRaises(Exception) as context:
                self.player.set_hand(DeckOfCards())

    # Test case- check that all objects in the player desk will be Cards type
    def test_set_hand_CardsType(self):
        with patch('DeckofCards_class.DeckOfCards.deal_one') as mock_deal_one:
            mock_deal_one.return_value=5
            with self.assertRaises(Exception) as context:
                self.player.set_hand(DeckOfCards())

    # Test case- check that the function show card from the desk
    def test_get_card(self):
        self.player.set_hand(DeckOfCards())
        self.assertTrue(type(self.player.get_card())==Card)

    # Test case- check the function added cards to player desk with valid values
    def test_add_cardValid(self):
        card1=Card(3, "Diamond")
        card2=Card(4, "Spade")
        self.player.add_card(card1)
        self.player.add_card(card2)
        self.assertListEqual(self.player.player_deck,[card1,card2])

    # Test case- check the function did not add invalid card to player desk
    def test_add_cardInValid(self):
       with self.assertRaises(Exception) as context:
            self.player.add_card(Card(3, "moshe"))

    # Test case- check the function did not add non Card type to player desk
    def test_add_cardInValid2(self):
        with self.assertRaises(Exception) as context:
            self.player.add_card(4)