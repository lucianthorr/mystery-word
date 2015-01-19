import mystery_word as mw

word_length = 0
guesses = 8
nightmare_wordlist = []
letters_found = []
mystery_word = ""

def initialize_nightmare_mode(difficulty):
    global word_length
    if difficulty == 'n':
        print("You have chosen Evil Mystery Word!")
        print("Please choose a word length")
        word_length = nightmare_length_input(input(">>"))
        nightmare_game_loop()
    else:
        word_length = 0

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
        if letter in word:
            for index, char in enumerate(word):
                if char == letter:
                    letter_location[index] = letter_location.get(index, 0) + 1
    return letter_location


def max_letter_location(letter_locations):
    max_location = 0
    max_count = 0
    for location, count in letter_locations.items():
        if count > max_count:
            max_location = location
            max_count = count
    print(max_location)
    return max_location


def refine_wordlist(wordlist,letter,max_location):
    new_wordlist = []
    for word in wordlist:
        if word[max_location] == letter:
            new_wordlist.append(word)
    return new_wordlist

def update_wordlist(wordlist, letter):
    letter_locations = map_letter_locations(wordlist,letter)
    max_location = max_letter_location(letter_locations)
    new_wordlist = refine_wordlist(wordlist,letter,max_location)
    return (new_wordlist,max_location)


def nightmare_won():
    pass


def print_progress():
    mystery_word = "_" * word_length
    for letter,location in letters_found:
        mystery_word = mystery_word[:location] + letter + mystery_word[location+1:]
    print(mystery_word)
    return mystery_word

def update_letters_found(letter,location):
    letters_found.append((letter,location))

def nightmare_game_loop():
    nightmare_wordlist = mw.get_wordlist(mw.default_wordlist)
    nightmare_wordlist = trim_wordlist(nightmare_wordlist, word_length)
    print_progress()
    while True:
        user_input = input(">>").lower()
        text_output = mw.validate_input(user_input)
        if text_output == "Thanks for playing.\n":
            break
        elif len(text_output) == 1:
            nightmare_tuple = update_wordlist(nightmare_wordlist,user_input)
            nightmare_wordlist = nightmare_tuple[0]
            nightmare_letter_location = nightmare_tuple[1]
            update_letters_found(user_input,nightmare_letter_location)
            scoreboard = print_progress()
        else:
            print(text_output)
        #print(scoreboard)
        if nightmare_won():
            print("You Won!")
            break
        if guesses <= 0:
            print("You're out of guesses!\n"
                  "The mystery word was: {}".format(mystery_word))
            break
