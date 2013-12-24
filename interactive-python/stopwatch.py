# URL http://www.codeskulptor.org/#user22_g0a7xd9wBq_6.py

import simplegui

# define global variables

trackseconds = 0
tries = 0
success = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D

def format(t):
    return str((trackseconds // 600) % 60) + ':'  + str ((trackseconds // 100) % 6) \
            + str((trackseconds // 10) % 10) + '.' + str(trackseconds%10)
    
# define event handlers for buttons; "Start", "Stop", "Reset"

def reset():
    # reset global variables and stop the timer
    global trackseconds, tries, success
    timer.stop()
    trackseconds = 0
    tries = 0
    success = 0
 
def start():
    timer.start()
    
def stop():
    # DON'T reset global variables, stop the timer
    # and update tries/success properly
    global tries, success
    if timer.is_running():
        tries += 1
        if (trackseconds % 10) == 0:
            success += 1
    timer.stop()

# define event handler for timer with 0.1 sec interval

def tick():
    # 1 tracksecond = 0.1 second
    global trackseconds
    trackseconds += 1

# define draw handler

def draw_handler(canvas):
    canvas.draw_text(format(trackseconds), (100,110), 42, 'White')
    canvas.draw_text(str(success) + '/' + str(tries), (220,30), 32, 'Red')
    canvas.draw_text('Success / Tries ->', (20, 30), 28, 'Red')

# create frame

frame = simplegui.create_frame('Stopwatch', 300, 200)

# register event handlers

timer = simplegui.create_timer(100, tick)
frame.add_button('Reset', reset)
frame.add_button('Stop', stop)
frame.add_button('Start', start)
frame.set_draw_handler(draw_handler)

# start frame

frame.start()

