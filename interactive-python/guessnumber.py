# URL http://www.codeskulptor.org/#user26_sITUEbTVWQ_7.py

# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import math
import random


# initialize global variables used in your code

game_range = 100
n_guesses = math.ceil(math.log(game_range, 2)) 

# With the new_game() code, line 13 could have been omitted. I left it for the sake of clarity

# helper function to start and restart the game

def new_game():   
    
    global secret_number, n_guesses
    # Using randint() avoid us weird syntax (i.e. print '...', (gamerange-1)
    secret_number = random.randint(0, game_range)
    # Scaling the number of guesses on game_range
    n_guesses = int(math.ceil(math.log(game_range, 2)))
    print 'New game started! Range set from 0 to', str(game_range) + '.',
    print '\nYou can change it by pressing the buttons.'
    print 'Number of remaining guesses:', str(n_guesses) + '.', '\n'

# define event handlers for control panel

def range100():
    # button that changes range to range [0,100) and restarts
    
    global game_range
    game_range = 100
    new_game()

def range1000():
    # button that changes range to range [0,1000) and restarts
    
    global game_range
    game_range = 1000
    new_game()
    
def input_guess(guess):
    # main game logic goes here	
    
    global n_guesses
    n_guesses -= 1
    print 'Guess was', str(guess) + '.'
    print 'Number of remaining guesses:', str(n_guesses) + '.'   
    # This order of conditionals is needed: i.e. the player's guess is right AND n_guesses == 0
    if int(guess) == secret_number:    
        print 'Correct, you got it! \n'
        new_game()
    elif n_guesses == 0:
        print 'You ran out of guesses! Number was', secret_number,
        print '\nYoda said you should point to the center...\n'
        new_game()
        return    
    else:
        if int(guess) < secret_number:
            print 'Shoot higher! \n'
        else:
            print 'Shoot lower! \n'    
# create frame

frame = simplegui.create_frame("Guess the number!", 200, 200)

# register event handlers for control elements

frame.add_button('Set Range to 0-100', range100, 200)
frame.add_button('Set Range to 0-1000', range1000, 200)
frame.add_input('Enter your guess!', input_guess, 200)

# call new_game and start frame

new_game()
frame.start()

# always remember to check your completed program against the grading rubric
