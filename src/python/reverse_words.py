"""
Code challenge: Reverse words.

Write a function that will take a given string and reverse the order of the words.
"Hello world" becomes "world Hello" and
"May the Fourth be with you" becomes "you with be Fourth the May"
"""


def reverse_words(phrase: str) -> str:

    if not (phrase and isinstance(phrase, str)):
        raise ValueError('The phrase argument must be a string.')

    word_list = phrase.split(' ')
    reversed_word_list = reversed(word_list)
    return ' '.join(reversed_word_list)


if __name__ == '__main__':

    phrase = "Hello World!"
    reversed_phrase = reverse_words(phrase)
    print(f"Phrase: {phrase} | Reversed: {reversed_phrase}")
