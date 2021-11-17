from unittest import TestCase
from Card_class import *


class TestCard(TestCase):
    def setUp(self):
        print("setUp")
        self.card1 = Card(8, "Diamond")

    def tearDown(self):
        print("tearDown")

    # Test case- check valid value
    def test__init__valid1(self):
        card = Card(8,"Diamond")
        self.assertEqual(8,card.value)
        self.assertEqual("Diamond",card.suit)

    # Test case- check valid edge value
    def test__init__valid2(self):
        card = Card(1, "Heart")
        self.assertEqual(1, card.value)
        self.assertEqual("Heart", card.suit)

    # Test case- check valid edge value
    def test__init__valid3(self):
        card = Card(13, "Club")
        self.assertEqual(13, card.value)
        self.assertEqual("Club", card.suit)

    # Test case- check invalid edge value
    def test__init__invalid1(self):
        with self.assertRaises(Exception) as context:
            card = Card(0,"Diamond")

    # Test case- check invalid edge value
    def test__init__invalid2(self):
        with self.assertRaises(Exception) as context:
            card = Card(14, "Heart")

    # Test case- check invalid suit input
    def test__init__invalid3(self):
        with self.assertRaises(Exception) as context:
            card = Card(13, "triangular")

    # Test case- check invalid type of inputs
    def test__init__invalid4(self):
        with self.assertRaises(Exception) as context:
            card = Card("triangular",8)

    # Test case- check valid values
    def test__gt__valid(self):
        card2 = Card(4, "Heart")
        self.assertTrue(self.card1>card2)
        card3=Card(1,"Spade")
        self.assertTrue(card3>card2)
        card4=Card(1,"Club")
        self.assertTrue(card4>card3)
        self.assertFalse(card2>card3)

    # Test case- check invalid values
    def test__gt__invalid(self):
        card2 = 8
        with self.assertRaises(Exception) as context:
            self.assertTrue(self.card1 > card2)

    # Test case- check invalid values
    def test__gt__invalid2(self):
        card2 = "gal"
        with self.assertRaises(Exception) as context:
            self.assertTrue(self.card1 > card2)