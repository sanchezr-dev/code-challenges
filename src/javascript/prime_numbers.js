/**
 * Code challenge: Sum of prime factors
 *
 * Write a function that finds the sum of all prime factors of a given number, n.
 *
 * Prime numbers are natural numbers that are divisible by only one and the number itself.
 *
 * In other words, prime numbers are positive integers greater than 1 with exactly two factors, one and the number itself.
 *
 * Some prime numbers include 2, 3, 5, 7, 11, 13, etc.
 *
 * And the sum of prime numbers denotes the summation of all the prime numbers less than or equal to the given input.
 */

function isPrime(number) {
  for (let i = 2; i < number; i++) {
    if (number % i === 0) return false;
  }

  return true;
}

function getPrimeFactors(number) {
  const factors = [];
  for (let i = 2; i < number; i++) {
    if (isPrime(i)) factors.push(i);
  }

  return factors;
}

function sumArrayValues(numberArray) {
  const total = numberArray.reduce((acumulator, n) => (acumulator += n));
  return total;
}

function main() {
  const number = 10;
  const primeFactors = getPrimeFactors(number);
  const sum = sumArrayValues(primeFactors);
  console.log(`\nNumber: ${number} | Primes: ${primeFactors} | Sum: ${sum}`);
}

main();
