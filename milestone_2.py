
import random

# Creates initial list of words
word_list = ["melon", "pear", "cherry", "kiwi", "watermelon"]
print(word_list)

# Selects a word randomly from the list
word = random.choice(word_list)
print(word)

# Asks the user for a guess
guess = str(input("Please enter a single letter: "))

# Checks if the guess is a single letter
if (len(guess) == 1) and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")


