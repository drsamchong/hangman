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

    def ask_for_input(self):
        while True:
            guess = input("Please enter a single character: ")
            if len(guess) != 1 or not (guess.isalpha()):
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
#                self.list_of_guesses.append(guess)
                break

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for idx, char in enumerate(self.word):
                if char == guess:
                    self.word_guessed[idx] = char
            self.num_letters -= 1

        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word. Try again.\n")
            print(f"You have {self.num_lives} lives left.")
        self.list_of_guesses.append(guess)    
 

# %%
def play_game(word_list):
#    num_lives=None
    game = Hangman(word_list) #, num_lives)
    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        if game.num_letters > 0:
            game.ask_for_input()
        else:
            print("Congratulations. You won the game!")
            break


# %%
word_list = ['horse', 'cat', 'elephant']

play_game(word_list)


# %%
#word_list = ['horse', 'cat', 'elephant']

#game = Hangman(word_list, None)

#print(game.word)
#print(game.word_guessed)
#print(game.num_letters)
#print(game.list_of_guesses)
# %%
#game.ask_for_input()
#print(game.word_guessed)
#print(game.list_of_guesses)


# %%
