/**
 * Code challenge: Repeat the characters
 *
 * Create a function that accepts a string.
 * The function should return a string, with each character in the original string doubled.
 * If you send the function “now” as a parameter, it should return “nnooww,”
 * and if you send “123a!”, it should return “112233aa!!”.
 */

function repeatCharacters(stringValue) {
  const result = stringValue
    .split("")
    .map((c) => c + c)
    .join("");
  return result;
}

function main() {
  const testValue = "Found sounds";
  const result = repeatCharacters(testValue);
  console.log(`Original: ${testValue} | Doubled: ${result}`);
}

main();
