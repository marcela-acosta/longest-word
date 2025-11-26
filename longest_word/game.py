# longest_word/game.py

import random
import string
import requests

class Game:
    def __init__(self):
        """
        Initialize a new game, generating a random grid
        of 9 uppercase letters.
        """
        # Creates a list of 9 random uppercase letters (A-Z). This fixes
        # the AttributeError: 'Game' object has no attribute 'grid'.
        self.grid = [random.choice(string.ascii_uppercase) for _ in range(9)]

    def is_valid(self, word):
        """
        Validates if the word can be built from the grid and exists in the dictionary.
        """
        # 1. Check for empty word (to pass test_empty_word_is_invalid and prevent KeyError in API call)
        if not word:
            return False

        # 2. Check if the word can be built using the grid's letters
        grid_letters = self.grid.copy()
        for letter in word:
            if letter in grid_letters:
                # Consume the letter from the available grid letters
                grid_letters.remove(letter)
            else:
                # Word cannot be built from the grid (Fixes test_is_invalid)
                return False

        # 3. If it can be built, check against the dictionary API
        return self.__check_dictionary(word)


    @staticmethod
    def __check_dictionary(word):
        """
        Checks if a word exists in the dictionary using the Le Wagon API.
        """
        response = requests.get(f"https://dictionary.lewagon.com/{word}")
        json_response = response.json()

        # Use .get('found', False) to safely retrieve the value,
        # ensuring False is returned if 'found' key is missing.
        return json_response.get('found', False)
