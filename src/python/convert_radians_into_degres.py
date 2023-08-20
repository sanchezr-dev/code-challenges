"""
Code challenge: Convert radians into degrees.

Write a function in Python that accepts one numeric parameter.
This parameter will be the measure of an angle in radians.
The function should convert the radians into degrees and then return that value.

While you might find a Python library to do this for you, you should write the function yourself.
One hint you get is that you'll need to use Pi in order to solve this problem. 
You can import the value for Pi from Python's math module.
"""

import math


def radians_to_degrees(radians):
    """ Function to convert radians into degrees

    Args:
        radians: Numeric value in radians.
    
    Returns:
        float: A value in degrees.

    Raises:
        ValueError if the radians arg is not a numeric value.
    """

    if not (isinstance(radians, (int, float, complex)) and not isinstance(radians, bool)):
        raise ValueError("The radians value is not a number. (int, float, complex)")

    return radians * (180 / math.pi)


def print_values(radians, degrees):
    """ Function to print radian and degrees values."""
    print(f"{radians} radians -> {degrees} degrees")


if __name__ == "__main__":

    radians = 10
    print_values(radians,  radians_to_degrees(radians))

    radians = 10.
    print_values(radians,  radians_to_degrees(radians))

    radians = 25j
    print_values(radians,  radians_to_degrees(radians))

    radians = '10'
    print_values(radians,  radians_to_degrees(radians))
