# %%
import random

class Hangman():
    def __init__(self, word_list, num_lives: int=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for char in [*self.word]]
        self.num_letters = len(set(self.word))
        self.list_of_guesses= []

# %%
words = ['horse', 'cat', 'elephant']

game = Hangman(words)
# %%
print(game.word)
print(game.word_guessed)
print(game.num_letters)
print(game.list_of_guesses)
# %%
