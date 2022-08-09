import os
import random
## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
clear = lambda: os.system('clear')
def game () :
    pCards= []
    dCards= []
    pScore = 0 
    dScore = 0 
    for i in range (2):
        point=random.choice(cards)
        pCards.append(point)
        pScore+=point
    for i in range (2):
        point=random.choice(cards)
        dCards.append(point)
        dScore+=point
    def score_board():
        print(f'dealer has {dCards} cards with point of {dScore}')
        print(f'player has {pCards} cards with point of {pScore}')


    score_board()

    while(True):
        if pScore == 21 :
            print('player won ! ')
            score_board()
            game ()
            break
        elif dScore == 21 :
            print('dealer won ! ')
            score_board()
            game ()
            break
        elif pScore >21 :
            print('player lose ! ')
            score_board()
            game ()
            break
        elif dScore >21 :
            print('dealer lose ! ')
            score_board()
            game ()
            break

        elif dScore == pScore:
            print('Draw ! ')
            score_board()
            game ()
            break
        else:
            ask_user= input('do you take an other card or not  y or n')
            if ask_user =='y':
                point=random.choice(cards)
                pCards.append(point)
                pScore+=point
                score_board()
            elif ask_user =='n':
                point=random.choice(cards)
                dCards.append(point)
                dScore+=point
                score_board()
game()
