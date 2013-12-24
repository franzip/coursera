# URL http://www.codeskulptor.org/#user20_l2wcTEgGkh_5.py

# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions
import random

def number_to_name(number):
    # fill in your code below
    if number == 0:
        return 'rock'
    elif number == 1:
        return 'Spock'
    elif number == 2:
        return 'paper'
    elif number == 3:
        return 'lizard'
    elif number == 4:
        return 'scissors'
    else:
        print 'Numbers must be between 0 and 4!'
    # convert number to a name using if/elif/else
    # don't forget to return the result!

    
def name_to_number(name):
    # fill in your code below
    if name == 'rock':
        return 0
    elif name == 'Spock':
        return 1
    elif name == 'paper':
        return 2
    elif name == 'lizard':
        return 3
    elif name == 'scissors':
        return 4
    else:
        print 'Sorry, but "' + name + '" is not a valid choice! \n'
    # convert name to number using if/elif/else
    # don't forget to return the result!


def rpsls(name): 
    # fill in your code below
    player_guess = name_to_number(name)
    # checking player_guess content for invalid inputs
    if player_guess == None: 
        return
    # convert name to player_number using name_to_number
    comp_guess = random.randrange(0,5)
    # compute random guess for comp_number using random.randrange()
    result = (comp_guess - player_guess) % 5
    # compute difference of player_number and comp_number modulo five
    if result == 1 or result == 2:
        winner = 'Computer'
    elif result == 3 or result == 4:
        winner = 'Player'
    # use if/elif/else to determine winner
    comp_choice = number_to_name(comp_guess)
    # convert comp_number to name using number_to_name
    print 'Player chooses', name, '\n', 'Computer chooses', comp_choice
    if result:
        print winner, 'wins!', '\n'
    else:
        print 'Player and computer tie!', '\n'
    # print results

    
# test your code
rpsls('cat')
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


