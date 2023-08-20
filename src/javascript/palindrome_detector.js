/**
 * Code Challenge: Palindrome detector.
 *
 * Write a function that will test if a given string is a permutation of a palindrome.
 *
 * A string is said to be palindrome if it remains the same on reading from both ends.
 * It means that when you reverse a given string, it should be the same as the original string.
 * For instance, the string 'level' is a palindrome because it remains the same
 * when you read it from the beginning to the end and vice versa.
 */

function isPalindrome(word) {
  const reversedWord = word.split("").reverse().join("");
  return word === reversedWord;
}

function main() {
  let testWord = "kayak";
  let palindromeTest = isPalindrome(testWord);
  console.log(`Word: ${testWord} | Is palindrome?: ${palindromeTest}`);

  testWord = "level";
  palindromeTest = isPalindrome(testWord);
  console.log(`Word: ${testWord} | Is palindrome?: ${palindromeTest}`);

  testWord = "Hola";
  palindromeTest = isPalindrome(testWord);
  console.log(`Word: ${testWord} | Is palindrome?: ${palindromeTest}`);
}

main();
