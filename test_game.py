import mystery_word as mw


def test_file_to_wordlist():
    print("File")
    assert isinstance(mw.get_wordlist("requirements.txt"),list)
    assert isinstance(mw.get_wordlist("/usr/share/dict/words"),list)

def test_random_word_generator():
    mw.difficulty = "4"
    print("Gen")
    assert mw.generate_word("/usr/share/dict/words") != mw.generate_word("/usr/share/dict/words")

def test_character_in_mystery_word():
    print("char in")
    mw.mystery_word = "titanic"
    assert mw.check_guessed_letter_in_mystery_word("t") == True
    assert mw.check_guessed_letter_in_mystery_word("i") == True
    assert mw.check_guessed_letter_in_mystery_word("c") == True

def test_character_not_in_mystery_word():
    print("char not")
    mw.mystery_word = "titanic"
    assert mw.check_guessed_letter_in_mystery_word("j") == False
    assert mw.check_guessed_letter_in_mystery_word("s") == False
    assert mw.check_guessed_letter_in_mystery_word("h") == False

def test_game_won():
    print("won")
    mw.mystery_word = "titanic"
    assert mw.game_won("titanic") == True
    assert mw.game_won("itanic") == True
    assert mw.game_won("xitan") == False
    assert mw.game_won("botcs") == False

def test_insert_character():
    print("insert")
    assert mw.insert_character(["S","o","n","n"], "u", 1) == ["S","u","n","n"]
    assert mw.insert_character(["L","e","f","t"], "T", 2) == ["L","e","T","t"]
