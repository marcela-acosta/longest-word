# longest_word/game.py

import random
import string

class Game:
    def __init__(self):
        """
        Initialize a new game, generating a random grid
        of 9 uppercase letters.
        """
        # Creates a list of 9 random uppercase letters (A-Z)
        self.grid = [random.choice(string.ascii_uppercase) for _ in range(9)]

    def is_valid(self, word):
        if not word:
            return False
        letters = self.grid.copy() # Consume letters from the grid
        for letter in word:
            if letter in letters:
                letters.remove(letter)
            else:
                return False
        return True
