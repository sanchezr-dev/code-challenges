/**
 * Code challenge: Just the numbers
 *
 * Write a function that accepts a list of any length that contains
 * a mix of non-negative integers and strings.
 * The function should return a list with only the integers in the original list in the same order.
 */

function getNumbersFromList(mixedArray) {
  const numberArray = mixedArray.filter((item) => typeof item === "number");
  return numberArray;
}

function main() {
  let testArray = [1, 2, "A", "BB", "CCC", 3];
  let filteredArray = getNumbersFromList(testArray);
  console.log(`Original list: ${testArray} | Numbers: ${filteredArray}`);

  testArray = [10, 5, "A", "BB", 99, "CCC", 3];
  filteredArray = getNumbersFromList(testArray);
  console.log(`Original list: ${testArray} | Numbers: ${filteredArray}`);

  testArray = [10, "100", 3];
  filteredArray = getNumbersFromList(testArray);
  console.log(`Original list: ${testArray} | Numbers: ${filteredArray}`);
}

main();
