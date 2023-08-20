/**
 * Code challenge: Fibonacci series.
 *
 * Write a function that will find the Nth numbers in the Fibonacci Sequence.
 *
 * A Fibonacci series is a mathematical numbers series that starts with fixed numbers 0 and 1.
 * All the next numbers can be generated using the sum of the last two numbers.
 *
 * A series of numbers in which each number ( Fibonacci number )
 * is the sum of the two preceding numbers.
 * The simplest is the series 1, 1, 2, 3, 5, 8, etc.
 */

function* fibonacci(number) {
  let current = 0;
  let next = 1;

  for (let i = 0; i < number; i++) {
    yield current;
    [current, next] = [next, current + next];
  }
}

function main() {
  const fibonacciSeries = fibonacci(30);
  console.log([...fibonacciSeries]);
}

main();
