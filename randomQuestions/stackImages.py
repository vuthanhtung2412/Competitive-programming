from typing import List

# Meaning of in order (must be contiguous)
# VALID EXAMPLE : r1: 1,2,3; r2: 4,5
# NOT VALID EXAMPLE : r1: 1,3,5; r2: 2,4

def stackImages(photos: List[(int, int)], maxW: int) -> int:
    """
    :param photos: list of dim of photos (w,h)
    :param maxW: maximum width of each row
    :return: min sum of height

    ----
    description of solution:
    dp[i][j] : min height if we arrange from j-th image to i-th image into a new row
    2D dynamic programming each cell contain the following info: (remaining length, curr min height sum , curr max height)
    dp[i][j][0] = dp[i-1][j][0] - photos[i].width
    if not reach limited width condition
    if i == j : dp[i][j][1] = min([dp[i-1][j][1] for j in range(i)]) + photos[i].height
    Store last min height sum
    dp[i][j][1] = dp[i-1][j][1] if dp[i-1][j][2] >= photos[i].width
    else dp[i][j][1] += photos[i].height - dp[i-1][j][2]
    dp[i][j][2] = max(dp[i-1][j][2], photos[i].height)
    return min([dp[n-1][j][1] for j in range(n) if dp[n-1][j][0] >= 0])
    """
    dp = [[(maxW, 0, 0) for _ in range(len(photos))] for _ in range(len(photos))]
    lastMin = 0
    currMin = 1000000
    for i in range(len(photos)):
        for j in range(i + 1):
            if j == i:
                dp[i][i] = (maxW - photos[i][0], lastMin + photos[i][1], photos[i][1])
                currMin = min(currMin,dp[i][i][1])
            else:
                if dp[i-1][j][0] - photos[i][0] < 0:
                    # if the stacked photos reach max width stop studying the case
                    dp[i][j][0] = -1
                else:
                    dp[i][j][0] = dp[i-1][j][0] - photos[i][0]
                    if dp[i-1][j][2] < photos[i][1]:
                        dp[i][j][2] = photos[i][1]
                        dp[i][j][1] += photos[i][1] - dp[i-1][j][2]
                    else:
                        dp[i][j][2] = dp[i-1][j][2]
                        dp[i][j][1] = dp[i-1][j][1]

                    currMin = min(currMin, dp[i][j][1])

        lastMin = currMin
        currMin = 1000000

    return lastMin
