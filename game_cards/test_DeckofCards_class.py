from unittest import TestCase
from DeckofCards_class import *


class TestDeckOfCards(TestCase):

    def setUp(self):
        print("setUp")
        self.card_desk = DeckOfCards()

    def tearDown(self):
        print("tearDown")

    # Test case- can initialize new deck of cards valid
    def test__init__valid(self):
        desk=DeckOfCards()

    # Test case- put input attribute in object initialize invalid
    def test__init__invalid(self):
        with self.assertRaises(Exception) as context:
            desk=DeckOfCards(5)

    # Test case- check that function actual shuffle the desk.
    def test_cards_shuffle(self):
        card_desk2=DeckOfCards()
        card_desk2.cards_shuffle()
        self.assertNotEqual(card_desk2,self.card_desk)

    # Test case- check deal_one function returns Card
    def test_deal_one(self):
        self.assertTrue(type( self.card_desk.deal_one())==Card)

    # Test case- deal one function raise exception when cards deck is empty
    def test_deal_oneInvalid1(self):
        self.card_desk.cards_deck=[]
        with self.assertRaises(Exception) as context:
            self.card_desk.deal_one()

    # Test case- deal_one function raise exception when the list do not contain cards
    def test_deal_oneInvalid2(self):
        self.card_desk.cards_deck=[1,2,3,4]
        with self.assertRaises(Exception) as context:
            self.card_desk.deal_one()