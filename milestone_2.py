
import random

word_list = ["melon", "pear", "cherry", "kiwi", "watermelon"]
print(word_list)

word = random.choice(word_list)
print(word)

guess = str(input("Please enter a single letter: "))


if (len(guess) == 1) and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")


