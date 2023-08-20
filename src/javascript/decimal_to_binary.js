/**
 * Code challenge: Convert a decimal number into a binary.
 *
 * Write a function in Python that accepts a decimal number and returns the equivalent binary number.
 * To make this simple, the decimal number will always be less than 1,024
 * so the binary number returned will always be less than ten digits long.
 */

function decimalToBinary(number) {
  if (number >= 1) {
    if (number % 2 === 0) {
      return decimalToBinary(number / 2) + 0;
    } else {
      return decimalToBinary((number - 1) / 2) + 1;
    }
  } else {
    return "";
  }
}

function main() {
  for (let n = 1; n <= 10; n++) {
    console.log(decimalToBinary(n));
  }
}

main();
