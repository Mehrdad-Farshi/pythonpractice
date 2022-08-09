import random

def game () :
    attempts = 5 
    print('welcome to The number Guessing Game! ')
    print('im thinking of a number between 1 to 100  ')
    difficulty = input('make your difficulty easy or hard  : ')
    if difficulty == 'easy':
        attempts = 10
    the_number = random.randrange(1,100)
    def can_play():
        global attempts
        if attempts == 0:
            print('you lose :(')
            replay=input('you wanna still play yes or no ?')
            if replay == 'yes':
                # clear()
                game()
                
            else:
                return False
        else :
            return True

    def attempt_reduce() :
        return attempts -1

    game_continue = True
    while(game_continue):
        guess = int(input('guess your number : '))
        if guess == the_number:
            print('you win ! ')
            game_continue = False
        elif guess < the_number:
            attempts = attempt_reduce()
            print ('you guessed too low')
            print (f'you have {attempts} attempts left')
            game_continue = can_play()
        else :
            attempts = attempt_reduce()
            print('you guessed too high')
            print (f'you have {attempts} attempts left')
            game_continue = can_play()
            
game()
