from typing import List


def solve(board: List[List[str]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    visited = set()
    currVisit = set()
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    isSurrounded = True

    def dfs(i, j):
        # if isSurrounded then modify else put it in visited nodes
        # base case
        nonlocal isSurrounded
        nonlocal visited
        nonlocal currVisit
        if (i, j) in currVisit:
            return

        currVisit.add((i, j))
        if board[i][j] == "O" and (i == 0 or j == 0 or i == len(board) - 1 or j == len(board[0]) - 1):
            isSurrounded = False

        for d in directions:
            if 0 <= i + d[0] <= len(board) - 1 and 0 <= j + d[1] <= len(board[0]) - 1 and board[i + d[0]][
                j + d[1]] == "O":
                dfs(i + d[0], j + d[1])

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "O" and (i, j) not in visited:
                isSurrounded = True
                dfs(i, j)
                for e in currVisit:
                    visited.add(e)

                if isSurrounded:
                    for e in currVisit:
                        board[e[0]][e[1]] = "X"

                currVisit.clear()