# ASCII logo for the game
logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

import random  # Importing random module to select random cards

# Function to deal a card randomly
def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]  # The deck of cards
    card = random.choice(cards)  # Select a random card from the deck
    return card  # Return the selected card

# Function to calculate the score of a hand
def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    # If the hand is an exact Blackjack (Ace + 10)
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # 0 represents a Blackjack

    # If hand contains an Ace (11) and the total score exceeds 21, replace Ace (11) with 1
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)  # Return the total score of the hand

# Function to compare user score with computer score and determine the result
def compare(u_score, c_score):
    """Compares the user score u_score against the computer score c_score."""
    if u_score == c_score:
        return "Draw 🙃"
    elif c_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif u_score == 0:
        return "Win with a Blackjack 😎"
    elif u_score > 21:
        return "You went over. You lose 😭"
    elif c_score > 21:
        return "Opponent went over. You win 😁"
    elif u_score > c_score:
        return "You win 😃"
    else:
        return "You lose 😤"

# Function to run the game
def play_game():
    print(logo)  # Display the game logo at the start

    # Initialize hands for the user and the computer
    user_cards = []
    computer_cards = []
    is_game_over = False

    # Deal two initial cards to both player and dealer
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # Game loop for player's turn
    while not is_game_over:
        user_score = calculate_score(user_cards)  # Calculate user's score
        computer_score = calculate_score(computer_cards)  # Calculate computer's score
        
        # Display player's cards and first computer card
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        # Check if the game should end (Blackjack or bust)
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            # Ask user if they want to draw another card
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())  # Add a new card to the user's hand
            else:
                is_game_over = True  # End player's turn

    # Computer's turn (must draw cards until score is at least 17)
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())  # Dealer draws a card
        computer_score = calculate_score(computer_cards)  # Recalculate dealer's score

    # Show final results
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))  # Compare scores and print result

# Game loop to allow replaying
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)  # Clears screen for a new game
    play_game()  # Start a new game
