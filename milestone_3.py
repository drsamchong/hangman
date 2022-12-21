# TODO ask user for input and verify - loop if it doesn't pass

while True:
    guess = input("Please guess a single letter: ")
    if (len(guess) == 1) and guess.isalpha():
       break
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")
 