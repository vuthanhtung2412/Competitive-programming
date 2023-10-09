def numDistinct(s: str, t: str) -> int:
    # Recursive relation :
    # Sol(s,tar) = sol(s[:-1],tar) + sol(s,tar[:-1]) if s[-1] == tar[-1] else sol(s[:-1], tar)
    dp = [[0 for _ in range(len(s) + 1)] for _ in range(len(t) + 1)]
    for i in range(len(s) + 1):
        dp[0][i] = 1

    for i in range(1, len(t) + 1):
        for j in range(1, len(s) + 1):
            if s[j - 1] == t[i - 1]:
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j - 1]
            else:
                dp[i][j] = dp[i][j - 1]

    for e in dp:
        print(e)

    return dp[len(t)][len(s)]


print(numDistinct("rabbbit", "rabbit"))
