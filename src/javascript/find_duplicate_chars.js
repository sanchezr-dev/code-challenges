/**
 * Code challenge: Unique characters in a string.
 *
 * Write a function that determines if any given string has all unique characters,
 * (i.e. no character in the string is duplicated).
 *
 * If the string has all unique characters, print "all unique".
 * If the string does not have all unique characters, print "duplicates found".
 */

const findDuplicates = (stringValue) => {
  let chars = {};

  for (const c of stringValue.split("")) {
    if (chars[c]) return "duplicates found";
    chars[c] = true;
  }

  return "all unique";
};

function main() {
  let test_data = "ABC DEF";
  let result = findDuplicates(test_data);
  console.log(`String: ${test_data} | Result: ${result}`);

  test_data = "Lorem Ipsum";
  result = findDuplicates(test_data);
  console.log(`String: ${test_data} | Result: ${result}`);

  test_data = "abc $%& 123  AB3";
  result = findDuplicates(test_data);
  console.log(`String: ${test_data} | Result: ${result}`);
}

main();
