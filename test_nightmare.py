import mystery_word as mw
import nightmare as nm

def test_initialize_scoreboard():
    nm.word_length = 8
    assert nm.initialize_scoreboard() == "________"

    
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
    edict = {(0,1):["eel"], (1,2):["bee"], (1,):["pep"], ("N/A",):["cat","dog","mat","cow","rat","pop","owl"]}
    adict = {(1,):["cat","mat","rat"],("N/A",):["dog","cow","pop","pep","bee","eel","owl"]}
    tdict = {(2,):["cat","mat","rat"],("N/A",):["dog","cow","pop","pep","bee","eel","owl"]}
    odict = {(1,):["dog","cow","pop"], (0,):["owl"], ("N/A",):["cat","mat","rat","pep","bee","eel"]}
    assert nm.map_letter_locations(wordlist, "e") == edict
    assert nm.map_letter_locations(wordlist, "a") == adict
    assert nm.map_letter_locations(wordlist, "t") == tdict
    assert nm.map_letter_locations(wordlist, "o") == odict
    assert nm.map_letter_locations(wordlist, "x") == {("N/A",):["cat","dog","mat","cow","rat","pop","pep","bee","eel","owl"]}


def test_max_locations():
    location_dict = {(0,):["dog","cow","pop","pep","bee"],
                     (1,):["dog","cow","pop","pep"],
                     (2,5):["dog","cow","pop","pep","bee","eel","owl"],
                     (1,8):["dog","cow","pop","pep","bee","eel"]}
    assert nm.max_letter_location(location_dict) == (2,5)
    location_dict[("N/A",)] = ["cat","dog","mat","cow","rat","pop","pep","bee","eel","owl"]
    assert nm.max_letter_location(location_dict) == ("N/A",)


def test_update_wordlist():
    wordlist = ["hello","bello","hardy","eaten","doggy","kitty","howdy","yello"]
    y_tuple = sorted(["hardy","doggy","kitty","howdy"])
    nm_tuple = nm.update_wordlist(wordlist,"y")
    assert sorted(nm_tuple) == y_tuple
    wordlist.append("tank")
    e_tuple = sorted(["hardy","doggy","kitty","howdy","tank"])
    nm_tuple = nm.update_wordlist(wordlist,"e")
    assert sorted(nm_tuple) == e_tuple

def test_get_locations():
    assert nm.get_locations("e", "hello") == (1,)
    assert nm.get_locations("e", "feet") == (1,2)
    assert nm.get_locations("e", "reese") == (1,2,4)
    assert nm.get_locations("e", "snout") == ("N/A",)

def test_print_progress():
    nm.word_length = 5
    nm.letters_found = [("e",(0,)),("t",(3,))]
    assert nm.print_progress() == "e__t_"
    nm.letters_found = [("t",(0,3)),("h",(1,)),("a",(2,))]
    assert nm.print_progress() == "that_"
