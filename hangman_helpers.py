# Author: Dakota Rubin
# Date: August 2nd, 2023
# File: hangman_helpers.py provides necessary functionality for hangman.py.

from random import randint

"""This helper function imports a file's contents and sorts its lines into a
dictionary by line length."""
def import_file(filename):

    dictionary = {word_list: [] for word_list in range(2, 23)}
    max_word_length = 22 # Length of longest word in provided file

    file = open(filename, "r")

    for line in file:

        word = line.strip()
        word_length = len(word)

        if word_length > 1:

            # All words with lengths greater than max_word_length should be
            # added to max_word_length's list anyway
            if word_length > max_word_length:
                word_length = max_word_length

            dictionary[word_length].append(word)
        else:
            continue

    file.close()

    return dictionary

"""This helper function assists with debugging an imported dictionary."""
def print_dictionary(dictionary):
    for key, value in dictionary.items():
        print(key, ": ", value)

"""This helper function randomly generates a default dictionary word length."""
def get_default_word_length():
    default_word_length = randint(2, 22)
    print("A dictionary word length will be chosen at random.")
    print(f"The word length is set to {default_word_length}.")
    return default_word_length

"""This helper function gets the chosen word length and number of lives from
the user."""
def get_game_options():

    # Handles user input for dictionary word length
    try:
        user_word_length = int(input("Choose a word length for guessing (2 - 22): "))
        if (2 <= user_word_length <= 22):
                print(f"The word length is set to {user_word_length}.")
        else:
            user_word_length = get_default_word_length()
    except:
        user_word_length = get_default_word_length()

    # Handles user input for number of lives
    try:
        number_of_lives = int(input("Choose a number of lives (1 - 10): "))
        if (1 <= number_of_lives <= 10):
            print(f"You have {number_of_lives} lives.")
        else:
            number_of_lives = 5
            print("You have 5 lives.")
    except:
        number_of_lives = 5
        print("You have 5 lives.")

    return (user_word_length, number_of_lives)