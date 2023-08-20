"""
Code challenge: Convert a decimal number into a binary.

Write a function in Python that accepts a decimal number and returns the equivalent binary number.
To make this simple, the decimal number will always be less than 1,024, 
so the binary number returned will always be less than ten digits long.
"""


def decimal_to_binary_1(number):
    """
    Function to convert an integer number into a binary.

    Args:
        number: An integer number.

    Returns:
        The equivalent binary number representation.

    Raises:
        ValueError: If the number argument is not an integer.
    """

    if not isinstance(number, int):
        raise ValueError("Number argument must be an int.")

    if number >= 1:
        decimal_to_binary_1(number // 2)

    print(number % 2, end='')


def decimal_to_binary_2(number):
    """
    Function to convert an integer number into a binary.

    Args:
        number: An integer number.

    Returns:
        The equivalent binary number representation.

    Raises:
        ValueError: If the number argument is not an integer.
    """

    if not isinstance(number, int):
        raise ValueError("Number argument must be an integer.")

    return bin(number).replace('0b', '')


if __name__ == '__main__':

    DECIMAL_VALUE = 24
    decimal_to_binary_1(DECIMAL_VALUE)
    print('\n')
    print(decimal_to_binary_2(DECIMAL_VALUE))
