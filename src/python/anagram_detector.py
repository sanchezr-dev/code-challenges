"""
Code challenge: Anagram detector.

Write a function in your favorite programming language that will accept any two strings
as parameters and return “1” if they are anagrams and “0” if they are not.

An anagram is a word or phrase that's formed by rearranging the letters of another word or phrase.
For example, the letters that make up "A decimal point"
can be turned into the anagram "I'm a dot in place."
People mainly make anagrams just for fun, but sometimes they're used as pseudonyms or codes.

Anagrams are strings with the same character content, and the 
characters' frequency(or number) are also the same.
"""


def check_anagram(phrase_a: str, phrase_b: str) -> bool:

    normalized_phrase_a = ''.join(
        char for char in phrase_a if char.isalnum()
    ).lower()

    normalized_phrase_b = ''.join(
        char for char in phrase_b if char.isalnum()
    ).lower()

    if len(normalized_phrase_a) != len(normalized_phrase_b):
        return False

    return sorted(normalized_phrase_a) == sorted(normalized_phrase_b)


if __name__ == "__main__":

    phrase_a = "Eleven plus two"
    phrase_b = "Twelve plus one"
    are_anagrams = check_anagram(phrase_a, phrase_b)
    print(f"Phrase A: '{phrase_a}' | Phrase B: '{phrase_b}' | Anagrams?: {are_anagrams}")

    phrase_a = "A decimal point"
    phrase_b = "I'm a dot in place"
    are_anagrams = check_anagram(phrase_a, phrase_b)
    print(f"Phrase A: '{phrase_a}' | Phrase B: '{phrase_b}' | Anagrams?: {are_anagrams}")

    phrase_a = "Vacation time!"
    phrase_b = "I am not active"
    are_anagrams = check_anagram(phrase_a, phrase_b)
    print(f"Phrase A: '{phrase_a}' | Phrase B: '{phrase_b}' | Anagrams?: {are_anagrams}")

    phrase_a = "City"
    phrase_b = "Hola"
    are_anagrams = check_anagram(phrase_a, phrase_b)
    print(f"Phrase A: '{phrase_a}' | Phrase B: '{phrase_b}' | Anagrams?: {are_anagrams}")
