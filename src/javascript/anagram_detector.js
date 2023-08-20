/**
 * Code challenge: Anagram detector.
 *
 * Write a function in your favorite programming language that will accept any two strings
 * as parameters and return true if they are anagrams and false if they are not.
 *
 * An anagram is a word or phrase that's formed by rearranging the letters of another word or phrase.
 *
 * For example, the letters that make up "A decimal point" can be turned into the anagram "I'm a dot in place."
 * People mainly make anagrams just for fun, but sometimes they're used as pseudonyms or codes.
 *
 * Anagrams are strings with the same character content, and the
 * characters' frequency (or number) are also the same.
 */

function checkAnagram(phraseA, phraseB) {
  const normalizedPhraseA = phraseA
    .replace(/[^0-9A-Z]+/gi, "")
    .toLowerCase()
    .split("")
    .sort()
    .join("");

  const normalizedPhraseB = phraseB
    .replace(/[^0-9A-Z]+/gi, "")
    .toLowerCase()
    .split("")
    .sort()
    .join("");

  return normalizedPhraseA === normalizedPhraseB;
}

function main() {
  let phraseA = "A decimal point";
  let phraseB = "I'm a dot in place";
  let areAnagrams = checkAnagram(phraseA, phraseB);
  console.log(
    `Phrase A: '${phraseA}' | Phrase B: '${phraseB}' | Anagrams?: ${areAnagrams}\n`
  );

  phraseA = "Vacation time!";
  phraseB = "I am not active";
  areAnagrams = checkAnagram(phraseA, phraseB);
  console.log(
    `Phrase A: '${phraseA}' | Phrase B: '${phraseB}' | Anagrams?: ${areAnagrams}\n`
  );

  phraseA = "City";
  phraseB = "Hola";
  areAnagrams = checkAnagram(phraseA, phraseB);
  console.log(
    `Phrase A: '${phraseA}' | Phrase B: '${phraseB}' | Anagrams?: ${areAnagrams}\n`
  );
}

main();
