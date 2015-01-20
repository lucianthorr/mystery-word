# Mystery Word

# Jason Aylward
# Homework 4

To run, simply type at the command line:

>>python mystery_word.py

You are then given the option of four modes of difficulty,
Easy, Medium and Hard are all standard games of Mystery Word.
You are given 8 tries to guess the letters in a word of a given length.
Only wrong guesses are counted.

Nightmare Mode is an evil version where the computer changes its Mystery Word
until the user's guesses have narrowed the set of possible words.  In this mode,
the user is allowed to choose the exact length of the Mystery Word.
A more thorough explanation can be found at
http://nifty.stanford.edu/2011/schwarz-evil-hangman/
Because Nightmare Mode is significantly more difficult, the user is given
25 guesses.

All user input is error checked.  Besides when a user is choosing difficulty,
input must be a single alphabetic character. The only exception input is "quit",
which allows the user to quit the game at any time.
