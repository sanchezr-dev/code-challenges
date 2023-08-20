/**
 * Code challenge: Count the vowels in a string
 *
 * Create a function that accepts a single word
 * and returns the number of vowels in that word.
 * In this function, only a, e, i, o, and u will be counted as vowels — not y.
 */

function countVowels(stringValue) {
  const matches = stringValue.match(/[aeiou]/gi);
  return matches.length;
}

function main() {
  let testValue = "Hello";
  let totalVowels = countVowels(testValue);
  console.log(`"${testValue}" has ${totalVowels} vowels.`);

  testValue = "Lorem ipsum dolor.";
  totalVowels = countVowels(testValue);
  console.log(`"${testValue}" has ${totalVowels} vowels.`);
}

main();
