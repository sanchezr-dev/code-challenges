"""
Code challenge: Fibonacci series.

Write a function that will find the Nth numbers in the Fibonacci Sequence.

A Fibonacci series is a mathematical numbers series that starts with fixed numbers 0 and 1.
All the next numbers can be generated using the sum of the last two numbers. 

A series of numbers in which each number ( Fibonacci number ) 
is the sum of the two preceding numbers.
The simplest is the series 1, 1, 2, 3, 5, 8, etc.
"""


def generate_fibonacci_series(total_elements: int):

    actual_number, next_number = 0, 1

    for _ in range(total_elements):
        yield actual_number
        actual_number, next_number = next_number, actual_number + next_number


if __name__ == '__main__':

    fibonacci_series = generate_fibonacci_series(30)
    print(list(fibonacci_series))
