"""
Code challenge: Sum of prime factors

Write a function that finds the sum of all prime factors of a given number, n.

Prime numbers are natural numbers that are divisible by only one and the number itself.

In other words, prime numbers are positive integers greater than 1 with exactly two factors, 
one and the number itself. 

Some prime numbers include 2, 3, 5, 7, 11, 13, etc. 

And the sum of prime numbers denotes the summation of all the prime numbers 
less than or equal to the given input.
"""


def is_prime(number):

    for divisor in range(2, number):
        if number % divisor == 0:
            return False

    return True


def get_prime_factors(last_number):
    return [number for number in range(2, last_number + 1) if is_prime(number)]


def sum_prime_factors(number):
    prime_factors = get_prime_factors(last_number=number)
    primes_sum = sum(prime_factors)
    print(
        f"\nNumber: {number} | Factors: {list(prime_factors)} | Sum: {primes_sum}")


if __name__ == '__main__':

    # sum_prime_factors(2)
    # sum_prime_factors(3)
    # sum_prime_factors(5)
    # sum_prime_factors(6)
    # sum_prime_factors(7)
    # sum_prime_factors(10)
    # sum_prime_factors(11)
    sum_prime_factors(13)
