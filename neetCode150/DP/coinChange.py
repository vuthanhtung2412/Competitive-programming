from typing import List


def coinChange(coins: List[int], amount: int) -> int:
    # first thought : can we be greedy (counter proof with example [1,3,4,5] amount = 7)
    # second thought : DFS + backtracking
    # memoization to reduce number of repeated calculation
    # cover all cases possible by subtracting coins from amount
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

def NCCoinChange(coins: List[int], amount: int) -> int:
    # bottom up dynamic programing aproach, keep track of 0 -> amount
    # cover all cases that amount can have (0 -> amount)
    if amount == 0:
        return 0
    dp = [-1] * (amount+1)
    dp[0] = 0
    for i in range(1,amount+1):
        for c in coins:
            if i-c >= 0 and dp[i-c] != -1:
                if dp[i] == -1:
                    dp[i] = dp[i-c] + 1
                elif dp[i] > dp[i-c] + 1:
                    dp[i] = dp[i-c] + 1
    print(dp)
    return dp[-1]