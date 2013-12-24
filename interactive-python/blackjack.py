# http://www.codeskulptor.org/#user28_XcysKUjlpn_1.py


# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10,
          'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE,
                          [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]],
                          CARD_SIZE)
    
        
# define hand class
class Hand:
    # create Hand object
    def __init__(self):
        self.hand = list()	

    def __str__(self):
        # return a string representation of a hand
        cards = ''
        for card in self.hand:
            cards += str(card) + ' '
        return 'Hand contains ' + cards     

    def add_card(self, card):
        # add a card object to a hand
        self.hand.append(card)	

    def get_value(self):
        # compute the value of the hand, see Blackjack video
        value = sum([VALUES[card.get_rank()] for card in self.hand])	
        for card in self.hand:
            # handle the aces properly   
            if card.get_rank() == 'A' and (value + 10) <= 21:
                value += 10
        return value
    
    def draw(self, canvas, pos):
        offset = 0
        for card in self.hand:
            # draw a hand on the canvas, use the draw method for cards
            card.draw(canvas, [pos[0] + offset, pos[1]])	
            offset += CARD_SIZE[0]
    
    def draw_hidden(self, canvas, pos):
        # draw method to trigger when in_play status is True
        offset = CARD_SIZE[0]
        for x in range(1, len(self.hand)):
            # drawing from 1 to n (dealer_hand[0] is hidden)
            # draw a hand on the canvas, use the draw method for cards	
            self.hand[x].draw(canvas, [pos[0] + offset, pos[1]])            
            offset += CARD_SIZE[0]
        
# define deck class 
class Deck:
    def __init__(self):
        # create a Deck object
        self.deck = [Card(suit, rank) for suit in SUITS for rank in RANKS]	

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.deck)    
        # use random.shuffle()

    def deal_card(self):
        return self.deck.pop()	# deal a card object from the deck
    
    def __str__(self):
        cards = ''	# return a string representing the deck
        for card in self.deck:
            cards += str(card) + ' '
        return 'Deck contains ' + cards



#define event handlers for buttons
def deal():
    global score, deck, outcome, in_play, deck, dealer_hand, player_hand
    outcome = "> Press Hit or Stand..."
    deck = Deck()
    deck.shuffle()   
    dealer_hand = Hand()
    player_hand = Hand()
    for x in range(2):
        dealer_hand.add_card(deck.deal_card())
        player_hand.add_card(deck.deal_card())
    # subtract 1 point if deal is called before the hand ends
    if in_play:
        score -= 1
    in_play = True

def hit():
    global player_hand, outcome, in_play, score
    # if the hand is in play, hit the player
    if player_hand.get_value() <= 21 and in_play:
        player_hand.add_card(deck.deal_card())
    if player_hand.get_value() > 21 and in_play:
        # if busted, assign a message to outcome, update in_play and score
        outcome = "> You have busted! New deal?"
        score -= 1
        in_play = False
    
def stand():
    global dealer_hand, outcome, in_play, score
    player = player_hand.get_value()
    if player > 21:
        outcome = "> Press Deal to play a new hand!"
        return
    while dealer_hand.get_value() < 17:
        # as long as dealer score is less than 17...
        dealer_hand.add_card(deck.deal_card())
    if dealer_hand.get_value() > 21:
        # dealer has busted
        outcome = "> Dealer has busted. You win!"
        if in_play:
            score += 1
        in_play = False
    else:
        # check player_hand and dealer_hand values
        if player > dealer_hand.get_value():
            outcome = "> You win! New deal?"
            if in_play:
                score += 1
            in_play = False
        else:
            outcome = "> Dealer wins! New deal?"
            if in_play:
                score -= 1
            in_play = False

# draw handler    
def draw(canvas):  
    player_hand.draw(canvas, [150, 500])
    # handle in_play status calling draw_hidden on dealer_hand
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, (187, 48),
                          CARD_SIZE)
        dealer_hand.draw_hidden(canvas, [150, 0])
    else:
        dealer_hand.draw(canvas,[150, 0])
    # drawing stuff
    canvas.draw_text(outcome, [0,455], 30, "Black", "monospace")
    canvas.draw_text("BLACKJACK PAYS 3 TO 2", [100,280], 32, "Red", "sans-serif")
    canvas.draw_text("DEALER MUST STAND ON 17 AND HIT ON 16", [60,310], 22, "Red", "sans-serif")
    canvas.draw_polygon([(0, 0), (145, 0), (145, 93), (0,93)], 12, "black", "black")
    canvas.draw_polygon([(0, 600), (145, 600), (145, 507), (0,507)], 12, "black", "black")
    canvas.draw_text("Player Hand", [0, 555], 28, "White")
    canvas.draw_text("Dealer Hand", [0, 50], 28, "White")
    canvas.draw_text("Your Score:", [250, 180], 28, "Black")
    canvas.draw_text(str(score), [300,210], 28, "Black")
    # initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

# create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
dealer_hand = Hand()
player_hand = Hand()
deal()
frame.start()


# remember to review the gradic rubric
