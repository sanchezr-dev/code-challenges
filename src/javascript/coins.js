/**
 * Code Challenge: Coin change
 * 
 * You are given an integer array coins representing coins of different denominations 
 * and an integer amount representing a total amount of money.
 * 
 * Return the fewest number of coins that you need to make up that amount.
 * If that amount of money cannot be made up by any combination of the coins, return -1.
 * 
 * You may assume that you have an infinite number of each kind of coin.
 * 
>>> change(coins=[1,2,5], amount=11)
3
>>> change(coins=[1,2,5], amount=20)
4
>>> change(coins=[2], amount=3)
-1
>>> change(coins=[1], amount=0)
0
>>> change(coins=[1], amount=1)
1
>>> change(coins=[1], amount=2)
2
"""
*/

const coinChange = (coins, amount) => {
  if (amount === 0) return 0;

  if (amount < 0) return Number.MAX_SAFE_INTEGER;

  let coinCounter = Number.MAX_SAFE_INTEGER;

  coins.forEach((coin) => {
    const result = coinChange(coins, amount - coin);

    if (result != Number.MAX_SAFE_INTEGER) {
      coinCounter = Math.min(coinCounter, result + 1);
    }
  });

  return coinCounter;
};

function main() {
  let coins = [1, 2, 5];
  let amount = 11;
  console.log(
    `Coins: ${coins} | Amount: ${amount} | Change: ${coinChange(coins, amount)}`
  );

  coins = [1, 2, 5];
  amount = 20;
  console.log(
    `Coins: ${coins} | Amount: ${amount} | Change: ${coinChange(coins, amount)}`
  );

  coins = [2];
  amount = 3;
  console.log(
    `Coins: ${coins} | Amount: ${amount} | Change: ${coinChange(coins, amount)}`
  );

  coins = [1];
  amount = 0;
  console.log(
    `Coins: ${coins} | Amount: ${amount} | Change: ${coinChange(coins, amount)}`
  );

  coins = [1, 5, 10, 50];
  amount = 25;
  console.log(
    `Coins: ${coins} | Amount: ${amount} | Change: ${coinChange(coins, amount)}`
  );
}

main();
