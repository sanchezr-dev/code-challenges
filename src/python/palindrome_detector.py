"""
Code Challenge: Palindrome detector.

Write a function that will test if a given string is a permutation of a palindrome.

A string is said to be palindrome if it remains the same on reading from both ends.
It means that when you reverse a given string, it should be the same as the original string.
For instance, the string 'level' is a palindrome because it remains the same 
when you read it from the beginning to the end and vice versa.
"""


def is_palindrome(word: str) -> bool:

    if word == word[::-1]:
        return True

    return False


if __name__ == '__main__':

    test_word = 'kayak'
    palindrome_test = is_palindrome(test_word)
    print(f"Word: {test_word} | Is palindrome?: {palindrome_test}")

    test_word = 'level'
    palindrome_test = is_palindrome(test_word)
    print(f"Word: {test_word} | Is palindrome?: {palindrome_test}")

    test_word = 'Hola'
    palindrome_test = is_palindrome(test_word)
    print(f"Word: {test_word} | Is palindrome?: {palindrome_test}")
