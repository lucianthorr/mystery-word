import mystery_word as mw


def test_check_proper_nouns():
    assert mw.is_common_noun("Titanic") == False
    assert mw.is_common_noun("NASA") == False
    assert mw.is_common_noun("titanic") == True
    assert mw.is_common_noun("hometown") == True

def test_word_length_easy():
    mw.difficulty = "e"
    assert mw.is_proper_word_length("four") == True
    assert mw.is_proper_word_length("fourtwo") == False
    assert mw.is_proper_word_length("fo") == False

def test_word_length_medium():
    mw.difficulty = "m"
    assert mw.is_proper_word_length("seventy") == True
    assert mw.is_proper_word_length("sevensevens") == False
    assert mw.is_proper_word_length("seve") == False

def test_word_length_hard():
    mw.difficulty = "h"
    assert mw.is_proper_word_length("seventysevennine") == True
    assert mw.is_proper_word_length("seventy") == False
    assert mw.is_proper_word_length("sev") == False

def test_quit():
    assert mw.validate_input("quit") == "Thanks for playing.\n"

def test_invalid_large_input():
    assert mw.validate_input("AA") == "One letter at a time!\n"

def test_invalid_character_input():
    assert mw.validate_input("1") == "Letters only.\n"
    assert mw.validate_input(".") == "Letters only.\n"
    assert mw.validate_input("\n") == "Letters only.\n"
    assert mw.validate_input(" ") == "Letters only.\n"

def test_redundant_character_input():
    mw.guessed_letters = ['a','b','c']
    assert mw.validate_input("a") == "You already tried that one."
    assert mw.validate_input("b") == "You already tried that one."
    assert mw.validate_input("x") == "x"

def test_choose_difficulty():
    assert mw.choose_difficulty("e") == "e"
    assert mw.choose_difficulty("m") == "m"
    assert mw.choose_difficulty("h") == "h"
    # requires "py.test -s " with the user input "h"
    # assert mw.choose_difficulty("hard") == "h"

def test_play_again():
    assert mw.play_again("yes") == True
    assert mw.play_again("no") == False
