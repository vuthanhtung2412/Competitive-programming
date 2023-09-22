from typing import List


def numIslands(grid: List[List[str]]) -> int:
    def searchIle(i: int, j: int):
        nonlocal grid
        if 0 <= i < len(grid) and 0 <= j < len(grid[0]):
            if grid[i][j] == "1":
                grid[i][j] = "0"
                searchIle(i + 1, j)
                searchIle(i - 1, j)
                searchIle(i, j + 1)
                searchIle(i, j - 1)

    res = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "1":
                res += 1
                searchIle(i, j)

    return res