import random
from traceback import print_tb
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
pCards= []
dCards= []
pScore = 0 
dScore = 0 

def start_game (player_Cards,playes_score):
    # couldn't add point to pScore ! so i just return it from func
    for i in range (2):
        point=random.choice(cards)
        player_Cards.append(point)
        playes_score+=sum(player_Cards)
        return playes_score

def take_a_card(player_Cards,player_score):
    point=random.choice(cards)
    player_Cards.append(point)
    playes_score+=sum(player_Cards)
    return playes_score


pScore+=start_game(pCards,pScore)
dScore+=start_game(dCards,dScore)

print(f'dealer has {dCards} cards with point of {dScore}')
print(f'player has {pCards} cards with point of {pScore}')

if input('do you take an other card or not  y or n') =='y':
    pScore+=take_a_card
else:
    



# for i in range (2):
#     point=random.choice(cards)
#     pCards.append(point)
#     pScore+=point

# for i in range (2):
#     point=random.choice(cards)
#     dCards.append(point)
#     dScore+=point


