import math
from typing import List
from recviz import recviz


def coinChange(coins: List[int], amount: int) -> int:
    lookup = {}
    res = coin_change(coins, amount, lookup)
    return res if res != math.inf else -1


@recviz
def coin_change(coins, amount, memo):
    if amount == 0:
        return 0
    if not coins:
        return math.inf
    if amount < 0:
        return math.inf

    if amount in memo:
        return memo[amount]

    memo[amount] = min(coin_change(coins[1:], amount, memo),
                       1 + coin_change(coins, amount - coins[0], memo))
    return memo[amount]


coinChange([2, 5, 10, 1], 27)
