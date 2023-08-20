/**
 * Code challenge: Reverse words.
 *
 * Write a function that will take a given string and reverse the order of the words.
 * "Hello world" becomes "world Hello" and
 * "May the Fourth be with you" becomes "you with be Fourth the May"
 */

function reverseWords(phrase) {
  const wordArray = phrase.split(" ");
  return wordArray.reverse().join(" ");
}

function reverseWordsLetters(phrase) {
  const reverseWordArray = phrase
    .split(" ")
    .map((word) => word.split("").reverse().join(""));

  return reverseWordArray.reverse().join(" ");
}

function main() {
  const phrase = "Hello World!";
  const reversedPhrase = reverseWords(phrase);
  console.log(`Phrase: ${phrase} | Reversed: ${reversedPhrase}`);
  const reversedWordLetters = reverseWordsLetters(phrase);
  console.log(`Phrase: ${phrase} | Reversed: ${reversedWordLetters}`);
}

main();
