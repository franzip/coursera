# URL http://www.codeskulptor.org/#user26_Zjgbm5F8AE_7.py

# implementation of card game - Memory

import simplegui
import random

# card img size
img = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")
imgsize = [71, 96] 
# non random deck with 1 pair of coupled values from (0,0) to (7,7)
deck = range(8) * 2 

# helper function to initialize globals
def new_game():  
    # declaring global variables
    global state, count, prev_turn, prev_turn2, exposed
    # variable to keep tracks of game status
    state = 0
    # counting moves (1 each 2 click)
    count = 0
    # booleans list to keep track of users clicks 
    exposed = [False for x in range(16)]
    # prev_turn and prev_turn2 keep track of flipped cards
    prev_turn, prev_turn2 = None, None
    # randomizing the list indexes when a new game start
    random.shuffle(deck)
    # resetting the moves counter
    label.set_text("Turns = " + str(count))
     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state, prev_turn, prev_turn2, exposed, count
    # getting the mouse x value 
    # by dividing pos[0] by 50 we get a suitable index
    # for our list -> exposed[pos[0] // 5]
    turn = pos[0] // 50
    # game core logic
    if state == 0:
        # flip the card
        exposed[turn] = True
        # save the last card index
        prev_turn = turn
        # switch to state 1
        state = 1
        count += 1
        label.set_text("Turns = " + str(count))
    elif state == 1:
        # ignore clicks on exposed cards
        if not exposed[turn]:
            # flip the card
            exposed[turn] = True
            # save the last card index
            prev_turn2 = turn
            # switch to state 2
            state = 2
    elif state == 2:
        if not exposed[turn]:
            if deck[prev_turn] == deck[prev_turn2]:
                # if the (nth - 1) and (nth - 2) cards match
                # keep them shown
                exposed[turn] = True
                prev_turn = turn
            else:
                # else, hide them again
                exposed[turn] = True
                exposed[prev_turn] = exposed[prev_turn2] = False
                prev_turn = turn
            count += 1
            label.set_text("Turns = " + str(count))
            state = 1
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    # looping through card interval using 50 px as threshold
    for breakline in range(10, 801, 50):
        if exposed[breakline//50]:
            # checking if a card is exposed using index math
            canvas.draw_text(str(deck[breakline//50]), [breakline, 65], 50, 'White')
        else:
            canvas.draw_image(img, [imgsize[0] / 2, imgsize[1] / 2], imgsize,
                              [breakline + 15, 50], (50, 110))
            
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric
