from random import choice
import string

# GAME SETUP
# Method for selecting word to guess
def select_word():
    with open("words.txt", mode="r") as words:
        word_list = words.readlines()
    return choice(word_list).strip()


# Set maximum number incorrect guesses
MAX_INCORRECT_GUESSES = 6


# USER INPUT
# Private method for validating user's input
def _validate_input(player_input, guessed_letters):
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
        player_input = input("Guess a letter: ").lower()
        if _validate_input(player_input, guessed_letters):
            guessed_letters.add(player_input)
            return player_input




# Method for showing word to the player
def build_guessed_word(target_word, guessed_letters):
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

# print(build_guessed_word(target_word))

# Method for drawing hangman depending on number of incorrect guesses
def draw_hanged_man(number_wrong_guesses):
    hanged_man = [
        # using raw strings so backslashes not escaped
        r"""
  -----
  |   |
      |
      |
      |
      |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
      |
      |
      |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 >.<  |
  |   |
  |   |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 >.<  |
/ |   |
  |   |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 >.<  |
/ | \ |
  |   |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 >.<  |
/ | \ |
  |   |
 ---  |
/     |
|     |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 >.<  |
/ | \ |
  |   |
 ---  |
/   \ |
|   | |
      |
-------
""",
    ]
    # use number of guesses as index to return correct drawing
    print(hanged_man[number_wrong_guesses])

# draw_hanged_man(6)

# Method to check if game is over
def game_over():
    # game is over if user reaches max number of incorrect guesses
    if number_wrong_guesses == MAX_INCORRECT_GUESSES:
        draw_hanged_man(number_wrong_guesses)
        print("Game over! A bear with a sack on his head pulls the lever and your lover meets a brutal but short end. You will be reunited in the next life!")
        return True
    # turn target word into a set object, which will automatically contain every unique letter from target word
    # compared this set to the set of guessed letters.
    # <= operator checks if every item in left-hand set is a member of right hand set.
    if set(target_word) <= guessed_letters:
        print("VICTORY! The bears keep their word and begrudgingly let you go. You and your lover flee into the night together, to fight the teddy power another day.")
        return True
    # otherwise game is not yet over so return false
    return False


if __name__ == "__main__":
    # Initial setup
    # Set word for guessing using above method
    target_word = select_word()

    # Create set for guessed_letters
    guessed_letters = set()

    # Initialise at 0 number of wrong guesses
    number_wrong_guesses = 0

    # game exposition
    print("""It's 2034, and it has been 10 long years since the bloody and terrible Teddy Bear Uprising. 🩸 🧸
          You and your lover have led the human resistance from the start, but yesterday your heist of the Stuffing Treasury went badly wrong and your partner in rebellion and life was captured. Your love is due to be hung to death this very day 💀
          Droves of teddy bears have come to witness the execution. The oversized plaid bowtie noose has been prepared. The fake cups of tea have been poured. The picnics have been laid out.
          But you know that teddy bears can't resist a game, so you challenge their leader, the Prime Cuddler, to hangman.
          If you win, you and your lover go free. If they win, your lover will be executed, and you will turn yourself in.
          So this one's for all the eye marbles.""")

    # game loop
    while not game_over():
        draw_hanged_man(number_wrong_guesses)
        guessed_word = build_guessed_word(target_word, guessed_letters)
        print(f"Your word is: {guessed_word}")
        # if not first go print guessed letters
        if number_wrong_guesses > 0:
            print(
            "Current guessed letters: "
            f"{' '.join(guessed_letters)}\n"
            )
        # get player input and assign to variable
        current_guess = get_player_input()
        if current_guess in target_word:
            print("Yes! One step closer to freeing your baby from the bears")
        else:
            print("Oh no! That's not right - the bears are tittering with bloodlust")
            number_wrong_guesses += 1
        guessed_letters.add(current_guess)
