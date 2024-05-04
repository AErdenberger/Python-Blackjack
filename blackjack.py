# we just need something here for github

# make a "cards"
# shuffle those cards into a deck
    # deck is a stack (deque) of card objects
# deal out two cards each to start

# players are asked to "hit" or "stay"
    # player who hits gains a new card
    # player who stay stop gaining cards and then their score is checked
    
# dealer will always stay on 17
    # if the dealer's total is 16 or under they will always "hit"

# if you got over 21 you lose
# compare player's hand to dealer's hand
# greater hand value wins

CARDS = {"ace": 1,
         "two": 2,
         "three": 3,
         "four": 4,
         "five": 5,
         "six": 6,
         "seven" : 7,
         "eight" : 8,
         "nine" : 9,
         "ten" : 10,
         "jack" : 10,
         "queen" : 10,
         "king" : 10}

SUITS = ["hearts", "clubs", "spades", "diamonds"]

def build_cards():
