#Hang Nguyen, Stefan Garbee
#Programming assignment 5
#Professor Chung
#Wed, Nov. 14, 2018

from PlayingCard import*
class Deck:
    """A class  that represents a deck of cards."""
    
    #Creates a deck
    def __init__(self):
        cardlist = []
        for suit in ["d","c","h","s"]:
            for r in range(1,14):
                card = PlayingCard(r, suit)
                cardlist.append(card)
        self.cardlist = cardlist
        
    #Shuffles the deck
    def shuffle(self):
        for i in range(100):
            card1 = randrange(0,52)
            card2 = randrange(0,52)
            self.cardlist[card1], self.cardlist[card2] = self.cardlist[card2], self.cardlist[card1]
        return self.cardlist

    #Pops out the first card in the shuffled deck
    def dealCard(self):
        return self.cardlist.pop(0)

    #Returns the amount of cards left after dealing.
    def cardsLeft(self):
        return len(self.cardlist)




def main():
    deck = Deck()
    deck.shuffle()
    cardsList = []
  
    for i in range(52):
        cards = deck.dealCard()
        cardsList.append(cards)
        print(cards)

if __name__ == '__main__':
    main()

