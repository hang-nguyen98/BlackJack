#Hang Nguyen, Stefan Garbee
#Programming assignment 5
#Professor Chung
#Wed, Nov. 14, 2018



from random import *
class PlayingCard:
    def __init__(self,rank,suit):
        """Create a card with a rank and a suit. Rank is an int in the range 1-13
indicating the ranks ace-king and suit is a single character "d", "c", "h", or "s"
indicating the suit (diamonds, clubs, hearts, or spades)."""
        self.rank = rank #int, 1-13
        self.suit = suit #character "d", "c", "h", "s"


        
    def getRank(self):
        """Returns the rank of the card."""
        return self.rank

    def getSuit(self):
        """Returns the suit of the card."""
        return self.suit
    
    def value(self):
        """Returns the Blackjack value of a card. Ace counts as 1, face cards count
as 10."""
        if self.rank > 10: #rank of face cards
            return 10
        else:
            return self.rank

    def __str__(self):
        """Returns a string that names the card. For example, "Ace of Spades"."""
        rankName = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven",
                         "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
        name = rankName[self.rank - 1]

        suitName = {"d":"Diamond","c": "Clubs", "h": "Hearts", "s":"Spades"}

        suit = suitName[self.suit]
        
        #rank = string object
        #suit = string
        return name + " of " + suit


def main():
        c = PlayingCard(1,"s")
        print(c)

if __name__ == '__main__':
    main()

