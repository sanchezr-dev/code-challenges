"""
Are the Xs equal to the Os?

Create a Python function that accepts a string.
This function should count the number of Xs and the number of Os in the string.
It should then return a boolean value of either True or False.

If the count of Xs and Os are equal, then the function should return True.
If the count isn't the same, it should return False.
If there are no Xs or Os in the string, it should also return True because 0 equals 0.
The string can contain any type and number of characters.
"""

import re


def x_equal_to_o(str_value):

    if not isinstance(str_value, str):
        raise ValueError("The argument value must bu a string.")

    x_count = len(re.findall('[x, X]', str_value))
    o_count = len(re.findall('[o, O]', str_value))

    return x_count == o_count


if __name__ == '__main__':

    test_value = 'xoxoXOXO'
    print(f"Original string: {test_value} | Result: {x_equal_to_o(test_value)}")

    test_value = 'ABC xo DEF x'
    print(f"Original string: {test_value} | Result: {x_equal_to_o(test_value)}")

    test_value = 'ABC DEF'
    print(f"Original string: {test_value} | Result: {x_equal_to_o(test_value)}")
