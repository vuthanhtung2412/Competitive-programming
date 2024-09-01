from typing import List
def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    def recur(sr: int, er: int, sc: int, ec: int):
        print("%s%s%s%s" % (sr, er, sc, ec))
        if sr <= er and sc <= ec:
            if matrix[(er + sr) // 2][(sc + ec) // 2] == target:
                return True
            elif matrix[(er + sr) // 2][(sc + ec) // 2] < target:
                return recur((er + sr) // 2, (er + sr) // 2, (sc + ec) // 2 + 1, ec) or recur((er + sr) // 2 + 1, er,
                                                                                              sc, ec)
            elif matrix[(er + sr) // 2][(sc + ec) // 2] > target:
                return recur((er + sr) // 2, (er + sr) // 2, sc, (sc + ec) // 2 - 1) or recur(sr, (er + sr) // 2 - 1,
                                                                                              sc, ec)
        else:
            return False

    return recur(0, len(matrix) - 1, 0, len(matrix[0]) - 1)