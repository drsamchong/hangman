# %%
import random

class Hangman():
    def __init__(self, word_list: list, num_lives: int=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for char in [*self.word]]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for idx, char in enumerate(self.word):
                if char == guess:
                    self.word_guessed[idx] = char

        else:
            print(f"Sorry, {guess} is not in the word. Try again.")
   
    def ask_for_input(self):
        pass
#        while True:
#            guess = input("Please guess a single letter: ")
#            if not ((len(guess) == 1) and guess.isalpha()):
#                print("Invalid letter. Please, enter a single alphabetical character.")
#                # break
#            elif guess in self.list_of_guesses:
#                print("You already tried that letter!")
#                break
#            else:
#                self.check_guess(guess)
#                break
#        self.list_of_guesses.append(guess)



 


# %%
words = ['horse', 'cat', 'elephant']

game = Hangman(words)
# %%
print(game.word)
print(game.word_guessed)
print(game.num_letters)
print(game.list_of_guesses)
# %%
game.ask_for_input()
print(game.word_guessed)
print(game.list_of_guesses)

# %%