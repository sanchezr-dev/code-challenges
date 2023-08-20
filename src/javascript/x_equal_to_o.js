/**
 * Code Challenge: Are the Xs equal to the Os?
 *
 * Create a function that accepts a string.
 * This function should count the number of Xs and the number of Os in the string.
 * It should then return a boolean value of either True or False.
 *
 * If the count of Xs and Os are equal, then the function should return True.
 * If the count isn't the same, it should return False.
 * If there are no Xs or Os in the string, it should also return True because 0 equals 0.
 * The string can contain any type and number of characters.
 */

function xEqualsToO(stringValue) {
  const xMatches = stringValue.match(/x/gi) || [];
  const oMatches = stringValue.match(/o/gi) || [];
  return xMatches.length === oMatches.length;
}

function main() {
  let testValue = "xoxoXOXO";
  console.log(`Original: ${testValue} | Result: ${xEqualsToO(testValue)}`);

  testValue = "ABC xo DEF x";
  console.log(`Original: ${testValue} | Result: ${xEqualsToO(testValue)}`);

  testValue = "ABC DEF";
  console.log(`Original: ${testValue} | Result: ${xEqualsToO(testValue)}`);
}

main();
