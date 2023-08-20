"""
Code challenge: Count the vowels in a string

Create a function in Python that accepts a single word 
and returns the number of vowels in that word.
In this function, only a, e, i, o, and u will be counted as vowels — not y.
"""


def count_vowels(str_value):

    if not isinstance(str_value, str):
        raise ValueError("The input parameter only accepts strings")

    vowels = ['a', 'e', 'i', 'o', 'u']
    count = len([char for char in str_value if char.lower() in vowels])
    return count


if __name__ == '__main__':

    test_value = 'Hello'
    total_vowels = count_vowels(test_value)
    print(f'"{test_value}" has {total_vowels} vowels.')

    test_value = 'Lorem Ipsum'
    total_vowels = count_vowels(test_value)
    print(f'"{test_value}" has {total_vowels} vowels.')
