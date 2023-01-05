# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 


## Milestone 1

The implementation uses Python 3.9, a highly human-readable, high-level language that enables rapid prototyping.

In this milestone, the foundations for the Hangman were coded: 

1. A list of possible words is sorted
1. The built-in random module is used to choose a word randonly from the list
1. The user is asked for a single letter input which constitutes a guess at a letter in the word
1. The guess is checked to verify that it is a single-character, alphabetical string


![](images/hangman_milestone_2_py.png)

## Milestone 3

As part of this milestone, the code to request that the user inputs a single character as a guess and validates it was moved to a function: ask_for_input
A second function, check_guess, was added to check whether the guessed character appears in the target word. It takes the user's guessed character and provides feedback to the user on whether the character is present in the word or not.