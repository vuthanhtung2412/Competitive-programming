from typing import List


def change(amount: int, coins: List[int]) -> int:
    # recursive relation
    # change(amount, coins) = sum([change(amount - c, coins) for c in coins if amount - c >= 0 else 0])
    # no permutation is allowed
    # we can forbid permutation by only abiding by one strict order (increasing, decreasing)
    # change(amount, coins, maxC) = sum([change(amount - c, coins, min(c,maxC)) for c in coins if amount - c >= 0 and c < maxC else 0])
    # SUBPROBLEM: dp[i][j] number of coin change of amount j if we use zero or multiple coins of value coins[i] before using smaller coins
    coins.sort()
    dp = [[0] * (amount + 1) for _ in range(len(coins))]

    for i in range(len(coins)):
        dp[i][0] = 1

    for i in range(len(coins)):
        for j in range(1, amount + 1):
            tmp = 0
            if j - coins[i] >= 0:
                tmp += dp[i][j - coins[i]] + dp[i - 1][j]
            else:
                tmp += dp[i - 1][j]

            dp[i][j] = tmp

    for e in dp:
        print(e)

    return dp[-1][-1]
def change1(amount: int, coins: List[int]) -> int:
    # recursive relation
    # change(amount, coins) = sum([change(amount - c, coins) for c in coins if amount - c >= 0 else 0])
    # no permutation is allowed
    # we can forbid permutation by only abiding by one strict order (increasing, decreasing)
    # change(amount, coins, maxC) = sum([change(amount - c, coins, min(c,maxC)) for c in coins if amount - c >= 0 and c < maxC else 0])
    # SUBPROBLEM: dp[i][j] number of coin change of amount j if we only use smaller or equal coins of value smaller than coins[i]
    coins.sort()
    dp = [[0] * (amount + 1) for _ in range(len(coins))]

    for i in range(len(coins)):
        dp[i][0] = 1

    for i in range(len(coins)):
        for j in range(1, amount + 1):
            tmp = 0
            for k in range(i + 1):
                if j - coins[k] >= 0:
                    tmp += dp[k][j - coins[k]]
            dp[i][j] = tmp

    for e in dp:
        print(e)

    return dp[-1][-1]


print(change(5, [1, 2, 5]))
