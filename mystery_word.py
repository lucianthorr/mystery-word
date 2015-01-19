# Jason Aylward
# Homework 3
import random


default_wordlist = "/usr/share/dict/words"
mystery_word = ""
discovered_letters = ""
guessed_letters = ""
scoreboard = ""
guesses = 8
difficulty = 0


def start_game():
    print("Welcome to Mystery Word!\nEnter 'Quit' to Quit anytime.")
    print("""Choose your level of difficulty
            (E)asy
            (M)edium
            (H)ard""")
    difficulty = choose_difficulty(input(">>").lower())
    return difficulty


def choose_difficulty(mode):
    if mode == "e":
        return "e"
    if mode == "m":
        return "m"
    if mode == "h":
        return "h"
    else:
        print("Try Again\n")
        return choose_difficulty(input(">>").lower())


def get_wordlist(file_address):
    with open(file_address) as file:
        file_string = file.read()
    word_list = file_string.split()
    return word_list


def generate_word(file_address):
    wordlist = get_wordlist(file_address)
    random_int = random.randint(0, len(wordlist)-1)
    random_word = wordlist[random_int]
    if is_common_noun(random_word) and is_proper_word_length(random_word):
        print("Your mystery word "
              "is {} characters long.".format(len(random_word)))
        return random_word
    else:
        return generate_word(file_address)


def is_common_noun(word):
    if word == word.lower():
        return True
    else:
        return False


def is_proper_word_length(word):
    if difficulty == "e":
        return 4 <= len(word) <= 6
    elif difficulty == "m":
        return 6 <= len(word) <= 10
    elif difficulty == "h":
        return 10 <= len(word)
    else:
        return True


def validate_input(user_input):
    if user_input == 'quit':
        return "Thanks for playing.\n"
    elif len(user_input) > 1:
        return "One letter at a time!\n"
    elif user_input == "":
        return "Give it another shot.\n"
    elif not user_input.isalpha():
        return "Letters only.\n"
    elif user_input in guessed_letters:
        return "You already tried that one."
    else:
        return user_input


def check_guessed_letter_in_mystery_word(user_input):
    global discovered_letters
    global guesses
    if user_input in mystery_word:
        discovered_letters = discovered_letters + user_input
        print("Great! You found one!")
        return True
    else:
        guesses -= 1
        print("Try Again. You have {} more guesses".format(guesses))
        return False


def game_won(discoveries):
    for mystery_letter in mystery_word:
        if mystery_letter not in discoveries:
            return False
    return True


def insert_character(word_as_list, letter, index):
    word_as_list[index] = letter
    return word_as_list


def print_progress():
    scoreboard_list = list("_"*len(mystery_word))
    [insert_character(scoreboard_list, letter, index) for index,
        letter in enumerate(mystery_word, 0) if letter in discovered_letters]
    scoreboard = "".join(scoreboard_list)
    return scoreboard


def reset_globals():
    global scoreboard, discovered_letters, mystery_word
    global guessed_letters, guesses, difficulty
    guesses = 8
    guessed_letters = ""
    discovered_letters = ""
    mystery_word = ""
    scoreboard = ""
    difficulty = 4


def play_again(answer):
    if answer == "y" or answer == "yes":
        return True
    elif answer == "n" or answer == "no":
        return False
    else:
        print("Would you like to play again?\n"
              "[Y]es\n[N]o")
        return play_again(input(">>").lower())


if __name__ == '__main__':
    while True:
        reset_globals()
        difficulty = start_game()
        mystery_word = generate_word(default_wordlist)
        while True:
            user_input = input(">>").lower()
            text_output = validate_input(user_input)
            if text_output == "Thanks for playing.\n":
                break
            elif len(text_output) == 1:
                guessed_letters = guessed_letters + text_output
                check_guessed_letter_in_mystery_word(user_input)
                scoreboard = print_progress()
            else:
                print(text_output)
            print(scoreboard)
            if game_won(discovered_letters):
                print("You Won!")
                break
            if guesses <= 0:
                print("You're out of guesses!\n"
                      "The mystery word was: {}".format(mystery_word))
                break
        print("Would you like to play again?\n"
              "[Y]es\n[N]o")
        if(not play_again(input(">>").lower())):
            "Thanks for playing!"
            break
