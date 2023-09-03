"""
Problem Statement

You are given an integer array representing coins of different denominations 
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

import sys


def change(coin_list: list[int], amount: int) -> int:

    if amount == 0:
        return 0

    if amount < 0:
        return sys.maxsize

    coin_count = sys.maxsize

    for coin in coin_list:
        result = change(coin_list, amount - coin)

        if result != sys.maxsize:
            coin_count = min(coin_count, result + 1)

    return coin_count


if __name__ == '__main__':

    print(f"Number of coins: {change([1,2,5], 11)}")
    print(f"Number of coins: {change([1,2,5], 20)}")
    print(f"Number of coins: {change([2], 3)}")
    print(f"Number of coins: {change([1], 0)}")
