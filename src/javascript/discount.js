/**
 * Code challenge: Give me the discount.
 *
 * Create a function that accepts two parameters.
 * - The first should be the full price of an item as an integer.
 * - The second should be the discount percentage as an integer.
 *
 * The function should return the price of the item after the discount has been applied.
 * For example, if the price is 100 and the discount is 20, the function should return 80.
 */

function getPriceWithDiscount(price, discountPercentage) {
  const result = price - (price * discountPercentage) / 100;
  return result;
}

function main() {
  const price = 100;
  const discountPercentage = 10;
  const priceWithDiscount = getPriceWithDiscount(price, discountPercentage);
  console.log(
    `Price: ${price} | Discount: ${discountPercentage}% | Price with discount: ${priceWithDiscount}`
  );
}

main();
