import os
clear = lambda: os.system('clear')
bider=[]
bid_going_on= True
while(bid_going_on):
    name=input('What is your name? :')
    bid=int(input('What is your bid? : $'))
    bider.append({
        'name':name,
        'bid':bid,
        })        
    state=input('are there any other Bidders? \'yes\' or \'no\'')
    clear()
    if state =='no':
        bid_going_on= False
highest_bid=0
winner = None
for i in bider:
    if i['bid']>=highest_bid:
        winner = i

print('winner is', winner['name'], 'with' ,winner['bid'], 'bid')