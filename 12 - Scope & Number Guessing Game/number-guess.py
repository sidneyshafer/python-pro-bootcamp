# Number Guessing Game
from random import randint

# Global constants
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# DEFINCE FUNCTIONS
# Function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    elif level == "hard":
        return HARD_LEVEL_TURNS
    else:
        print("Please type 'easy' or 'hard'.")

# Function to check user's guess against actual answer
def check_answer(guess, answer, turns):
    """ Checks answer against guess. Returns the number of turns remaining. """
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")

def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    # Choose a random number between 1 and 100
    # randint includes both (a, b) --> ie. 1 and 100 will be included
    answer = randint(1, 100)


    # Call the set_difficulty() function to get the number of turns the user can have
    turns = set_difficulty()


    # Repeat the guess functionality if wrong
    # initilize a guess variable
    guess = 0
    while guess != answer:
         # Print the number of turns the user has
        print(f"You have {turns} attempts remaining to guess the number.")

        # Let the user guess a number
        guess = int(input("Make a guess: "))

        # Call the check_answer() function and pass in the user guess, actual answer, and number of turns
        # Track the number of turns and reduce by 1 if wrong
        turns = check_answer(guess, answer, turns)

        # End game if number of turns == 0
        if turns == 0:
            print("You've run out of guesses, you lose.")
            print(f"The answer was {answer}.")
            return # just writing return will exit and end the game() function
        elif guess != answer:
            print("Guess again.")

# Call the game() function
game()



