#Hang Nguyen, Stefan Garbee
#Programming assignment 5
#Professor Chung
#Wed, Nov. 14, 2018

from graphics import *
from BlackJack import*
from PlayingCard import*
from Deck import*
import math

#we tried adding bet function but it didn't work so we commented it out

class Button:

    """A button is a labeled rectangle in a window.
    It is enabled or disabled with the activate()
    and deactivate() methods. The clicked(pt) method
    returns True if and only if the button is enabled and pt is inside it."""

    def __init__(self, win, center, width, height, label):
        ## as you read through this, ask yourself:  what are the instance variables here?
        ## it would be useful to add comments describing what some of these variables are for...
        """ Creates a rectangular button, eg:
        qb = Button(myWin, centerPoint, width, height, 'Quit') """ 
        w,h = width/2.0, height/2.0
        x,y = center.getX(), center.getY()
        ## you should comment these variables...
        self.xmax, self.xmin = x+w, x-w 
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1,p2)
        self.rect.setFill('lightgray')
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.activate() ##this line was not there in class, what does it do?

    def getLabel(self):
        """Returns the label string of this button."""
        return self.label.getText()

    def activate(self):
        """Sets this button to 'active'."""
        self.label.setFill('black') #color the text "black"
        self.rect.setWidth(2)       #set the outline to look bolder
        self.active = True          #set the boolean variable that tracks "active"-ness to True

    ##check 3.  complete the deactivate() method
    def deactivate(self):
        """Sets this button to 'inactive'."""
        self.label.setFill('grey')  ##color the text "darkgray"
        self.rect.setWidth(1)       ##set the outline to look finer/thinner
        self.active = False         ##set the boolean variable that tracks "active"-ness to False

    ##check 4.  complete the clicked() method
    def isClicked(self, p):
        """Returns true if button active and Point p is inside"""
        ##your code here
        while not self.active or (not (p.getX() >= self.xmin and p.getX() <= self.xmax and p.getY() >= self.ymin and p.getY() <= self.ymax)):
            return False
            
        return True

     

def announcement(hitbutton,standbutton,betbutton):
    
    #betDisplay.setText("Total money: " + str(totalBet))
    hitbutton.deactivate()
    standbutton.deactivate()
    betbutton.deactivate()

