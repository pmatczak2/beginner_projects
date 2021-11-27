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
                #  Get dealer hits:
                print("Dealer Hits...")
                dealerHand.append(deck.pop())
                displayHands(playerHand, dealerHand, False)

                if getHandValue(dealerHand) > 21:
                    break  # Dealer ha busted
                input("Press Enter to continue...")
                print('\n\n')

        # Show final hands:
        displayHands(playerHand, dealerHand, True)

        playerValue = getHandValue(playerHand)
        dealerValue = getHandValue(dealerHand)
        # Handle whether the player won, lost, or tied:
        if dealerValue > 21:
            print(f'Dealer busts! You win {bet}!')
            money += bet
        elif (playerValue > 21) or (playerValue < dealerValue):
            print('you lost!')
            money -= bet
        elif playerValue > dealerValue:
            print(f"You won {bet}")
            money += bet
        elif playerValue == dealerValue:
            print('It\'s a tie, the bet is returned to you.')

        input('Press enter to continue...')
        print('\n\n')

def getBet(maxBet):
    while True:  # Keep asking until they enter a valid amount.
        print(f'How much do you want to bet? (1-{maxBet}, or QUIT)')
        bet = input('> ').upper().strip()
        if bet == "QUIT":
            print("Thanks for playing")
            sys.exit()

        if not bet.isdecimal():
            continue #  If the player didn't enter a number, ask again.

        bet = int(bet)
        if 1 <= bet <= maxBet:
            return bet  # Player entered a valid bet.

def displayHands(playerHand, dealerHand, showDealerHand):
    print()
    if showDealerHand:
        print('DEALER:', getHandValue(dealerHand) )
        displayCards(dealerHand)
    else:
        print('DEALER:???')
        # Hide the dealer's first card:
        displayCards([BACKSIDE] + dealerHand[1:])

    # Show Player cards
    print('PLAYER:', getHandValue(playerHand))
    displayCards(playerHand)

def getHandValue(cards):
    value = 0
    numberOfAces = 0

    #  Add value for a none-ace card
    for card in cards:
        rank = card[0] # card is a tuple like (rank, suit)
        if rank == 'A':
            numberOfAces += 1
        elif rank in ('K', 'Q', 'J'):  #  Face cards are worth 10 points
            value += 10
        else:
            value += int(rank)  #  Numbered cards are worth their number.

    #  Add the values for the aces.
    value += numberOfAces  #  Add 1 per ace
    for i in range(numberOfAces):
        #  If another 10 can be added with busting, do so:
        if value + 10 <= 21:
            value += 10

    return value

def displayCards(cards):
    rows = ['', '', '', '', ''] #  The text to display on each row

    for i, card in enumerate(cards):
        rows[0] += ' ___  '  # Print the top line of the card.
        if card == 'BACKSIDE':
            #  Pint the cards backside.
            rows[1] += '[## ] '
            rows[2] += '[###] '
            rows[3] += '[_##] '
        else:
            #  Print the cards front.
            rank, suit = card #  The card is a tuple data structure.
            rows[1] += '|{} | '.format(rank.ljust(2))
            rows[2] += '| {} | '.format(suit)
            rows[3] += '|_{}| '.format(rank.ljust(2,'_'))

    # print each row on the screen:
    for row in rows:
        print(row)
