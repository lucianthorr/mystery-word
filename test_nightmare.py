import mystery_word as mw
import nightmare as nm


def test_nightmare_length_input():
    assert nm.nightmare_length_input("5") == 5
    assert nm.nightmare_length_input("19") == 19
    # the following tests require "py.test -s"
    # and requre tester to enter an "5" to break out of recursion
    # assert nm.nightmare_length_input("0") == 5
    # assert nm.nightmare_length_input("Five") == 5
    # assert nm.nightmare_length_input("1.5") == 5

def test_trim_wordlist():
    assert nm.trim_wordlist(["abc","cdf","a","abcd"],3) == ["abc","cdf"]
    assert nm.trim_wordlist(["abcd","a"], 0) == []
    assert nm.trim_wordlist(["abcd","a"], 3) == []
    assert nm.trim_wordlist(["abcde","ab","abcdef"], 5) == ["abcde"]

def test_map_locations():
    wordlist = ["cat","dog","mat","cow","rat","pop","pep","bee","eel","owl"]
    edict = {0:1, 1:3, 2:1}
    adict = {1:3}
    tdict = {2:3}
    odict = {1:3, 0:1}
    assert nm.map_letter_locations(wordlist, "e") == edict
    assert nm.map_letter_locations(wordlist, "a") == adict
    assert nm.map_letter_locations(wordlist, "t") == tdict
    assert nm.map_letter_locations(wordlist, "o") == odict
    assert nm.map_letter_locations(wordlist, "x") == {}


def test_max_locations():
    location_dict = {0:4, 1:3, 4:2, 8:5}
    assert nm.max_letter_location(location_dict) == 8

def test_refine_wordlist():
    wordlist = ["cat","dog","mat","cow","rat","pop","pep","bee","eel","owl"]
    assert sorted(nm.refine_wordlist(wordlist,"e",1)) == sorted(["pep","bee","eel"])
    assert sorted(nm.refine_wordlist(wordlist,"o",1)) == sorted(["dog","cow","pop"])

def test_update_wordlist():
    wordlist = ["hello","bello","hardy","eaten","doggy","kitty","howdy","yello"]
    y_tuple = (sorted(["hardy","doggy","howdy","kitty"]),4)
    nm_tuple = nm.update_wordlist(wordlist,"y")
    assert (sorted(nm_tuple[0]),nm_tuple[1]) == y_tuple
    wordlist = ["hello","bello","hardy","eaten","doggy","kitty","howdy","yello"]
    e_tuple = (sorted(["bello","hello","yello"]), 1)
    nm_tuple = nm.update_wordlist(wordlist,"e")
    assert (sorted(nm_tuple[0]),nm_tuple[1]) == e_tuple

def test_print_progress():
    nm.word_length = 5
    nm.letters_found = [(0,"e"),(3,"t")]
    assert nm.print_progress() == "e__t_"
    nm.letters_found = [(0,"t"),(1,"h"),(2,"a"),(3,"t")]
    assert nm.print_progress() == "that_"
