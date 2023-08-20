"""
You are given an integer array coins representing coins of different denominations 
and an integer amount representing a total amount of money.
Return the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.
You may assume that you have an infinite number of each kind of coin."
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


def change(coin_list, amount):

    ordered_coins = sorted(coin_list, reverse=True)
    coin_count = 0
    total = 0

    for coin in ordered_coins:

        diff = amount - total

        if diff % coin == 0:
            coin_count += diff // coin
            total += coin * (diff // coin)

        else:
            coin_count += diff // coin
            total += coin * (diff // coin)

    if total != amount:
        return -1

    return coin_count


if __name__ == '__main__':

    print(f"Number of coins: {change([1,2,5], 11)}")
    print(f"Number of coins: {change([1,2,5], 20)}")
    print(f"Number of coins: {change([2], 3)}")
    print(f"Number of coins: {change([1], 0)}")
