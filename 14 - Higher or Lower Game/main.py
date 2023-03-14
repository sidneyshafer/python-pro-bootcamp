from art import logo, vs
from game_data import data
import random

def format_data(account):
    """ Takes the account data and returns the printable format """
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_desc} from {account_country}"

def check_answer(guess, a_followers, b_followers):
    """ Takes the user guess and follower counts and returns if they got it correct. """
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

# Display logo from art
print(logo)
# Initialize a variable to keep track of score
score = 0
game_on = True
account_b = random.choice(data)

# Make the game repeatable
while game_on:

    # Generate a random account from the game_data

    # Make account at position B become next account a position A
    account_a = account_b
    account_b = random.choice(data)
    
    # Make sure accounts are different
    if account_a == account_b:
        account_b = random.choice(data)

    # Call format_data function and print the accounts
    print(f"Compare A: {format_data(account_a)}")
    # Display vs logo from art
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    # Ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Check if user is correct
    # Get follower count of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Give user feeback on their guess
    if is_correct:
        # increment the score by 1
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        game_on = False
        print(f"Sorry, that's wrong. Final score: {score}.")
