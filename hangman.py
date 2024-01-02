from random import choice
import string

# GAME SETUP
# Method for selecting word to guess
def select_word():
    with open("words.txt", mode="r") as words:
        word_list = words.readlines()
    return choice(word_list).strip()

# Set word for guessing using above method
target_word = select_word()

# Create empty array for guessed_letters
guessed_letters = {"a", "e", "o"}


# USER INPUT
# Private method for validating user's input
def _validate_input(player_input):
    # return true if three conditions met
    return (
        # only one character entered
        len(player_input) == 1
        # character is a lowercase letter of the alphabet (a to z - no speical characters)
        and player_input in string.ascii_lowercase
        # character has not already been guessed
        and player_input not in guessed_letters
    )

# Method for getting using input
def get_player_input():
    while True:
        player_input = input("Guess a letter:").lower()
        if _validate_input(player_input):
            guessed_letters.add(player_input)
            return player_input

get_player_input()


# Method for showing word to the player
def build_guessed_word(target_word, guessed_letters=guessed_letters):
    # create empty list to add letters and underscores to, which we can later join
    current_letters = []
    # loop over the letters in the target word
    for letter in target_word:
        # if the letter is in the set of guessed letters
        if letter in guessed_letters:
            # then add letter to list
            current_letters.append(letter)
        # otherwise add underscore to list instead
        else:
            current_letters.append("_")
    # join list elements together with spaces
    return " ".join(current_letters)

print(build_guessed_word(target_word))
