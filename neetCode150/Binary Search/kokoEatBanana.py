import math
from functools import reduce
from typing import List


def minEatingSpeed(piles: List[int], h: int) -> int:
    # binary search can be implemented with while loop
    ma = max(piles)
    res = ma
    l = 1
    r = ma
    while l <= r:
        speed = (l + r) // 2
        time = 0
        for b in piles:
            time += math.ceil(b/speed)
        if time <= h:
            print("l: %s; r :%s" % (l, r))
            res = speed
            r = speed - 1
        else:
            l = speed + 1

    return res


print(minEatingSpeed([3, 6, 7, 11], 8))