#elif pScore <= 21 and pScore ==dScore:
#announce = "You tie. Play again?"
def main():
    win = GraphWin("Black Jack GUI", 1000, 600)
    win.setBackground("Black")
    aPolygon = Polygon(Point(0,0), Point(700,0), Point(800,183.33), Point(800,366.67), Point(700,550), Point(0,550))
    aPolygon.setFill("green")
    aPolygon.setOutline("burlywood4")
    aPolygon.draw(win)
    title = Text(Point(875, 75), "BLACK JACK")
    title.setFill("white")
    title.setSize(30)
    title.draw(win)
    Names = Text(Point(900, 125), "Made by: \n Stefan Garbee & Hang Nguyen")
    Names.setFill("white")
    Names.setSize(12)
    Names.draw(win)

    #text object for dealer and player's total points:
    pText = Text(Point(110, 350), "Player's total:")
    pText.setFill("white")
    pText.setSize(15)
    pText.draw(win)

    dText = Text(Point(110, 50), "Dealer's total:")
    dText.setFill("white")
    dText.setSize(15) #the text is not drawn until player wins/loses
    dText.draw(win)

    #Display point for player and dealer
    pDisplay = Text(Point(170,350), "")
    pDisplay.setFill("white")
    pDisplay.setSize(15)
    pDisplay.draw(win)

    dDisplay = Text(Point(170,50), "")
    dDisplay.setFill("white")
    dDisplay.setSize(15)
    dDisplay.draw(win)
                    
    #text object for win/lose announcement:
    announce = Text (Point(900,300), "")
    announce.setFill("white")
    announce.setSize(20)
    announce.draw(win)

    #Input object for betting
    inputBet = Entry(Point(925,500), 5)
    inputBet.setFill("white")
    inputBet.draw(win)

    #button objects
    hitbutton = Button(win, Point(900, 400), 120,30, "Hit")
    standbutton = Button(win, Point(900, 450), 120, 30, "Stand")
    quitbutton = Button(win, Point(980,590), 40,20, "Quit")
    betbutton = Button(win, Point(865,500), 50,30, "Bet")
    quitbutton.deactivate()


    #call the class, initialize the game
    bGame = BlackJack()    
    #initial cards for dealer and player:    
    bGame.initDeal(win, 125, 50, 125, 475)

    #cards display
    for i in range(2):
        imP = Image(Point(100+85*i,450), "playingcards/" +
                    str(bGame.pHand[i].getSuit()) +
                    str(bGame.pHand[i].getRank()) + ".gif")
        imP.draw(win)
        imD = Image(Point(100+85*i,150), "playingcards/b1fv.gif")  #hide dealer's card
        imD.draw(win)
        print(bGame.dHand[i].getSuit(), bGame.dHand[i].value())
        

    
    imDshow = Image (Point(185,150), "playingcards/" +
                     str(bGame.dHand[i].getSuit()) +
                     str(bGame.dHand[i].getRank()) + ".gif") #show the 1st card of the dealer
    imDshow.draw(win)
    

    dTotal = bGame.evaluateHand(bGame.dHand)
    pTotal = bGame.evaluateHand(bGame.pHand) #total of the player hand for initial cards    
    pDisplay.setText(pTotal) #display player's initial total
    pt = win.getMouse()

    totalBet = 0
    numBet = 0
    i, j = 2, 0 #i and j are for the iteration in the while loop
    while not quitbutton.isClicked(pt):
        betDisplay = Text(Point (880,550), "Total money: " + "")
        if betbutton.isClicked(pt):
            numBet = inputBet.getText() #amount of bet
            currentBet = Text(Point(880,530), "Current bet: " + numBet)
            currentBet.setFill("white")
            currentBet.draw(win)

            betDisplay = Text(Point (880,550), "Total money: " + str(totalBet))
            betDisplay.setFill("white")
            betDisplay.draw(win)

        if hitbutton.isClicked(pt): #if the user click the hit button
            quitbutton.activate()
            bGame.hit(win,125+85*i,450) #call hit from BlackJack
            #i is to find a new place to draw the card
            
            imP = Image(Point(125+85*i,450), "playingcards/" +
                    str(bGame.pHand[i].getSuit()) +
                    str(bGame.pHand[i].getRank()) + ".gif")
            imP.draw(win)
            i = i + 1 #iterate i by 1

            #display player's total
            pTotal = bGame.evaluateHand(bGame.pHand) 
            pDisplay.setText(pTotal)

            if pTotal > 21:  #check if player busts
                dTotal = bGame.evaluateHand(bGame.dHand)
                dDisplay.setText(dTotal)
                imDshow = Image(Point(100, 150), "playingcards/" +
                            str(bGame.dHand[0].getSuit()) +
                            str(bGame.dHand[0].getRank()) +".gif")
                imDshow.draw(win)
                announce.setText("You bust.\nYou lose.")
                #totalBet = totalBet - int(numBet)
                announcement(hitbutton, standbutton, betbutton)

            
        elif standbutton.isClicked(pt): #if the user click the stand button
            quitbutton.activate()
            
            hitbutton.deactivate()
            standbutton.deactivate()
            bGame.dealerPlays(win,125+85*j, 150)
            imDshow = Image(Point(100, 150), "playingcards/" +
                            str(bGame.dHand[0].getSuit()) +
                            str(bGame.dHand[0].getRank()) +".gif")
            #show the 1st card of the dealer, which has position 0 in the dHand list.
            imDshow.draw(win)

            for k in range(2, len(bGame.dHand)):
                #k is to find a new place to draw the card
                imD = Image(Point(125+85*k, 150), "playingcards/" +
                    str(bGame.dHand[k].getSuit()) +
                    str(bGame.dHand[k].getRank()) + ".gif")
            
                imD.draw(win)
            
            #evaluate player and dealer's total
            pTotal = bGame.evaluateHand(bGame.pHand) 
            dTotal = bGame.evaluateHand(bGame.dHand)
            pDisplay.setText(pTotal)
            dDisplay.setText(dTotal)
            
            if dTotal > 21: #check if dealer busts
                announce.setText ("Dealer busts. \nYou win.")
                #totalBet = totalBet + int(numBet)
                announcement(hitbutton, standbutton, betbutton)


            else: #check dealer and player's total
                if pTotal > dTotal:
                    announce.setText ("You win.")
                    #totalBet = totalBet + int(numBet)
                    announcement(hitbutton, standbutton, betbutton)
                                      
                elif pTotal < dTotal:
                    announce.setText ("You lose.")
                    #totalBet = totalBet - int(numBet)
                    announcement(hitbutton, standbutton, betbutton)
                else:
                    announce.setText ("You tie.")
                    announcement(hitbutton, standbutton, betbutton)

        pt = win.getMouse()
        
                
    win.close() 



if __name__ == "__main__": 
    main()
    
