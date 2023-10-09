from typing import List


# Travel in increasing order approach
def longestIncreasingPath(matrix: List[List[int]]) -> int:
    # condition adjacent
    # the previous element in the path must be smaller to the current element
    # dp[i][j] = max(dp[i+-1][j+-1] : tmp if matrix[i][j] < tmp) + 1
    dp = [[1 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    orderList = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            orderList.append((i, j))

    orderList.sort(key=lambda a: matrix[a[0]][a[1]])

    res = 1
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for i, j in orderList:
        for d in directions:
            if 0 <= i + d[0] < len(dp) and 0 <= j + d[1] < len(dp[0]) and matrix[i][j] > matrix[i + d[0]][j + d[1]]:
                dp[i][j] = max(dp[i][j], dp[i + d[0]][j + d[1]] + 1)

        res = max(dp[i][j], res)

    return res


# DFS + DP approach


print(longestIncreasingPath([[9, 9, 4], [6, 6, 8], [2, 1, 1]]))
