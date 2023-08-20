/**
 * Code challenge: FizzBuzz
 *
 * Write a program that prints the numbers from 1 to 100.
 *
 * - If the number can be divided by 3, it will output Fizz instead of the number.
 * - If the number is divisible by 5, the result will display Buzz instead of the number.
 * - And if the given number is divisible by both 3 and 5, FizzBuzz will be printed instead of the number.
 * - If the number cannot be divided by 3 or 5, it will be printed as a string.
 */

function fizzbuzz(numberArray) {
  numberArray.forEach((number) => {
    if (number % 5 === 0 && number % 3 === 0) {
      console.log("FizzBuzz");
    } else if (number % 3 === 0) {
      console.log("Fizz");
    } else if (number % 5 === 0) {
      console.log("Buzz");
    } else {
      console.log(number);
    }
  });
}

function main() {
  const testArray = Array(100)
    .fill()
    .map((_, index) => index + 1);

  fizzbuzz(testArray);
}

main();
