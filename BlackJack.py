#Hang Nguyen, Stefan Garbee
#Programming assignment 5
#Professor Chung
#Wed, Nov. 14, 2018



from graphics import*
from PlayingCard import*
from Deck import*

class BlackJack:

    def __init__(self, dHand=[], pHand =[]):
        self.dHand = dHand     #type: list, class: PlayingCard
        self.pHand = pHand     #type: list, class: PlayingCard
        self.deck = Deck()       #type: Object, class: Deck
        self.deck.shuffle()

    def initDeal(self, gwin, xposD, yposD, xposP, yposP):
        #deals out initial cards, 2 per player and
        #displays dealer and player hands on graphical win
        #xposD and yposD give initial position for dealer cards
        #xposP and yposP are analogous

        self.gwin = gwin
        self.xposD = xposD
        self.yposD = yposD
        self.xposP = xposP
        self.yposP = yposP
        
        for d in range (2): #create 2 cards and append to lists by for loop
            initDealer = self.deck.dealCard()
            self.dHand.append(initDealer)
          
        for p in range(2):
            initPlayer = self.deck.dealCard()
            self.pHand.append(initPlayer)
            
        
    
    def hit(self, gwin, xPos, yPos):
        # create a new card to the player's hand list and places it at xPos, yPos
        
        self.gwin = gwin
        self.xPos = xPos
        self.yPos = yPos

        player = self.deck.dealCard()
        self.pHand.append(player)
             


    def evaluateHand(self, hand):
        #totals the cards in the hand that is passed in and returns total
        # (ace counts as 11 if doing so allows total to stay under 21)
        #for score of both player and dealer
        
        self.hand = hand #objects
        total = 0
        #do a for loop and loop through to get the rank
        for card in self.hand: 
            if total < 11 and card.getRank() == 1: #if the total is less than 11 and the card is an Ace
                total = total + 11 #the Ace value is 11.
            else:
                total = total + card.value()
            
        return total


    def dealerPlays(self, gwin, xPos, yPos):
        #dealer deals cards to herself, stopping when hitting "soft 17"
        #dealer only

        self.gwin = gwin
        self.xPos = xPos
        self.yPos = yPos
        while self.evaluateHand(self.dHand) < 17: #soft 17 condition
            dealer = self.deck.dealCard()
            self.dHand.append(dealer)
            #self.evaluateHand(self, self.dHand)

            
if __name__ == '__main__':
    main()
