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
        deck = getDeck()
        dealerHand = [deck.pop(), deck.pop()]
        playerHand = [deck.pop(), deck.pop()]

        # Handle player action:
        print('Bet:', bet)
        while True:  # Keep looping until player stands or busts.
            displayHands(playerHand, dealerHand, False)
            print()

            # Check if the player has bust:
            if getHandValue(playerHand) > 21:
                break

            # Get the player's move, either H, S, or D:
            move = getMove(playerHand, money - bet)

            # Handle the payer action:
            if move == 'D':
                # Player is doubling down, they have increased their bet:
                additionalBet = getBet(min(bet, (money - bet)))
                bet += additionalBet
                print(f"Bet increased to {bet}")
                print('Bet:', bet)

            if move in ('H', 'D'):
                # Hit/doubling down take another card.
                newCard = deck.pop()
                rank, suit = newCard
                print(f"You drew a {rank} of {suit}")
                playerHand.append(newCard)

            if getHandValue(playerHand) > 21:
                # The player has busted
                continue

            if move in ('S', 'D'):
                # Stand/doubling down stops the player's turn.
                break

        # Handle the dealer action:
        if getHandValue(playerHand) < 21:
            while getHandValue(dealerHand) < 17:
                # Get dealer hits:
            print("Dealer Hits...")
            dealerHand.append(deck.pop())
            displayHands(playerHand, dealerHand, False)

            if getHandValue(dealerHand) > 21:
                break # Dealer ha busted