# URL http://www.codeskulptor.org/#user23_S0hAyUjlTR_6.py

# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    if direction == RIGHT:
        ball_vel = [random.randrange(120/60., 240/60.),-random.randrange(60/60., 180/60.)]
    elif direction == LEFT:
        ball_vel = [-random.randrange(120/60., 240/60.),-random.randrange(60/60., 180/60.)]

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    score1, score2 = 0,0
    # set up paddles
    paddle1_vel, paddle2_vel = 0,0
    paddle1_pos = [HEIGHT/2 - HALF_PAD_HEIGHT, HEIGHT/2 + HALF_PAD_HEIGHT]
    paddle2_pos = [HEIGHT/2 - HALF_PAD_HEIGHT, HEIGHT/2 + HALF_PAD_HEIGHT]    
    # randomly spawn the ball
    spawn_ball(random.choice([LEFT,RIGHT]))

def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_text(str(score1), ((WIDTH/2)/2, 50), 38, 'White')
    c.draw_text(str(score2), ((WIDTH) * 3/4.0, 50), 38, 'White')
    # check for bouncing
    if ball_pos[1] == BALL_RADIUS or ball_pos[1] == HEIGHT - BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]

    #check for gutters collision / paddle
    if ball_pos[0] - BALL_RADIUS <= PAD_WIDTH * 2:
        # ball collision with paddle 1
        if paddle1_pos[0] <= ball_pos[1] <= paddle1_pos[1]:
            ball_vel[0] -= 0.5
            ball_vel[0] = - ball_vel[0]   
        else:
            # right paddle scored
            spawn_ball(RIGHT)  
            score2 += 1
    if ball_pos[0] + BALL_RADIUS > WIDTH - (PAD_WIDTH * 2):
        # ball collision with paddle 2
        if paddle2_pos[0] <= ball_pos[1] <= paddle2_pos[1]:
            ball_vel[0] += 0.5
            ball_vel[0] = - ball_vel[0]        
        else:
            # left paddle scored
            spawn_ball(LEFT)
            score1 += 1

    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    # draw ball
    c.draw_circle(ball_pos, BALL_RADIUS, 2, "White", "White")
    
    # update paddle's vertical position, keep paddle on the screen
    if paddle1_pos[0] < 0:
        paddle1_pos[0] = 0
        paddle1_pos[1] = PAD_HEIGHT
    else:
        paddle1_pos[0] += paddle1_vel
        paddle1_pos[1] += paddle1_vel
    if paddle1_pos[1] > HEIGHT:
        # keep the paddle on the canvas
        paddle1_pos[1] = HEIGHT
        paddle1_pos[0] = HEIGHT - PAD_HEIGHT
    else:
        paddle1_pos[0] += paddle1_vel
        paddle1_pos[1] += paddle1_vel  
        
    if paddle2_pos[0] < 0:
        paddle2_pos[0] = 0
        paddle2_pos[1] = PAD_HEIGHT
    else:
        paddle2_pos[0] += paddle2_vel
        paddle2_pos[1] += paddle2_vel
    if paddle2_pos[1] > HEIGHT:
        paddle2_pos[1] = HEIGHT
        paddle2_pos[0] = HEIGHT - PAD_HEIGHT
    else:
        paddle2_pos[0] += paddle2_vel
        paddle2_pos[1] += paddle2_vel

    # draw paddles
    c.draw_line([0, paddle1_pos[0]], [0, paddle1_pos[1]], PAD_WIDTH * 2, 'White')
    c.draw_line([WIDTH, paddle2_pos[0]], [WIDTH, paddle2_pos[1]], PAD_WIDTH * 2, 'White')
    
    # draw scores
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['up']:
        paddle1_vel -= 5
    elif key == simplegui.KEY_MAP['down']:
        paddle1_vel += 5
    if key == simplegui.KEY_MAP['w']:
        paddle2_vel -= 5
    elif key == simplegui.KEY_MAP['s']:
        paddle2_vel += 5

   
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['up'] or key == simplegui.KEY_MAP['down']:
        paddle1_vel = 0
    if key == simplegui.KEY_MAP['w'] or key == simplegui.KEY_MAP['s']:
        paddle2_vel = 0

def restart():
    new_game()
  
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", restart)


# start frame
new_game()
frame.start()
