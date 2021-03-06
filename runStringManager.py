'''
This script is an example of how the StringManager class can be
instantiated and worked with.
'''
# Instantiating the class StringManager and using it's functionalities.

from stringmanager import StringManager

number = int(input("Enter the number to pick alphabets : "))
string_manager = StringManager()

# Prints the factorial of entered number
print(f"Factorial of given number {number} is : {string_manager.get_factorial(number)}")

# Picks random alphabets
word = string_manager.pick_random_alphabets(number)
print(f"Picked random alphabets and the word formed is : {word}")

# Prints the new word after removing duplicates from the given word
new_word = string_manager.remove_repeated_alphabets(word)
print(f"New word formed after removing repeated letters : {new_word}")

# Prints the all possible combinations for given string/word
permuted_words = string_manager.string_permutations(new_word)

print(f"List of all possible word combinations : ")
print(permuted_words)

# Prints the synonyms of the words/string


def synonyms(words):

    word_list = []
    for word in words:
        word_list.append(f"{word} :: {string_manager.get_synonyms(word)}")
    return word_list

print("Synonyms for the words : ")
print(synonyms(permuted_words))
