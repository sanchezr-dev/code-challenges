/**
 * Challenge: Sort a list.
 *
 * Create a function that accepts two parameters.
 * - The first will be a list of numbers.
 * - The second parameter will be a string that can be one of the following values: asc, desc, and none.
 *
 * If the second parameter is “asc,” then the function should return a list with the numbers in ascending order.
 * If it's “desc,” then the list should be in descending order, and if it's “none,”
 * it should return the original list unaltered.
 */

function getSortedArray(numberArray, sortingOrder) {
  switch (sortingOrder) {
    case undefined:
    case null:
      return numberArray;
    case "asc":
      return [...numberArray].sort();
    case "desc":
      return [...numberArray].sort().reverse();
    default:
      throw Error(
        "The ordering param can only accept the values: 'asc', 'desc', and 'undefined'"
      );
  }
}

function main() {
  const original_list = [5, 1, 3, 4, 2];

  let result = getSortedArray(original_list, "asc");
  console.log(
    `Original: ${original_list} - Sort: ${"asc"} - Result: ${result}`
  );

  result = getSortedArray(original_list, "desc");
  console.log(
    `Original: ${original_list} - Sort: ${"desc"} - Result: ${result}`
  );

  result = getSortedArray(original_list, undefined);
  console.log(
    `Original: ${original_list} - Sort: ${"undefined"} - Result: ${result}`
  );

  result = getSortedArray(original_list, null);
}

main();
