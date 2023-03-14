# Blackjack Game

############### Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

from art import logo
import random

# Deal a random card
def deal_card():
    """ Returns a random card from the deck. """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

# Sum the list of cards
def calculate_score(card_list):
    """ Take a list of cards and return the score calculated from the cards.""" 

    # Check for blackjack (a hand with only 2 cards and ace + 10)
    # return 0 instead of score
    if sum(card_list) == 21 and len(card_list) == 2:
        return 0 
    
    # Check for an 11. If score is > 21, remove 11 and replace with 1
    if 11 in card_list and sum(card_list) > 21:
        card_list.remove(11)
        card_list.append(1)
        # Return the sum of the cards
        return sum(card_list)
    return sum(card_list)

# Compare the user_score and computer_score
def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You both went over. You lose."
    elif user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "You lose, opponent has Blackjack."
    elif user_score == 0:
        return "You wine with a Blackjack!"
    elif user_score > 21:
        return "You went over 21. You lose."
    elif computer_score > 21:
        return "Opponent went over. You win."
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose."

def play_game():
    # Show logo from art.py
    print(logo)

    # Create two empty lists to store the
    # user cards and computer cards
    user_cards = []
    computer_cards = []
    is_game_over = False

    # Create a for loop to deal the user and cumputer two cards each
    # and add those cards to the empty lists
    for _ in range(2): # _ means we do not need variable
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # While loop for user to continue taking cards
    while not is_game_over:

        # Call calculate_score(). If the computer or the user has a blackjack(0)
        # or if the user's score is over 21, then the game ends
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"    Your cards: {user_cards}, current score: {user_score}")
        print(f"    Computer's first card: {computer_cards[0]}")

        # Check if anyone has gotten a blackjack or has a score of over 21
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True
        
    # While loop for computer to continue taking cards
    # the computer should keep drawing cards as long as it has a score less than 17
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"    Your final hand: {user_cards}, finale score: {user_score}")
    print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")

    # Call compare() function and pass in user_score and computer_score
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_game()