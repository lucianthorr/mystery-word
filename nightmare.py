import mystery_word as mw

word_length = 0
guesses = 25
nightmare_wordlist = []
letters_found = []
scoreboard = ""

def initialize_nightmare_mode(difficulty):
    global word_length
    if difficulty == 'n':
        print("You have chosen Evil Mystery Word!")
        print("Please choose a word length")
        word_length = nightmare_length_input(input(">>"))
        nightmare_game_loop()
    else:
        word_length = 0
        guesses = 25
        nightmare_wordlist = []
        letters_found = []
        scoreboard = ""

def initialize_scoreboard():
    return "_"*word_length

def nightmare_length_input(user_input):
    if(user_input.isdigit()) and (0 < int(user_input) < 20):
        return int(user_input)
    else:
        print("Please choose a word length.")
        return nightmare_length_input(input(">>"))


def trim_wordlist(wordlist,length):
    new_wordlist = []
    for word in wordlist:
        if len(word) == length and mw.is_common_noun(word):
            new_wordlist.append(word)
    return new_wordlist

def map_letter_locations(wordlist, letter):
    letter_location = {}
    for word in wordlist:
        index = get_locations(letter,word)
        if letter_location.get(index, 0) == 0:
            letter_location[index] = []
        letter_location[index].append(word)
    return letter_location

def get_locations(letter,word):
    locations = []
    for index, char in enumerate(word):
        if char == letter:
            locations.append(index)
    if locations == []:
            locations = ["N/A"]
    return tuple(locations)


def max_letter_location(letter_locations):
    max_key = 0
    max_count = 0
    for key, words in letter_locations.items():
        if len(words) > max_count:
            max_key = key
            max_count = len(words)
    return max_key


def update_wordlist(wordlist, letter):
    global letter_locations
    global letters_found
    letter_locations = map_letter_locations(wordlist,letter)
    max_location = max_letter_location(letter_locations)
    new_wordlist = letter_locations[max_location]
    letters_found.append((letter,max_location))
    return new_wordlist


def nightmare_won():
    if len(nightmare_wordlist) == 1:
        final_word = nightmare_wordlist[0]
        for letter in final_word:
            if not letter in mw.guessed_letters:
                return False
        return True
    else:
        return False


def print_progress():
    global scoreboard, guesses
    mystery_word = list("_"*word_length)
    for letter, indices in letters_found:
        for index in indices:
            if(index != "N/A"):
                mystery_word[index] = letter

    mystery_word = "".join(mystery_word)
    if mystery_word != scoreboard:
        print("You found one!")
    else:
        print("You have {} guesses left.".format(guesses))
        guesses -= 1
    return mystery_word


def nightmare_game_loop():
    global scoreboard, guesses, letters_found, word_length
    global nightmare_wordlist
    nightmare_wordlist = mw.get_wordlist(mw.default_wordlist)
    nightmare_wordlist = trim_wordlist(nightmare_wordlist, word_length)
    scoreboard = initialize_scoreboard()
    print_progress()
    while True:
        user_input = input(">>").lower()
        text_output = mw.validate_input(user_input)
        if text_output == "Thanks for playing.\n":
            break
        elif len(text_output) == 1:
            nightmare_wordlist = update_wordlist(nightmare_wordlist,user_input)
            mw.guessed_letters = mw.guessed_letters+user_input
            print(nightmare_wordlist)
            scoreboard = print_progress()
        else:
            print(text_output)
        print(scoreboard)
        if nightmare_won():
            print("You Won!")
            break
        if guesses <= 0:
            print("You're out of guesses!\n"
                  "The mystery word was: {}".format(mystery_word))
            break
