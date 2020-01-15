# -*- coding: utf-8 -*-
"""
## SCRIPT EXPLANATION ::
StringManager class have multiple functionalities. They are -
    1. Pick alphabets for given number/s randomly and forms a word from the
    randomly picked alphabets
        E.g. "abc"
    2. Find the factorial of formed word. Plainly, it can give the number
    of possible combinations
    that can be formed from the formed word.
        E.g. Possible combinations that can be made from "abc" is 6.
    3. Remove the repeated letters in the word.
        E.g. "aabbc" will be formatted to "abc"
    4. Find the word combinations or permutations for the word.
        E.g. for "abc" the word combinations are
        ( "abc","acb","bac","bca","cab","cba")
    5. Find the synonyms for meaningful word.
        E.g. Synonym for "cab" is taxi.

@author: Harish Karthic
"""
# Import necessary libraries
import random
import math
from PyDictionary import PyDictionary

# Creating string manager class


class StringManager():

    # Attribute alphabets library
    alphabets_library = list(map(chr, range(97, 123)))

    # String Manager
    def __init__(self, number=0, string="StringManager"):
        self.number = number
        self.string = string

    # Print string manager details
    def __str__(self):
        return "Number : %i \nString : %s" % (self.number, self.string)

    # Get factorial of given integer
    def get_factorial(self, integer):
        self.integer = integer
        return math.factorial(self.integer)

    # Pick random alphabets from alphabets library
    def pick_random_alphabets(self, number):
        self.number = number

        # Validate if passed integer is non 0
        if self.number == 0:
            return "Pass valid integer"

        else:
            counter = 1
            word = ""

            while counter <= self.number:
                counter = counter + 1
                word += random.choice(self.alphabets_library)
            return word

    # Remove repeated alphabets
    def remove_repeated_alphabets(self, string):
        self.string = string

        word = ""
        for letter in list(set(string)):
            word += letter
        return word

    # Get string permutations
    def string_permutations(self, string):
        self.string = string

        # Validating passed string
        if len(self.string) == 0:
            return ""

        elif len(self.string) == 1:
            return self.string

        else:
            word_list = []
            for letter in range(len(string)):
                first_letter = string[letter]
                remaining_letters = string[:letter] + string[letter + 1:]

                for newletter in self.string_permutations(remaining_letters):
                    word_list.append(first_letter + newletter)
            return word_list

    # Get the synonyms of a string
    def get_synonyms(self, string):
        self.string = string

        # Getting meaning of given string
        dictionary = PyDictionary()
        return dictionary.meaning(self.string)
