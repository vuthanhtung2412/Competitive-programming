from typing import List


def isValidSudoku(board: List[List[str]]) -> bool:

    # In this expression all 9 sets will refer to the same mem address
    # col = [set()] * 9
    # row = [set()] * 9
    # sq = [set()] * 9

    col = [set() for _ in range(9)]
    row = [set() for _ in range(9)]
    sq = [set() for _ in range(9)]

    for r in range(9):
        for c in range(9):
            if board[r][c] != ".":
                # check column
                if board[r][c] in col[c]:
                    return False
                else:
                    col[c].add(board[r][c])
                # check row
                if board[r][c] in row[r]:
                    return False
                else:
                    row[r].add(board[r][c])
                # check square
                if board[r][c] in sq[(r // 3) * 3 + c // 3]:
                    return False
                else:
                    sq[(r // 3) * 3 + c // 3].add(board[r][c])

    return True


board = [["5", "3", ".", ".", "7", ".", ".", ".", "."]
    , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
    , [".", "9", "8", ".", ".", ".", ".", "6", "."]
    , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
    , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
    , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
    , [".", "6", ".", ".", ".", ".", "2", "8", "."]
    , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
    , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

print(isValidSudoku(board))
