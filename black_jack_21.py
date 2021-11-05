import random, sys

# Set up the constant
HEARTS = chr(9829) # Character 9829 is '♥'
DIAMONDS = chr(9830) # Character 9830 is '♦'
SPADES = chr(9824) # Character 9824 is '♠'
CLUBS = chr(9827) # Character 9827 is '♣'

BACKSIDE = 'backside'


def main():
    print('''BlackJack
    
    Try to get as close to 21 without going over.
    Kings, Queens, and Jacks are worth 10 points
    Aces are worth 1 or 11 points.
    Cards 2 through 10 are worth their face value.
    (H)it to take another card
    (S)tand to stop taking cards.
    On your first play, you can (D)ouble down to increase your bet
    but must hit exactly one more time before standing.
    In case of a tie, the bet is returned to the player.
    The dealer stops hitting at 17.''')

    money = 500
    while True:  # Main game loop
        # Check if the player is out of money
        if money <= 0:
            print("You're broke!")
            print("Good thing you weren't playing with real money.")
            print('Thanks for playing!')
            sys.exit()

        # Let the player make bet for this round:
        print('Money:', money)
        bet = getBet(money)

        # Give the dealer and the player two cards form the deck:
        deck - giveDeck()
        dealerHand = [deck.pop(), deck.pop()]
        palyerHand = [deck.pop(), deck.pop()]

        # Handle player action:
        print('Bet:', bet)
        while True:  # Keep looping until player stands or busts.
            displayHands(palyerHand, dealerHand, False)
            print()

            # Check if the player has bust:
            if getHandValue(playerHand) > 21:
                break

            # Get the player's move, either H, S, or D:
            move = getMove(playerHand, money - bet)
