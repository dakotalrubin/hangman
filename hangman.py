# Author: Dakota Rubin
# Date: August 2nd, 2023
# File: hangman.py prompts the user to enter a word size from 2 to 22 letters,
#       along with a number of lives from 1 to 20, handling unexpected input
#       using default values. The program opens the provided dictionary file
#       and reads each line as a new word. Each word length is a key, and each
#       value is a list of words with that word length.
#
#       The game of Hangman begins, showing the initial game interface. The
#       player must enter letters to guess the hidden word, whose digits are
#       displayed on-screen along with the number of remaining lives. The
#       player will lose lives for incorrect guesses, while proper guesses
#       will update the interface to reflect the player's progression. After
#       losing all lives or guessing all letters, the game ends. A message
#       will appear which reflects the player's win or loss, and a new prompt
#       will be displayed that allows the user to quit or play again.

# Helps with randomly selecting a word from the dictionary
from random import choice
from hangman_helpers import *

# Creates a dictionary from provided file
dictionary = import_file("words.txt")
print("Welcome to Hangman!")

# Variable determines whether to continue playing Hangman
play_game = True

while (play_game == True):

    # Retrieves word length and number of lives as a tuple
    game_options = get_game_options()

    # choice() randomly selects a word from the dictionary with given word length
    word = choice(dictionary[game_options[0]])
    hidden_word_list = list(word.upper())

    # Creates initial gameplay interface
    digits = []
    for letter in hidden_word_list:
        if letter == "-":
            digits.append("-")
        else:
            digits.append("_")

    # Creates initial life counter interface
    life_counter = []
    for i in range(game_options[1]):
        life_counter.append("O")

    guessed_letter_list = []
    lives_lost = 0

    # Variable determines whether to keep playing a round of Hangman
    continue_round = True

    while (continue_round == True):

        if len(guessed_letter_list) > 0:
            print(f"Letters chosen: {', '.join(str(i) for i in guessed_letter_list)}")
        else:
            print("Letters chosen: ")

        # Updates game interface
        print(f"{' '.join(str(i) for i in digits)}   " +
            f"Lives: {game_options[1] - lives_lost} {''.join(str(i) for i in life_counter)}")

        # Ends round if player correctly guesses all letters
        if "_" not in digits:
            continue_round = False
            print(f"You won! The word is {word.upper()}.")

        # Ends round if player loses all their lives
        if (lives_lost == game_options[1]):
            continue_round = False
            print(f"You lost! The word is {word.upper()}.")

        if (continue_round == True):

            # While loop prompts user again if unexpected input
            while True:

                guessed_letter = input("Choose a new letter: ").upper()

                # Prompt user for new input if letter invalid or already chosen
                if len(guessed_letter) == 1 and guessed_letter.isalpha():
                    if guessed_letter in guessed_letter_list:
                        print("You have already chosen this letter.")
                        continue
                    else:
                        guessed_letter_list.append(guessed_letter)
                        break
                else:
                    continue

            # User guessed letter correctly
            if guessed_letter in hidden_word_list:
                print("You guessed right!")

                # Updates display to show correctly-guessed letters
                digit = 0
                for letter in hidden_word_list:
                    if guessed_letter == letter:
                        digits[digit] = guessed_letter
                    digit += 1

            else:
                print("You guessed wrong! You lost one life.")

                # Change one "O" to an "X" sequentially in the lives display 
                life_counter[lives_lost] = "X"
                lives_lost += 1

    play_again = input("Would you like to play again? (y/n): ").lower()

    if (play_again != "y"):
        play_game = False
        print("Thanks for playing!")