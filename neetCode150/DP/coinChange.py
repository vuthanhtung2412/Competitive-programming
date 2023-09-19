from typing import List


def coinChange(coins: List[int], amount: int) -> int:
    d = {}
    for c in coins:
        d[c] = 1

    def minCoin(target: int):
        if target < 0:
            return -1

        if target == 0:
            return 0

        nonlocal d
        if target in d:
            return d[target]
        else:
            l = [minCoin(target - c) for c in coins if minCoin(target - c) != -1]
            if l:
                d[target] = min(l) + 1
                return d[target]
            else:
                d[target] = -1
                return -1

    return minCoin(amount)