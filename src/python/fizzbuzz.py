"""
Code challenge: FizzBuzz

Write a program that prints the numbers from 1 to 100.

- If the number can be divided by 3, it will output Fizz instead of the number.

- If the number is divisible by 5, the result will display Buzz instead of the number.

- And if the given number is divisible by both 3 and 5, 
FizzBuzz will be printed instead of the number.

- If the number cannot be divided by 3 or 5, it will be printed as a string.
"""


def print_fizzbuzz(number_list):

    for number in number_list:

        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")

        elif number % 3 == 0:
            print("Fizz")

        elif number % 5 == 0:
            print("Buzz")

        else:
            print(str(number))


if __name__ == '__main__':

    test_data = range(1, 101)
    print_fizzbuzz(test_data)
