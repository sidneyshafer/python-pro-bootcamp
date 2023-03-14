import random
from hangman_art import stages, logo
from hangman_words import word_list
# from replit import clear

# Randomly choose a word from the word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Keep track of lives
lives = 6

# Print logo
print(logo)

# Create an empty list
# For each letter in the chosen_word, add a "_" to 'display'
display = []
for _ in range(word_length):
    display += "_"

# Check if the player has won
end_of_game = False
while not end_of_game:
    # Ask the user to guess a letter
    guess = input("Guess a letter: ").lower()

    # clear()

    # Check if the user enters a letter they have already guessed
    if guess in display:
        print(f"You've already guessed {guess}.")

    # Check if the letter the user guessed is in the chosen word
    # If the letter is in the word, replace the letter in the 'display' list
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    # if guess is not a letter in chosen word, reduce lives by 1
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"You lose. The word was {chosen_word}")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You Win!")
    
    # Print stages
    print(stages[lives])