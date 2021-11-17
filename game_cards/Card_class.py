class Card:
    # init function getting value of card and his suit.For Example:Card(3,"Diamond")
    def __init__(self,value:int,suit:str):
        # self.__values - dictionary the card numbers which have unique names.For Example Card number 1 is Ace
        # I used this dictionary in the __repr__ function
        self.__values = {1: "Ace", 11: "Jack", 12: "Queen", 13: "King"}
        if type(value)==int and 1<=value<=13:
            self.value=value
        else:
            raise TypeError("value attribute has to be integer and between 1 to 13.")
        # self.__suits - dictionary with the value of any suit key
        # I used it to compare 2 cards who have the same values
        # Check suite input attribute is one of the keys in this dictionary.
        self.__suits = {"Diamond": 1, "Spade": 2, "Heart": 3, "Club": 4}
        if type(suit) == str:
            suit=suit.lower()
            suit=suit.capitalize()
            if suit in self.__suits:
                self.suit=suit
            else:
                raise TypeError("Suit need to be one of these:Diamond,Spade,Heart,Club.")
        else:
            raise TypeError("suit attribute has to be string.")

    def __repr__(self):
        # Check if card value has unique name if he has one the func will return the unique name with the suit.
        if self.value in self.__values:
            return f"{self.__values[self.value]} of {self.suit}"
        return f"{self.value} of {self.suit}"

    # Check which card is bigger by its value and his suit value in case their value cards are equal.
    def __gt__(self,other):
        if type(other)==Card:
            if (self.value > other.value and other.value != 1) or (self.value==1 and other.value!=1):
                return True
            if self.value==other.value and self.__suits[self.suit]>other.__suits[other.suit]:
                return True
            return False
        else:
            raise TypeError("input attribute type has to be Card.")












