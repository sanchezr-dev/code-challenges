/**
 * Code Challenge
 *
 * You have a JSON file containing information about various products,
 * including their names, prices, ratings and update date.
 *
 * The goal of this exercise is to read the JSON file,
 * sort the products by price, and calculate the average rating of the top 10
 * most expensive products without considering the ones updated more than 3 months ago.
 */
const data = require("./data/products.json");

function sortProductsDescending(a, b) {
  if (a.price < b.price) return 1;
  if (a.price > b.price) return -1;
  return 0;
}

function main() {
  console.log("\n\nProducts loaded from the JSON file");
  console.table(data);

  data.sort(sortProductsDescending);
  console.log("\n\nProducts sorted descending by price");
  console.table(data);

  const today = new Date();
  const threeMonthsAgo = new Date();
  threeMonthsAgo.setMonth(today.getMonth() - 3);
  const filteredData = data.filter(
    (p) => Date.parse(p.updated_at) > threeMonthsAgo
  );
  console.log(
    `\n\nTop 10 most expensive products for the last 3 months from today.`
  );
  console.table(filteredData);

  const topTenRatings = filteredData.slice(0, 10).map((p) => p.rating);
  const sum = topTenRatings.reduce((total, price) => {
    return (total += price);
  }, 0);
  const average = sum / topTenRatings.length;
  console.log(
    `\n\nAverage rating of the top 10 most expensive products for the last 3 months.`
  );

  console.log(average);
}

main();
